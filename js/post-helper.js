function initToggleShowToc(){KEEP.utils.postHelper={postPageContainerDom:document.querySelector(".post-page-container"),toggleShowTocBtnDom:document.querySelector(".toggle-show-toc"),toggleShowTocIcon:document.querySelector(".toggle-show-toc i"),mainContentDom:document.querySelector(".main-content"),postToolsDom:document.querySelector(".post-tools"),goToCommentsDom:document.querySelector(".post-tools .go-to-comments"),isShowToc:!1,initToggleToc(){this.toggleShowTocBtnDom&&this.toggleShowTocBtnDom.addEventListener("click",()=>{this.isShowToc=!this.isShowToc,KEEP.styleStatus.isShowToc=this.isShowToc,KEEP.setStyleStatus(),this.handleToggleToc(this.isShowToc)})},handleToggleToc(o){o?(this.postPageContainerDom.classList.add("show-toc"),document.body.classList.add("has-toc")):(this.postPageContainerDom.classList.remove("show-toc"),document.body.classList.remove("has-toc")),setTimeout(()=>{this.setPostToolsLeft()},120)},hasToc(o){this.toggleShowTocBtnDom.style.display="flex",this.isShowToc=o,this.handleToggleToc(o)},setPostToolsLeft(o){o=o||this.mainContentDom.getBoundingClientRect().width.toFixed(0);let t=5;window.innerWidth<=800&&(t=3),this.postToolsDom.style.opacity="1",this.postToolsDom.style.left=`calc((100vw - ${o}px) / 2 - ${t}rem)`},initSetPostToolsLeft(){setTimeout(()=>{this.setPostToolsLeft()},150),window.addEventListener("resize",()=>{this.setPostToolsLeft()})},goToComments(){const e=document.querySelector("#comments-anchor");this.goToCommentsDom&&e&&this.goToCommentsDom.addEventListener("click",o=>{o.preventDefault();let t=window.scrollY;t=0===t?-20:t;o=e.getBoundingClientRect().top+t;window.anime({targets:document.scrollingElement,duration:300,easing:"linear",scrollTop:o,complete:()=>{setTimeout(()=>{KEEP.utils.pageTop_dom.classList.add("hide")},150)}})})},watchPostCommentsCount(){const t=this.postToolsDom.querySelector(".post-comments-count");if(!t)return;const e=new MutationObserver(function(o){o.forEach(o=>{"childList"!==o.type||0<(o=Number(o.target.innerHTML))&&(t.style.display="flex",99<o&&(t.innerHTML="99+",e.disconnect()))})});e.observe(t,{attributes:!0,childList:!0})}},KEEP.utils.postHelper.initToggleToc(),KEEP.utils.postHelper.initSetPostToolsLeft(),KEEP.utils.postHelper.goToComments(),KEEP.utils.postHelper.watchPostCommentsCount()}!0===KEEP.theme_config.pjax.enable&&KEEP.utils?initToggleShowToc():window.addEventListener("DOMContentLoaded",initToggleShowToc);