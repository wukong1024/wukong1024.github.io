KEEP.initLocalSearch=()=>{let e=KEEP.hexo_config.path;if(e){let n=!1,r,o=!0;0===e.length?e="search.xml":e.endsWith("json")&&(o=!1);const t=document.querySelector(".search-input"),l=document.getElementById("search-result"),f=(e,t,n)=>{var r=e.length;if(0===r)return[];let o=0;var l;let s=[];for(n||(t=t.toLowerCase(),e=e.toLowerCase());-1<(l=t.indexOf(e,o));)s.push({position:l,word:e}),o=l+r;return s},v=(e,t,n,r)=>{var o;let{position:l,word:s}=o=n[n.length-1],i=[],a=0;for(;l+s.length<=t&&0!==n.length;){s===r&&a++,i.push({position:l,length:s.length});var c=l+s.length;for(n.pop();0!==n.length&&(o=n[n.length-1],l=o.position,s=o.word,c>l);)n.pop()}return{hits:i,start:e,end:t,searchTextCount:a}},x=(n,e)=>{let r="",o=e.start;return e.hits.forEach(e=>{r+=n.substring(o,e.position);var t=e.position+e.length;r+=`<b class="search-keyword">${n.substring(e.position,t)}</b>`,o=t}),r+=n.substring(o,e.end),r},s=()=>{if(n){let p=t.value.trim().toLowerCase(),e=p.split(/[-\s]+/);1<e.length&&e.push(p);let g=[];if(0<p.length&&r.forEach(({title:r,content:o,url:l})=>{let t=r.toLowerCase(),n=o.toLowerCase(),s=[],i=[],a=0;if(e.forEach(e=>{s=s.concat(f(e,t,!1)),i=i.concat(f(e,n,!1))}),0<s.length||0<i.length){var c=s.length+i.length;[s,i].forEach(e=>{e.sort((e,t)=>t.position!==e.position?t.position-e.position:e.word.length-t.word.length)});let e=[];0!==s.length&&(d=v(0,r.length,s,p),a+=d.searchTextCountInSlice,e.push(d));let n=[];for(;0!==i.length;){var{position:h,word:u}=i[i.length-1];let e=h-20,t=h+80;e<0&&(e=0),t<h+u.length&&(t=h+u.length),t>o.length&&(t=o.length);u=v(e,t,i,p);a+=u.searchTextCountInSlice,n.push(u)}n.sort((e,t)=>e.searchTextCount!==t.searchTextCount?t.searchTextCount-e.searchTextCount:e.hits.length!==t.hits.length?t.hits.length-e.hits.length:e.start-t.start);var d=parseInt(KEEP.theme_config.local_search.top_n_per_article||1,10);0<=d&&(n=n.slice(0,d));let t="";0!==e.length?t+=`<li><a href="${l}" class="search-result-title">${x(r,e[0])}</a>`:t+=`<li><a href="${l}" class="search-result-title">${r}</a>`,n.forEach(e=>{t+=`<a href="${l}"><p class="search-result">${x(o,e)}...</p></a>`}),t+="</li>",g.push({item:t,id:g.length,hitCount:c,searchTextCount:a})}}),1===e.length&&""===e[0])l.innerHTML='<div id="no-result"><i class="fas fa-search fa-5x"></i></div>';else if(0===g.length)l.innerHTML='<div id="no-result"><i class="fas fa-box-open fa-5x"></i></div>';else{g.sort((e,t)=>e.searchTextCount!==t.searchTextCount?t.searchTextCount-e.searchTextCount:e.hitCount!==t.hitCount?t.hitCount-e.hitCount:t.id-e.id);let t='<ul class="search-result-list">';g.forEach(e=>{t+=e.item}),t+="</ul>",l.innerHTML=t,window.pjax&&window.pjax.refresh(l)}}},i=()=>{fetch(KEEP.hexo_config.root+e).then(e=>e.text()).then(e=>{n=!0,r=o?[...(new DOMParser).parseFromString(e,"text/xml").querySelectorAll("entry")].map(e=>({title:e.querySelector("title").textContent,content:e.querySelector("content").textContent,url:e.querySelector("url").textContent})):JSON.parse(e),r=r.filter(e=>e.title).map(e=>(e.title=e.title.trim(),e.content=e.content?e.content.trim().replace(/<[^>]+>/g,""):"",e.url=decodeURIComponent(e.url).replace(/\/{2,}/g,"/"),e));const t=document.querySelector("#no-result");t&&(t.innerHTML='<i class="fas fa-search fa-5x"></i>')})};KEEP.theme_config.local_search.preload&&i(),t&&t.addEventListener("input",s),document.querySelectorAll(".search-popup-trigger").forEach(e=>{e.addEventListener("click",()=>{document.body.style.overflow="hidden",document.querySelector(".search-pop-overlay").classList.add("active"),setTimeout(()=>t.focus(),500),n||i()})});const a=()=>{document.body.style.overflow="",document.querySelector(".search-pop-overlay").classList.remove("active")};document.querySelector(".search-pop-overlay").addEventListener("click",e=>{e.target===document.querySelector(".search-pop-overlay")&&a()}),document.querySelector(".search-input-field-pre").addEventListener("click",()=>{t.value="",t.focus(),s()}),document.querySelector(".close-popup-btn").addEventListener("click",a),window.addEventListener("pjax:success",a),window.addEventListener("keyup",e=>{"Escape"===e.key&&a()})}else console.warn("`hexo-generator-searchdb` plugin is not installed!")};