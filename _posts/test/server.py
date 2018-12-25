import socket
import threading
import time


class Channel(threading.Thread):

    def __init__(self, client, address):
        threading.Thread.__init__(self)
        self.client = client
        self.address = address

    def run(self):
        while True:
            data = self.client.recv(1024)
            if not data:
                break
            ##########################################
            #  校验和 : 校验和位置之前所有16进制数据所表示的数值的和对256的求余
            decoded_data = self.decode(data)
            #  是否登陆帧
            is_login_frame = decoded_data[10] == '33'
            #  数据帧，读取数据
            if not is_login_frame:
                self.extract_data(decoded_data)
            response = self.make_response(decoded_data, is_login_frame)
            self.client.send(response)
            ##########################################
            time.sleep(0.1)
        else:
            self.client.close()

    def decode(self, data):
        decoded_data = []
        for d in data:
            hex_d = hex(d)
            decoded_data.append(hex_d[2:] if len(hex_d) > 3 else '0' + hex_d[2:])

        return decoded_data

    def extract_data(self, decoded_data):
        hex_33_value = int('33', 16)
        data_part = [int(d, 16) - hex_33_value for d in decoded_data[12:-22]]
        num_nodes = int(len(data_part) / 5)
        nodes = []
        for i in range(num_nodes):
            start_index = i * 5
            node_name = str(data_part[0 + start_index])
            temperature = (data_part[2 + start_index] * 256 + data_part[1 + start_index]) / 10
            humidity = (data_part[4 + start_index] * 256 + data_part[3 + start_index]) / 10
            nodes.append((
                'Node : {0}'.format(node_name),
                'Temperature : {0}C'.format(temperature),
                'Humidity : {0}%RH'.format(humidity)
            ))
        print('DATA\t', nodes)

    def make_response(self, decoded_data, is_login_frame=True):
        response_data = decoded_data[0:8] + ['20', '06', '33' if is_login_frame else '36', '1d'] + decoded_data[-6:]
        checknum = hex(sum([int(d, 16) for d in response_data[0:-2]]) % 256)
        response_data[-2] = checknum[2:] if len(checknum) > 3 else '0' + checknum[2:]
        for i, d in enumerate(response_data):
            response_data[i] = int(d, 16)

        return bytes(response_data)


bind_ip = '0.0.0.0'
bind_port = 2000

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))
server.listen(10)

try:
    while True:
        client, address = server.accept()
        print('Listening\t{0}:{1}'.format(address[0], address[1]))
        channel = Channel(client, address)
        channel.start()
except Exception as e:
    print(e)

server.close()
