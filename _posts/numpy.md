# Numpy

自定义列表类型

``` python
import numpy as np
tab=np.dtype[('name',np.str_,40),('numitems',np.int32),('price',np.float32)]
items=np.array([('DVD',42,3.14),('Butter',13,2.72)],dtype=tab)
```