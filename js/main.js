window.addEventListener("DOMContentLoaded",()=>{const{version:e,local_search:t,code_block:o,code_copy:E,lazyload:a}=KEEP.theme_config;KEEP.themeInfo={theme:`Keep v${e}`,author:"XPoet",repository:"https://github.com/XPoet/hexo-theme-keep"},KEEP.localStorageKey="KEEP-THEME-STATUS",KEEP.styleStatus={isExpandPageWidth:!1,isDark:!1,fontSizeLevel:0,isShowToc:!0},KEEP.printThemeInfo=()=>{console.log(`\n %c ${KEEP.themeInfo.theme} %c ${KEEP.themeInfo.repository} \n`,"color: #fadfa3; background: #333; padding: 6px 0;","padding: 6px 0;")},KEEP.setStyleStatus=()=>{localStorage.setItem(KEEP.localStorageKey,JSON.stringify(KEEP.styleStatus))},KEEP.getStyleStatus=()=>{var e=localStorage.getItem(KEEP.localStorageKey);if(e){for(var t in e=JSON.parse(e),KEEP.styleStatus)KEEP.styleStatus[t]=e[t];return e}return null},KEEP.refresh=()=>{KEEP.initUtils(),KEEP.initHeaderShrink(),KEEP.initModeToggle(),KEEP.initBack2Top(),!0===t?.enable&&KEEP.initLocalSearch(),!0!==o?.tools?.enable&&!0!==o?.enable&&!0!==E?.enable||KEEP.initCodeBlockTools(),!0===a?.enable&&KEEP.initLazyLoad()},KEEP.printThemeInfo(),KEEP.refresh()});