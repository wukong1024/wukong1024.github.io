




<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://github.githubassets.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" media="all" integrity="sha512-YR0i2ZAJ3fFf7L2CvMny+FWH76iHZNNIcD1YX57o4cdBHev8ffMXOfzy5F/lpBJpLttwPahk3zY/8XXaRH12ew==" rel="stylesheet" href="https://github.githubassets.com/assets/frameworks-611d22d99009ddf15fecbd82bcc9f2f8.css" />
  
    <link crossorigin="anonymous" media="all" integrity="sha512-cGOLZD3OVF/M/+99KmgPU6rP4hL+RHX6PAFE9AyMS798R0FvPmaPg6k9SowLhhBSUnXUdM3vspLmkuotNCRSoQ==" rel="stylesheet" href="https://github.githubassets.com/assets/github-70638b643dce545fccffef7d2a680f53.css" />
    
    
    
    


  <meta name="viewport" content="width=device-width">
  
  <title>Python-Interview-Bible/Python面试宝典-基础篇-2020.md at master · jackfrued/Python-Interview-Bible</title>
    <meta name="description" content="Python面试宝典2020版. Contribute to jackfrued/Python-Interview-Bible development by creating an account on GitHub.">
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">
  <meta name="apple-itunes-app" content="app-id=1477376905">

    <meta name="twitter:image:src" content="https://avatars2.githubusercontent.com/u/7474657?s=400&amp;v=4" /><meta name="twitter:site" content="@github" /><meta name="twitter:card" content="summary" /><meta name="twitter:title" content="jackfrued/Python-Interview-Bible" /><meta name="twitter:description" content="Python面试宝典2020版. Contribute to jackfrued/Python-Interview-Bible development by creating an account on GitHub." />
    <meta property="og:image" content="https://avatars2.githubusercontent.com/u/7474657?s=400&amp;v=4" /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="jackfrued/Python-Interview-Bible" /><meta property="og:url" content="https://github.com/jackfrued/Python-Interview-Bible" /><meta property="og:description" content="Python面试宝典2020版. Contribute to jackfrued/Python-Interview-Bible development by creating an account on GitHub." />

  <link rel="assets" href="https://github.githubassets.com/">
    <link rel="shared-web-socket" href="wss://alive.github.com/_sockets/u/39375246/ws?session=eyJ2IjoiVjMiLCJ1IjozOTM3NTI0NiwicyI6NTM0MTkyMjk3LCJjIjo2MzQ5Njk2NTksInQiOjE1OTU5MjQ3NDl9--ab0788d2ab584ef32f23c7f571031b74ff46018c85cf4b711bf887f564a12377" data-refresh-url="/_ws">
  <link rel="sudo-modal" href="/sessions/sudo_modal">

  <meta name="request-id" content="51DE:79AD:19A4CB9:230FFC0:5F1FE10C" data-pjax-transient="true" /><meta name="html-safe-nonce" content="1a7ecc174a1d63e4d675bf1f981c1c2d7909e450" data-pjax-transient="true" /><meta name="visitor-payload" content="eyJyZWZlcnJlciI6Imh0dHBzOi8vZ2l0aHViLmNvbS9qYWNrZnJ1ZWQvUHl0aG9uLUludGVydmlldy1CaWJsZSIsInJlcXVlc3RfaWQiOiI1MURFOjc5QUQ6MTlBNENCOToyMzBGRkMwOjVGMUZFMTBDIiwidmlzaXRvcl9pZCI6IjEwMjYyMjMxOTIxODk2NTc5OTciLCJyZWdpb25fZWRnZSI6ImFwLXNvdXRoZWFzdC0xIiwicmVnaW9uX3JlbmRlciI6ImlhZCJ9" data-pjax-transient="true" /><meta name="visitor-hmac" content="2dbbb23651ec08b5dea62f4f1b2c9d11e0533fd88a2c94344f4d1413162e8680" data-pjax-transient="true" />

    <meta name="hovercard-subject-tag" content="repository:259815382" data-pjax-transient>


  <meta name="github-keyboard-shortcuts" content="repository,source-code" data-pjax-transient="true" />

  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

    <meta name="google-site-verification" content="c1kuD-K2HIVF635lypcsWPoD4kilo5-jA_wBFyT4uMY">
  <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
  <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
  <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">

  <meta name="octolytics-host" content="collector.githubapp.com" /><meta name="octolytics-app-id" content="github" /><meta name="octolytics-event-url" content="https://collector.githubapp.com/github-external/browser_event" /><meta name="octolytics-dimension-ga_id" content="" class="js-octo-ga-id" /><meta name="octolytics-actor-id" content="39375246" /><meta name="octolytics-actor-login" content="wukong1024" /><meta name="octolytics-actor-hash" content="d7fcecd96e64fe9b726a5122f9a95538138bc3fb5bd4124c56d910dbcc302173" />

  <meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" />

  




    <meta name="google-analytics" content="UA-3769691-2">

  <meta class="js-ga-set" name="userId" content="b5bb7c913933a60884ac8a13cb56486e">

<meta class="js-ga-set" name="dimension10" content="Responsive" data-pjax-transient>

<meta class="js-ga-set" name="dimension1" content="Logged In">



  

      <meta name="hostname" content="github.com">
    <meta name="user-login" content="wukong1024">


      <meta name="expected-hostname" content="github.com">

      <meta name="js-proxy-site-detection-payload" content="ZmQ4N2YxMjUxM2NlMWNlNzFhYTEzOGRhNzcxNWQ5ZGVjOGFkYmYwOGNlOTA4OWMzYmY0OGU3ODA1ZjYyY2FjZnx7InJlbW90ZV9hZGRyZXNzIjoiMTQwLjI0MC4zMi41MiIsInJlcXVlc3RfaWQiOiI1MURFOjc5QUQ6MTlBNENCOToyMzBGRkMwOjVGMUZFMTBDIiwidGltZXN0YW1wIjoxNTk1OTI0NzQ5LCJob3N0IjoiZ2l0aHViLmNvbSJ9">

    <meta name="enabled-features" content="MARKETPLACE_PENDING_INSTALLATIONS,ACTIONS_DEFAULT_BRANCH_WARNING">

  <meta http-equiv="x-pjax-version" content="c865770308d4dd8668ec6c56080abc6a">
  

      <link href="https://github.com/jackfrued/Python-Interview-Bible/commits/master.atom" rel="alternate" title="Recent Commits to Python-Interview-Bible:master" type="application/atom+xml">

  <meta name="go-import" content="github.com/jackfrued/Python-Interview-Bible git https://github.com/jackfrued/Python-Interview-Bible.git">

  <meta name="octolytics-dimension-user_id" content="7474657" /><meta name="octolytics-dimension-user_login" content="jackfrued" /><meta name="octolytics-dimension-repository_id" content="259815382" /><meta name="octolytics-dimension-repository_nwo" content="jackfrued/Python-Interview-Bible" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="259815382" /><meta name="octolytics-dimension-repository_network_root_nwo" content="jackfrued/Python-Interview-Bible" /><meta name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" content="false" />


    <link rel="canonical" href="https://github.com/jackfrued/Python-Interview-Bible/blob/master/Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://github.githubassets.com/pinned-octocat.svg" color="#000000">
  <link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon.png">
  <link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon.svg">

<meta name="theme-color" content="#1e2327">


  <link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="logged-in env-production page-responsive page-blob">
    

    <div class="position-relative js-header-wrapper ">
      <a href="#start-of-content" class="p-3 bg-blue text-white show-on-focus js-skip-to-content">Skip to content</a>
      <span class="Progress progress-pjax-loader position-fixed width-full js-pjax-loader-bar">
        <span class="progress-pjax-loader-bar top-0 left-0" style="width: 0%;"></span>
      </span>

      
      



          <header class="Header py-md-0 js-details-container Details flex-wrap flex-md-nowrap px-3" role="banner">
  <div class="Header-item d-none d-md-flex">
    <a class="Header-link" href="https://github.com/" data-hotkey="g d"
  aria-label="Homepage " data-ga-click="Header, go to dashboard, icon:logo">
  <svg class="octicon octicon-mark-github v-align-middle" height="32" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>
</a>

  </div>

  <div class="Header-item d-md-none">
    <button class="Header-link btn-link js-details-target" type="button" aria-label="Toggle navigation" aria-expanded="false">
      <svg height="24" class="octicon octicon-three-bars" viewBox="0 0 16 16" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" d="M1 2.75A.75.75 0 011.75 2h12.5a.75.75 0 110 1.5H1.75A.75.75 0 011 2.75zm0 5A.75.75 0 011.75 7h12.5a.75.75 0 110 1.5H1.75A.75.75 0 011 7.75zM1.75 12a.75.75 0 100 1.5h12.5a.75.75 0 100-1.5H1.75z"></path></svg>
    </button>
  </div>

  <div class="Header-item Header-item--full flex-column flex-md-row width-full flex-order-2 flex-md-order-none mr-0 mr-md-3 mt-3 mt-md-0 Details-content--hidden-not-important d-md-flex">
        <div class="header-search header-search-current js-header-search-current flex-auto  flex-self-stretch flex-md-self-auto mr-0 mr-md-3 mb-3 mb-md-0 scoped-search site-scoped-search js-site-search position-relative js-jump-to js-header-search-current-jump-to"
  role="combobox"
  aria-owns="jump-to-results"
  aria-label="Search or jump to"
  aria-haspopup="listbox"
  aria-expanded="false"
>
  <div class="position-relative">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-site-search-form" role="search" aria-label="Site" data-scope-type="Repository" data-scope-id="259815382" data-scoped-search-url="/jackfrued/Python-Interview-Bible/search" data-unscoped-search-url="/search" action="/jackfrued/Python-Interview-Bible/search" accept-charset="UTF-8" method="get">
      <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container">
        <input type="text"
          class="form-control input-sm header-search-input jump-to-field js-jump-to-field js-site-search-focus js-site-search-field is-clearable"
          data-hotkey="s,/"
          name="q"
          value=""
          placeholder="Search or jump to…"
          data-unscoped-placeholder="Search or jump to…"
          data-scoped-placeholder="Search or jump to…"
          autocapitalize="off"
          aria-autocomplete="list"
          aria-controls="jump-to-results"
          aria-label="Search or jump to…"
          data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations"
          spellcheck="false"
          autocomplete="off"
          >
          <input type="hidden" value="LtPqDWIsnSS4/j8L9uJ6+A1b0TQykAFyBK3JgpSHPpV5IFpk5O8SN/wumxHs+pbLaN/3f1w11LjfAmQfk5GZpg==" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf" />
          <input type="hidden" class="js-site-search-type-field" name="type" >
            <img src="https://github.githubassets.com/images/search-key-slash.svg" alt="" class="mr-2 header-search-key-slash">

            <div class="Box position-absolute overflow-hidden d-none jump-to-suggestions js-jump-to-suggestions-container">
              
<ul class="d-none js-jump-to-suggestions-template-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-suggestion" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z"></path></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

</ul>

<ul class="d-none js-jump-to-no-results-template-container">
  <li class="d-flex flex-justify-center flex-items-center f5 d-none js-jump-to-suggestion p-2">
    <span class="text-gray">No suggested jump to results</span>
  </li>
</ul>

<ul id="jump-to-results" role="listbox" class="p-0 m-0 js-navigation-container jump-to-suggestions-results-container js-jump-to-suggestions-results-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-scoped-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z"></path></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-global-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z"></path></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>


    <li class="d-flex flex-justify-center flex-items-center p-0 f5 js-jump-to-suggestion">
      <img src="https://github.githubassets.com/images/spinners/octocat-spinner-128.gif" alt="Octocat Spinner Icon" class="m-2" width="28">
    </li>
</ul>

            </div>
      </label>
</form>  </div>
</div>


    <nav class="d-flex flex-column flex-md-row flex-self-stretch flex-md-self-auto" aria-label="Global">
    <a class="Header-link py-md-3 d-block d-md-none py-2 border-top border-md-top-0 border-white-fade-15" data-ga-click="Header, click, Nav menu - item:dashboard:user" aria-label="Dashboard" href="/dashboard">
      Dashboard
</a>
  <a class="js-selected-navigation-item Header-link py-md-3  mr-0 mr-md-3 py-2 border-top border-md-top-0 border-white-fade-15" data-hotkey="g p" data-ga-click="Header, click, Nav menu - item:pulls context:user" aria-label="Pull requests you created" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls" href="/pulls">
      Pull<span class="d-inline d-md-none d-lg-inline"> request</span>s
</a>
  <a class="js-selected-navigation-item Header-link py-md-3  mr-0 mr-md-3 py-2 border-top border-md-top-0 border-white-fade-15" data-hotkey="g i" data-ga-click="Header, click, Nav menu - item:issues context:user" aria-label="Issues you created" data-selected-links="/issues /issues/assigned /issues/mentioned /issues" href="/issues">
    Issues
</a>

    <div class="mr-0 mr-md-3 py-2 py-md-0 border-top border-md-top-0 border-white-fade-15">
      <a class="js-selected-navigation-item Header-link py-md-3 d-inline-block" data-ga-click="Header, click, Nav menu - item:marketplace context:user" data-octo-click="marketplace_click" data-octo-dimensions="location:nav_bar" data-selected-links=" /marketplace" href="/marketplace">
        Marketplace
</a>      

    </div>

  <a class="js-selected-navigation-item Header-link py-md-3  mr-0 mr-md-3 py-2 border-top border-md-top-0 border-white-fade-15" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship showcases showcases_search showcases_landing /explore" href="/explore">
    Explore
</a>


    <a class="Header-link d-block d-md-none mr-0 mr-md-3 py-2 py-md-3 border-top border-md-top-0 border-white-fade-15" href="/wukong1024">
      <img class="avatar avatar-user" src="https://avatars3.githubusercontent.com/u/39375246?s=40&amp;v=4" width="20" height="20" alt="@wukong1024" />
      wukong1024
</a>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form action="/logout" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="lA4Zwl3iOiRCGyZBTW2JuPIFY8awo0UU4PWSuy8QsDl0GB3nR8zxLOMjDW+7jdbcfX9023R6ujTcJHR6zcGwIg==" />
      <button type="submit" class="Header-link mr-0 mr-md-3 py-2 py-md-3 border-top border-md-top-0 border-white-fade-15 d-md-none btn-link d-block width-full text-left" data-ga-click="Header, sign out, icon:logout" style="padding-left: 2px;">
        <svg class="octicon octicon-sign-out v-align-middle" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M2 2.75C2 1.784 2.784 1 3.75 1h2.5a.75.75 0 010 1.5h-2.5a.25.25 0 00-.25.25v10.5c0 .138.112.25.25.25h2.5a.75.75 0 010 1.5h-2.5A1.75 1.75 0 012 13.25V2.75zm10.44 4.5H6.75a.75.75 0 000 1.5h5.69l-1.97 1.97a.75.75 0 101.06 1.06l3.25-3.25a.75.75 0 000-1.06l-3.25-3.25a.75.75 0 10-1.06 1.06l1.97 1.97z"></path></svg>
        Sign out
      </button>
</form></nav>

  </div>

  <div class="Header-item Header-item--full flex-justify-center d-md-none position-relative">
    <a class="Header-link" href="https://github.com/" data-hotkey="g d"
  aria-label="Homepage " data-ga-click="Header, go to dashboard, icon:logo">
  <svg class="octicon octicon-mark-github v-align-middle" height="32" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>
</a>

  </div>

  <div class="Header-item mr-0 mr-md-3 flex-order-1 flex-md-order-none">
    
    <a aria-label="You have unread notifications" class="Header-link notification-indicator position-relative tooltipped tooltipped-sw js-socket-channel js-notification-indicator" data-hotkey="g n" data-ga-click="Header, go to notifications, icon:unread" data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6MzkzNzUyNDYiLCJ0IjoxNTk1OTI0NzQ5fQ==--61da4300d4205fdae67f6997fe582509167b994ee2767a3626484a82e7176de6" href="/notifications">
        <span class="js-indicator-modifier mail-status unread"></span>
        <svg class="octicon octicon-bell" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="M8 16a2 2 0 001.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 008 16z"></path><path fill-rule="evenodd" d="M8 1.5A3.5 3.5 0 004.5 5v2.947c0 .346-.102.683-.294.97l-1.703 2.556a.018.018 0 00-.003.01l.001.006c0 .002.002.004.004.006a.017.017 0 00.006.004l.007.001h10.964l.007-.001a.016.016 0 00.006-.004.016.016 0 00.004-.006l.001-.007a.017.017 0 00-.003-.01l-1.703-2.554a1.75 1.75 0 01-.294-.97V5A3.5 3.5 0 008 1.5zM3 5a5 5 0 0110 0v2.947c0 .05.015.098.042.139l1.703 2.555A1.518 1.518 0 0113.482 13H2.518a1.518 1.518 0 01-1.263-2.36l1.703-2.554A.25.25 0 003 7.947V5z"></path></svg>
</a>
  </div>


  <div class="Header-item position-relative d-none d-md-flex">
    <details class="details-overlay details-reset">
  <summary class="Header-link"
      aria-label="Create new…"
      data-ga-click="Header, create new, icon:add">
    <svg class="octicon octicon-plus" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 2a.75.75 0 01.75.75v4.5h4.5a.75.75 0 010 1.5h-4.5v4.5a.75.75 0 01-1.5 0v-4.5h-4.5a.75.75 0 010-1.5h4.5v-4.5A.75.75 0 018 2z"></path></svg> <span class="dropdown-caret"></span>
  </summary>
  <details-menu class="dropdown-menu dropdown-menu-sw mt-n2">
    
<a role="menuitem" class="dropdown-item" href="/new" data-ga-click="Header, create new repository">
  New repository
</a>

  <a role="menuitem" class="dropdown-item" href="/new/import" data-ga-click="Header, import a repository">
    Import repository
  </a>

<a role="menuitem" class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, create new gist">
  New gist
</a>

  <a role="menuitem" class="dropdown-item" href="/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>


  <div role="none" class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="jackfrued/Python-Interview-Bible">This repository</span>
  </div>
    <a role="menuitem" class="dropdown-item" href="/jackfrued/Python-Interview-Bible/issues/new/choose" data-ga-click="Header, create new issue" data-skip-pjax>
      New issue
    </a>


  </details-menu>
</details>

  </div>

  <div class="Header-item position-relative mr-0 d-none d-md-flex">
    
  <details class="details-overlay details-reset js-feature-preview-indicator-container" data-feature-preview-indicator-src="/users/wukong1024/feature_preview/indicator_check">

  <summary class="Header-link"
    aria-label="View profile and more"
    data-ga-click="Header, show menu, icon:avatar">
    <img
  alt="@wukong1024"
  width="20"
  height="20"
  src="https://avatars0.githubusercontent.com/u/39375246?s=60&amp;v=4"
  class="avatar avatar-user " />

      <span class="feature-preview-indicator js-feature-preview-indicator" style="top: 10px;" hidden></span>
    <span class="dropdown-caret"></span>
  </summary>
  <details-menu class="dropdown-menu dropdown-menu-sw mt-n2" style="width: 180px" >
    <div class="header-nav-current-user css-truncate"><a role="menuitem" class="no-underline user-profile-link px-3 pt-2 pb-2 mb-n2 mt-n1 d-block" href="/wukong1024" data-ga-click="Header, go to profile, text:Signed in as">Signed in as <strong class="css-truncate-target">wukong1024</strong></a></div>
    <div role="none" class="dropdown-divider"></div>

      <div class="pl-3 pr-3 f6 user-status-container js-user-status-context lh-condensed" data-url="/users/status?compact=1&amp;link_mentions=0&amp;truncate=1">
        
<div class="js-user-status-container rounded-1 px-2 py-1 mt-2 border"
  data-team-hovercards-enabled>
  <details class="js-user-status-details details-reset details-overlay details-overlay-dark">
    <summary class="btn-link btn-block link-gray no-underline js-toggle-user-status-edit toggle-user-status-edit "
      role="menuitem" data-hydro-click="{&quot;event_type&quot;:&quot;user_profile.click&quot;,&quot;payload&quot;:{&quot;profile_user_id&quot;:7474657,&quot;target&quot;:&quot;EDIT_USER_STATUS&quot;,&quot;user_id&quot;:39375246,&quot;originating_url&quot;:&quot;https://github.com/jackfrued/Python-Interview-Bible/blob/master/Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md&quot;}}" data-hydro-click-hmac="97a2f0d9c3ce2e01b556492a77cac77e9d646125257dd3a3ce6c7cabcdadb9d9">
      <div class="d-flex flex-items-center flex-items-stretch">
        <div class="f6 lh-condensed user-status-header d-flex user-status-emoji-only-header circle">
          <div class="user-status-emoji-container flex-shrink-0 mr-2 d-flex flex-items-center flex-justify-center lh-condensed-ultra v-align-bottom">
            <svg class="octicon octicon-smiley" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 8a6.5 6.5 0 1113 0 6.5 6.5 0 01-13 0zM8 0a8 8 0 100 16A8 8 0 008 0zM5 8a1 1 0 100-2 1 1 0 000 2zm7-1a1 1 0 11-2 0 1 1 0 012 0zM5.32 9.636a.75.75 0 011.038.175l.007.009c.103.118.22.222.35.31.264.178.683.37 1.285.37.602 0 1.02-.192 1.285-.371.13-.088.247-.192.35-.31l.007-.008a.75.75 0 111.222.87l-.614-.431c.614.43.614.431.613.431v.001l-.001.002-.002.003-.005.007-.014.019a1.984 1.984 0 01-.184.213c-.16.166-.338.316-.53.445-.63.418-1.37.638-2.127.629-.946 0-1.652-.308-2.126-.63a3.32 3.32 0 01-.715-.657l-.014-.02-.005-.006-.002-.003v-.002h-.001l.613-.432-.614.43a.75.75 0 01.183-1.044h.001z"></path></svg>
          </div>
        </div>
        <div class="
          
           user-status-message-wrapper f6 min-width-0"
           style="line-height: 20px;" >
          <div class="css-truncate css-truncate-target width-fit text-gray-dark text-left">
              <span class="text-gray">Set status</span>
          </div>
        </div>
      </div>
    </summary>
    <details-dialog class="details-dialog rounded-1 anim-fade-in fast Box Box--overlay" role="dialog" tabindex="-1">
      <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="position-relative flex-auto js-user-status-form" action="/users/status?circle=0&amp;compact=1&amp;link_mentions=0&amp;truncate=1" accept-charset="UTF-8" method="post"><input type="hidden" name="_method" value="put" /><input type="hidden" name="authenticity_token" value="lo3dDhv0ZwWjYsEg4tPkF8Yc+bt9TwbewEEVQGYs5W4V1oL8wZQGU7S35jIiH7/LGhGR6DBHVVMaWe4e6o9cVw==" />
        <div class="Box-header bg-gray border-bottom p-3">
          <button class="Box-btn-octicon js-toggle-user-status-edit btn-octicon float-right" type="reset" aria-label="Close dialog" data-close-dialog>
            <svg class="octicon octicon-x" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path></svg>
          </button>
          <h3 class="Box-title f5 text-bold text-gray-dark">Edit status</h3>
        </div>
        <input type="hidden" name="emoji" class="js-user-status-emoji-field" value="">
        <input type="hidden" name="organization_id" class="js-user-status-org-id-field" value="">
        <div class="px-3 py-2 text-gray-dark">
          <div class="js-characters-remaining-container position-relative mt-2">
            <div class="input-group d-table form-group my-0 js-user-status-form-group">
              <span class="input-group-button d-table-cell v-align-middle" style="width: 1%">
                <button type="button" aria-label="Choose an emoji" class="btn-outline btn js-toggle-user-status-emoji-picker btn-open-emoji-picker p-0">
                  <span class="js-user-status-original-emoji" hidden></span>
                  <span class="js-user-status-custom-emoji"></span>
                  <span class="js-user-status-no-emoji-icon" >
                    <svg class="octicon octicon-smiley" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 8a6.5 6.5 0 1113 0 6.5 6.5 0 01-13 0zM8 0a8 8 0 100 16A8 8 0 008 0zM5 8a1 1 0 100-2 1 1 0 000 2zm7-1a1 1 0 11-2 0 1 1 0 012 0zM5.32 9.636a.75.75 0 011.038.175l.007.009c.103.118.22.222.35.31.264.178.683.37 1.285.37.602 0 1.02-.192 1.285-.371.13-.088.247-.192.35-.31l.007-.008a.75.75 0 111.222.87l-.614-.431c.614.43.614.431.613.431v.001l-.001.002-.002.003-.005.007-.014.019a1.984 1.984 0 01-.184.213c-.16.166-.338.316-.53.445-.63.418-1.37.638-2.127.629-.946 0-1.652-.308-2.126-.63a3.32 3.32 0 01-.715-.657l-.014-.02-.005-.006-.002-.003v-.002h-.001l.613-.432-.614.43a.75.75 0 01.183-1.044h.001z"></path></svg>
                  </span>
                </button>
              </span>
              <text-expander keys=": @" data-mention-url="/autocomplete/user-suggestions" data-emoji-url="/autocomplete/emoji">
                <input
                  type="text"
                  autocomplete="off"
                  data-no-org-url="/autocomplete/user-suggestions"
                  data-org-url="/suggestions?mention_suggester=1"
                  data-maxlength="80"
                  class="d-table-cell width-full form-control js-user-status-message-field js-characters-remaining-field"
                  placeholder="What's happening?"
                  name="message"
                  value=""
                  aria-label="What is your current status?">
              </text-expander>
              <div class="error">Could not update your status, please try again.</div>
            </div>
            <div style="margin-left: 53px" class="my-1 text-small label-characters-remaining js-characters-remaining" data-suffix="remaining" hidden>
              80 remaining
            </div>
          </div>
          <include-fragment class="js-user-status-emoji-picker" data-url="/users/status/emoji"></include-fragment>
          <div class="overflow-auto ml-n3 mr-n3 px-3 border-bottom" style="max-height: 33vh">
            <div class="user-status-suggestions js-user-status-suggestions collapsed overflow-hidden">
              <h4 class="f6 text-normal my-3">Suggestions:</h4>
              <div class="mx-3 mt-2 clearfix">
                  <div class="float-left col-6">
                      <button type="button" value=":palm_tree:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="palm_tree" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f334.png">🌴</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          On vacation
                        </div>
                      </button>
                      <button type="button" value=":face_with_thermometer:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="face_with_thermometer" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f912.png">🤒</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          Out sick
                        </div>
                      </button>
                  </div>
                  <div class="float-left col-6">
                      <button type="button" value=":house:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="house" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f3e0.png">🏠</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          Working from home
                        </div>
                      </button>
                      <button type="button" value=":dart:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="dart" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f3af.png">🎯</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          Focusing
                        </div>
                      </button>
                  </div>
              </div>
            </div>
            <div class="user-status-limited-availability-container">
              <div class="form-checkbox my-0">
                <input type="checkbox" name="limited_availability" value="1" class="js-user-status-limited-availability-checkbox" data-default-message="I may be slow to respond." aria-describedby="limited-availability-help-text-truncate-true-compact-true" id="limited-availability-truncate-true-compact-true">
                <label class="d-block f5 text-gray-dark mb-1" for="limited-availability-truncate-true-compact-true">
                  Busy
                </label>
                <p class="note" id="limited-availability-help-text-truncate-true-compact-true">
                  When others mention you, assign you, or request your review,
                  GitHub will let them know that you have limited availability.
                </p>
              </div>
            </div>
          </div>
          <div class="d-inline-block f5 mr-2 pt-3 pb-2" >
  <div class="d-inline-block mr-1">
    Clear status
  </div>

  <details class="js-user-status-expire-drop-down f6 dropdown details-reset details-overlay d-inline-block mr-2">
    <summary class="btn btn-sm v-align-baseline" aria-haspopup="true">
      <div class="js-user-status-expiration-interval-selected d-inline-block v-align-baseline">
        Never
      </div>
      <div class="dropdown-caret"></div>
    </summary>

    <ul class="dropdown-menu dropdown-menu-se pl-0 overflow-auto" style="width: 220px; max-height: 15.5em">
      <li>
        <button type="button" class="btn-link dropdown-item js-user-status-expire-button ws-normal" title="Never">
          <span class="d-inline-block text-bold mb-1">Never</span>
          <div class="f6 lh-condensed">Keep this status until you clear your status or edit your status.</div>
        </button>
      </li>
      <li class="dropdown-divider" role="none"></li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="in 30 minutes" value="2020-07-28T16:55:49+08:00">
            in 30 minutes
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="in 1 hour" value="2020-07-28T17:25:49+08:00">
            in 1 hour
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="in 4 hours" value="2020-07-28T20:25:49+08:00">
            in 4 hours
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="today" value="2020-07-28T23:59:59+08:00">
            today
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="this week" value="2020-08-02T23:59:59+08:00">
            this week
          </button>
        </li>
    </ul>
  </details>
  <input class="js-user-status-expiration-date-input" type="hidden" name="expires_at" value="">
</div>

          <include-fragment class="js-user-status-org-picker" data-url="/users/status/organizations"></include-fragment>
        </div>
        <div class="d-flex flex-items-center flex-justify-between p-3 border-top">
          <button type="submit" disabled class="width-full btn btn-primary mr-2 js-user-status-submit">
            Set status
          </button>
          <button type="button" disabled class="width-full js-clear-user-status-button btn ml-2 ">
            Clear status
          </button>
        </div>
</form>    </details-dialog>
  </details>
</div>

      </div>
      <div role="none" class="dropdown-divider"></div>

    <a role="menuitem" class="dropdown-item" href="/wukong1024" data-ga-click="Header, go to profile, text:your profile" data-hydro-click="{&quot;event_type&quot;:&quot;global_header.user_menu_dropdown.click&quot;,&quot;payload&quot;:{&quot;request_url&quot;:&quot;https://github.com/jackfrued/Python-Interview-Bible/blob/master/Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md&quot;,&quot;target&quot;:&quot;YOUR_PROFILE&quot;,&quot;originating_url&quot;:&quot;https://github.com/jackfrued/Python-Interview-Bible/blob/master/Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md&quot;,&quot;user_id&quot;:39375246}}" data-hydro-click-hmac="55f03296a201e2f550f62fc52669f909747a876d4f096ba4f8c7f10565e6510f" >Your profile</a>

    <a role="menuitem" class="dropdown-item" href="/wukong1024?tab=repositories" data-ga-click="Header, go to repositories, text:your repositories" data-hydro-click="{&quot;event_type&quot;:&quot;global_header.user_menu_dropdown.click&quot;,&quot;payload&quot;:{&quot;request_url&quot;:&quot;https://github.com/jackfrued/Python-Interview-Bible/blob/master/Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md&quot;,&quot;target&quot;:&quot;YOUR_REPOSITORIES&quot;,&quot;originating_url&quot;:&quot;https://github.com/jackfrued/Python-Interview-Bible/blob/master/Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md&quot;,&quot;user_id&quot;:39375246}}" data-hydro-click-hmac="9df58de84a063ca6d0484cb3e432fa19733685e2ad861846f1106c4ae4cb6590" >Your repositories</a>


    <a role="menuitem" class="dropdown-item" href="/wukong1024?tab=projects" data-ga-click="Header, go to projects, text:your projects" data-hydro-click="{&quot;event_type&quot;:&quot;global_header.user_menu_dropdown.click&quot;,&quot;payload&quot;:{&quot;request_url&quot;:&quot;https://github.com/jackfrued/Python-Interview-Bible/blob/master/Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md&quot;,&quot;target&quot;:&quot;YOUR_PROJECTS&quot;,&quot;originating_url&quot;:&quot;https://github.com/jackfrued/Python-Interview-Bible/blob/master/Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md&quot;,&quot;user_id&quot;:39375246}}" data-hydro-click-hmac="07018a6a692ec70d292da7f82bf4bf7f51e63d8719af30c7917e233bd14e90ae" >Your projects</a>


    <a role="menuitem" class="dropdown-item" href="/wukong1024?tab=stars" data-ga-click="Header, go to starred repos, text:your stars" data-hydro-click="{&quot;event_type&quot;:&quot;global_header.user_menu_dropdown.click&quot;,&quot;payload&quot;:{&quot;request_url&quot;:&quot;https://github.com/jackfrued/Python-Interview-Bible/blob/master/Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md&quot;,&quot;target&quot;:&quot;YOUR_STARS&quot;,&quot;originating_url&quot;:&quot;https://github.com/jackfrued/Python-Interview-Bible/blob/master/Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md&quot;,&quot;user_id&quot;:39375246}}" data-hydro-click-hmac="4513c75b883afb509e2e46a216b53ebae5e767651407ad5bf9735e1e52fbd6ed" >Your stars</a>
      <a role="menuitem" class="dropdown-item" href="https://gist.github.com/mine" data-ga-click="Header, your gists, text:your gists" data-hydro-click="{&quot;event_type&quot;:&quot;global_header.user_menu_dropdown.click&quot;,&quot;payload&quot;:{&quot;request_url&quot;:&quot;https://github.com/jackfrued/Python-Interview-Bible/blob/master/Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md&quot;,&quot;target&quot;:&quot;YOUR_GISTS&quot;,&quot;originating_url&quot;:&quot;https://github.com/jackfrued/Python-Interview-Bible/blob/master/Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md&quot;,&quot;user_id&quot;:39375246}}" data-hydro-click-hmac="8904ba01e50672bc251269d2a9c19faf68704a8752b3db1aa4cc201062de79e0" >Your gists</a>





    <div role="none" class="dropdown-divider"></div>
      <a role="menuitem" class="dropdown-item" href="/settings/billing" data-ga-click="Header, go to billing, text:upgrade" data-hydro-click="{&quot;event_type&quot;:&quot;global_header.user_menu_dropdown.click&quot;,&quot;payload&quot;:{&quot;request_url&quot;:&quot;https://github.com/jackfrued/Python-Interview-Bible/blob/master/Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md&quot;,&quot;target&quot;:&quot;UPGRADE&quot;,&quot;originating_url&quot;:&quot;https://github.com/jackfrued/Python-Interview-Bible/blob/master/Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md&quot;,&quot;user_id&quot;:39375246}}" data-hydro-click-hmac="a44ec0cd45a9ba4031ed155dbeb7054d37d7f6ab01e071b5d483a4330ddaf9ce" >Upgrade</a>
      
<div id="feature-enrollment-toggle" class="hide-sm hide-md feature-preview-details position-relative">
  <button
    type="button"
    class="dropdown-item btn-link"
    role="menuitem"
    data-feature-preview-trigger-url="/users/wukong1024/feature_previews"
    data-feature-preview-close-details="{&quot;event_type&quot;:&quot;feature_preview.clicks.close_modal&quot;,&quot;payload&quot;:{&quot;originating_url&quot;:&quot;https://github.com/jackfrued/Python-Interview-Bible/blob/master/Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md&quot;,&quot;user_id&quot;:39375246}}"
    data-feature-preview-close-hmac="52cbf8fd965bbf45a9d93da4b93c4280390d6e72bcf41f3cc7c1ac2127679687"
    data-hydro-click="{&quot;event_type&quot;:&quot;feature_preview.clicks.open_modal&quot;,&quot;payload&quot;:{&quot;link_location&quot;:&quot;user_dropdown&quot;,&quot;originating_url&quot;:&quot;https://github.com/jackfrued/Python-Interview-Bible/blob/master/Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md&quot;,&quot;user_id&quot;:39375246}}"
    data-hydro-click-hmac="9e4860b6f79032eacaa45afb39ec70a6fee9f62f32d4dc2181b28e60278eaf1c"
  >
    Feature preview
  </button>
    <span class="feature-preview-indicator js-feature-preview-indicator" hidden></span>
</div>

    <a role="menuitem" class="dropdown-item" href="https://help.github.com" data-ga-click="Header, go to help, text:help" data-hydro-click="{&quot;event_type&quot;:&quot;global_header.user_menu_dropdown.click&quot;,&quot;payload&quot;:{&quot;request_url&quot;:&quot;https://github.com/jackfrued/Python-Interview-Bible/blob/master/Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md&quot;,&quot;target&quot;:&quot;HELP&quot;,&quot;originating_url&quot;:&quot;https://github.com/jackfrued/Python-Interview-Bible/blob/master/Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md&quot;,&quot;user_id&quot;:39375246}}" data-hydro-click-hmac="481246401d41cdf1b1a94b643ef9824abc20568cb05afb8766d0222e50739cad" >Help</a>
    <a role="menuitem" class="dropdown-item" href="/settings/profile" data-ga-click="Header, go to settings, icon:settings" data-hydro-click="{&quot;event_type&quot;:&quot;global_header.user_menu_dropdown.click&quot;,&quot;payload&quot;:{&quot;request_url&quot;:&quot;https://github.com/jackfrued/Python-Interview-Bible/blob/master/Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md&quot;,&quot;target&quot;:&quot;SETTINGS&quot;,&quot;originating_url&quot;:&quot;https://github.com/jackfrued/Python-Interview-Bible/blob/master/Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md&quot;,&quot;user_id&quot;:39375246}}" data-hydro-click-hmac="8b06fd6370aca4c3bc4af40f0e5aa6e6d99b74a464da167d3c7102fbaaeec0c5" >Settings</a>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="logout-form" action="/logout" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="pjkebu/2wMtSE2+/IMTP50rUv9oN7Z2YOh+vSyTcoPtGLxpL9dgLw/MrRJHWJJCDxa6ox8k0YrgGzkmKxg2g4A==" />
      
      <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout" data-hydro-click="{&quot;event_type&quot;:&quot;global_header.user_menu_dropdown.click&quot;,&quot;payload&quot;:{&quot;request_url&quot;:&quot;https://github.com/jackfrued/Python-Interview-Bible/blob/master/Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md&quot;,&quot;target&quot;:&quot;SIGN_OUT&quot;,&quot;originating_url&quot;:&quot;https://github.com/jackfrued/Python-Interview-Bible/blob/master/Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md&quot;,&quot;user_id&quot;:39375246}}" data-hydro-click-hmac="9f246bee518ff7464a0dc39b61b1bbda42cabcc63a4eae52a1582864ba782a1b"  role="menuitem">
        Sign out
      </button>
      <input type="text" name="required_field_e8b5" hidden="hidden" class="form-control" /><input type="hidden" name="timestamp" value="1595924749924" class="form-control" /><input type="hidden" name="timestamp_secret" value="1560e5c3664b09a196dbad266d2618364c2a2fe8b914760dfb217da05f950a73" class="form-control" />
</form>  </details-menu>
</details>

  </div>

</header>

          

    </div>

  <div id="start-of-content" class="show-on-focus"></div>




    <div id="js-flash-container">


  <template class="js-flash-template">
    <div class="flash flash-full  js-flash-template-container">
  <div class=" px-2" >
    <button class="flash-close js-flash-close" type="button" aria-label="Dismiss this message">
      <svg class="octicon octicon-x" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path></svg>
    </button>
    
      <div class="js-flash-template-message"></div>

  </div>
</div>
  </template>
</div>


  

  <include-fragment class="js-notification-shelf-include-fragment" data-base-src="https://github.com/notifications/beta/shelf"></include-fragment>



  <div
    class="application-main "
    data-commit-hovercards-enabled
    data-discussion-hovercards-enabled
    data-issue-and-pr-hovercards-enabled
  >
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main  >
      

  










  <div class="bg-gray-light pt-3 hide-full-screen mb-5">

    <div class="d-flex mb-3 px-3 px-md-4 px-lg-5">

      <div class="flex-auto min-width-0 width-fit mr-3">
        <h1 class=" d-flex flex-wrap flex-items-center break-word f3 text-normal">
    <svg class="octicon octicon-repo text-gray" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"></path></svg>
  <span class="author ml-2 flex-self-stretch" itemprop="author">
    <a class="url fn" rel="author" data-hovercard-type="user" data-hovercard-url="/users/jackfrued/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/jackfrued">jackfrued</a>
  </span>
  <span class="mx-1 flex-self-stretch">/</span>
  <strong itemprop="name" class="mr-2 flex-self-stretch">
    <a data-pjax="#js-repo-pjax-container" href="/jackfrued/Python-Interview-Bible">Python-Interview-Bible</a>
  </strong>
  
</h1>


      </div>

      <ul class="pagehead-actions flex-shrink-0 d-none d-md-inline" style="padding: 2px 0;">

  <li>
        <form data-remote="true" class="d-flex js-social-form js-social-container" action="/notifications/subscribe" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="XixKm8STzHFnryf3P0BEqw0JAhI+c/erNo+HjmZjTleKUbmZodSS8v5u6qk5hA9MDDe0VLAD4TlvnLLqFfjKyA==" />      <input type="hidden" name="repository_id" value="259815382">

      <details class="details-reset details-overlay select-menu hx_rsm">
        <summary class="btn btn-sm btn-with-count" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;WATCH_BUTTON&quot;,&quot;repository_id&quot;:259815382,&quot;originating_url&quot;:&quot;https://github.com/jackfrued/Python-Interview-Bible/blob/master/Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md&quot;,&quot;user_id&quot;:39375246}}" data-hydro-click-hmac="dad562b3267883d962e018c8bce67c94036350a7a01b4c083ff32d9333782b1a" data-ga-click="Repository, click Watch settings, action:blob#show">          <span data-menu-button>
              <svg height="16" class="octicon octicon-eye" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.679 7.932c.412-.621 1.242-1.75 2.366-2.717C5.175 4.242 6.527 3.5 8 3.5c1.473 0 2.824.742 3.955 1.715 1.124.967 1.954 2.096 2.366 2.717a.119.119 0 010 .136c-.412.621-1.242 1.75-2.366 2.717C10.825 11.758 9.473 12.5 8 12.5c-1.473 0-2.824-.742-3.955-1.715C2.92 9.818 2.09 8.69 1.679 8.068a.119.119 0 010-.136zM8 2c-1.981 0-3.67.992-4.933 2.078C1.797 5.169.88 6.423.43 7.1a1.619 1.619 0 000 1.798c.45.678 1.367 1.932 2.637 3.024C4.329 13.008 6.019 14 8 14c1.981 0 3.67-.992 4.933-2.078 1.27-1.091 2.187-2.345 2.637-3.023a1.619 1.619 0 000-1.798c-.45-.678-1.367-1.932-2.637-3.023C11.671 2.992 9.981 2 8 2zm0 8a2 2 0 100-4 2 2 0 000 4z"></path></svg>
              Watch
          </span>
          <span class="dropdown-caret"></span>
</summary>        <details-menu
          class="select-menu-modal position-absolute mt-5"
          style="z-index: 99;">
          <div class="select-menu-header">
            <span class="select-menu-title">Notifications</span>
          </div>
          <div class="select-menu-list">
            <button type="submit" name="do" value="included" class="select-menu-item width-full" aria-checked="true" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" height="16" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Not watching</span>
                <span class="description">Be notified only when participating or @mentioned.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg height="16" class="octicon octicon-eye" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.679 7.932c.412-.621 1.242-1.75 2.366-2.717C5.175 4.242 6.527 3.5 8 3.5c1.473 0 2.824.742 3.955 1.715 1.124.967 1.954 2.096 2.366 2.717a.119.119 0 010 .136c-.412.621-1.242 1.75-2.366 2.717C10.825 11.758 9.473 12.5 8 12.5c-1.473 0-2.824-.742-3.955-1.715C2.92 9.818 2.09 8.69 1.679 8.068a.119.119 0 010-.136zM8 2c-1.981 0-3.67.992-4.933 2.078C1.797 5.169.88 6.423.43 7.1a1.619 1.619 0 000 1.798c.45.678 1.367 1.932 2.637 3.024C4.329 13.008 6.019 14 8 14c1.981 0 3.67-.992 4.933-2.078 1.27-1.091 2.187-2.345 2.637-3.023a1.619 1.619 0 000-1.798c-.45-.678-1.367-1.932-2.637-3.023C11.671 2.992 9.981 2 8 2zm0 8a2 2 0 100-4 2 2 0 000 4z"></path></svg>
                  Watch
                </span>
              </div>
            </button>

            <button type="submit" name="do" value="release_only" class="select-menu-item width-full" aria-checked="false" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" height="16" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Releases only</span>
                <span class="description">Be notified of new releases, and when participating or @mentioned.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg height="16" class="octicon octicon-eye" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.679 7.932c.412-.621 1.242-1.75 2.366-2.717C5.175 4.242 6.527 3.5 8 3.5c1.473 0 2.824.742 3.955 1.715 1.124.967 1.954 2.096 2.366 2.717a.119.119 0 010 .136c-.412.621-1.242 1.75-2.366 2.717C10.825 11.758 9.473 12.5 8 12.5c-1.473 0-2.824-.742-3.955-1.715C2.92 9.818 2.09 8.69 1.679 8.068a.119.119 0 010-.136zM8 2c-1.981 0-3.67.992-4.933 2.078C1.797 5.169.88 6.423.43 7.1a1.619 1.619 0 000 1.798c.45.678 1.367 1.932 2.637 3.024C4.329 13.008 6.019 14 8 14c1.981 0 3.67-.992 4.933-2.078 1.27-1.091 2.187-2.345 2.637-3.023a1.619 1.619 0 000-1.798c-.45-.678-1.367-1.932-2.637-3.023C11.671 2.992 9.981 2 8 2zm0 8a2 2 0 100-4 2 2 0 000 4z"></path></svg>
                  Unwatch releases
                </span>
              </div>
            </button>

            <button type="submit" name="do" value="subscribed" class="select-menu-item width-full" aria-checked="false" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" height="16" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Watching</span>
                <span class="description">Be notified of all conversations.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-eye v-align-text-bottom" height="16" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.679 7.932c.412-.621 1.242-1.75 2.366-2.717C5.175 4.242 6.527 3.5 8 3.5c1.473 0 2.824.742 3.955 1.715 1.124.967 1.954 2.096 2.366 2.717a.119.119 0 010 .136c-.412.621-1.242 1.75-2.366 2.717C10.825 11.758 9.473 12.5 8 12.5c-1.473 0-2.824-.742-3.955-1.715C2.92 9.818 2.09 8.69 1.679 8.068a.119.119 0 010-.136zM8 2c-1.981 0-3.67.992-4.933 2.078C1.797 5.169.88 6.423.43 7.1a1.619 1.619 0 000 1.798c.45.678 1.367 1.932 2.637 3.024C4.329 13.008 6.019 14 8 14c1.981 0 3.67-.992 4.933-2.078 1.27-1.091 2.187-2.345 2.637-3.023a1.619 1.619 0 000-1.798c-.45-.678-1.367-1.932-2.637-3.023C11.671 2.992 9.981 2 8 2zm0 8a2 2 0 100-4 2 2 0 000 4z"></path></svg>
                  Unwatch
                </span>
              </div>
            </button>

            <button type="submit" name="do" value="ignore" class="select-menu-item width-full" aria-checked="false" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" height="16" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Ignoring</span>
                <span class="description">Never be notified.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg height="16" class="octicon octicon-mute" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 2.75a.75.75 0 00-1.238-.57L3.472 5H1.75A1.75 1.75 0 000 6.75v2.5C0 10.216.784 11 1.75 11h1.723l3.289 2.82A.75.75 0 008 13.25V2.75zM4.238 6.32L6.5 4.38v7.24L4.238 9.68a.75.75 0 00-.488-.18h-2a.25.25 0 01-.25-.25v-2.5a.25.25 0 01.25-.25h2a.75.75 0 00.488-.18zm7.042-1.1a.75.75 0 10-1.06 1.06L11.94 8l-1.72 1.72a.75.75 0 101.06 1.06L13 9.06l1.72 1.72a.75.75 0 101.06-1.06L14.06 8l1.72-1.72a.75.75 0 00-1.06-1.06L13 6.94l-1.72-1.72z"></path></svg>
                  Stop ignoring
                </span>
              </div>
            </button>
          </div>
        </details-menu>
      </details>
        <a class="social-count js-social-count"
          href="/jackfrued/Python-Interview-Bible/watchers"
          aria-label="1 user is watching this repository">
          1
        </a>
</form>
  </li>

  <li>
      <div class="js-toggler-container js-social-container starring-container ">
    <form class="starred js-social-form" action="/jackfrued/Python-Interview-Bible/unstar" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="wmCibrMc61WCOwwSMx0kTGSP4Edy4bUfLfH663IKiNYzlCgPAKuXKkSu2Plw26Iko0XgIfOEGi3RqEjQtUFAjA==" />
      <input type="hidden" name="context" value="repository"></input>
      <button type="submit" class="btn btn-sm btn-with-count  js-toggler-target" aria-label="Unstar this repository" title="Unstar jackfrued/Python-Interview-Bible" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;UNSTAR_BUTTON&quot;,&quot;repository_id&quot;:259815382,&quot;originating_url&quot;:&quot;https://github.com/jackfrued/Python-Interview-Bible/blob/master/Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md&quot;,&quot;user_id&quot;:39375246}}" data-hydro-click-hmac="de49171bc6f44dffcdcab2a8f57c7ec8c1c3bd83d87789799b398dff4a9f8c98" data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">        <svg height="16" class="octicon octicon-star-fill" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25z"></path></svg>
        Unstar
</button>        <a class="social-count js-social-count" href="/jackfrued/Python-Interview-Bible/stargazers"
           aria-label="52 users starred this repository">
           52
        </a>
</form>
    <form class="unstarred js-social-form" action="/jackfrued/Python-Interview-Bible/star" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="yLvptLxv8DCow/lwCUlOapDZUoEkGa3i+YtKXHiW3guEReguqcooE5nCLsKytrTJaX4mRZryWskc4vhAc8s3Lw==" />
      <input type="hidden" name="context" value="repository"></input>
      <button type="submit" class="btn btn-sm btn-with-count  js-toggler-target" aria-label="Unstar this repository" title="Star jackfrued/Python-Interview-Bible" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;STAR_BUTTON&quot;,&quot;repository_id&quot;:259815382,&quot;originating_url&quot;:&quot;https://github.com/jackfrued/Python-Interview-Bible/blob/master/Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md&quot;,&quot;user_id&quot;:39375246}}" data-hydro-click-hmac="84e28502a1d48cc1a4f6eefbf6917a7376ac60107c7c73b3af71060c07922a97" data-ga-click="Repository, click star button, action:blob#show; text:Star">        <svg height="16" class="octicon octicon-star" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25zm0 2.445L6.615 5.5a.75.75 0 01-.564.41l-3.097.45 2.24 2.184a.75.75 0 01.216.664l-.528 3.084 2.769-1.456a.75.75 0 01.698 0l2.77 1.456-.53-3.084a.75.75 0 01.216-.664l2.24-2.183-3.096-.45a.75.75 0 01-.564-.41L8 2.694v.001z"></path></svg>
        Star
</button>        <a class="social-count js-social-count" href="/jackfrued/Python-Interview-Bible/stargazers"
           aria-label="52 users starred this repository">
          52
        </a>
</form>  </div>

  </li>

  <li>
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="btn-with-count" action="/jackfrued/Python-Interview-Bible/fork" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="u3sHbm1UZQYy9VUJRgPnpqUxv4gjojk+1iqAGYBZVxRA0MwWp8tWPF3Zf/ouCVt3ahf6dPGF12YL4XtNMM++jg==" />
            <button class="btn btn-sm btn-with-count" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;FORK_BUTTON&quot;,&quot;repository_id&quot;:259815382,&quot;originating_url&quot;:&quot;https://github.com/jackfrued/Python-Interview-Bible/blob/master/Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md&quot;,&quot;user_id&quot;:39375246}}" data-hydro-click-hmac="224314ecbec2ba77e6884e2550a7fc89cb625c4db0088bb5af737c591bdc976f" data-ga-click="Repository, show fork modal, action:blob#show; text:Fork" type="submit" title="Fork your own copy of jackfrued/Python-Interview-Bible to your account" aria-label="Fork your own copy of jackfrued/Python-Interview-Bible to your account">              <svg class="octicon octicon-repo-forked" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0 2.122a2.25 2.25 0 10-1.5 0v.878A2.25 2.25 0 005.75 8.5h1.5v2.128a2.251 2.251 0 101.5 0V8.5h1.5a2.25 2.25 0 002.25-2.25v-.878a2.25 2.25 0 10-1.5 0v.878a.75.75 0 01-.75.75h-4.5A.75.75 0 015 6.25v-.878zm3.75 7.378a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm3-8.75a.75.75 0 100-1.5.75.75 0 000 1.5z"></path></svg>
              Fork
</button></form>
    <a href="/jackfrued/Python-Interview-Bible/network/members" class="social-count"
       aria-label="12 users forked this repository">
      12
    </a>
  </li>
</ul>

    </div>
    
<nav class="js-repo-nav js-sidenav-container-pjax js-responsive-underlinenav overflow-hidden UnderlineNav px-3 px-md-4 px-lg-5 bg-gray-light" aria-label="Repository" data-pjax="#js-repo-pjax-container">
  <ul class="UnderlineNav-body list-style-none ">
          <li class="d-flex">
        <a class="js-selected-navigation-item selected UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item" data-tab-item="code-tab" data-hotkey="g c" data-ga-click="Repository, Navigation click, Code tab" aria-current="page" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments /jackfrued/Python-Interview-Bible" href="/jackfrued/Python-Interview-Bible">
              <svg classes="UnderlineNav-octicon" display="none inline" height="16" class="octicon octicon-code UnderlineNav-octicon d-none d-sm-inline" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M4.72 3.22a.75.75 0 011.06 1.06L2.06 8l3.72 3.72a.75.75 0 11-1.06 1.06L.47 8.53a.75.75 0 010-1.06l4.25-4.25zm6.56 0a.75.75 0 10-1.06 1.06L13.94 8l-3.72 3.72a.75.75 0 101.06 1.06l4.25-4.25a.75.75 0 000-1.06l-4.25-4.25z"></path></svg>
            <span data-content="Code">Code</span>
              <span class="Counter " title="Not available"></span>
</a>      </li>
      <li class="d-flex">
        <a class="js-selected-navigation-item UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item" data-tab-item="issues-tab" data-hotkey="g i" data-ga-click="Repository, Navigation click, Issues tab" data-selected-links="repo_issues repo_labels repo_milestones /jackfrued/Python-Interview-Bible/issues" href="/jackfrued/Python-Interview-Bible/issues">
              <svg classes="UnderlineNav-octicon" display="none inline" height="16" class="octicon octicon-issue-opened UnderlineNav-octicon d-none d-sm-inline" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm9 3a1 1 0 11-2 0 1 1 0 012 0zm-.25-6.25a.75.75 0 00-1.5 0v3.5a.75.75 0 001.5 0v-3.5z"></path></svg>
            <span data-content="Issues">Issues</span>
              <span class="Counter " title="0" hidden="hidden">0</span>
</a>      </li>
      <li class="d-flex">
        <a class="js-selected-navigation-item UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item" data-tab-item="pull-requests-tab" data-hotkey="g p" data-ga-click="Repository, Navigation click, Pull requests tab" data-selected-links="repo_pulls checks /jackfrued/Python-Interview-Bible/pulls" href="/jackfrued/Python-Interview-Bible/pulls">
              <svg classes="UnderlineNav-octicon" display="none inline" height="16" class="octicon octicon-git-pull-request UnderlineNav-octicon d-none d-sm-inline" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.177 3.073L9.573.677A.25.25 0 0110 .854v4.792a.25.25 0 01-.427.177L7.177 3.427a.25.25 0 010-.354zM3.75 2.5a.75.75 0 100 1.5.75.75 0 000-1.5zm-2.25.75a2.25 2.25 0 113 2.122v5.256a2.251 2.251 0 11-1.5 0V5.372A2.25 2.25 0 011.5 3.25zM11 2.5h-1V4h1a1 1 0 011 1v5.628a2.251 2.251 0 101.5 0V5A2.5 2.5 0 0011 2.5zm1 10.25a.75.75 0 111.5 0 .75.75 0 01-1.5 0zM3.75 12a.75.75 0 100 1.5.75.75 0 000-1.5z"></path></svg>
            <span data-content="Pull requests">Pull requests</span>
              <span class="Counter " title="0" hidden="hidden">0</span>
</a>      </li>
      <li class="d-flex">
        <a class="js-selected-navigation-item UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item" data-tab-item="actions-tab" data-hotkey="g w" data-ga-click="Repository, Navigation click, Actions tab" data-selected-links="repo_actions /jackfrued/Python-Interview-Bible/actions" href="/jackfrued/Python-Interview-Bible/actions">
              <svg classes="UnderlineNav-octicon" display="none inline" height="16" class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 8a6.5 6.5 0 1113 0 6.5 6.5 0 01-13 0zM8 0a8 8 0 100 16A8 8 0 008 0zM6.379 5.227A.25.25 0 006 5.442v5.117a.25.25 0 00.379.214l4.264-2.559a.25.25 0 000-.428L6.379 5.227z"></path></svg>
            <span data-content="Actions">Actions</span>
              <span class="Counter " title="Not available"></span>
</a>      </li>
      <li class="d-flex">
        <a class="js-selected-navigation-item UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item" data-tab-item="projects-tab" data-hotkey="g b" data-ga-click="Repository, Navigation click, Projects tab" data-selected-links="repo_projects new_repo_project repo_project /jackfrued/Python-Interview-Bible/projects" href="/jackfrued/Python-Interview-Bible/projects">
              <svg classes="UnderlineNav-octicon" display="none inline" height="16" class="octicon octicon-project UnderlineNav-octicon d-none d-sm-inline" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z"></path></svg>
            <span data-content="Projects">Projects</span>
              <span class="Counter " title="0" hidden="hidden">0</span>
</a>      </li>
      <li class="d-flex">
        <a class="js-selected-navigation-item UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item" data-tab-item="wiki-tab" data-ga-click="Repository, Navigation click, Wikis tab" data-selected-links="repo_wiki /jackfrued/Python-Interview-Bible/wiki" href="/jackfrued/Python-Interview-Bible/wiki">
              <svg classes="UnderlineNav-octicon" display="none inline" height="16" class="octicon octicon-book UnderlineNav-octicon d-none d-sm-inline" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 1.75A.75.75 0 01.75 1h4.253c1.227 0 2.317.59 3 1.501A3.744 3.744 0 0111.006 1h4.245a.75.75 0 01.75.75v10.5a.75.75 0 01-.75.75h-4.507a2.25 2.25 0 00-1.591.659l-.622.621a.75.75 0 01-1.06 0l-.622-.621A2.25 2.25 0 005.258 13H.75a.75.75 0 01-.75-.75V1.75zm8.755 3a2.25 2.25 0 012.25-2.25H14.5v9h-3.757c-.71 0-1.4.201-1.992.572l.004-7.322zm-1.504 7.324l.004-5.073-.002-2.253A2.25 2.25 0 005.003 2.5H1.5v9h3.757a3.75 3.75 0 011.994.574z"></path></svg>
            <span data-content="Wiki">Wiki</span>
              <span class="Counter " title="Not available"></span>
</a>      </li>
      <li class="d-flex">
        <a class="js-selected-navigation-item UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item" data-tab-item="security-tab" data-hotkey="g s" data-ga-click="Repository, Navigation click, Security tab" data-selected-links="security overview alerts policy token_scanning code_scanning /jackfrued/Python-Interview-Bible/security" href="/jackfrued/Python-Interview-Bible/security">
              <svg classes="UnderlineNav-octicon" display="none inline" height="16" class="octicon octicon-shield UnderlineNav-octicon d-none d-sm-inline" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.467.133a1.75 1.75 0 011.066 0l5.25 1.68A1.75 1.75 0 0115 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.7 1.7 0 01-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 011.217-1.667l5.25-1.68zm.61 1.429a.25.25 0 00-.153 0l-5.25 1.68a.25.25 0 00-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.2.2 0 00.154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.25.25 0 00-.174-.237l-5.25-1.68zM9 10.5a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.75a.75.75 0 10-1.5 0v3a.75.75 0 001.5 0v-3z"></path></svg>
            <span data-content="Security">Security</span>
              <span class="js-security-tab-count Counter " data-url="/jackfrued/Python-Interview-Bible/security/overall-count" title="Not available"></span>
</a>      </li>
      <li class="d-flex">
        <a class="js-selected-navigation-item UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item" data-tab-item="insights-tab" data-ga-click="Repository, Navigation click, Insights tab" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people /jackfrued/Python-Interview-Bible/pulse" href="/jackfrued/Python-Interview-Bible/pulse">
              <svg classes="UnderlineNav-octicon" display="none inline" height="16" class="octicon octicon-graph UnderlineNav-octicon d-none d-sm-inline" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 1.75a.75.75 0 00-1.5 0v12.5c0 .414.336.75.75.75h14.5a.75.75 0 000-1.5H1.5V1.75zm14.28 2.53a.75.75 0 00-1.06-1.06L10 7.94 7.53 5.47a.75.75 0 00-1.06 0L3.22 8.72a.75.75 0 001.06 1.06L7 7.06l2.47 2.47a.75.75 0 001.06 0l5.25-5.25z"></path></svg>
            <span data-content="Insights">Insights</span>
              <span class="Counter " title="Not available"></span>
</a>      </li>

</ul>        <div class="position-absolute right-0 pr-3 pr-md-4 pr-lg-5 js-responsive-underlinenav-overflow" style="visibility:hidden;">
      <details class="details-overlay details-reset position-relative">
  <summary role="button">
              <div class="UnderlineNav-item mr-0 border-0">
            <svg class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="M8 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm13 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"></path></svg>
            <span class="sr-only">More</span>
          </div>

</summary>            <details-menu class="dropdown-menu dropdown-menu-sw " role="menu">
  
            <ul>
                <li data-menu-item="code-tab" hidden>
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links=" /jackfrued/Python-Interview-Bible" href="/jackfrued/Python-Interview-Bible">
                    Code
</a>                </li>
                <li data-menu-item="issues-tab" hidden>
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links=" /jackfrued/Python-Interview-Bible/issues" href="/jackfrued/Python-Interview-Bible/issues">
                    Issues
</a>                </li>
                <li data-menu-item="pull-requests-tab" hidden>
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links=" /jackfrued/Python-Interview-Bible/pulls" href="/jackfrued/Python-Interview-Bible/pulls">
                    Pull requests
</a>                </li>
                <li data-menu-item="actions-tab" hidden>
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links=" /jackfrued/Python-Interview-Bible/actions" href="/jackfrued/Python-Interview-Bible/actions">
                    Actions
</a>                </li>
                <li data-menu-item="projects-tab" hidden>
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links=" /jackfrued/Python-Interview-Bible/projects" href="/jackfrued/Python-Interview-Bible/projects">
                    Projects
</a>                </li>
                <li data-menu-item="wiki-tab" hidden>
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links=" /jackfrued/Python-Interview-Bible/wiki" href="/jackfrued/Python-Interview-Bible/wiki">
                    Wiki
</a>                </li>
                <li data-menu-item="security-tab" hidden>
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links=" /jackfrued/Python-Interview-Bible/security" href="/jackfrued/Python-Interview-Bible/security">
                    Security
</a>                </li>
                <li data-menu-item="insights-tab" hidden>
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links=" /jackfrued/Python-Interview-Bible/pulse" href="/jackfrued/Python-Interview-Bible/pulse">
                    Insights
</a>                </li>
            </ul>

</details-menu>
</details>    </div>

</nav>
  </div>

<div class="container-xl clearfix new-discussion-timeline  px-3 px-md-4 px-lg-5">
  <div class="repository-content " >

    
    

  


    <a class="d-none js-permalink-shortcut" data-hotkey="y" href="/jackfrued/Python-Interview-Bible/blob/4d5aae2fca81b104d399be7f42b6efc4cbe24c4d/Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md">Permalink</a>

    <!-- blob contrib key: blob_contributors:v22:4106d373aa9a247abd53c29dcbd32e65 -->
    

    <div class="d-flex flex-items-start flex-shrink-0 pb-3 flex-wrap flex-md-nowrap flex-justify-between flex-md-justify-start">
      
<details class="details-reset details-overlay mr-0 mb-0 " id="branch-select-menu">
  <summary class="btn css-truncate"
           data-hotkey="w"
           title="Switch branches or tags">
    <svg text="gray" height="16" class="octicon octicon-git-branch text-gray" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M11.75 2.5a.75.75 0 100 1.5.75.75 0 000-1.5zm-2.25.75a2.25 2.25 0 113 2.122V6A2.5 2.5 0 0110 8.5H6a1 1 0 00-1 1v1.128a2.251 2.251 0 11-1.5 0V5.372a2.25 2.25 0 111.5 0v1.836A2.492 2.492 0 016 7h4a1 1 0 001-1v-.628A2.25 2.25 0 019.5 3.25zM4.25 12a.75.75 0 100 1.5.75.75 0 000-1.5zM3.5 3.25a.75.75 0 111.5 0 .75.75 0 01-1.5 0z"></path></svg>
    <span class="css-truncate-target" data-menu-button>master</span>
    <span class="dropdown-caret"></span>
  </summary>

  <details-menu class="SelectMenu SelectMenu--hasFilter" src="/jackfrued/Python-Interview-Bible/refs/master/Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md?source_action=show&amp;source_controller=blob" preload>
    <div class="SelectMenu-modal">
      <include-fragment class="SelectMenu-loading" aria-label="Menu is loading">
        <svg class="octicon octicon-octoface anim-pulse" height="32" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M14.7 5.34c.13-.32.55-1.59-.13-3.31 0 0-1.05-.33-3.44 1.3-1-.28-2.07-.32-3.13-.32s-2.13.04-3.13.32c-2.39-1.64-3.44-1.3-3.44-1.3-.68 1.72-.26 2.99-.13 3.31C.49 6.21 0 7.33 0 8.69 0 13.84 3.33 15 7.98 15S16 13.84 16 8.69c0-1.36-.49-2.48-1.3-3.35zM8 14.02c-3.3 0-5.98-.15-5.98-3.35 0-.76.38-1.48 1.02-2.07 1.07-.98 2.9-.46 4.96-.46 2.07 0 3.88-.52 4.96.46.65.59 1.02 1.3 1.02 2.07 0 3.19-2.68 3.35-5.98 3.35zM5.49 9.01c-.66 0-1.2.8-1.2 1.78s.54 1.79 1.2 1.79c.66 0 1.2-.8 1.2-1.79s-.54-1.78-1.2-1.78zm5.02 0c-.66 0-1.2.79-1.2 1.78s.54 1.79 1.2 1.79c.66 0 1.2-.8 1.2-1.79s-.53-1.78-1.2-1.78z"></path></svg>
      </include-fragment>
    </div>
  </details-menu>
</details>

      <h2 id="blob-path" class="breadcrumb flex-auto min-width-0 text-normal mx-0 mx-md-3 width-full width-md-auto flex-order-1 flex-md-order-none mt-3 mt-md-0">
        <span class="js-repo-root text-bold"><span class="js-path-segment d-inline-block wb-break-all"><a data-pjax="true" href="/jackfrued/Python-Interview-Bible"><span>Python-Interview-Bible</span></a></span></span><span class="separator">/</span><strong class="final-path">Python面试宝典-基础篇-2020.md</strong>
      </h2>
      <a href="/jackfrued/Python-Interview-Bible/find/master"
            class="js-pjax-capture-input btn mr-2 d-none d-md-block"
            data-pjax
            data-hotkey="t">
        Go to file
      </a>

      <details class="details-overlay details-reset position-relative" id="blob-more-options-details">
  <summary role="button">
              <span class="btn">
            <svg aria-label="More options" height="16" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" version="1.1" width="16" role="img"><path d="M8 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm13 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"></path></svg>
          </span>

</summary>            <ul class="dropdown-menu dropdown-menu-sw">
            <li class="d-block d-md-none">
              <a class="dropdown-item d-flex flex-items-baseline" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;FIND_FILE_BUTTON&quot;,&quot;repository_id&quot;:259815382,&quot;originating_url&quot;:&quot;https://github.com/jackfrued/Python-Interview-Bible/blob/master/Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md&quot;,&quot;user_id&quot;:39375246}}" data-hydro-click-hmac="0c9fffdce893b3b2f66472ad039f09e38cbe5571d2ca7af485a102be3c0e2f0d" data-ga-click="Repository, find file, location:repo overview" data-hotkey="t" data-pjax="true" href="/jackfrued/Python-Interview-Bible/find/master">
                <span class="flex-auto">Go to file</span>
                <span class="text-small text-gray" aria-hidden="true">T</span>
</a>            </li>
            <li data-toggle-for="blob-more-options-details">
              <button type="button" data-toggle-for="jumpto-line-details-dialog" class="btn-link dropdown-item">
                <span class="d-flex flex-items-baseline">
                  <span class="flex-auto">Go to line</span>
                  <span class="text-small text-gray" aria-hidden="true">L</span>
                </span>
              </button>
            </li>
            <li class="dropdown-divider" role="none"></li>
            <li>
              <clipboard-copy value="Python面试宝典-基础篇-2020.md" class="dropdown-item cursor-pointer" data-toggle-for="blob-more-options-details">
                Copy path
              </clipboard-copy>
            </li>
          </ul>

</details>    </div>



    <div class="Box d-flex flex-column flex-shrink-0 mb-3">
      <include-fragment src="/jackfrued/Python-Interview-Bible/contributors/master/Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md" class="commit-loader">
        <div class="Box-header Box-header--blue d-flex flex-items-center">
          <div class="Skeleton avatar avatar-user flex-shrink-0 ml-n1 mr-n1 mt-n1 mb-n1" style="width:24px;height:24px;"></div>
          <div class="Skeleton Skeleton--text col-5 ml-2">&nbsp;</div>
        </div>

        <div class="Box-body d-flex flex-items-center" >
          <div class="Skeleton Skeleton--text col-1">&nbsp;</div>
          <span class="text-red h6 loader-error">Cannot retrieve contributors at this time</span>
        </div>
</include-fragment>    </div>






    <div class="Box mt-3 position-relative
      ">
      
<div class="Box-header py-2 d-flex flex-column flex-shrink-0 flex-md-row flex-md-items-center">
  <div class="text-mono f6 flex-auto pr-3 flex-order-2 flex-md-order-1 mt-2 mt-md-0">

      1335 lines (975 sloc)
      <span class="file-info-divider"></span>
    72.3 KB
  </div>

  <div class="d-flex py-1 py-md-0 flex-auto flex-order-1 flex-md-order-2 flex-sm-grow-0 flex-justify-between">

    <div class="BtnGroup">
      <a class="btn btn-sm BtnGroup-item " href="/jackfrued/Python-Interview-Bible/raw/master/Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md" id="raw-url" role="button">Raw</a>
        <a class="btn js-update-url-with-hash btn-sm BtnGroup-item " href="/jackfrued/Python-Interview-Bible/blame/master/Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md" data-hotkey="b" role="button">Blame</a>
    </div>

    <div>
          <a class="btn-octicon tooltipped tooltipped-nw js-remove-unless-platform"
             data-platforms="windows,mac"
             href="x-github-client://openRepo/https://github.com/jackfrued/Python-Interview-Bible?branch=master&amp;filepath=Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md"
             aria-label="Open this file in GitHub Desktop"
             data-ga-click="Repository, open with desktop">
              <svg class="octicon octicon-device-desktop" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.75 2.5h12.5a.25.25 0 01.25.25v7.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25v-7.5a.25.25 0 01.25-.25zM14.25 1H1.75A1.75 1.75 0 000 2.75v7.5C0 11.216.784 12 1.75 12h3.727c-.1 1.041-.52 1.872-1.292 2.757A.75.75 0 004.75 16h6.5a.75.75 0 00.565-1.243c-.772-.885-1.193-1.716-1.292-2.757h3.727A1.75 1.75 0 0016 10.25v-7.5A1.75 1.75 0 0014.25 1zM9.018 12H6.982a5.72 5.72 0 01-.765 2.5h3.566a5.72 5.72 0 01-.765-2.5z"></path></svg>
          </a>

          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="inline-form js-update-url-with-hash" action="/jackfrued/Python-Interview-Bible/edit/master/Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="t3g+TbqT1UrnIatPKYaO4JGnn/yRXz/x04rAAtwdrOvtItTlwzlngPfXwIBsqSDHK8ydNqb1ihgkf/BgF0zA5A==" />
            <button class="btn-octicon tooltipped tooltipped-nw" type="submit"
              aria-label="Fork this project and edit the file" data-hotkey="e" data-disable-with>
              <svg class="octicon octicon-pencil" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11.013 1.427a1.75 1.75 0 012.474 0l1.086 1.086a1.75 1.75 0 010 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 01-.927-.928l.929-3.25a1.75 1.75 0 01.445-.758l8.61-8.61zm1.414 1.06a.25.25 0 00-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 000-.354l-1.086-1.086zM11.189 6.25L9.75 4.81l-6.286 6.287a.25.25 0 00-.064.108l-.558 1.953 1.953-.558a.249.249 0 00.108-.064l6.286-6.286z"></path></svg>
            </button>
</form>
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="inline-form" action="/jackfrued/Python-Interview-Bible/delete/master/Python%E9%9D%A2%E8%AF%95%E5%AE%9D%E5%85%B8-%E5%9F%BA%E7%A1%80%E7%AF%87-2020.md" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="1qW/Fd7QdcHiedIckylbIu0zn7/781d2D0jHlqmjhf8EcfhdS+xMTT+CJ+sSAEVEfAF899F2bOA3Pi29NcGcEw==" />
            <button class="btn-octicon btn-octicon-danger tooltipped tooltipped-nw" type="submit"
              aria-label="Fork this project and delete the file" data-disable-with>
              <svg class="octicon octicon-trashcan" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M6.5 1.75a.25.25 0 01.25-.25h2.5a.25.25 0 01.25.25V3h-3V1.75zm4.5 0V3h2.25a.75.75 0 010 1.5H2.75a.75.75 0 010-1.5H5V1.75C5 .784 5.784 0 6.75 0h2.5C10.216 0 11 .784 11 1.75zM4.496 6.675a.75.75 0 10-1.492.15l.66 6.6A1.75 1.75 0 005.405 15h5.19c.9 0 1.652-.681 1.741-1.576l.66-6.6a.75.75 0 00-1.492-.149l-.66 6.6a.25.25 0 01-.249.225h-5.19a.25.25 0 01-.249-.225l-.66-6.6z"></path></svg>
            </button>
</form>    </div>
  </div>
</div>



      
  <div id="readme" class="Box-body readme blob js-code-block-container p-5 p-xl-6">
    <article class="markdown-body entry-content container-lg" itemprop="text"><h2><a id="user-content-python面试宝典---基础篇---2020" class="anchor" aria-hidden="true" href="#python面试宝典---基础篇---2020"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Python面试宝典 - 基础篇 - 2020</h2>
<h4><a id="user-content-题目001-在python中如何实现单例模式" class="anchor" aria-hidden="true" href="#题目001-在python中如何实现单例模式"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目001: 在Python中如何实现单例模式。</h4>
<blockquote>
<p><strong>点评</strong>：单例模式是指让一个类只能创建出唯一的实例，这个题目在面试中出现的频率极高，因为它考察的不仅仅是单例模式，更是对Python语言到底掌握到何种程度，建议大家用装饰器和元类这两种方式来实现单例模式，因为这两种方式的通用性最强，而且也可以顺便展示自己对装饰器和元类中两个关键知识点的理解。</p>
</blockquote>
<p>方法一：使用装饰器实现单例模式。</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">from</span> <span class="pl-s1">functools</span> <span class="pl-k">import</span> <span class="pl-s1">wraps</span>


<span class="pl-k">def</span> <span class="pl-en">singleton</span>(<span class="pl-s1">cls</span>):
    <span class="pl-s">"""单例类装饰器"""</span>
    <span class="pl-s1">instances</span> <span class="pl-c1">=</span> {}

    <span class="pl-en">@<span class="pl-s1">wraps</span>(<span class="pl-s1">cls</span>)</span>
    <span class="pl-k">def</span> <span class="pl-en">wrapper</span>(<span class="pl-c1">*</span><span class="pl-s1">args</span>, <span class="pl-c1">**</span><span class="pl-s1">kwargs</span>):
        <span class="pl-k">if</span> <span class="pl-s1">cls</span> <span class="pl-c1">not</span> <span class="pl-c1">in</span> <span class="pl-s1">instances</span>:
            <span class="pl-s1">instances</span>[<span class="pl-s1">cls</span>] <span class="pl-c1">=</span> <span class="pl-en">cls</span>(<span class="pl-c1">*</span><span class="pl-s1">args</span>, <span class="pl-c1">**</span><span class="pl-s1">kwargs</span>)
        <span class="pl-k">return</span> <span class="pl-s1">instances</span>[<span class="pl-s1">cls</span>]

    <span class="pl-k">return</span> <span class="pl-s1">wrapper</span>


<span class="pl-en">@<span class="pl-s1">singleton</span></span>
<span class="pl-k">class</span> <span class="pl-v">President</span>:
    <span class="pl-k">pass</span></pre></div>
<blockquote>
<p><strong>扩展</strong>：装饰器是Python中非常有特色的语法，用一个函数去装饰另一个函数或类，为其添加额外的能力。通常通过装饰来实现的功能都属横切关注功能，也就是跟正常的业务逻辑没有必然联系，可以动态添加或移除的功能。装饰器可以为代码提供缓存、代理、上下文环境等服务，它是对设计模式中代理模式的践行。在写装饰器的时候，带装饰功能的函数（上面代码中的<code>wrapper</code>函数）通常都会用<code>functools</code>模块中的<code>wraps</code>再加以装饰，这个装饰器最重要的作用是给被装饰的类或函数动态添加一个<code>__wrapped__</code>属性，这个属性会将被装饰之前的类或函数保留下来，这样在我们不需要装饰功能的时候，可以通过它来取消装饰器，例如可以使用<code>President = President.__wrapped__</code>来取消对<code>President</code>类做的单例处理。需要提醒大家的是：上面的单例并不是线程安全的，如果要做到线程安全，需要对创建对象的代码进行加锁的处理。在Python中可以使用<code>threading</code>模块的<code>RLock</code>对象来提供锁，可以使用锁对象的<code>acquire</code>和<code>release</code>方法来实现加锁和解锁的操作。当然，更为简便的做法是使用锁对象的<code>with</code>上下文语法来进行隐式的加锁和解锁操作。</p>
</blockquote>
<p>方法二：使用元类实现单例模式。</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">class</span> <span class="pl-v">SingletonMeta</span>(<span class="pl-s1">type</span>):
    <span class="pl-s">"""自定义单例元类"""</span>

    <span class="pl-k">def</span> <span class="pl-en">__init__</span>(<span class="pl-s1">cls</span>, <span class="pl-c1">*</span><span class="pl-s1">args</span>, <span class="pl-c1">**</span><span class="pl-s1">kwargs</span>):
        <span class="pl-s1">cls</span>.<span class="pl-s1">__instance</span> <span class="pl-c1">=</span> <span class="pl-c1">None</span>
        <span class="pl-en">super</span>().<span class="pl-en">__init__</span>(<span class="pl-c1">*</span><span class="pl-s1">args</span>, <span class="pl-c1">**</span><span class="pl-s1">kwargs</span>)

    <span class="pl-k">def</span> <span class="pl-en">__call__</span>(<span class="pl-s1">cls</span>, <span class="pl-c1">*</span><span class="pl-s1">args</span>, <span class="pl-c1">**</span><span class="pl-s1">kwargs</span>):
        <span class="pl-k">if</span> <span class="pl-s1">cls</span>.<span class="pl-s1">__instance</span> <span class="pl-c1">is</span> <span class="pl-c1">None</span>:
            <span class="pl-s1">cls</span>.<span class="pl-s1">__instance</span> <span class="pl-c1">=</span> <span class="pl-en">super</span>().<span class="pl-en">__call__</span>(<span class="pl-c1">*</span><span class="pl-s1">args</span>, <span class="pl-c1">**</span><span class="pl-s1">kwargs</span>)
        <span class="pl-k">return</span> <span class="pl-s1">cls</span>.<span class="pl-s1">__instance</span>


<span class="pl-k">class</span> <span class="pl-v">President</span>(<span class="pl-s1">metaclass</span><span class="pl-c1">=</span><span class="pl-v">SingletonMeta</span>):
    <span class="pl-k">pass</span></pre></div>
<blockquote>
<p><strong>扩展</strong>：Python是面向对象的编程语言，在面向对象的世界中，一切皆为对象。对象是通过类来创建的，而类本身也是对象，类这样的对象是通过元类来创建的。我们在定义类时，如果没有给一个类指定父类，那么默认的父类是<code>object</code>，如果没有给一个类指定元类，那么默认的元类是<code>type</code>。通过自定义的元类，我们可以改变一个类默认的行为，就如同上面的代码中，我们通过元类的<code>__call__</code>魔术方法，改变了<code>President</code>类的构造器那样。</p>
</blockquote>
<blockquote>
<p><strong>补充</strong>：关于单例模式，在面试中还有可能被问到它的应用场景。通常一个对象的状态是被其他对象共享的，就可以将其设计为单例，例如项目中使用的数据库连接池对象和配置对象通常都是单例，这样才能保证所有地方获取到的数据库连接和配置信息是完全一致的；而且由于对象只有唯一的实例，因此从根本上避免了重复创建对象造成的时间和空间上的开销，也避免了对资源的多重占用。再举个例子，项目中的日志操作通常也会使用单例模式，这是因为共享的日志文件一直处于打开状态，只能有一个实例去操作它，否则在写入日志的时候会产生混乱。</p>
</blockquote>
<h4><a id="user-content-题目002不使用中间变量交换两个变量a和b的值" class="anchor" aria-hidden="true" href="#题目002不使用中间变量交换两个变量a和b的值"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目002：不使用中间变量，交换两个变量<code>a</code>和<code>b</code>的值。</h4>
<blockquote>
<p><strong>点评</strong>：典型的送人头的题目，通常交换两个变量需要借助一个中间变量，如果不允许使用中间变量，在其他编程语言中可以使用异或运算的方式来实现交换两个变量的值，但是Python中有更为简单明了的做法。</p>
</blockquote>
<p>方法一：</p>
<div class="highlight highlight-source-python"><pre><span class="pl-s1">a</span> <span class="pl-c1">=</span> <span class="pl-s1">a</span> <span class="pl-c1">^</span> <span class="pl-s1">b</span>
<span class="pl-s1">b</span> <span class="pl-c1">=</span> <span class="pl-s1">a</span> <span class="pl-c1">^</span> <span class="pl-s1">b</span>
<span class="pl-s1">a</span> <span class="pl-c1">=</span> <span class="pl-s1">a</span> <span class="pl-c1">^</span> <span class="pl-s1">b</span></pre></div>
<p>方法二：</p>
<div class="highlight highlight-source-python"><pre><span class="pl-s1">a</span>, <span class="pl-s1">b</span> <span class="pl-c1">=</span> <span class="pl-s1">b</span>, <span class="pl-s1">a</span></pre></div>
<blockquote>
<p><strong>扩展</strong>：需要注意，<code>a, b = b, a</code>这种做法其实并不是元组解包，虽然很多人都这样认为。Python字节码指令中有<code>ROT_TWO</code>指令来支持这个操作，类似的还有<code>ROT_THREE</code>，对于3个以上的元素，如<code>a, b, c, d = b, c, d, a</code>，才会用到创建元组和元组解包。想知道你的代码对应的字节码指令，可以使用Python标准库中<code>dis</code>模块的<code>dis</code>函数来反汇编你的Python代码。</p>
</blockquote>
<h4><a id="user-content-题目003写一个删除列表中重复元素的函数要求去重后元素相对位置保持不变" class="anchor" aria-hidden="true" href="#题目003写一个删除列表中重复元素的函数要求去重后元素相对位置保持不变"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目003：写一个删除列表中重复元素的函数，要求去重后元素相对位置保持不变。</h4>
<blockquote>
<p><strong>点评</strong>：这个题目在初中级Python岗位面试的时候经常出现，题目源于《Python Cookbook》这本书第一章的第10个问题，有很多面试题其实都是这本书上的原题，所以建议大家有时间好好研读一下这本书。</p>
</blockquote>
<div class="highlight highlight-source-python"><pre><span class="pl-k">def</span> <span class="pl-en">dedup</span>(<span class="pl-s1">items</span>):
    <span class="pl-s1">no_dup_items</span> <span class="pl-c1">=</span> []
    <span class="pl-s1">seen</span> <span class="pl-c1">=</span> <span class="pl-en">set</span>()
    <span class="pl-k">for</span> <span class="pl-s1">item</span> <span class="pl-c1">in</span> <span class="pl-s1">items</span>:
        <span class="pl-k">if</span> <span class="pl-s1">item</span> <span class="pl-c1">not</span> <span class="pl-c1">in</span> <span class="pl-s1">seen</span>:
            <span class="pl-s1">no_dup_items</span>.<span class="pl-en">append</span>(<span class="pl-s1">item</span>)
            <span class="pl-s1">seen</span>.<span class="pl-en">add</span>(<span class="pl-s1">item</span>)
    <span class="pl-k">return</span> <span class="pl-s1">no_dup_items</span></pre></div>
<p>如果愿意也可以把上面的函数改造成一个生成器，代码如下所示。</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">def</span> <span class="pl-en">dedup</span>(<span class="pl-s1">items</span>):
    <span class="pl-s1">seen</span> <span class="pl-c1">=</span> <span class="pl-en">set</span>()
    <span class="pl-k">for</span> <span class="pl-s1">item</span> <span class="pl-c1">in</span> <span class="pl-s1">items</span>:
        <span class="pl-k">if</span> <span class="pl-s1">item</span> <span class="pl-c1">not</span> <span class="pl-c1">in</span> <span class="pl-s1">seen</span>:
            <span class="pl-k">yield</span> <span class="pl-s1">item</span>
            <span class="pl-s1">seen</span>.<span class="pl-en">add</span>(<span class="pl-s1">item</span>)</pre></div>
<blockquote>
<p><strong>扩展</strong>：由于Python中的集合底层使用哈希存储，所以集合的<code>in</code>和<code>not in</code>成员运算在性能上远远优于列表，所以上面的代码我们使用了集合来保存已经出现过的元素。集合中的元素必须是<code>hashable</code>对象，因此上面的代码在列表元素不是<code>hashable</code>对象时会失效，要解决这个问题可以给函数增加一个参数，该参数可以设计为返回哈希码或<code>hashable</code>对象的函数。</p>
</blockquote>
<h4><a id="user-content-题目004假设你使用的是官方的cpython说出下面代码的运行结果" class="anchor" aria-hidden="true" href="#题目004假设你使用的是官方的cpython说出下面代码的运行结果"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目004：假设你使用的是官方的CPython，说出下面代码的运行结果。</h4>
<blockquote>
<p><strong>点评</strong>：下面的程序对实际开发并没有什么意义，但却是CPython中的一个大坑，这道题旨在考察面试者对官方的Python解释器到底了解到什么程度。</p>
</blockquote>
<div class="highlight highlight-source-python"><pre><span class="pl-s1">a</span>, <span class="pl-s1">b</span>, <span class="pl-s1">c</span>, <span class="pl-s1">d</span> <span class="pl-c1">=</span> <span class="pl-c1">1</span>, <span class="pl-c1">1</span>, <span class="pl-c1">1000</span>, <span class="pl-c1">1000</span>
<span class="pl-en">print</span>(<span class="pl-s1">a</span> <span class="pl-c1">is</span> <span class="pl-s1">b</span>, <span class="pl-s1">c</span> <span class="pl-c1">is</span> <span class="pl-s1">d</span>)

<span class="pl-k">def</span> <span class="pl-en">foo</span>():
    <span class="pl-s1">e</span> <span class="pl-c1">=</span> <span class="pl-c1">1000</span>
    <span class="pl-s1">f</span> <span class="pl-c1">=</span> <span class="pl-c1">1000</span>
    <span class="pl-en">print</span>(<span class="pl-s1">e</span> <span class="pl-c1">is</span> <span class="pl-s1">f</span>, <span class="pl-s1">e</span> <span class="pl-c1">is</span> <span class="pl-s1">d</span>)
    <span class="pl-s1">g</span> <span class="pl-c1">=</span> <span class="pl-c1">1</span>
    <span class="pl-en">print</span>(<span class="pl-s1">g</span> <span class="pl-c1">is</span> <span class="pl-s1">a</span>)

<span class="pl-en">foo</span>()</pre></div>
<p>运行结果：</p>
<pre><code>True False
True False
True
</code></pre>
<p>上面代码中<code>a is b</code>的结果是<code>True</code>但<code>c is d</code>的结果是<code>False</code>，这一点的确让人费解。CPython解释器出于性能优化的考虑，把频繁使用的整数对象用一个叫<code>small_ints</code>的对象池缓存起来造成的。<code>small_ints</code>缓存的整数值被设定为<code>[-5, 256]</code>这个区间，也就是说，在任何引用这些整数的地方，都不需要重新创建<code>int</code>对象，而是直接引用缓存池中的对象。如果整数不在该范围内，那么即便两个整数的值相同，它们也是不同的对象。</p>
<p>CPython底层为了进一步提升性能还做了另一个设定，对于同一个代码块中值不在<code>small_ints</code>缓存范围内的整数，如果同一个代码块中已经存在一个值与其相同的整数对象，那么就直接引用该对象，否则创建新的<code>int</code>对象。需要大家注意的是，这条规则对数值型适用，但对字符串则需要考虑字符串的长度，这一点大家可以自行证明。</p>
<blockquote>
<p><strong>扩展</strong>：如果你用PyPy（另一种Python解释器实现，支持JIT，对CPython的缺点进行了改良，在性能上优于CPython，但对三方库的支持略差）来运行上面的代码，你会发现所有的输出都是True。</p>
</blockquote>
<h4><a id="user-content-题目005lambda函数是什么举例说明的它的应用场景" class="anchor" aria-hidden="true" href="#题目005lambda函数是什么举例说明的它的应用场景"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目005：Lambda函数是什么，举例说明的它的应用场景。</h4>
<blockquote>
<p><strong>点评</strong>：这个题目主要想考察的是Lambda函数的应用场景，潜台词是问你在项目中有没有使用过Lambda函数，具体在什么场景下会用到Lambda函数，借此来判断你写代码的能力。因为Lambda函数通常用在高阶函数中，主要的作用是通过向函数传入函数或让函数返回函数最终实现代码的解耦合。</p>
</blockquote>
<p>Lambda函数也叫匿名函数，它是功能简单用一行代码就能实现的小型函数。Python中的Lambda函数只能写一个表达式，这个表达式的执行结果就是函数的返回值，不用写<code>return</code>关键字。Lambda函数因为没有名字，所以也不会跟其他函数发生命名冲突的问题。</p>
<blockquote>
<p><strong>扩展</strong>：面试的时候有可能还会考你用Lambda函数来实现一些功能，也就是用一行代码来实现题目要求的功能，例如：用一行代码实现求阶乘的函数，用一行代码实现求最大公约数的函数等。</p>
<div class="highlight highlight-source-python"><pre><span class="pl-s1">fac</span> <span class="pl-c1">=</span> <span class="pl-k">lambda</span> <span class="pl-s1">x</span>: <span class="pl-en">__import__</span>(<span class="pl-s">'functools'</span>).<span class="pl-en">reduce</span>(<span class="pl-s1">int</span>.<span class="pl-s1">__mul__</span>, <span class="pl-en">range</span>(<span class="pl-c1">1</span>, <span class="pl-s1">x</span> <span class="pl-c1">+</span> <span class="pl-c1">1</span>), <span class="pl-c1">1</span>)
<span class="pl-s1">gcd</span> <span class="pl-c1">=</span> <span class="pl-k">lambda</span> <span class="pl-s1">x</span>, <span class="pl-s1">y</span>: <span class="pl-s1">y</span> <span class="pl-c1">%</span> <span class="pl-s1">x</span> <span class="pl-c1">and</span> <span class="pl-en">gcd</span>(<span class="pl-s1">y</span> <span class="pl-c1">%</span> <span class="pl-s1">x</span>, <span class="pl-s1">x</span>) <span class="pl-c1">or</span> <span class="pl-s1">x</span></pre></div>
</blockquote>
<p>Lambda函数其实最为主要的用途是把一个函数传入另一个高阶函数（如Python内置的<code>filter</code>、<code>map</code>等）中来为函数做解耦合，增强函数的灵活性和通用性。下面的例子通过使用<code>filter</code>和<code>map</code>函数，实现了从列表中筛选出奇数并求平方构成新列表的操作，因为用到了高阶函数，过滤和映射数据的规则都是函数的调用者通过另外一个函数传入的，因此这<code>filter</code>和<code>map</code>函数没有跟特定的过滤和映射数据的规则耦合在一起。</p>
<div class="highlight highlight-source-python"><pre><span class="pl-s1">items</span> <span class="pl-c1">=</span> [<span class="pl-c1">12</span>, <span class="pl-c1">5</span>, <span class="pl-c1">7</span>, <span class="pl-c1">10</span>, <span class="pl-c1">8</span>, <span class="pl-c1">19</span>]
<span class="pl-s1">items</span> <span class="pl-c1">=</span> <span class="pl-en">list</span>(<span class="pl-en">map</span>(<span class="pl-k">lambda</span> <span class="pl-s1">x</span>: <span class="pl-s1">x</span> <span class="pl-c1">**</span> <span class="pl-c1">2</span>, <span class="pl-en">filter</span>(<span class="pl-k">lambda</span> <span class="pl-s1">x</span>: <span class="pl-s1">x</span> <span class="pl-c1">%</span> <span class="pl-c1">2</span>, <span class="pl-s1">items</span>)))
<span class="pl-en">print</span>(<span class="pl-s1">items</span>)    <span class="pl-c"># [25, 49, 361]</span></pre></div>
<blockquote>
<p><strong>扩展</strong>：用列表的生成式来实现上面的代码会更加简单明了，代码如下所示。</p>
<div class="highlight highlight-source-python"><pre><span class="pl-s1">items</span> <span class="pl-c1">=</span> [<span class="pl-c1">12</span>, <span class="pl-c1">5</span>, <span class="pl-c1">7</span>, <span class="pl-c1">10</span>, <span class="pl-c1">8</span>, <span class="pl-c1">19</span>]
<span class="pl-s1">items</span> <span class="pl-c1">=</span> [<span class="pl-s1">x</span> <span class="pl-c1">**</span> <span class="pl-c1">2</span> <span class="pl-k">for</span> <span class="pl-s1">x</span> <span class="pl-c1">in</span> <span class="pl-s1">items</span> <span class="pl-k">if</span> <span class="pl-s1">x</span> <span class="pl-c1">%</span> <span class="pl-c1">2</span>]
<span class="pl-en">print</span>(<span class="pl-s1">items</span>)    <span class="pl-c"># [25, 49, 361]</span></pre></div>
</blockquote>
<h4><a id="user-content-题目006说说python中的浅拷贝和深拷贝" class="anchor" aria-hidden="true" href="#题目006说说python中的浅拷贝和深拷贝"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目006：说说Python中的浅拷贝和深拷贝。</h4>
<blockquote>
<p><strong>点评</strong>：这个题目本身出现的频率非常高，但是就题论题而言没有什么技术含量。对于这种面试题，在<strong>回答的时候一定要让你的答案能够超出面试官的预期</strong>，这样才能<strong>获得更好的印象分</strong>。所以回答这个题目的要点不仅仅是能够说出浅拷贝和深拷贝的区别，深拷贝的时候可能遇到的两大问题，还要说出Python标准库对浅拷贝和深拷贝的支持，然后可以说说列表、字典如何实现拷贝操作以及如何通过序列化和反序列的方式实现深拷贝，最后还可以提到设计模式中的原型模式以及它在项目中的应用。</p>
</blockquote>
<p>浅拷贝通常只复制对象本身，而深拷贝不仅会复制对象，还会递归的复制对象所关联的对象。深拷贝可能会遇到两个问题：一是一个对象如果直接或间接的引用了自身，会导致无休止的递归拷贝；二是深拷贝可能对原本设计为多个对象共享的数据也进行拷贝。Python通过<code>copy</code>模块中的<code>copy</code>和<code>deepcopy</code>函数来实现浅拷贝和深拷贝操作，其中<code>deepcopy</code>可以通过<code>memo</code>字典来保存已经拷贝过的对象，从而避免刚才所说的自引用递归问题；此外，可以通过<code>copyreg</code>模块的<code>pickle</code>函数来定制指定类型对象的拷贝行为。</p>
<p><code>deepcopy</code>函数的本质其实就是对象的一次序列化和一次返回序列化，面试题中还考过用自定义函数实现对象的深拷贝操作，显然我们可以使用<code>pickle</code>模块的<code>dumps</code>和<code>loads</code>来做到，代码如下所示。</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> <span class="pl-s1">pickle</span>

<span class="pl-s1">my_deep_copy</span> <span class="pl-c1">=</span> <span class="pl-k">lambda</span> <span class="pl-s1">obj</span>: <span class="pl-s1">pickle</span>.<span class="pl-en">loads</span>(<span class="pl-s1">pickle</span>.<span class="pl-en">dumps</span>(<span class="pl-s1">obj</span>))</pre></div>
<p>列表的切片操作<code>[:]</code>相当于实现了列表对象的浅拷贝，而字典的<code>copy</code>方法可以实现字典对象的浅拷贝。对象拷贝其实是更为快捷的创建对象的方式。在Python中，通过构造器创建对象属于两阶段构造，首先是分配内存空间，然后是初始化。在创建对象时，我们也可以基于“原型”对象来创建新对象，通过对原型对象的拷贝（复制内存）就完成了对象的创建和初始化，这种做法更加高效，这也就是设计模式中的原型模式。在Python中，我们可以通过元类的方式来实现原型模式，代码如下所示。</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> <span class="pl-s1">copy</span>


<span class="pl-k">class</span> <span class="pl-v">PrototypeMeta</span>(<span class="pl-s1">type</span>):
    <span class="pl-s">"""实现原型模式的元类"""</span>

    <span class="pl-k">def</span> <span class="pl-en">__init__</span>(<span class="pl-s1">cls</span>, <span class="pl-c1">*</span><span class="pl-s1">args</span>, <span class="pl-c1">**</span><span class="pl-s1">kwargs</span>):
        <span class="pl-en">super</span>().<span class="pl-en">__init__</span>(<span class="pl-c1">*</span><span class="pl-s1">args</span>, <span class="pl-c1">**</span><span class="pl-s1">kwargs</span>)
        <span class="pl-c"># 为对象绑定clone方法来实现对象拷贝</span>
        <span class="pl-s1">cls</span>.<span class="pl-s1">clone</span> <span class="pl-c1">=</span> <span class="pl-k">lambda</span> <span class="pl-s1">self</span>, <span class="pl-s1">is_deep</span><span class="pl-c1">=</span><span class="pl-c1">True</span>: \
            <span class="pl-s1">copy</span>.<span class="pl-en">deepcopy</span>(<span class="pl-s1">self</span>) <span class="pl-k">if</span> <span class="pl-s1">is_deep</span> <span class="pl-k">else</span> <span class="pl-s1">copy</span>.<span class="pl-en">copy</span>(<span class="pl-s1">self</span>)


<span class="pl-k">class</span> <span class="pl-v">Person</span>(<span class="pl-s1">metaclass</span><span class="pl-c1">=</span><span class="pl-v">PrototypeMeta</span>):
    <span class="pl-k">pass</span>


<span class="pl-s1">p1</span> <span class="pl-c1">=</span> <span class="pl-v">Person</span>()
<span class="pl-s1">p2</span> <span class="pl-c1">=</span> <span class="pl-s1">p1</span>.<span class="pl-en">clone</span>()                 <span class="pl-c"># 深拷贝</span>
<span class="pl-s1">p3</span> <span class="pl-c1">=</span> <span class="pl-s1">p1</span>.<span class="pl-en">clone</span>(<span class="pl-s1">is_deep</span><span class="pl-c1">=</span><span class="pl-c1">False</span>)    <span class="pl-c"># 浅拷贝</span></pre></div>
<h4><a id="user-content-题目007python是如何实现内存管理的" class="anchor" aria-hidden="true" href="#题目007python是如何实现内存管理的"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目007：Python是如何实现内存管理的？</h4>
<blockquote>
<p><strong>点评</strong>：当面试官问到这个问题的时候，一个展示自己的机会就摆在面前了。你要先反问面试官：“你说的是官方的CPython解释器吗？”。这个反问可以展示出你了解过Python解释器的不同的实现版本，而且你也知道面试官想问的是CPython。当然，很多面试官对不同的Python解释器底层实现到底有什么差别也没有概念。所以，<strong>千万不要觉得面试官一定比你强</strong>，怀揣着这份自信可以让你更好的完成面试。</p>
</blockquote>
<p>Python提供了自动化的内存管理，也就是说内存空间的分配与释放都是由Python解释器在运行时自动进行的，自动管理内存功能极大的减轻程序员的工作负担，也能够帮助程序员在一定程度上解决内存泄露的问题。以CPython解释器为例，它的内存管理有三个关键点：引用计数、标记清理、分代收集。</p>
<p><strong>引用计数</strong>：对于CPython解释器来说，Python中的每一个对象其实就是<code>PyObject</code>结构体，它的内部有一个名为<code>ob_refcnt</code> 的引用计数器成员变量。程序在运行的过程中<code>ob_refcnt</code>的值会被更新并藉此来反映引用有多少个变量引用到该对象。当对象的引用计数值为0时，它的内存就会被释放掉。</p>
<div class="highlight highlight-source-c"><pre><span class="pl-k">typedef</span> <span class="pl-k">struct</span> _object {
    _PyObject_HEAD_EXTRA
    Py_ssize_t ob_refcnt;
    <span class="pl-k">struct</span> _typeobject *ob_type;
} PyObject;</pre></div>
<p>以下情况会导致引用计数加<code>1</code>：</p>
<ul>
<li>对象被创建</li>
<li>对象被引用</li>
<li>对象作为参数传入到一个函数中</li>
<li>对象作为元素存储到一个容器中</li>
</ul>
<p>以下情况会导致引用计数减<code>1</code>：</p>
<ul>
<li>用<code>del</code>语句显示删除对象引用</li>
<li>对象引用被重新赋值其他对象</li>
<li>一个对象离开它所在的作用域</li>
<li>持有该对象的容器自身被销毁</li>
<li>持有该对象的容器删除该对象</li>
</ul>
<p>可以通过<code>sys</code>模块的<code>getrefcount</code>函数来获得对象的引用计数。引用计数的内存管理方式在遇到循环引用的时候就会出现致命伤，因此需要其他的垃圾回收算法对其进行补充。</p>
<p><strong>标记清理</strong>：CPython使用了“标记-清理”（Mark and Sweep）算法解决容器类型可能产生的循环引用问题。该算法在垃圾回收时分为两个阶段：标记阶段，遍历所有的对象，如果对象是可达的（被其他对象引用），那么就标记该对象为可达；清除阶段，再次遍历对象，如果发现某个对象没有标记为可达，则就将其回收。CPython底层维护了两个双端链表，一个链表存放着需要被扫描的容器对象（姑且称之为链表A），另一个链表存放着临时不可达对象（姑且称之为链表B）。为了实现“标记-清理”算法，链表中的每个节点除了有记录当前引用计数的<code>ref_count</code>变量外，还有一个<code>gc_ref</code>变量，这个<code>gc_ref</code>是<code>ref_count</code>的一个副本，所以初始值为<code>ref_count</code>的大小。执行垃圾回收时，首先遍历链表A中的节点，并且将当前对象所引用的所有对象的<code>gc_ref</code>减<code>1</code>，这一步主要作用是解除循环引用对引用计数的影响。再次遍历链表A中的节点，如果节点的<code>gc_ref</code>值为<code>0</code>，那么这个对象就被标记为“暂时不可达”（<code>GC_TENTATIVELY_UNREACHABLE</code>）并被移动到链表B中；如果节点的<code>gc_ref</code>不为<code>0</code>，那么这个对象就会被标记为“可达“（<code>GC_REACHABLE</code>），对于”可达“对象，还要递归的将该节点可以到达的节点标记为”可达“；链表B中被标记为”可达“的节点要重新放回到链表A中。在两次遍历之后，链表B中的节点就是需要释放内存的节点。</p>
<p><strong>分代回收</strong>：在循环引用对象的回收中，整个应用程序会被暂停，为了减少应用程序暂停的时间，Python 通过分代回收（空间换时间）的方法提高垃圾回收效率。分代回收的基本思想是：<strong>对象存在的时间越长，是垃圾的可能性就越小，应该尽量不对这样的对象进行垃圾回收</strong>。CPython将对象分为三种世代分别记为<code>0</code>、<code>1</code>、<code>2</code>，每一个新生对象都在第<code>0</code>代中，如果该对象在一轮垃圾回收扫描中存活下来，那么它将被移到第<code>1</code>代中，存在于第<code>1</code>代的对象将较少的被垃圾回收扫描到；如果在对第<code>1</code>代进行垃圾回收扫描时，这个对象又存活下来，那么它将被移至第2代中，在那里它被垃圾回收扫描的次数将会更少。分代回收扫描的门限值可以通过<code>gc</code>模块的<code>get_threshold</code>函数来获得，该函数返回一个三元组，分别表示多少次内存分配操作后会执行<code>0</code>代垃圾回收，多少次<code>0</code>代垃圾回收后会执行<code>1</code>代垃圾回收，多少次<code>1</code>代垃圾回收后会执行<code>2</code>代垃圾回收。需要说明的是，如果执行一次<code>2</code>代垃圾回收，那么比它年轻的代都要执行垃圾回收。如果想修改这几个门限值，可以通过<code>gc</code>模块的<code>set_threshold</code>函数来做到。</p>
<h4><a id="user-content-题目008说一下你对python中迭代器和生成器的理解" class="anchor" aria-hidden="true" href="#题目008说一下你对python中迭代器和生成器的理解"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目008：说一下你对Python中迭代器和生成器的理解。</h4>
<blockquote>
<p><strong>点评</strong>：很多人面试者都会写迭代器和生成器，但是却无法准确的解释什么是迭代器和生成器。如果你也有同样的困惑，可以参考下面的回答。</p>
</blockquote>
<p>迭代器是实现了迭代器协议的对象。跟其他编程语言不通，Python中没有用于定义协议或表示约定的关键字，像<code>interface</code>、<code>protocol</code>这些单词并不在Python语言的关键字列表中。Python语言通过魔法方法来表示约定，也就是我们所说的协议，而<code>__next__</code>和<code>__iter__</code>这两个魔法方法就代表了迭代器协议。可以通过<code>for-in</code>循环从迭代器对象中取出值，也可以使用<code>next</code>函数取出迭代器对象中的下一个值。生成器是迭代器的语法升级版本，可以用更为简单的代码来实现一个迭代器。</p>
<blockquote>
<p><strong>扩展</strong>：面试中经常让写生成斐波那契数列的迭代器，大家可以参考下面的代码。</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">class</span> <span class="pl-v">Fib</span>(<span class="pl-s1">object</span>):
    
    <span class="pl-k">def</span> <span class="pl-en">__init__</span>(<span class="pl-s1">self</span>, <span class="pl-s1">num</span>):
        <span class="pl-s1">self</span>.<span class="pl-s1">num</span> <span class="pl-c1">=</span> <span class="pl-s1">num</span>
        <span class="pl-s1">self</span>.<span class="pl-s1">a</span>, <span class="pl-s1">self</span>.<span class="pl-s1">b</span> <span class="pl-c1">=</span> <span class="pl-c1">0</span>, <span class="pl-c1">1</span>
        <span class="pl-s1">self</span>.<span class="pl-s1">idx</span> <span class="pl-c1">=</span> <span class="pl-c1">0</span>
   
    <span class="pl-k">def</span> <span class="pl-en">__iter__</span>(<span class="pl-s1">self</span>):
        <span class="pl-k">return</span> <span class="pl-s1">self</span>

    <span class="pl-k">def</span> <span class="pl-en">__next__</span>(<span class="pl-s1">self</span>):
        <span class="pl-k">if</span> <span class="pl-s1">self</span>.<span class="pl-s1">idx</span> <span class="pl-c1">&lt;</span> <span class="pl-s1">self</span>.<span class="pl-s1">num</span>:
            <span class="pl-s1">self</span>.<span class="pl-s1">a</span>, <span class="pl-s1">self</span>.<span class="pl-s1">b</span> <span class="pl-c1">=</span> <span class="pl-s1">self</span>.<span class="pl-s1">b</span>, <span class="pl-s1">self</span>.<span class="pl-s1">a</span> <span class="pl-c1">+</span> <span class="pl-s1">self</span>.<span class="pl-s1">b</span>
            <span class="pl-s1">self</span>.<span class="pl-s1">idx</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span>
            <span class="pl-k">return</span> <span class="pl-s1">self</span>.<span class="pl-s1">a</span>
        <span class="pl-k">raise</span> <span class="pl-v">StopIteration</span>()</pre></div>
<p>如果用生成器的语法来改写上面的代码，代码会简单优雅很多。</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">def</span> <span class="pl-en">fib</span>(<span class="pl-s1">num</span>):
    <span class="pl-s1">a</span>, <span class="pl-s1">b</span> <span class="pl-c1">=</span> <span class="pl-c1">0</span>, <span class="pl-c1">1</span>
    <span class="pl-k">for</span> <span class="pl-s1">_</span> <span class="pl-c1">in</span> <span class="pl-en">range</span>(<span class="pl-s1">num</span>):
        <span class="pl-s1">a</span>, <span class="pl-s1">b</span> <span class="pl-c1">=</span> <span class="pl-s1">b</span>, <span class="pl-s1">a</span> <span class="pl-c1">+</span> <span class="pl-s1">b</span>
        <span class="pl-k">yield</span> <span class="pl-s1">a</span></pre></div>
</blockquote>
<h4><a id="user-content-题目009正则表达式的match方法和search方法有什么区别" class="anchor" aria-hidden="true" href="#题目009正则表达式的match方法和search方法有什么区别"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目009：正则表达式的match方法和search方法有什么区别？</h4>
<blockquote>
<p><strong>点评</strong>：正则表达式是字符串处理的重要工具，所以也是面试中经常考察的知识点。在Python中，使用正则表达式有两种方式，一种是直接调用<code>re</code>模块中的函数，传入正则表达式和需要处理的字符串；一种是先通过<code>re</code>模块的<code>compile</code>函数创建正则表达式对象，然后再通过对象调用方法并传入需要处理的字符串。<strong>如果一个正则表达式被频繁的使用，我们推荐用<code>re.compile</code>函数创建正则表达式对象，这样会减少频繁编译同一个正则表达式所造成的开销</strong>。</p>
</blockquote>
<p><code>match</code>方法是从字符串的起始位置进行正则表达式匹配，返回<code>Match</code>对象或None。<code>search</code>方法会扫描整个字符串来找寻匹配的模式，同样也是返回Match对象或None。</p>
<h4><a id="user-content-题目010下面这段代码的执行结果是什么" class="anchor" aria-hidden="true" href="#题目010下面这段代码的执行结果是什么"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目010：下面这段代码的执行结果是什么。</h4>
<div class="highlight highlight-source-python"><pre><span class="pl-k">def</span> <span class="pl-en">multiply</span>():
    <span class="pl-k">return</span> [<span class="pl-k">lambda</span> <span class="pl-s1">x</span>: <span class="pl-s1">i</span> <span class="pl-c1">*</span> <span class="pl-s1">x</span> <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-en">range</span>(<span class="pl-c1">4</span>)]

<span class="pl-en">print</span>([<span class="pl-en">m</span>(<span class="pl-c1">100</span>) <span class="pl-k">for</span> <span class="pl-s1">m</span> <span class="pl-c1">in</span> <span class="pl-en">multiply</span>()])</pre></div>
<p>运行结果：</p>
<pre><code>[300, 300, 300, 300]
</code></pre>
<p>上面代码的运行结果很容易被误判为<code>[0, 100, 200, 300]</code>。首先需要注意的是<code>multiply</code>函数用生成式语法返回了一个列表，列表中保存了4个Lambda函数，这4个Lambda函数会返回传入的参数乘以<code>i</code>的结果。需要注意的是这里有闭包（closure）现象，<code>multiply</code>函数中的局部变量<code>i</code>的生命周期被延展了，由于<code>i</code>最终的值是<code>3</code>，所以通过<code>m(100)</code>调列表中的Lambda函数时会返回<code>300</code>，而且4个调用都是如此。</p>
<p>如果想得到<code>[0, 100, 200, 300]</code>这个结果，可以按照下面几种方式来修改<code>multiply</code>函数。</p>
<p>方法一：使用生成器，让函数获得<code>i</code>的当前值。</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">def</span> <span class="pl-en">multiply</span>():
    <span class="pl-k">return</span> (<span class="pl-k">lambda</span> <span class="pl-s1">x</span>: <span class="pl-s1">i</span> <span class="pl-c1">*</span> <span class="pl-s1">x</span> <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-en">range</span>(<span class="pl-c1">4</span>))

<span class="pl-en">print</span>([<span class="pl-en">m</span>(<span class="pl-c1">100</span>) <span class="pl-k">for</span> <span class="pl-s1">m</span> <span class="pl-c1">in</span> <span class="pl-en">multiply</span>()])</pre></div>
<p>或者</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">def</span> <span class="pl-en">multiply</span>():
    <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-en">range</span>(<span class="pl-c1">4</span>):
        <span class="pl-k">yield</span> <span class="pl-k">lambda</span> <span class="pl-s1">x</span>: <span class="pl-s1">x</span> <span class="pl-c1">*</span> <span class="pl-s1">i</span>

<span class="pl-en">print</span>([<span class="pl-en">m</span>(<span class="pl-c1">100</span>) <span class="pl-k">for</span> <span class="pl-s1">m</span> <span class="pl-c1">in</span> <span class="pl-en">multiply</span>()])</pre></div>
<p>方法二：使用偏函数，彻底避开闭包。</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">from</span> <span class="pl-s1">functools</span> <span class="pl-k">import</span> <span class="pl-s1">partial</span>
<span class="pl-k">from</span> <span class="pl-s1">operator</span> <span class="pl-k">import</span> <span class="pl-s1">__mul__</span>

<span class="pl-k">def</span> <span class="pl-en">multiply</span>():
    <span class="pl-k">return</span> [<span class="pl-en">partial</span>(<span class="pl-s1">__mul__</span>, <span class="pl-s1">i</span>) <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-en">range</span>(<span class="pl-c1">4</span>)]

<span class="pl-en">print</span>([<span class="pl-en">m</span>(<span class="pl-c1">100</span>) <span class="pl-k">for</span> <span class="pl-s1">m</span> <span class="pl-c1">in</span> <span class="pl-en">multiply</span>()])</pre></div>
<h4><a id="user-content-题目011python中为什么没有函数重载" class="anchor" aria-hidden="true" href="#题目011python中为什么没有函数重载"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目011：Python中为什么没有函数重载？</h4>
<blockquote>
<p><strong>点评</strong>：C++、Java、C#等诸多编程语言都支持函数重载，所谓函数重载指的是在同一个作用域中有多个同名函数，它们拥有不同的参数列表（参数个数不同或参数类型不同或二者皆不同），可以相互区分。重载也是一种多态性，因为通常是在编译时通过参数的个数和类型来确定到底调用哪个重载函数，所以也被称为编译时多态性或者叫前绑定。这个问题的潜台词其实是问面试者是否有其他编程语言的经验，是否理解Python是动态类型语言，是否知道Python中函数的可变参数、关键字参数这些概念。</p>
</blockquote>
<p>首先Python是解释型语言，函数重载现象通常出现在编译型语言中。其次Python是动态类型语言，函数的参数没有类型约束，也就无法根据参数类型来区分重载。再者Python中函数的参数可以有默认值，可以使用可变参数和关键字参数，因此即便没有函数重载，也要可以让一个函数根据调用者传入的参数产生不同的行为。</p>
<h4><a id="user-content-题目012用python代码实现python内置函数max" class="anchor" aria-hidden="true" href="#题目012用python代码实现python内置函数max"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目012：用Python代码实现Python内置函数max。</h4>
<blockquote>
<p><strong>点评</strong>：这个题目看似简单，但实际上还是比较考察面试者的功底。因为Python内置的<code>max</code>函数既可以传入可迭代对象找出最大，又可以传入两个或多个参数找出最大；最为关键的是还可以通过命名关键字参数<code>key</code>来指定一个用于元素比较的函数，还可以通过<code>default</code>命名关键字参数来指定当可迭代对象为空时返回的默认值。</p>
</blockquote>
<p>下面的代码仅供参考：</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">def</span> <span class="pl-en">my_max</span>(<span class="pl-c1">*</span><span class="pl-s1">args</span>, <span class="pl-s1">key</span><span class="pl-c1">=</span><span class="pl-c1">None</span>, <span class="pl-s1">default</span><span class="pl-c1">=</span><span class="pl-c1">None</span>):
    <span class="pl-s">"""</span>
<span class="pl-s">    获取可迭代对象中最大的元素或两个及以上实参中最大的元素</span>
<span class="pl-s">    :param args: 一个可迭代对象或多个元素</span>
<span class="pl-s">    :param key: 提取用于元素比较的特征值的函数，默认为None</span>
<span class="pl-s">    :param default: 如果可迭代对象为空则返回该默认值，如果没有给默认值则引发ValueError异常</span>
<span class="pl-s">    :return: 返回可迭代对象或多个元素中的最大元素</span>
<span class="pl-s">    """</span>
    <span class="pl-k">if</span> <span class="pl-en">len</span>(<span class="pl-s1">args</span>) <span class="pl-c1">==</span> <span class="pl-c1">1</span> <span class="pl-c1">and</span> <span class="pl-en">len</span>(<span class="pl-s1">args</span>[<span class="pl-c1">0</span>]) <span class="pl-c1">==</span> <span class="pl-c1">0</span>:
        <span class="pl-k">if</span> <span class="pl-s1">default</span>:
            <span class="pl-k">return</span> <span class="pl-s1">default</span>
        <span class="pl-k">else</span>:
            <span class="pl-k">raise</span> <span class="pl-v">ValueError</span>(<span class="pl-s">'max() arg is an empty sequence'</span>)
    <span class="pl-s1">items</span> <span class="pl-c1">=</span> <span class="pl-s1">args</span>[<span class="pl-c1">0</span>] <span class="pl-k">if</span> <span class="pl-en">len</span>(<span class="pl-s1">args</span>) <span class="pl-c1">==</span> <span class="pl-c1">1</span> <span class="pl-k">else</span> <span class="pl-s1">args</span>
    <span class="pl-s1">max_elem</span>, <span class="pl-s1">max_value</span> <span class="pl-c1">=</span> <span class="pl-s1">items</span>[<span class="pl-c1">0</span>], <span class="pl-s1">items</span>[<span class="pl-c1">0</span>]
    <span class="pl-k">if</span> <span class="pl-s1">key</span>:
        <span class="pl-s1">max_value</span> <span class="pl-c1">=</span> <span class="pl-en">key</span>(<span class="pl-s1">max_value</span>)
    <span class="pl-k">for</span> <span class="pl-s1">item</span> <span class="pl-c1">in</span> <span class="pl-s1">items</span>:
        <span class="pl-s1">value</span> <span class="pl-c1">=</span> <span class="pl-s1">item</span>
        <span class="pl-k">if</span> <span class="pl-s1">key</span>:
            <span class="pl-s1">value</span> <span class="pl-c1">=</span> <span class="pl-en">key</span>(<span class="pl-s1">item</span>)
        <span class="pl-k">if</span> <span class="pl-s1">value</span> <span class="pl-c1">&gt;</span> <span class="pl-s1">max_value</span>:
            <span class="pl-s1">max_elem</span>, <span class="pl-s1">max_value</span> <span class="pl-c1">=</span> <span class="pl-s1">item</span>, <span class="pl-s1">value</span>
    <span class="pl-k">return</span> <span class="pl-s1">max_elem</span></pre></div>
<h4><a id="user-content-题目013写一个函数统计传入的列表中每个数字出现的次数并返回对应的字典" class="anchor" aria-hidden="true" href="#题目013写一个函数统计传入的列表中每个数字出现的次数并返回对应的字典"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目013：写一个函数统计传入的列表中每个数字出现的次数并返回对应的字典。</h4>
<blockquote>
<p><strong>点评</strong>：送人头的题目，不解释。</p>
</blockquote>
<div class="highlight highlight-source-python"><pre><span class="pl-k">def</span> <span class="pl-en">count_letters</span>(<span class="pl-s1">items</span>):
    <span class="pl-s1">result</span> <span class="pl-c1">=</span> {}
    <span class="pl-k">for</span> <span class="pl-s1">item</span> <span class="pl-c1">in</span> <span class="pl-s1">items</span>:
        <span class="pl-k">if</span> <span class="pl-en">isinstance</span>(<span class="pl-s1">item</span>, (<span class="pl-s1">int</span>, <span class="pl-s1">float</span>)):
            <span class="pl-s1">result</span>[<span class="pl-s1">item</span>] <span class="pl-c1">=</span> <span class="pl-s1">result</span>.<span class="pl-en">get</span>(<span class="pl-s1">item</span>, <span class="pl-c1">0</span>) <span class="pl-c1">+</span> <span class="pl-c1">1</span>
    <span class="pl-k">return</span> <span class="pl-s1">result</span></pre></div>
<p>也可以直接使用Python标准库中<code>collections</code>模块的<code>Counter</code>类来解决这个问题，<code>Counter</code>是<code>dict</code>的子类，它会将传入的序列中的每个元素作为键，元素出现的次数作为值来构造字典。</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">from</span> <span class="pl-s1">collections</span> <span class="pl-k">import</span> <span class="pl-v">Counter</span>

<span class="pl-k">def</span> <span class="pl-en">count_letters</span>(<span class="pl-s1">items</span>):
    <span class="pl-s1">counter</span> <span class="pl-c1">=</span> <span class="pl-v">Counter</span>(<span class="pl-s1">items</span>)
    <span class="pl-k">return</span> {<span class="pl-s1">key</span>: <span class="pl-s1">value</span> <span class="pl-k">for</span> <span class="pl-s1">key</span>, <span class="pl-s1">value</span> <span class="pl-c1">in</span> <span class="pl-s1">counter</span>.<span class="pl-en">items</span>() \
            <span class="pl-k">if</span> <span class="pl-en">isinstance</span>(<span class="pl-s1">key</span>, (<span class="pl-s1">int</span>, <span class="pl-s1">float</span>))}</pre></div>
<h4><a id="user-content-题目014使用python代码实现遍历一个文件夹的操作" class="anchor" aria-hidden="true" href="#题目014使用python代码实现遍历一个文件夹的操作"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目014：使用Python代码实现遍历一个文件夹的操作。</h4>
<blockquote>
<p><strong>点评</strong>：基本也是送人头的题目，只要用过<code>os</code>模块就应该知道怎么做。</p>
</blockquote>
<p>Python标准库<code>os</code>模块的<code>walk</code>函数提供了遍历一个文件夹的功能，它返回一个生成器。</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> <span class="pl-s1">os</span>

<span class="pl-s1">g</span> <span class="pl-c1">=</span> <span class="pl-s1">os</span>.<span class="pl-en">walk</span>(<span class="pl-s">'/Users/Hao/Downloads/'</span>)
<span class="pl-k">for</span> <span class="pl-s1">path</span>, <span class="pl-s1">dir_list</span>, <span class="pl-s1">file_list</span> <span class="pl-c1">in</span> <span class="pl-s1">g</span>:
    <span class="pl-k">for</span> <span class="pl-s1">dir_name</span> <span class="pl-c1">in</span> <span class="pl-s1">dir_list</span>:
        <span class="pl-en">print</span>(<span class="pl-s1">os</span>.<span class="pl-s1">path</span>.<span class="pl-en">join</span>(<span class="pl-s1">path</span>, <span class="pl-s1">dir_name</span>))
    <span class="pl-k">for</span> <span class="pl-s1">file_name</span> <span class="pl-c1">in</span> <span class="pl-s1">file_list</span>:
        <span class="pl-en">print</span>(<span class="pl-s1">os</span>.<span class="pl-s1">path</span>.<span class="pl-en">join</span>(<span class="pl-s1">path</span>, <span class="pl-s1">file_name</span>))</pre></div>
<blockquote>
<p><strong>说明</strong>：<code>os.path</code>模块提供了很多进行路径操作的工具函数，在项目开发中也是经常会用到的。如果题目明确要求不能使用<code>os.walk</code>函数，那么可以使用<code>os.listdir</code>函数来获取指定目录下的文件和文件夹，然后再通过循环遍历用<code>os.isdir</code>函数判断哪些是文件夹，对于文件夹可以通过<strong>递归调用</strong>进行遍历，这样也可以实现遍历一个文件夹的操作。</p>
</blockquote>
<h4><a id="user-content-题目015现有2元3元5元共三种面额的货币如果需要找零99元一共有多少种找零的方式" class="anchor" aria-hidden="true" href="#题目015现有2元3元5元共三种面额的货币如果需要找零99元一共有多少种找零的方式"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目015：现有2元、3元、5元共三种面额的货币，如果需要找零99元，一共有多少种找零的方式？</h4>
<blockquote>
<p><strong>点评</strong>：还有一个非常类似的题目：“一个小朋友走楼梯，一次可以走1个台阶、2个台阶或3个台阶，问走完10个台阶一共有多少种走法？”，这两个题目的思路是一样，如果用递归函数来写的话非常简单。</p>
</blockquote>
<div class="highlight highlight-source-python"><pre><span class="pl-k">from</span> <span class="pl-s1">functools</span> <span class="pl-k">import</span> <span class="pl-s1">lru_cache</span>


<span class="pl-en">@<span class="pl-s1">lru_cache</span>()</span>
<span class="pl-k">def</span> <span class="pl-en">change_money</span>(<span class="pl-s1">total</span>):
    <span class="pl-k">if</span> <span class="pl-s1">total</span> <span class="pl-c1">==</span> <span class="pl-c1">0</span>:
        <span class="pl-k">return</span> <span class="pl-c1">1</span>
    <span class="pl-k">if</span> <span class="pl-s1">total</span> <span class="pl-c1">&lt;</span> <span class="pl-c1">0</span>:
        <span class="pl-k">return</span> <span class="pl-c1">0</span>
    <span class="pl-k">return</span> <span class="pl-en">change_money</span>(<span class="pl-s1">total</span> <span class="pl-c1">-</span> <span class="pl-c1">2</span>) <span class="pl-c1">+</span> <span class="pl-en">change_money</span>(<span class="pl-s1">total</span> <span class="pl-c1">-</span> <span class="pl-c1">3</span>) <span class="pl-c1">+</span> \
        <span class="pl-en">change_money</span>(<span class="pl-s1">total</span> <span class="pl-c1">-</span> <span class="pl-c1">5</span>)</pre></div>
<blockquote>
<p><strong>说明</strong>：在上面的代码中，我们用<code>lru_cache</code>装饰器装饰了递归函数<code>change_money</code>，如果不做这个优化，上面代码的渐近时间复杂度将会是$O(3^N)$，而如果参数<code>total</code>的值是<code>99</code>，这个运算量是非常巨大的。<code>lru_cache</code>装饰器会缓存函数的执行结果，这样就可以减少重复运算所造成的开销，这是空间换时间的策略，也是动态规划的编程思想。</p>
</blockquote>
<h4><a id="user-content-题目016写一个函数给定矩阵的阶数n输出一个螺旋式数字矩阵" class="anchor" aria-hidden="true" href="#题目016写一个函数给定矩阵的阶数n输出一个螺旋式数字矩阵"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目016：写一个函数，给定矩阵的阶数<code>n</code>，输出一个螺旋式数字矩阵。</h4>
<blockquote>
<p>例如：n = 2，返回：</p>
<pre><code>1 2
4 3
</code></pre>
<p>例如：n = 3，返回：</p>
<pre><code>1 2 3
8 9 4
7 6 5
</code></pre>
</blockquote>
<p>这个题目本身并不复杂，下面的代码仅供参考。</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">def</span> <span class="pl-en">show_spiral_matrix</span>(<span class="pl-s1">n</span>):
    <span class="pl-s1">matrix</span> <span class="pl-c1">=</span> [[<span class="pl-c1">0</span>] <span class="pl-c1">*</span> <span class="pl-s1">n</span> <span class="pl-k">for</span> <span class="pl-s1">_</span> <span class="pl-c1">in</span> <span class="pl-en">range</span>(<span class="pl-s1">n</span>)]
    <span class="pl-s1">row</span>, <span class="pl-s1">col</span> <span class="pl-c1">=</span> <span class="pl-c1">0</span>, <span class="pl-c1">0</span>
    <span class="pl-s1">num</span>, <span class="pl-s1">direction</span> <span class="pl-c1">=</span> <span class="pl-c1">1</span>, <span class="pl-c1">0</span>
    <span class="pl-k">while</span> <span class="pl-s1">num</span> <span class="pl-c1">&lt;=</span> <span class="pl-s1">n</span> <span class="pl-c1">**</span> <span class="pl-c1">2</span>:
        <span class="pl-k">if</span> <span class="pl-s1">matrix</span>[<span class="pl-s1">row</span>][<span class="pl-s1">col</span>] <span class="pl-c1">==</span> <span class="pl-c1">0</span>:
            <span class="pl-s1">matrix</span>[<span class="pl-s1">row</span>][<span class="pl-s1">col</span>] <span class="pl-c1">=</span> <span class="pl-s1">num</span>
            <span class="pl-s1">num</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span>
        <span class="pl-k">if</span> <span class="pl-s1">direction</span> <span class="pl-c1">==</span> <span class="pl-c1">0</span>:
            <span class="pl-k">if</span> <span class="pl-s1">col</span> <span class="pl-c1">&lt;</span> <span class="pl-s1">n</span> <span class="pl-c1">-</span> <span class="pl-c1">1</span> <span class="pl-c1">and</span> <span class="pl-s1">matrix</span>[<span class="pl-s1">row</span>][<span class="pl-s1">col</span> <span class="pl-c1">+</span> <span class="pl-c1">1</span>] <span class="pl-c1">==</span> <span class="pl-c1">0</span>:
                <span class="pl-s1">col</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span>
            <span class="pl-k">else</span>:
                <span class="pl-s1">direction</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span>
        <span class="pl-k">elif</span> <span class="pl-s1">direction</span> <span class="pl-c1">==</span> <span class="pl-c1">1</span>:
            <span class="pl-k">if</span> <span class="pl-s1">row</span> <span class="pl-c1">&lt;</span> <span class="pl-s1">n</span> <span class="pl-c1">-</span> <span class="pl-c1">1</span> <span class="pl-c1">and</span> <span class="pl-s1">matrix</span>[<span class="pl-s1">row</span> <span class="pl-c1">+</span> <span class="pl-c1">1</span>][<span class="pl-s1">col</span>] <span class="pl-c1">==</span> <span class="pl-c1">0</span>:
                <span class="pl-s1">row</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span>
            <span class="pl-k">else</span>:
                <span class="pl-s1">direction</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span>
        <span class="pl-k">elif</span> <span class="pl-s1">direction</span> <span class="pl-c1">==</span> <span class="pl-c1">2</span>:
            <span class="pl-k">if</span> <span class="pl-s1">col</span> <span class="pl-c1">&gt;</span> <span class="pl-c1">0</span> <span class="pl-c1">and</span> <span class="pl-s1">matrix</span>[<span class="pl-s1">row</span>][<span class="pl-s1">col</span> <span class="pl-c1">-</span> <span class="pl-c1">1</span>] <span class="pl-c1">==</span> <span class="pl-c1">0</span>:
                <span class="pl-s1">col</span> <span class="pl-c1">-=</span> <span class="pl-c1">1</span>
            <span class="pl-k">else</span>:
                <span class="pl-s1">direction</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span>
        <span class="pl-k">else</span>:
            <span class="pl-k">if</span> <span class="pl-s1">row</span> <span class="pl-c1">&gt;</span> <span class="pl-c1">0</span> <span class="pl-c1">and</span> <span class="pl-s1">matrix</span>[<span class="pl-s1">row</span> <span class="pl-c1">-</span> <span class="pl-c1">1</span>][<span class="pl-s1">col</span>] <span class="pl-c1">==</span> <span class="pl-c1">0</span>:
                <span class="pl-s1">row</span> <span class="pl-c1">-=</span> <span class="pl-c1">1</span>
            <span class="pl-k">else</span>:
                <span class="pl-s1">direction</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span>
        <span class="pl-s1">direction</span> <span class="pl-c1">%=</span> <span class="pl-c1">4</span>
    <span class="pl-k">for</span> <span class="pl-s1">x</span> <span class="pl-c1">in</span> <span class="pl-s1">matrix</span>:
        <span class="pl-k">for</span> <span class="pl-s1">y</span> <span class="pl-c1">in</span> <span class="pl-s1">x</span>:
            <span class="pl-en">print</span>(<span class="pl-s1">y</span>, <span class="pl-s1">end</span><span class="pl-c1">=</span><span class="pl-s">'<span class="pl-cce">\t</span>'</span>)
        <span class="pl-en">print</span>()</pre></div>
<h4><a id="user-content-题目017阅读下面的代码写出程序的运行结果" class="anchor" aria-hidden="true" href="#题目017阅读下面的代码写出程序的运行结果"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目017：阅读下面的代码，写出程序的运行结果。</h4>
<div class="highlight highlight-source-python"><pre><span class="pl-s1">items</span> <span class="pl-c1">=</span> [<span class="pl-c1">1</span>, <span class="pl-c1">2</span>, <span class="pl-c1">3</span>, <span class="pl-c1">4</span>] 
<span class="pl-en">print</span>([<span class="pl-s1">i</span> <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">items</span> <span class="pl-k">if</span> <span class="pl-s1">i</span> <span class="pl-c1">&gt;</span> <span class="pl-c1">2</span>])
<span class="pl-en">print</span>([<span class="pl-s1">i</span> <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">items</span> <span class="pl-k">if</span> <span class="pl-s1">i</span> <span class="pl-c1">%</span> <span class="pl-c1">2</span>])
<span class="pl-en">print</span>([(<span class="pl-s1">x</span>, <span class="pl-s1">y</span>) <span class="pl-k">for</span> <span class="pl-s1">x</span>, <span class="pl-s1">y</span> <span class="pl-c1">in</span> <span class="pl-en">zip</span>(<span class="pl-s">'abcd'</span>, (<span class="pl-c1">1</span>, <span class="pl-c1">2</span>, <span class="pl-c1">3</span>, <span class="pl-c1">4</span>, <span class="pl-c1">5</span>))])
<span class="pl-en">print</span>({<span class="pl-s1">x</span>: <span class="pl-s">f'item<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">x</span> <span class="pl-c1">**</span> <span class="pl-c1">2</span><span class="pl-kos">}</span></span>'</span> <span class="pl-k">for</span> <span class="pl-s1">x</span> <span class="pl-c1">in</span> (<span class="pl-c1">2</span>, <span class="pl-c1">4</span>, <span class="pl-c1">6</span>)})
<span class="pl-en">print</span>(<span class="pl-en">len</span>({<span class="pl-s1">x</span> <span class="pl-k">for</span> <span class="pl-s1">x</span> <span class="pl-c1">in</span> <span class="pl-s">'hello world'</span> <span class="pl-k">if</span> <span class="pl-s1">x</span> <span class="pl-c1">not</span> <span class="pl-c1">in</span> <span class="pl-s">'abcdefg'</span>}))</pre></div>
<blockquote>
<p><strong>点评</strong>：<strong>生成式（推导式）属于Python的特色语法之一，几乎是面试必考内容</strong>。Python中通过生成式字面量语法，可以创建出列表、集合、字典。</p>
</blockquote>
<pre><code>[3, 4]
[1, 3]
[('a', 1), ('b', 2), ('c', 3), ('d', 4)]
{2: 'item4', 4: 'item16', 6: 'item36'}
6
</code></pre>
<h4><a id="user-content-题目018说出下面代码的运行结果" class="anchor" aria-hidden="true" href="#题目018说出下面代码的运行结果"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目018：说出下面代码的运行结果。</h4>
<div class="highlight highlight-source-python"><pre><span class="pl-k">class</span> <span class="pl-v">Parent</span>:
    <span class="pl-s1">x</span> <span class="pl-c1">=</span> <span class="pl-c1">1</span>

<span class="pl-k">class</span> <span class="pl-v">Child1</span>(<span class="pl-v">Parent</span>):
    <span class="pl-k">pass</span>

<span class="pl-k">class</span> <span class="pl-v">Child2</span>(<span class="pl-v">Parent</span>):
    <span class="pl-k">pass</span>

<span class="pl-en">print</span>(<span class="pl-v">Parent</span>.<span class="pl-s1">x</span>, <span class="pl-v">Child1</span>.<span class="pl-s1">x</span>, <span class="pl-v">Child2</span>.<span class="pl-s1">x</span>)
<span class="pl-v">Child1</span>.<span class="pl-s1">x</span> <span class="pl-c1">=</span> <span class="pl-c1">2</span>
<span class="pl-en">print</span>(<span class="pl-v">Parent</span>.<span class="pl-s1">x</span>, <span class="pl-v">Child1</span>.<span class="pl-s1">x</span>, <span class="pl-v">Child2</span>.<span class="pl-s1">x</span>)
<span class="pl-v">Parent</span>.<span class="pl-s1">x</span> <span class="pl-c1">=</span> <span class="pl-c1">3</span>
<span class="pl-en">print</span>(<span class="pl-v">Parent</span>.<span class="pl-s1">x</span>, <span class="pl-v">Child1</span>.<span class="pl-s1">x</span>, <span class="pl-v">Child2</span>.<span class="pl-s1">x</span>)</pre></div>
<blockquote>
<p><strong>点评</strong>：运行上面的代码首先输出<code>1 1 1</code>，这一点大家应该没有什么疑问。接下来，通过<code>Child1.x = 2</code>给类<code>Child1</code>重新绑定了属性<code>x</code>并赋值为<code>2</code>，所以<code>Child1.x</code>会输出<code>2</code>，而<code>Parent</code>和<code>Child2</code>并不受影响。执行<code>Parent.x = 3</code>会重新给<code>Parent</code>类的<code>x</code>属性赋值为<code>3</code>，由于<code>Child2</code>的<code>x</code>属性继承自<code>Parent</code>，所以<code>Child2.x</code>的值也是<code>3</code>；而之前我们为<code>Child1</code>重新绑定了<code>x</code>属性，那么它的<code>x</code>属性值不会受到<code>Parent.x = 3</code>的影响，还是之前的值<code>2</code>。</p>
</blockquote>
<pre><code>1 1 1
1 2 1
3 2 3
</code></pre>
<h4><a id="user-content-题目19说说你用过python标准库中的哪些模块" class="anchor" aria-hidden="true" href="#题目19说说你用过python标准库中的哪些模块"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目19：说说你用过Python标准库中的哪些模块。</h4>
<blockquote>
<p><strong>点评</strong>：Python标准库中的模块非常多，建议大家根据自己过往的项目经历来介绍你用过的标准库和三方库，因为这些是你最为熟悉的，经得起面试官深挖的。</p>
</blockquote>
<table>
<thead>
<tr>
<th>模块名</th>
<th>介绍</th>
</tr>
</thead>
<tbody>
<tr>
<td>sys</td>
<td>跟Python解释器相关的变量和函数，例如：<code>sys.version</code>、<code>sys.exit()</code></td>
</tr>
<tr>
<td>os</td>
<td>和操作系统相关的功能，例如：<code>os.listdir()</code>、<code>os.remove()</code></td>
</tr>
<tr>
<td>re</td>
<td>和正则表达式相关的功能，例如：<code>re.compile()</code>、<code>re.search()</code></td>
</tr>
<tr>
<td>math</td>
<td>和数学运算相关的功能，例如：<code>math.pi</code>、<code>math.e</code>、<code>math.cos</code></td>
</tr>
<tr>
<td>logging</td>
<td>和日志系统相关的类和函数，例如：<code>logging.Logger</code>、<code>logging.Handler</code></td>
</tr>
<tr>
<td>json / pickle</td>
<td>实现对象序列化和反序列的模块，例如：<code>json.loads</code>、<code>json.dumps</code></td>
</tr>
<tr>
<td>hashlib</td>
<td>封装了多种哈希摘要算法的模块，例如：<code>hashlib.md5</code>、<code>hashlib.sha1</code></td>
</tr>
<tr>
<td>urllib</td>
<td>包含了和URL相关的子模块，例如：<code>urllib.request</code>、<code>urllib.parse</code></td>
</tr>
<tr>
<td>itertools</td>
<td>提供各种迭代器的模块，例如：<code>itertools.cycle</code>、<code>itertools.product</code></td>
</tr>
<tr>
<td>functools</td>
<td>函数相关工具模块，例如：<code>functools.partial</code>、<code>functools.lru_cache</code></td>
</tr>
<tr>
<td>collections / heapq</td>
<td>封装了常用数据结构和算法的模块，例如：<code>collections.deque</code></td>
</tr>
<tr>
<td>threading / multiprocessing</td>
<td>多线程/多进程相关类和函数的模块，例如：<code>threading.Thread</code></td>
</tr>
<tr>
<td>concurrent.futures / asyncio</td>
<td>并发编程/异步编程相关的类和函数的模块，例如：<code>ThreadPoolExecutor</code></td>
</tr>
<tr>
<td>base64</td>
<td>提供BASE-64编码相关函数的模块，例如：<code>bas64.encode</code></td>
</tr>
<tr>
<td>csv</td>
<td>和读写CSV文件相关的模块，例如：<code>csv.reader</code>、<code>csv.writer</code></td>
</tr>
<tr>
<td>profile / cProfile / pstats</td>
<td>和代码性能剖析相关的模块，例如：<code>cProfile.run</code>、<code>pstats.Stats</code></td>
</tr>
<tr>
<td>unittest</td>
<td>和单元测试相关的模块，例如：<code>unittest.TestCase</code></td>
</tr>
</tbody>
</table>
<h4><a id="user-content-题目20__init__和__new__方法有什么区别" class="anchor" aria-hidden="true" href="#题目20__init__和__new__方法有什么区别"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目20：<code>__init__</code>和<code>__new__</code>方法有什么区别？</h4>
<p>Python中调用构造器创建对象属于两阶段构造过程，首先执行<code>__new__</code>方法获得保存对象所需的内存空间，再通过<code>__init__</code>执行对内存空间数据的填充（对象属性的初始化）。<code>__new__</code>方法的返回值是创建好的Python对象（的引用），而<code>__init__</code>方法的第一个参数就是这个对象（的引用），所以在<code>__init__</code>中可以完成对对象的初始化操作。<code>__new__</code>是类方法，它的第一个参数是类，<code>__init__</code>是对象方法，它的第一个参数是对象。</p>
<h4><a id="user-content-题目21输入年月日判断这个日期是这一年的第几天" class="anchor" aria-hidden="true" href="#题目21输入年月日判断这个日期是这一年的第几天"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目21：输入年月日，判断这个日期是这一年的第几天。</h4>
<p>方法一：不使用标准库中的模块和函数。</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">def</span> <span class="pl-en">is_leap_year</span>(<span class="pl-s1">year</span>):
    <span class="pl-s">"""判断指定的年份是不是闰年，平年返回False，闰年返回True"""</span>
    <span class="pl-k">return</span> <span class="pl-s1">year</span> <span class="pl-c1">%</span> <span class="pl-c1">4</span> <span class="pl-c1">==</span> <span class="pl-c1">0</span> <span class="pl-c1">and</span> <span class="pl-s1">year</span> <span class="pl-c1">%</span> <span class="pl-c1">100</span> <span class="pl-c1">!=</span> <span class="pl-c1">0</span> <span class="pl-c1">or</span> <span class="pl-s1">year</span> <span class="pl-c1">%</span> <span class="pl-c1">400</span> <span class="pl-c1">==</span> <span class="pl-c1">0</span>

<span class="pl-k">def</span> <span class="pl-en">which_day</span>(<span class="pl-s1">year</span>, <span class="pl-s1">month</span>, <span class="pl-s1">date</span>):
    <span class="pl-s">"""计算传入的日期是这一年的第几天"""</span>
    <span class="pl-c"># 用嵌套的列表保存平年和闰年每个月的天数</span>
    <span class="pl-s1">days_of_month</span> <span class="pl-c1">=</span> [
        [<span class="pl-c1">31</span>, <span class="pl-c1">28</span>, <span class="pl-c1">31</span>, <span class="pl-c1">30</span>, <span class="pl-c1">31</span>, <span class="pl-c1">30</span>, <span class="pl-c1">31</span>, <span class="pl-c1">31</span>, <span class="pl-c1">30</span>, <span class="pl-c1">31</span>, <span class="pl-c1">30</span>, <span class="pl-c1">31</span>],
        [<span class="pl-c1">31</span>, <span class="pl-c1">29</span>, <span class="pl-c1">31</span>, <span class="pl-c1">30</span>, <span class="pl-c1">31</span>, <span class="pl-c1">30</span>, <span class="pl-c1">31</span>, <span class="pl-c1">31</span>, <span class="pl-c1">30</span>, <span class="pl-c1">31</span>, <span class="pl-c1">30</span>, <span class="pl-c1">31</span>]
    ]
    <span class="pl-s1">days</span> <span class="pl-c1">=</span> <span class="pl-s1">days_of_month</span>[<span class="pl-en">is_leap_year</span>(<span class="pl-s1">year</span>)][:<span class="pl-s1">month</span> <span class="pl-c1">-</span> <span class="pl-c1">1</span>]
    <span class="pl-k">return</span> <span class="pl-en">sum</span>(<span class="pl-s1">days</span>) <span class="pl-c1">+</span> <span class="pl-s1">date</span></pre></div>
<p>方法二：使用标准库中的<code>datetime</code>模块。</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> <span class="pl-s1">datetime</span>

<span class="pl-k">def</span> <span class="pl-en">which_day</span>(<span class="pl-s1">year</span>, <span class="pl-s1">month</span>, <span class="pl-s1">date</span>):
    <span class="pl-s1">end</span> <span class="pl-c1">=</span> <span class="pl-s1">datetime</span>.<span class="pl-en">date</span>(<span class="pl-s1">year</span>, <span class="pl-s1">month</span>, <span class="pl-s1">date</span>)
    <span class="pl-s1">start</span> <span class="pl-c1">=</span> <span class="pl-s1">datetime</span>.<span class="pl-en">date</span>(<span class="pl-s1">year</span>, <span class="pl-c1">1</span>, <span class="pl-c1">1</span>)
    <span class="pl-k">return</span> (<span class="pl-s1">end</span> <span class="pl-c1">-</span> <span class="pl-s1">start</span>).<span class="pl-s1">days</span> <span class="pl-c1">+</span> <span class="pl-c1">1</span></pre></div>
<h4><a id="user-content-题目22平常工作中用什么工具进行静态代码分析" class="anchor" aria-hidden="true" href="#题目22平常工作中用什么工具进行静态代码分析"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目22：平常工作中用什么工具进行静态代码分析。</h4>
<blockquote>
<p><strong>点评</strong>：静态代码分析工具可以从代码中提炼出各种静态属性，这使得开发者可以对代码的复杂性、可维护性和可读性有更好的了解，这里所说的静态属性包括：</p>
<ol>
<li>代码是否符合编码规范，例如：PEP-8。</li>
<li>代码中潜在的问题，包括：语法错误、缩进问题、导入缺失、变量覆盖等。</li>
<li>代码中的坏味道。</li>
<li>代码的复杂度。</li>
<li>代码的逻辑问题。</li>
</ol>
</blockquote>
<p>工作中静态代码分析主要用到的是<a href="https://www.pylint.org/" rel="nofollow">Pylint</a>和<a href="https://flake8.pycqa.org/en/latest/" rel="nofollow">Flake8</a>。Pylint可以检查出代码错误、坏味道、不规范的代码等问题，较新的版本中还提供了代码复杂度统计数据，可以生成检查报告。Flake8封装了Pyflakes（检查代码逻辑错误）、McCabe（检查代码复杂性）和Pycodestyle（检查代码是否符合PEP-8规范）工具，它可以执行这三个工具提供的检查。</p>
<h4><a id="user-content-题目23说一下你知道的python中的魔术方法" class="anchor" aria-hidden="true" href="#题目23说一下你知道的python中的魔术方法"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目23：说一下你知道的Python中的魔术方法。</h4>
<blockquote>
<p><strong>点评</strong>：魔术方法也称为魔法方法，是Python中的特色语法，也是面试中的高频问题。</p>
</blockquote>
<table>
<thead>
<tr>
<th>魔术方法</th>
<th>作用</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>__new__</code>、<code>__init__</code>、<code>__del__</code></td>
<td>创建和销毁对象相关</td>
</tr>
<tr>
<td><code>__add__</code>、<code>__sub__</code>、<code>__mul__</code>、<code>__div__</code>、<code>__floordiv__</code>、<code>__mod__</code></td>
<td>算术运算符相关</td>
</tr>
<tr>
<td><code>__eq__</code>、<code>__ne__</code>、<code>__lt__</code>、<code>__gt__</code>、<code>__le__</code>、<code>__ge__</code></td>
<td>关系运算符相关</td>
</tr>
<tr>
<td><code>__pos__</code>、<code>__neg__</code>、<code>__invert__</code></td>
<td>一元运算符相关</td>
</tr>
<tr>
<td><code>__lshift__</code>、<code>__rshift__</code>、<code>__and__</code>、<code>__or__</code>、<code>__xor__</code></td>
<td>位运算相关</td>
</tr>
<tr>
<td><code>__enter__</code>、<code>__exit__</code></td>
<td>上下文管理器协议</td>
</tr>
<tr>
<td><code>__iter__</code>、<code>__next__</code>、<code>__reversed__</code></td>
<td>迭代器协议</td>
</tr>
<tr>
<td><code>__int__</code>、<code>__long__</code>、<code>__float__</code>、<code>__oct__</code>、<code>__hex__</code></td>
<td>类型/进制转换相关</td>
</tr>
<tr>
<td><code>__str__</code>、<code>__repr__</code>、<code>__hash__</code>、<code>__dir__</code></td>
<td>对象表述相关</td>
</tr>
<tr>
<td><code>__len__</code>、<code>__getitem__</code>、<code>__setitem__</code>、<code>__contains__</code>、<code>__missing__</code></td>
<td>序列相关</td>
</tr>
<tr>
<td><code>__copy__</code>、<code>__deepcopy__</code></td>
<td>对象拷贝相关</td>
</tr>
<tr>
<td><code>__call__</code>、<code>__setattr__</code>、<code>__getattr__</code>、<code>__delattr__</code></td>
<td>其他魔术方法</td>
</tr>
</tbody>
</table>
<h4><a id="user-content-题目24函数参数arg和kwargs分别代表什么" class="anchor" aria-hidden="true" href="#题目24函数参数arg和kwargs分别代表什么"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目24：函数参数<code>*arg</code>和<code>**kwargs</code>分别代表什么？</h4>
<p>Python中，函数的参数分为位置参数、可变参数、关键字参数、命名关键字参数。<code>*args</code>代表可变参数，可以接收<code>0</code>个或任意多个参数，当不确定调用者会传入多少个位置参数时，就可以使用可变参数，它会将传入的参数打包成一个元组。<code>**kwargs</code>代表关键字参数，可以接收用<code>参数名=参数值</code>的方式传入的参数，传入的参数的会打包成一个字典。定义函数时如果同时使用<code>*args</code>和<code>**kwargs</code>，那么函数可以接收任意参数。</p>
<h4><a id="user-content-题目25写一个记录函数执行时间的装饰器" class="anchor" aria-hidden="true" href="#题目25写一个记录函数执行时间的装饰器"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目25：写一个记录函数执行时间的装饰器。</h4>
<blockquote>
<p><strong>点评</strong>：高频面试题，也是最简单的装饰器，面试者<strong>必须要掌握的内容</strong>。</p>
</blockquote>
<p>方法一：用函数实现装饰器。</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">from</span> <span class="pl-s1">functools</span> <span class="pl-k">import</span> <span class="pl-s1">wraps</span>
<span class="pl-k">from</span> <span class="pl-s1">time</span> <span class="pl-k">import</span> <span class="pl-s1">time</span>


<span class="pl-k">def</span> <span class="pl-en">record_time</span>(<span class="pl-s1">func</span>):
    
    <span class="pl-en">@<span class="pl-s1">wraps</span>(<span class="pl-s1">func</span>)</span>
    <span class="pl-k">def</span> <span class="pl-en">wrapper</span>(<span class="pl-c1">*</span><span class="pl-s1">args</span>, <span class="pl-c1">**</span><span class="pl-s1">kwargs</span>):
        <span class="pl-s1">start</span> <span class="pl-c1">=</span> <span class="pl-en">time</span>()
        <span class="pl-s1">result</span> <span class="pl-c1">=</span> <span class="pl-en">func</span>(<span class="pl-c1">*</span><span class="pl-s1">args</span>, <span class="pl-c1">**</span><span class="pl-s1">kwargs</span>)
        <span class="pl-en">print</span>(<span class="pl-s">f'<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">func</span>.<span class="pl-s1">__name__</span><span class="pl-kos">}</span></span>执行时间: <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-en">time</span>() <span class="pl-c1">-</span> <span class="pl-s1">start</span><span class="pl-kos">}</span></span>秒'</span>)
        <span class="pl-k">return</span> <span class="pl-s1">result</span>
        
    <span class="pl-k">return</span> <span class="pl-s1">wrapper</span></pre></div>
<p>方法二：用类实现装饰器。类有<code>__call__</code>魔术方法，该类对象就是可调用对象，可以当做装饰器来使用。</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">from</span> <span class="pl-s1">functools</span> <span class="pl-k">import</span> <span class="pl-s1">wraps</span>
<span class="pl-k">from</span> <span class="pl-s1">time</span> <span class="pl-k">import</span> <span class="pl-s1">time</span>


<span class="pl-k">class</span> <span class="pl-v">Record</span>:
    
    <span class="pl-k">def</span> <span class="pl-en">__call__</span>(<span class="pl-s1">self</span>, <span class="pl-s1">func</span>):
        
        <span class="pl-en">@<span class="pl-s1">wraps</span>(<span class="pl-s1">func</span>)</span>
        <span class="pl-k">def</span> <span class="pl-en">wrapper</span>(<span class="pl-c1">*</span><span class="pl-s1">args</span>, <span class="pl-c1">**</span><span class="pl-s1">kwargs</span>):
            <span class="pl-s1">start</span> <span class="pl-c1">=</span> <span class="pl-en">time</span>()
            <span class="pl-s1">result</span> <span class="pl-c1">=</span> <span class="pl-en">func</span>(<span class="pl-c1">*</span><span class="pl-s1">args</span>, <span class="pl-c1">**</span><span class="pl-s1">kwargs</span>)
            <span class="pl-en">print</span>(<span class="pl-s">f'<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">func</span>.<span class="pl-s1">__name__</span><span class="pl-kos">}</span></span>执行时间: <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-en">time</span>() <span class="pl-c1">-</span> <span class="pl-s1">start</span><span class="pl-kos">}</span></span>秒'</span>)
            <span class="pl-k">return</span> <span class="pl-s1">result</span>
        
        <span class="pl-k">return</span> <span class="pl-s1">wrapper</span></pre></div>
<blockquote>
<p><strong>说明</strong>：装饰器可以用来装饰类或函数，为其提供额外的能力，属于设计模式中的<strong>代理模式</strong>。</p>
</blockquote>
<blockquote>
<p><strong>扩展</strong>：<strong>装饰器本身也可以参数化</strong>，例如上面的例子中，如果不希望在终端中显示函数的执行时间而是希望由调用者来决定如何输出函数的执行时间，可以通过参数化装饰器的方式来做到，代码如下所示。</p>
</blockquote>
<div class="highlight highlight-source-python"><pre><span class="pl-k">from</span> <span class="pl-s1">functools</span> <span class="pl-k">import</span> <span class="pl-s1">wraps</span>
<span class="pl-k">from</span> <span class="pl-s1">time</span> <span class="pl-k">import</span> <span class="pl-s1">time</span>


<span class="pl-k">def</span> <span class="pl-en">record_time</span>(<span class="pl-s1">output</span>):
    <span class="pl-s">"""可以参数化的装饰器"""</span>
	
	<span class="pl-k">def</span> <span class="pl-en">decorate</span>(<span class="pl-s1">func</span>):
		
		<span class="pl-en">@<span class="pl-s1">wraps</span>(<span class="pl-s1">func</span>)</span>
		<span class="pl-k">def</span> <span class="pl-en">wrapper</span>(<span class="pl-c1">*</span><span class="pl-s1">args</span>, <span class="pl-c1">**</span><span class="pl-s1">kwargs</span>):
			<span class="pl-s1">start</span> <span class="pl-c1">=</span> <span class="pl-en">time</span>()
			<span class="pl-s1">result</span> <span class="pl-c1">=</span> <span class="pl-en">func</span>(<span class="pl-c1">*</span><span class="pl-s1">args</span>, <span class="pl-c1">**</span><span class="pl-s1">kwargs</span>)
			<span class="pl-en">output</span>(<span class="pl-s1">func</span>.<span class="pl-s1">__name__</span>, <span class="pl-en">time</span>() <span class="pl-c1">-</span> <span class="pl-s1">start</span>)
			<span class="pl-k">return</span> <span class="pl-s1">result</span>
            
		<span class="pl-k">return</span> <span class="pl-s1">wrapper</span>
	
	<span class="pl-k">return</span> <span class="pl-s1">decorate</span></pre></div>
<h4><a id="user-content-题目26什么是鸭子类型duck-typing" class="anchor" aria-hidden="true" href="#题目26什么是鸭子类型duck-typing"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目26：什么是鸭子类型（duck typing）？</h4>
<p>鸭子类型是动态类型语言判断一个对象是不是某种类型时使用的方法，也叫做鸭子判定法。简单的说，鸭子类型是指判断一只鸟是不是鸭子，我们只关心它游泳像不像鸭子、叫起来像不像鸭子、走路像不像鸭子就足够了。换言之，如果对象的行为跟我们的预期是一致的（能够接受某些消息），我们就认定它是某种类型的对象。</p>
<p>在Python语言中，有很多bytes-like对象（如：<code>bytes</code>、<code>bytearray</code>、<code>array.array</code>、<code>memoryview</code>）、file-like对象（如：<code>StringIO</code>、<code>BytesIO</code>、<code>GzipFile</code>、<code>socket</code>）、path-like对象（如：<code>str</code>、<code>bytes</code>），其中file-like对象都能支持<code>read</code>和<code>write</code>操作，可以像文件一样读写，这就是所谓的对象有鸭子的行为就可以判定为鸭子的判定方法。再比如Python中列表的<code>extend</code>方法，它需要的参数并不一定要是列表，只要是可迭代对象就没有问题。</p>
<blockquote>
<p><strong>说明</strong>：动态语言的鸭子类型使得设计模式的应用被大大简化。</p>
</blockquote>
<h4><a id="user-content-题目27说一下python中变量的作用域" class="anchor" aria-hidden="true" href="#题目27说一下python中变量的作用域"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目27：说一下Python中变量的作用域。</h4>
<p>Python中有四种作用域，分别是局部作用域（<strong>L</strong>ocal）、嵌套作用域（<strong>E</strong>mbedded）、全局作用域（<strong>G</strong>lobal）、内置作用域（<strong>B</strong>uilt-in），搜索一个标识符时，会按照<strong>LEGB</strong>的顺序进行搜索，如果所有的作用域中都没有找到这个标识符，就会引发<code>NameError</code>异常。</p>
<h4><a id="user-content-题目28说一下你对闭包的理解" class="anchor" aria-hidden="true" href="#题目28说一下你对闭包的理解"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目28：说一下你对闭包的理解。</h4>
<p>闭包是支持一等函数的编程语言（Python、JavaScript等）中实现词法绑定的一种技术。当捕捉闭包的时候，它的自由变量（在函数外部定义但在函数内部使用的变量）会在捕捉时被确定，这样即便脱离了捕捉时的上下文，它也能照常运行。简单的说，可以将闭包理解为<strong>能够读取其他函数内部变量的函数</strong>。正在情况下，函数的局部变量在函数调用结束之后就结束了生命周期，但是<strong>闭包使得局部变量的生命周期得到了延展</strong>。使用闭包的时候需要注意，闭包会使得函数中创建的对象不会被垃圾回收，可能会导致很大的内存开销，所以<strong>闭包一定不能滥用</strong>。</p>
<h4><a id="user-content-题目29说一下python中的多线程和多进程的应用场景和优缺点" class="anchor" aria-hidden="true" href="#题目29说一下python中的多线程和多进程的应用场景和优缺点"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目29：说一下Python中的多线程和多进程的应用场景和优缺点。</h4>
<p>线程是操作系统分配CPU的基本单位，进程是操作系统分配内存的基本单位。通常我们运行的程序会包含一个或多个进程，而每个进程中又包含一个或多个线程。多线程的优点在于多个线程可以共享进程的内存空间，所以进程间的通信非常容易实现；但是如果使用官方的CPython解释器，多线程受制于GIL（全局解释器锁），并不能利用CPU的多核特性，这是一个很大的问题。使用多进程可以充分利用CPU的多核特性，但是进程间通信相对比较麻烦，需要使用IPC机制（管道、套接字等）。</p>
<p>多线程适合那些会花费大量时间在I/O操作上，但没有太多并行计算需求且不需占用太多内存的I/O密集型应用。多进程适合执行计算密集型任务（如：视频编码解码、数据处理、科学计算等）、可以分解为多个并行子任务并能合并子任务执行结果的任务以及在内存使用方面没有任何限制且不强依赖于I/O操作的任务。</p>
<blockquote>
<p><strong>扩展</strong>：Python中实现并发编程通常有多线程、多进程和异步编程三种选择。异步编程实现了协作式并发，通过多个相互协作的子程序的用户态切换，实现对CPU的高效利用，这种方式也是非常适合I/O密集型应用的。</p>
</blockquote>
<h4><a id="user-content-题目30说一下python-2和python-3的区别" class="anchor" aria-hidden="true" href="#题目30说一下python-2和python-3的区别"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目30：说一下Python 2和Python 3的区别。</h4>
<blockquote>
<p><strong>点评</strong>：这种问题千万不要背所谓的参考答案，说一些自己最熟悉的就足够了。</p>
</blockquote>
<ol>
<li>Python 2中的<code>print</code>和<code>exec</code>都是关键字，在Python 3中变成了函数。</li>
<li>Python 3中没有<code>long</code>类型，整数都是<code>int</code>类型。</li>
<li>Python 2中的不等号<code>&lt;&gt;</code>在Python 3中被废弃，统一使用<code>!=</code>。</li>
<li>Python 2中的<code>xrange</code>函数在Python 3中被<code>range</code>函数取代。</li>
<li>Python 3对Python 2中不安全的<code>input</code>函数做出了改进，废弃了<code>raw_input</code>函数。</li>
<li>Python 2中的<code>file</code>函数被Python 3中的<code>open</code>函数取代。</li>
<li>Python 2中的<code>/</code>运算对于<code>int</code>类型是整除，在Python 3中要用<code>//</code>来做整除除法。</li>
<li>Python 3中改进了Python 2捕获异常的代码，很明显Python 3的写法更合理。</li>
<li>Python 3生成式中循环变量的作用域得到了更好的控制，不会影响到生成式之外的同名变量。</li>
<li>Python 3中的<code>round</code>函数可以返回<code>int</code>或<code>float</code>类型，Python 2中的<code>round</code>函数返回<code>float</code>类型。</li>
<li>Python 3的<code>str</code>类型是Unicode字符串，Python 2的<code>str</code>类型是字节串，相当于Python 3中的<code>bytes</code>。</li>
<li>Python 3中的比较运算符必须比较同类对象。</li>
<li>Python 3中定义类的都是新式类，Python 2中定义的类有新式类（显式继承自<code>object</code>的类）和旧式类（经典类）之分，新式类和旧式类在MRO问题上有非常显著的区别，新式类可以使用<code>__class__</code>属性获取自身类型，新式类可以使用<code>__slots__</code>魔法。</li>
<li>Python 3对代码缩进的要求更加严格，如果混用空格和制表键会引发<code>TabError</code>。</li>
<li>Python 3中字典的<code>keys</code>、<code>values</code>、<code>items</code>方法都不再返回<code>list</code>对象，而是返回<code>view object</code>，内置的<code>map</code>、<code>filter</code>等函数也不再返回<code>list</code>对象，而是返回迭代器对象。</li>
<li>Python 3标准库中某些模块的名字跟Python 2是有区别的；而在三方库方面，有些三方库只支持Python 2，有些只能支持Python 3。</li>
</ol>
<h4><a id="user-content-题目31谈谈你对猴子补丁monkey-patching的理解" class="anchor" aria-hidden="true" href="#题目31谈谈你对猴子补丁monkey-patching的理解"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目31：谈谈你对“猴子补丁”（monkey patching）的理解。</h4>
<p>“猴子补丁”是动态类型语言的一个特性，代码运行时在不修改源代码的前提下改变代码中的方法、属性、函数等以达到热补丁（hot patch）的效果。很多系统的安全补丁也是通过猴子补丁的方式来实现的，但实际开发中应该避免对猴子补丁的使用，以免造成代码行为不一致的问题。</p>
<p>在使用<code>gevent</code>库的时候，我们会在代码开头的地方执行<code>gevent.monkey.patch_all()</code>，这行代码的作用是把标准库中的<code>socket</code>模块给替换掉，这样我们在使用<code>socket</code>的时候，不用修改任何代码就可以实现对代码的协程化，达到提升性能的目的，这就是对猴子补丁的应用。</p>
<p>另外，如果希望用<code>ujson</code>三方库替换掉标准库中的<code>json</code>，也可以使用猴子补丁的方式，代码如下所示。</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> <span class="pl-s1">json</span>, <span class="pl-s1">ujson</span>

<span class="pl-s1">json</span>.<span class="pl-s1">__name__</span> <span class="pl-c1">=</span> <span class="pl-s">'ujson'</span>
<span class="pl-s1">json</span>.<span class="pl-s1">dumps</span> <span class="pl-c1">=</span> <span class="pl-s1">ujson</span>.<span class="pl-s1">dumps</span>
<span class="pl-s1">json</span>.<span class="pl-s1">loads</span> <span class="pl-c1">=</span> <span class="pl-s1">ujson</span>.<span class="pl-s1">loads</span></pre></div>
<p>单元测试中的<code>Mock</code>技术也是对猴子补丁的应用，Python中的<code>unittest.mock</code>模块就是解决单元测试中用<code>Mock</code>对象替代被测对象所依赖的对象的模块。</p>
<h4><a id="user-content-题目32阅读下面的代码说出运行结果" class="anchor" aria-hidden="true" href="#题目32阅读下面的代码说出运行结果"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目32：阅读下面的代码说出运行结果。</h4>
<div class="highlight highlight-source-python"><pre><span class="pl-k">class</span> <span class="pl-v">A</span>:
    <span class="pl-k">def</span> <span class="pl-en">who</span>(<span class="pl-s1">self</span>):
        <span class="pl-en">print</span>(<span class="pl-s">'A'</span>, <span class="pl-s1">end</span><span class="pl-c1">=</span><span class="pl-s">''</span>)

<span class="pl-k">class</span> <span class="pl-v">B</span>(<span class="pl-v">A</span>):
    <span class="pl-k">def</span> <span class="pl-en">who</span>(<span class="pl-s1">self</span>):
        <span class="pl-en">super</span>(<span class="pl-v">B</span>, <span class="pl-s1">self</span>).<span class="pl-en">who</span>()
        <span class="pl-en">print</span>(<span class="pl-s">'B'</span>, <span class="pl-s1">end</span><span class="pl-c1">=</span><span class="pl-s">''</span>)

<span class="pl-k">class</span> <span class="pl-v">C</span>(<span class="pl-v">A</span>):
    <span class="pl-k">def</span> <span class="pl-en">who</span>(<span class="pl-s1">self</span>):
        <span class="pl-en">super</span>(<span class="pl-v">C</span>, <span class="pl-s1">self</span>).<span class="pl-en">who</span>()
        <span class="pl-en">print</span>(<span class="pl-s">'C'</span>, <span class="pl-s1">end</span><span class="pl-c1">=</span><span class="pl-s">''</span>)

<span class="pl-k">class</span> <span class="pl-v">D</span>(<span class="pl-v">B</span>, <span class="pl-v">C</span>):
    <span class="pl-k">def</span> <span class="pl-en">who</span>(<span class="pl-s1">self</span>):
        <span class="pl-en">super</span>(<span class="pl-v">D</span>, <span class="pl-s1">self</span>).<span class="pl-en">who</span>()
        <span class="pl-en">print</span>(<span class="pl-s">'D'</span>, <span class="pl-s1">end</span><span class="pl-c1">=</span><span class="pl-s">''</span>)

<span class="pl-s1">item</span> <span class="pl-c1">=</span> <span class="pl-v">D</span>()
<span class="pl-s1">item</span>.<span class="pl-en">who</span>()</pre></div>
<blockquote>
<p><strong>点评</strong>：这道题考查到了两个知识点：</p>
<ol>
<li>Python中的MRO（方法解析顺序）。在没有多重继承的情况下，向对象发出一个消息，如果对象没有对应的方法，那么向上（父类）搜索的顺序是非常清晰的。如果向上追溯到<code>object</code>类（所有类的父类）都没有找到对应的方法，那么将会引发<code>AttributeError</code>异常。但是有多重继承尤其是出现菱形继承（钻石继承）的时候，向上追溯到底应该找到那个方法就得确定MRO。Python 3中的类以及Python 2中的新式类使用<a href="https://www.jianshu.com/p/a08c61abe895" rel="nofollow">C3算法</a>来确定MRO，它是一种类似于广度优先搜索的方法；Python 2中的旧式类（经典类）使用深度优先搜索来确定MRO。在搞不清楚MRO的情况下，可以使用类的<code>mro</code>方法或<code>__mro__</code>属性来获得类的MRO列表。</li>
<li><code>super()</code>函数的使用。在使用<code>super</code>函数时，可以通过<code>super(类型, 对象)</code>来指定对哪个对象以哪个类为起点向上搜索父类方法。所以上面<code>B</code>类代码中的<code>super(B, self).who()</code>表示以B类为起点，向上搜索<code>self</code>（D类对象）的<code>who</code>方法，所以会找到<code>C</code>类中的<code>who</code>方法，因为<code>D</code>类对象的MRO列表是<code>D --&gt; B --&gt; C --&gt; A --&gt; object</code>。</li>
</ol>
</blockquote>
<pre><code>ACBD
</code></pre>
<h4><a id="user-content-题目33编写一个函数实现对逆波兰表达式求值不能使用python的内置函数" class="anchor" aria-hidden="true" href="#题目33编写一个函数实现对逆波兰表达式求值不能使用python的内置函数"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目33：编写一个函数实现对逆波兰表达式求值，不能使用Python的内置函数。</h4>
<blockquote>
<p><strong>点评</strong>：<a href="https://baike.baidu.com/item/%E9%80%86%E6%B3%A2%E5%85%B0%E5%BC%8F/128437" rel="nofollow">逆波兰表达式</a>也称为“后缀表达式”，相较于平常我们使用的“中缀表达式”，逆波兰表达式不需要括号来确定运算的优先级，例如<code>5 * (2 + 3)</code>对应的逆波兰表达式是<code>5 2 3 + *</code>。逆波兰表达式求值需要借助栈结构，扫描表达式遇到运算数就入栈，遇到运算符就出栈两个元素做运算，将运算结果入栈。表达式扫描结束后，栈中只有一个数，这个数就是最终的运算结果，直接出栈即可。</p>
</blockquote>
<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> <span class="pl-s1">operator</span>


<span class="pl-k">class</span> <span class="pl-v">Stack</span>:
    <span class="pl-s">"""栈（FILO）"""</span>

    <span class="pl-k">def</span> <span class="pl-en">__init__</span>(<span class="pl-s1">self</span>):
        <span class="pl-s1">self</span>.<span class="pl-s1">elems</span> <span class="pl-c1">=</span> []
    
    <span class="pl-k">def</span> <span class="pl-en">push</span>(<span class="pl-s1">self</span>, <span class="pl-s1">elem</span>):
        <span class="pl-s">"""入栈"""</span>
        <span class="pl-s1">self</span>.<span class="pl-s1">elems</span>.<span class="pl-en">append</span>(<span class="pl-s1">elem</span>)
    
    <span class="pl-k">def</span> <span class="pl-en">pop</span>(<span class="pl-s1">self</span>):
        <span class="pl-s">"""出栈"""</span>
        <span class="pl-k">return</span> <span class="pl-s1">self</span>.<span class="pl-s1">elems</span>.<span class="pl-en">pop</span>()
    
    <span class="pl-en">@<span class="pl-s1">property</span></span>
    <span class="pl-k">def</span> <span class="pl-en">is_empty</span>(<span class="pl-s1">self</span>):
        <span class="pl-s">"""检查栈是否为空"""</span>
        <span class="pl-k">return</span> <span class="pl-en">len</span>(<span class="pl-s1">self</span>.<span class="pl-s1">elems</span>) <span class="pl-c1">==</span> <span class="pl-c1">0</span>


<span class="pl-k">def</span> <span class="pl-en">eval_suffix</span>(<span class="pl-s1">expr</span>):
    <span class="pl-s">"""逆波兰表达式求值"""</span>
    <span class="pl-s1">operators</span> <span class="pl-c1">=</span> {
        <span class="pl-s">'+'</span>: <span class="pl-s1">operator</span>.<span class="pl-s1">add</span>,
        <span class="pl-s">'-'</span>: <span class="pl-s1">operator</span>.<span class="pl-s1">sub</span>,
        <span class="pl-s">'*'</span>: <span class="pl-s1">operator</span>.<span class="pl-s1">mul</span>,
        <span class="pl-s">'/'</span>: <span class="pl-s1">operator</span>.<span class="pl-s1">truediv</span>
    }
    <span class="pl-s1">stack</span> <span class="pl-c1">=</span> <span class="pl-v">Stack</span>()
    <span class="pl-k">for</span> <span class="pl-s1">item</span> <span class="pl-c1">in</span> <span class="pl-s1">expr</span>.<span class="pl-en">split</span>():
        <span class="pl-k">if</span> <span class="pl-s1">item</span>.<span class="pl-en">isdigit</span>():
            <span class="pl-s1">stack</span>.<span class="pl-en">push</span>(<span class="pl-en">float</span>(<span class="pl-s1">item</span>))
        <span class="pl-k">else</span>:              
            <span class="pl-s1">num2</span> <span class="pl-c1">=</span> <span class="pl-s1">stack</span>.<span class="pl-en">pop</span>()
            <span class="pl-s1">num1</span> <span class="pl-c1">=</span> <span class="pl-s1">stack</span>.<span class="pl-en">pop</span>()
            <span class="pl-s1">stack</span>.<span class="pl-en">push</span>(<span class="pl-s1">operators</span>[<span class="pl-s1">item</span>](<span class="pl-s1">num1</span>, <span class="pl-s1">num2</span>))
    <span class="pl-k">return</span> <span class="pl-s1">stack</span>.<span class="pl-en">pop</span>()</pre></div>
<h4><a id="user-content-题目34python中如何实现字符串替换操作" class="anchor" aria-hidden="true" href="#题目34python中如何实现字符串替换操作"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目34：Python中如何实现字符串替换操作？</h4>
<p>Python中实现字符串替换大致有两类方法：字符串的<code>replace</code>方法和正则表达式的<code>sub</code>方法。</p>
<p>方法一：使用字符串的<code>replace</code>方法。</p>
<div class="highlight highlight-source-python"><pre><span class="pl-s1">message</span> <span class="pl-c1">=</span> <span class="pl-s">'hello, world!'</span>
<span class="pl-en">print</span>(<span class="pl-s1">message</span>.<span class="pl-en">replace</span>(<span class="pl-s">'o'</span>, <span class="pl-s">'O'</span>).<span class="pl-en">replace</span>(<span class="pl-s">'l'</span>, <span class="pl-s">'L'</span>).<span class="pl-en">replace</span>(<span class="pl-s">'he'</span>, <span class="pl-s">'HE'</span>))</pre></div>
<p>方法二：使用正则表达式的<code>sub</code>方法。</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> <span class="pl-s1">re</span>

<span class="pl-s1">message</span> <span class="pl-c1">=</span> <span class="pl-s">'hello, world!'</span>
<span class="pl-s1">pattern</span> <span class="pl-c1">=</span> <span class="pl-s1">re</span>.<span class="pl-en">compile</span>(<span class="pl-s">'[aeiou]'</span>)
<span class="pl-en">print</span>(<span class="pl-s1">pattern</span>.<span class="pl-en">sub</span>(<span class="pl-s">'#'</span>, <span class="pl-s1">message</span>))</pre></div>
<blockquote>
<p><strong>扩展</strong>：还有一个相关的面试题，对保存文件名的列表排序，要求文件名按照字母表和数字大小进行排序，例如对于列表<code>filenames = ['a12.txt', 'a8.txt', 'b10.txt', 'b2.txt', 'b19.txt', 'a3.txt'] </code>，排序的结果是<code>['a3.txt', 'a8.txt', 'a12.txt', 'b2.txt', 'b10.txt', 'b19.txt']</code>。提示一下，可以通过字符串替换的方式为文件名补位，根据补位后的文件名用<code>sorted</code>函数来排序，大家可以思考下这个问题如何解决。</p>
</blockquote>
<h4><a id="user-content-题目35如何剖析python代码的执行性能" class="anchor" aria-hidden="true" href="#题目35如何剖析python代码的执行性能"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目35：如何剖析Python代码的执行性能？</h4>
<p>剖析代码性能可以使用Python标准库中的<code>cProfile</code>和<code>pstats</code>模块，<code>cProfile</code>的<code>run</code>函数可以执行代码并收集统计信息，创建出<code>Stats</code>对象并打印简单的剖析报告。<code>Stats</code>是<code>pstats</code>模块中的类，它是一个统计对象。当然，也可以使用三方工具<code>line_profiler</code>和<code>memory_profiler</code>来剖析每一行代码耗费的时间和内存，这两个三方工具都会用非常友好的方式输出剖析结构。如果使用PyCharm，可以利用“Run”菜单的“Profile”菜单项对代码进行性能分析，PyCharm中可以用表格或者调用图（Call Graph）的方式来显示性能剖析的结果。</p>
<p>下面是使用<code>cProfile</code>剖析代码性能的例子。</p>
<p><code>example.py</code></p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> <span class="pl-s1">cProfile</span>


<span class="pl-k">def</span> <span class="pl-en">is_prime</span>(<span class="pl-s1">num</span>):
    <span class="pl-k">for</span> <span class="pl-s1">factor</span> <span class="pl-c1">in</span> <span class="pl-en">range</span>(<span class="pl-c1">2</span>, <span class="pl-en">int</span>(<span class="pl-s1">num</span> <span class="pl-c1">**</span> <span class="pl-c1">0.5</span>) <span class="pl-c1">+</span> <span class="pl-c1">1</span>):
        <span class="pl-k">if</span> <span class="pl-s1">num</span> <span class="pl-c1">%</span> <span class="pl-s1">factor</span> <span class="pl-c1">==</span> <span class="pl-c1">0</span>:
            <span class="pl-k">return</span> <span class="pl-c1">False</span>
    <span class="pl-k">return</span> <span class="pl-c1">True</span>


<span class="pl-k">class</span> <span class="pl-v">PrimeIter</span>:

    <span class="pl-k">def</span> <span class="pl-en">__init__</span>(<span class="pl-s1">self</span>, <span class="pl-s1">total</span>):
        <span class="pl-s1">self</span>.<span class="pl-s1">counter</span> <span class="pl-c1">=</span> <span class="pl-c1">0</span>
        <span class="pl-s1">self</span>.<span class="pl-s1">current</span> <span class="pl-c1">=</span> <span class="pl-c1">1</span>
        <span class="pl-s1">self</span>.<span class="pl-s1">total</span> <span class="pl-c1">=</span> <span class="pl-s1">total</span>

    <span class="pl-k">def</span> <span class="pl-en">__iter__</span>(<span class="pl-s1">self</span>):
        <span class="pl-k">return</span> <span class="pl-s1">self</span>

    <span class="pl-k">def</span> <span class="pl-en">__next__</span>(<span class="pl-s1">self</span>):
        <span class="pl-k">if</span> <span class="pl-s1">self</span>.<span class="pl-s1">counter</span> <span class="pl-c1">&lt;</span> <span class="pl-s1">self</span>.<span class="pl-s1">total</span>:
            <span class="pl-s1">self</span>.<span class="pl-s1">current</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span>
            <span class="pl-k">while</span> <span class="pl-c1">not</span> <span class="pl-en">is_prime</span>(<span class="pl-s1">self</span>.<span class="pl-s1">current</span>):
                <span class="pl-s1">self</span>.<span class="pl-s1">current</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span>
            <span class="pl-s1">self</span>.<span class="pl-s1">counter</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span>
            <span class="pl-k">return</span> <span class="pl-s1">self</span>.<span class="pl-s1">current</span>
        <span class="pl-k">raise</span> <span class="pl-v">StopIteration</span>()


<span class="pl-s1">cProfile</span>.<span class="pl-en">run</span>(<span class="pl-s">'list(PrimeIter(10000))'</span>)</pre></div>
<p>如果使用<code>line_profiler</code>三方工具，可以直接剖析<code>is_prime</code>函数每行代码的性能，需要给<code>is_prime</code>函数添加一个<code>profiler</code>装饰器，代码如下所示。</p>
<div class="highlight highlight-source-python"><pre><span class="pl-en">@<span class="pl-s1">profiler</span></span>
<span class="pl-k">def</span> <span class="pl-en">is_prime</span>(<span class="pl-s1">num</span>):
    <span class="pl-k">for</span> <span class="pl-s1">factor</span> <span class="pl-c1">in</span> <span class="pl-en">range</span>(<span class="pl-c1">2</span>, <span class="pl-en">int</span>(<span class="pl-s1">num</span> <span class="pl-c1">**</span> <span class="pl-c1">0.5</span>) <span class="pl-c1">+</span> <span class="pl-c1">1</span>):
        <span class="pl-k">if</span> <span class="pl-s1">num</span> <span class="pl-c1">%</span> <span class="pl-s1">factor</span> <span class="pl-c1">==</span> <span class="pl-c1">0</span>:
            <span class="pl-k">return</span> <span class="pl-c1">False</span>
    <span class="pl-k">return</span> <span class="pl-c1">True</span></pre></div>
<p>安装<code>line_profiler</code>。</p>
<div class="highlight highlight-source-shell"><pre>pip install line_profiler</pre></div>
<p>使用<code>line_profiler</code>。</p>
<div class="highlight highlight-source-shell"><pre>kernprof -lv example.py</pre></div>
<p>运行结果如下所示。</p>
<pre><code>Line #    Hits    Time      Per Hit  % Time  Line Contents
==============================================================
     1                                       @profile
     2                                       def is_prime(num):
     3    86624   48420.0   0.6      50.5        for factor in range(2, int(num ** 0.5) + 1):
     4    85624   44000.0   0.5      45.9            if num % factor == 0:
     5    6918     3080.0   0.4       3.2                return False
     6    1000      430.0   0.4       0.4        return True
</code></pre>
<h4><a id="user-content-题目36如何使用random模块生成随机数实现随机乱序和随机抽样" class="anchor" aria-hidden="true" href="#题目36如何使用random模块生成随机数实现随机乱序和随机抽样"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目36：如何使用<code>random</code>模块生成随机数、实现随机乱序和随机抽样？</h4>
<blockquote>
<p><strong>点评</strong>：送人头的题目，因为Python标准库中的常用模块应该是Python开发者都比较熟悉的内容，这个问题回如果答不上来，整个面试基本也就砸锅了。</p>
</blockquote>
<ol>
<li><code>random.random()</code>函数可以生成<code>[0.0, 1.0)</code>之间的随机浮点数。</li>
<li><code>random.uniform(a, b)</code>函数可以生成<code>[a, b]</code>或<code>[b, a]</code>之间的随机浮点数。</li>
<li><code>random.randint(a, b)</code>函数可以生成<code>[a, b]</code>或<code>[b, a]</code>之间的随机整数。</li>
<li><code>random.shuffle(x)</code>函数可以实现对序列<code>x</code>的原地随机乱序。</li>
<li><code>random.choice(seq)</code>函数可以从非空序列中取出一个随机元素。</li>
<li><code>random.choices(population, weights=None, *, cum_weights=None, k=1)</code>函数可以从总体中随机抽取（有放回抽样）出容量为<code>k</code>的样本并返回样本的列表，可以通过参数指定个体的权重，如果没有指定权重，个体被选中的概率均等。</li>
<li><code>random.sample(population, k)</code>函数可以从总体中随机抽取（无放回抽样）出容量为<code>k</code>的样本并返回样本的列表。</li>
</ol>
<blockquote>
<p><strong>扩展</strong>：<code>random</code>模块提供的函数除了生成均匀分布的随机数外，还可以生成其他分布的随机数，例如<code>random.gauss(mu, sigma)</code>函数可以生成高斯分布（正态分布）的随机数；<code>random.paretovariate(alpha)</code>函数会生成帕累托分布的随机数；<code>random.gammavariate(alpha, beta)</code>函数会生成伽马分布的随机数。</p>
</blockquote>
<h4><a id="user-content-题目37解释一下线程池的工作原理" class="anchor" aria-hidden="true" href="#题目37解释一下线程池的工作原理"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目37：解释一下线程池的工作原理。</h4>
<blockquote>
<p><strong>点评</strong>：池化技术就是一种典型空间换时间的策略，我们使用的数据库连接池、线程池等都是池化技术的应用，Python标准库<code>currrent.futures</code>模块的<code>ThreadPoolExecutor</code>就是线程池的实现，如果要弄清楚它的工作原理，可以参考下面的内容。</p>
</blockquote>
<p>线程池是一种用于减少线程本身创建和销毁造成的开销的技术，属于典型的空间换时间操作。如果应用程序需要频繁的将任务派发到线程中执行，线程池就是必选项，因为创建和释放线程涉及到大量的系统底层操作，开销较大，如果能够在应用程序工作期间，将创建和释放线程的操作变成预创建和借还操作，将大大减少底层开销。线程池在应用程序启动后，立即创建一定数量的线程，放入空闲队列中。这些线程最开始都处于阻塞状态，不会消耗CPU资源，但会占用少量的内存空间。当任务到来后，从队列中取出一个空闲线程，把任务派发到这个线程中运行，并将该线程标记为已占用。当线程池中所有的线程都被占用后，可以选择自动创建一定数量的新线程，用于处理更多的任务，也可以选择让任务排队等待直到有空闲的线程可用。在任务执行完毕后，线程并不退出结束，而是继续保持在池中等待下一次的任务。当系统比较空闲时，大部分线程长时间处于闲置状态时，线程池可以自动销毁一部分线程，回收系统资源。基于这种预创建技术，线程池将线程创建和销毁本身所带来的开销分摊到了各个具体的任务上，执行次数越多，每个任务所分担到的线程本身开销则越小。</p>
<p>一般线程池都必须具备下面几个组成部分：</p>
<ol>
<li>线程池管理器：用于创建并管理线程池。</li>
<li>工作线程和线程队列：线程池中实际执行的线程以及保存这些线程的容器。</li>
<li>任务接口：将线程执行的任务抽象出来，形成任务接口，确保线程池与具体的任务无关。</li>
<li>任务队列：线程池中保存等待被执行的任务的容器。</li>
</ol>
<h4><a id="user-content-题目38举例说明什么情况下会出现keyerrortypeerrorvalueerror" class="anchor" aria-hidden="true" href="#题目38举例说明什么情况下会出现keyerrortypeerrorvalueerror"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目38：举例说明什么情况下会出现<code>KeyError</code>、<code>TypeError</code>、<code>ValueError</code>。</h4>
<p>举一个简单的例子，变量<code>a</code>是一个字典，执行<code>int(a['x'])</code>这个操作就有可能引发上述三种类型的异常。如果字典中没有键<code>x</code>，会引发<code>KeyError</code>；如果键<code>x</code>对应的值不是<code>str</code>、<code>float</code>、<code>int</code>、<code>bool</code>以及<code>bytes-like</code>类型，在调用<code>int</code>函数构造<code>int</code>类型的对象时，会引发<code>TypeError</code>；如果<code>a[x]</code>是一个字符串或者字节串，而对应的内容又无法处理成<code>int</code>时，将引发<code>ValueError</code>。</p>
<h4><a id="user-content-题目39说出下面代码的运行结果" class="anchor" aria-hidden="true" href="#题目39说出下面代码的运行结果"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目39：说出下面代码的运行结果。</h4>
<div class="highlight highlight-source-python"><pre><span class="pl-k">def</span> <span class="pl-en">extend_list</span>(<span class="pl-s1">val</span>, <span class="pl-s1">items</span><span class="pl-c1">=</span>[]):
    <span class="pl-s1">items</span>.<span class="pl-en">append</span>(<span class="pl-s1">val</span>)
    <span class="pl-k">return</span> <span class="pl-s1">items</span>

<span class="pl-s1">list1</span> <span class="pl-c1">=</span> <span class="pl-en">extend_list</span>(<span class="pl-c1">10</span>)
<span class="pl-s1">list2</span> <span class="pl-c1">=</span> <span class="pl-en">extend_list</span>(<span class="pl-c1">123</span>, [])
<span class="pl-s1">list3</span> <span class="pl-c1">=</span> <span class="pl-en">extend_list</span>(<span class="pl-s">'a'</span>)
<span class="pl-en">print</span>(<span class="pl-s1">list1</span>)
<span class="pl-en">print</span>(<span class="pl-s1">list2</span>)
<span class="pl-en">print</span>(<span class="pl-s1">list3</span>)</pre></div>
<blockquote>
<p><strong>点评</strong>：Python函数在定义的时候，默认参数<code>items</code>的值就被计算出来了，即<code>[]</code>。因为默认参数<code>items</code>引用了对象<code>[]</code>，每次调用该函数，如果对<code>items</code>引用的列表进行了操作，下次调用时，默认参数还是引用之前的那个列表而不是重新赋值为<code>[]</code>，所以列表中会有之前添加的元素。如果通过传参的方式为<code>items</code>重新赋值，那么<code>items</code>将引用到新的列表对象，而不再引用默认的那个列表对象。这个题在面试中经常被问到，通常不建议使用容器类型的默认参数，像PyLint这样的代码检查工具也会对这种代码提出质疑和警告。</p>
</blockquote>
<pre><code>[10, 'a']
[123]
[10, 'a']
</code></pre>
<h4><a id="user-content-题目40如何读取大文件例如内存只有4g如何读取一个大小为8g的文件" class="anchor" aria-hidden="true" href="#题目40如何读取大文件例如内存只有4g如何读取一个大小为8g的文件"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目40：如何读取大文件，例如内存只有4G，如何读取一个大小为8G的文件？</h4>
<p>很显然4G内存要一次性的加载大小为8G的文件是不现实的，遇到这种情况必须要考虑多次读取和分批次处理。在Python中读取文件可以先通过<code>open</code>函数获取文件对象，在读取文件时，可以通过<code>read</code>方法的<code>size</code>参数指定读取的大小，也可以通过<code>seek</code>方法的<code>offset</code>参数指定读取的位置，这样就可以控制单次读取数据的字节数和总字节数。除此之外，可以使用内置函数<code>iter</code>将文件对象处理成迭代器对象，每次只读取少量的数据进行处理，代码大致写法如下所示。</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s">'...'</span>, <span class="pl-s">'rb'</span>) <span class="pl-k">as</span> <span class="pl-s1">file</span>:
    <span class="pl-k">for</span> <span class="pl-s1">data</span> <span class="pl-c1">in</span> <span class="pl-en">iter</span>(<span class="pl-k">lambda</span>: <span class="pl-s1">file</span>.<span class="pl-en">read</span>(<span class="pl-c1">2097152</span>), <span class="pl-s">b''</span>):
        <span class="pl-k">pass</span></pre></div>
<p>在Linux系统上，可以通过<code>split</code>命令将大文件切割为小片，然后通过读取切割后的小文件对数据进行处理。例如下面的命令将名为<code>filename</code>的大文件切割为大小为512M的多个文件。</p>
<div class="highlight highlight-source-shell"><pre>split -b 512m filename</pre></div>
<p>如果愿意， 也可以将名为<code>filename</code>的文件切割为10个文件，命令如下所示。</p>
<div class="highlight highlight-source-shell"><pre>split -n 10 filename</pre></div>
<blockquote>
<p><strong>扩展</strong>：外部排序跟上述的情况非常类似，由于处理的数据不能一次装入内存，只能放在读写较慢的外存储器（通常是硬盘）上。“<strong>排序-归并算法</strong>”就是一种常用的外部排序策略。在排序阶段，先读入能放在内存中的数据量，将其排序输出到一个临时文件，依此进行，将待排序数据组织为多个有序的临时文件，然后在归并阶段将这些临时文件组合为一个大的有序文件，这个大的有序文件就是排序的结果。</p>
</blockquote>
<h4><a id="user-content-题目41说一下你对python中模块和包的理解" class="anchor" aria-hidden="true" href="#题目41说一下你对python中模块和包的理解"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目41：说一下你对Python中模块和包的理解。</h4>
<p>每个Python文件就是一个模块，而保存这些文件的文件夹就是一个包，但是这个作为Python包的文件夹必须要有一个名为<code>__init__.py</code>的文件，否则无法导入这个包。通常一个文件夹下还可以有子文件夹，这也就意味着一个包下还可以有子包，子包中的<code>__init__.py</code>并不是必须的。模块和包解决了Python中命名冲突的问题，不同的包下可以有同名的模块，不同的模块下可以有同名的变量、函数或类。在Python中可以使用<code>import</code>或<code>from ... import ...</code>来导入包和模块，在导入的时候还可以使用<code>as</code>关键字对包、模块、类、函数、变量等进行别名，从而彻底解决编程中尤其是多人协作团队开发时的命名冲突问题。</p>
<h4><a id="user-content-题目42说一下你知道的python编码规范" class="anchor" aria-hidden="true" href="#题目42说一下你知道的python编码规范"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目42：说一下你知道的Python编码规范。</h4>
<blockquote>
<p><strong>点评</strong>：企业的Python编码规范基本上是参照<a href="https://www.python.org/dev/peps/pep-0008/" rel="nofollow">PEP-8</a>或<a href="https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/" rel="nofollow">谷歌开源项目风格指南</a>来制定的，后者还提到了可以使用Lint工具来检查代码的规范程度，面试的时候遇到这类问题，可以先说下这两个参照标准，然后挑重点说一下Python编码的注意事项。</p>
</blockquote>
<ol>
<li>空格的使用
<ul>
<li>使用空格来表示缩进而不要用制表符（Tab）。</li>
<li>和语法相关的每一层缩进都用4个空格来表示。</li>
<li>每行的字符数不要超过79个字符，如果表达式因太长而占据了多行，除了首行之外的其余各行都应该在正常的缩进宽度上再加上4个空格。</li>
<li>函数和类的定义，代码前后都要用两个空行进行分隔。</li>
<li>在同一个类中，各个方法之间应该用一个空行进行分隔。</li>
<li>二元运算符的左右两侧应该保留一个空格，而且只要一个空格就好。</li>
</ul>
</li>
<li>标识符命名
<ul>
<li>变量、函数和属性应该使用小写字母来拼写，如果有多个单词就使用下划线进行连接。</li>
<li>类中受保护的实例属性，应该以一个下划线开头。</li>
<li>类中私有的实例属性，应该以两个下划线开头。</li>
<li>类和异常的命名，应该每个单词首字母大写。</li>
<li>模块级别的常量，应该采用全大写字母，如果有多个单词就用下划线进行连接。</li>
<li>类的实例方法，应该把第一个参数命名为<code>self</code>以表示对象自身。</li>
<li>类的类方法，应该把第一个参数命名为<code>cls</code>以表示该类自身。</li>
</ul>
</li>
<li>表达式和语句
<ul>
<li>采用内联形式的否定词，而不要把否定词放在整个表达式的前面。例如：<code>if a is not b</code>就比<code>if not a is b</code>更容易让人理解。</li>
<li>不要用检查长度的方式来判断字符串、列表等是否为<code>None</code>或者没有元素，应该用<code>if not x</code>这样的写法来检查它。</li>
<li>就算<code>if</code>分支、<code>for</code>循环、<code>except</code>异常捕获等中只有一行代码，也不要将代码和<code>if</code>、<code>for</code>、<code>except</code>等写在一起，分开写才会让代码更清晰。</li>
<li><code>import</code>语句总是放在文件开头的地方。</li>
<li>引入模块的时候，<code>from math import sqrt</code>比<code>import math</code>更好。</li>
<li>如果有多个<code>import</code>语句，应该将其分为三部分，从上到下分别是Python<strong>标准模块</strong>、<strong>第三方模块</strong>和<strong>自定义模块</strong>，每个部分内部应该按照模块名称的<strong>字母表顺序</strong>来排列。</li>
</ul>
</li>
</ol>
<h4><a id="user-content-题目43运行下面的代码是否会报错如果报错请说明哪里有什么样的错如果不报错请说出代码的执行结果" class="anchor" aria-hidden="true" href="#题目43运行下面的代码是否会报错如果报错请说明哪里有什么样的错如果不报错请说出代码的执行结果"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目43：运行下面的代码是否会报错，如果报错请说明哪里有什么样的错，如果不报错请说出代码的执行结果。</h4>
<div class="highlight highlight-source-python"><pre><span class="pl-k">class</span> <span class="pl-v">A</span>: 
    <span class="pl-k">def</span> <span class="pl-en">__init__</span>(<span class="pl-s1">self</span>, <span class="pl-s1">value</span>):
        <span class="pl-s1">self</span>.<span class="pl-s1">__value</span> <span class="pl-c1">=</span> <span class="pl-s1">value</span>

    <span class="pl-en">@<span class="pl-s1">property</span></span>
    <span class="pl-k">def</span> <span class="pl-en">value</span>(<span class="pl-s1">self</span>):
        <span class="pl-k">return</span> <span class="pl-s1">self</span>.<span class="pl-s1">__value</span>

<span class="pl-s1">obj</span> <span class="pl-c1">=</span> <span class="pl-v">A</span>(<span class="pl-c1">1</span>)
<span class="pl-s1">obj</span>.<span class="pl-s1">__value</span> <span class="pl-c1">=</span> <span class="pl-c1">2</span>
<span class="pl-en">print</span>(<span class="pl-s1">obj</span>.<span class="pl-s1">value</span>)
<span class="pl-en">print</span>(<span class="pl-s1">obj</span>.<span class="pl-s1">__value</span>)</pre></div>
<blockquote>
<p><strong>点评</strong>：这道题有两个考察点，一个考察点是对<code>_</code>和<code>__</code>开头的对象属性访问权限以及<code>@property</code>装饰器的了解，另外一个考察的点是对动态语言的理解，不需要过多的解释。</p>
</blockquote>
<pre><code>1
2
</code></pre>
<blockquote>
<p><strong>扩展</strong>：如果不希望代码运行时动态的给对象添加新属性，可以在定义类时使用<code>__slots__</code>魔法。例如，我们可以在上面的<code>A</code>中添加一行<code>__slots__ = ('__value', )</code>，再次运行上面的代码，将会在原来的第10行处产生<code>AttributeError</code>错误。</p>
</blockquote>
<h4><a id="user-content-题目44对下面给出的字典按值从大到小对键进行排序" class="anchor" aria-hidden="true" href="#题目44对下面给出的字典按值从大到小对键进行排序"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目44：对下面给出的字典按值从大到小对键进行排序。</h4>
<div class="highlight highlight-source-python"><pre><span class="pl-s1">prices</span> <span class="pl-c1">=</span> {
    <span class="pl-s">'AAPL'</span>: <span class="pl-c1">191.88</span>,
    <span class="pl-s">'GOOG'</span>: <span class="pl-c1">1186.96</span>,
    <span class="pl-s">'IBM'</span>: <span class="pl-c1">149.24</span>,
    <span class="pl-s">'ORCL'</span>: <span class="pl-c1">48.44</span>,
    <span class="pl-s">'ACN'</span>: <span class="pl-c1">166.89</span>,
    <span class="pl-s">'FB'</span>: <span class="pl-c1">208.09</span>,
    <span class="pl-s">'SYMC'</span>: <span class="pl-c1">21.29</span>
}</pre></div>
<blockquote>
<p><strong>点评</strong>：<code>sorted</code>函数的高阶用法在面试的时候经常出现，<code>key</code>参数可以传入一个函数名或一个Lambda函数，该函数的返回值代表了在排序时比较元素的依据。</p>
</blockquote>
<div class="highlight highlight-source-python"><pre><span class="pl-en">sorted</span>(<span class="pl-s1">prices</span>, <span class="pl-s1">key</span><span class="pl-c1">=</span><span class="pl-k">lambda</span> <span class="pl-s1">x</span>: <span class="pl-s1">prices</span>[<span class="pl-s1">x</span>], <span class="pl-s1">reverse</span><span class="pl-c1">=</span><span class="pl-c1">True</span>) </pre></div>
<h4><a id="user-content-题目45说一下namedtuple的用法和作用" class="anchor" aria-hidden="true" href="#题目45说一下namedtuple的用法和作用"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目45：说一下<code>namedtuple</code>的用法和作用。</h4>
<blockquote>
<p><strong>点评</strong>：Python标准库的<code>collections</code>模块提供了很多有用的数据结构，这些内容并不是每个开发者都清楚，就比如题目问到的<code>namedtuple</code>，在我参加过的面试中，90%的面试者都不能准确的说出它的作用和应用场景。此外，<code>deque</code>也是一个非常有用但又经常被忽视的类，还有<code>Counter</code>、<code>OrderedDict</code> 、<code>defaultdict</code> 、<code>UserDict</code>等类，大家清楚它们的用法吗？</p>
</blockquote>
<p>在使用面向对象编程语言的时候，定义类是最常见的一件事情，有的时候，我们会用到只有属性没有方法的类，这种类的对象通常只用于组织数据，并不能接收消息，所以我们把这种类称为数据类或者退化的类，就像C语言中的结构体那样。我们并不建议使用这种退化的类，在Python中可以用<code>namedtuple</code>（命名元组）来替代这种类。</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">from</span> <span class="pl-s1">collections</span> <span class="pl-k">import</span> <span class="pl-s1">namedtuple</span>

<span class="pl-v">Card</span> <span class="pl-c1">=</span> <span class="pl-en">namedtuple</span>(<span class="pl-s">'Card'</span>, (<span class="pl-s">'suite'</span>, <span class="pl-s">'face'</span>))
<span class="pl-s1">card1</span> <span class="pl-c1">=</span> <span class="pl-v">Card</span>(<span class="pl-s">'红桃'</span>, <span class="pl-c1">13</span>)
<span class="pl-s1">card2</span> <span class="pl-c1">=</span> <span class="pl-v">Card</span>(<span class="pl-s">'草花'</span>, <span class="pl-c1">5</span>)
<span class="pl-en">print</span>(<span class="pl-s">f'<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">card1</span>.<span class="pl-s1">suite</span><span class="pl-kos">}</span></span><span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">card1</span>.<span class="pl-s1">face</span><span class="pl-kos">}</span></span>'</span>)
<span class="pl-en">print</span>(<span class="pl-s">f'<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">card2</span>.<span class="pl-s1">suite</span><span class="pl-kos">}</span></span><span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">card2</span>.<span class="pl-s1">face</span><span class="pl-kos">}</span></span>'</span>)</pre></div>
<p>命名元组与普通元组一样是不可变容器，一旦将数据存储在<code>namedtuple</code>的顶层属性中，数据就不能再修改了，也就意味着对象上的所有属性都遵循“一次写入，多次读取”的原则。和普通元组不同的是，命名元组中的数据有访问名称，可以通过名称而不是索引来获取保存的数据，不仅在操作上更加简单，代码的可读性也会更好。</p>
<p>命名元组的本质就是一个类，所以它还可以作为父类创建子类。除此之外，命名元组内置了一系列的方法，例如，可以通过<code>_asdict</code>方法将命名元组处理成字典，也可以通过<code>_replace</code>方法创建命名元组对象的浅拷贝。</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">class</span> <span class="pl-v">MyCard</span>(<span class="pl-v">Card</span>):
    
    <span class="pl-k">def</span> <span class="pl-en">show</span>(<span class="pl-s1">self</span>):
        <span class="pl-s1">faces</span> <span class="pl-c1">=</span> [<span class="pl-s">''</span>, <span class="pl-s">'A'</span>, <span class="pl-s">'2'</span>, <span class="pl-s">'3'</span>, <span class="pl-s">'4'</span>, <span class="pl-s">'5'</span>, <span class="pl-s">'6'</span>, <span class="pl-s">'7'</span>, <span class="pl-s">'8'</span>, <span class="pl-s">'9'</span>, <span class="pl-s">'10'</span>, <span class="pl-s">'J'</span>, <span class="pl-s">'Q'</span>, <span class="pl-s">'K'</span>]
        <span class="pl-k">return</span> <span class="pl-s">f'<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">self</span>.<span class="pl-s1">suite</span><span class="pl-kos">}</span></span><span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">faces</span>[<span class="pl-s1">self</span>.<span class="pl-s1">face</span>]<span class="pl-kos">}</span></span>'</span>


<span class="pl-en">print</span>(<span class="pl-v">Card</span>)    <span class="pl-c"># &lt;class '__main__.Card'&gt;</span>
<span class="pl-s1">card3</span> <span class="pl-c1">=</span> <span class="pl-v">MyCard</span>(<span class="pl-s">'方块'</span>, <span class="pl-c1">12</span>)
<span class="pl-en">print</span>(<span class="pl-s1">card3</span>.<span class="pl-en">show</span>())    <span class="pl-c"># 方块Q</span>
<span class="pl-en">print</span>(<span class="pl-en">dict</span>(<span class="pl-s1">card1</span>.<span class="pl-en">_asdict</span>()))    <span class="pl-c"># {'suite': '红桃', 'face': 13}</span>
<span class="pl-en">print</span>(<span class="pl-s1">card2</span>.<span class="pl-en">_replace</span>(<span class="pl-s1">suite</span><span class="pl-c1">=</span><span class="pl-s">'方块'</span>))    <span class="pl-c"># Card(suite='方块', face=5)</span></pre></div>
<p>总而言之，命名元组能更好的组织数据结构，让代码更加清晰和可读，在很多场景下是元组、字典和数据类的替代品。在需要创建占用空间更少的不可变类时，命名元组就是很好的选择。</p>
<h4><a id="user-content-题目46按照题目要求写出对应的函数" class="anchor" aria-hidden="true" href="#题目46按照题目要求写出对应的函数"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目46：按照题目要求写出对应的函数。</h4>
<blockquote>
<p><strong>要求</strong>：写一个函数，传入一个有若干个整数的列表，该列表中某个元素出现的次数超过了50%，返回这个元素。</p>
</blockquote>
<div class="highlight highlight-source-python"><pre><span class="pl-k">def</span> <span class="pl-en">more_than_half</span>(<span class="pl-s1">items</span>):
    <span class="pl-s1">temp</span>, <span class="pl-s1">times</span> <span class="pl-c1">=</span> <span class="pl-c1">None</span>, <span class="pl-c1">0</span>
    <span class="pl-k">for</span> <span class="pl-s1">item</span> <span class="pl-c1">in</span> <span class="pl-s1">items</span>:
        <span class="pl-k">if</span> <span class="pl-s1">times</span> <span class="pl-c1">==</span> <span class="pl-c1">0</span>:
            <span class="pl-s1">temp</span> <span class="pl-c1">=</span> <span class="pl-s1">item</span>
            <span class="pl-s1">times</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span>
        <span class="pl-k">else</span>:
            <span class="pl-k">if</span> <span class="pl-s1">item</span> <span class="pl-c1">==</span> <span class="pl-s1">temp</span>:
                <span class="pl-s1">times</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span>
            <span class="pl-k">else</span>:
                <span class="pl-s1">times</span> <span class="pl-c1">-=</span> <span class="pl-c1">1</span>
    <span class="pl-k">return</span> <span class="pl-s1">temp</span></pre></div>
<blockquote>
<p><strong>点评</strong>：LeetCode上的题目，在Python面试中出现过，利用元素出现次数超过了50%这一特征，出现和<code>temp</code>相同的元素就将计数值加1，出现和<code>temp</code>不同的元素就将计数值减1。如果计数值为<code>0</code>，说明之前出现的元素已经对最终的结果没有影响，用<code>temp</code>记下当前元素并将计数值置为<code>1</code>。最终，出现次数超过了50%的这个元素一定会被赋值给变量<code>temp</code>。</p>
</blockquote>
<h4><a id="user-content-题目47按照题目要求写出对应的函数" class="anchor" aria-hidden="true" href="#题目47按照题目要求写出对应的函数"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目47：按照题目要求写出对应的函数。</h4>
<blockquote>
<p><strong>要求</strong>：写一个函数，传入的参数是一个列表（列表中的元素可能也是一个列表），返回该列表最大的嵌套深度。例如：列表<code>[1, 2, 3]</code>的嵌套深度为<code>1</code>，列表<code>[[1], [2, [3]]]</code>的嵌套深度为<code>3</code>。</p>
</blockquote>
<div class="highlight highlight-source-python"><pre><span class="pl-k">def</span> <span class="pl-en">list_depth</span>(<span class="pl-s1">items</span>):
    <span class="pl-k">if</span> <span class="pl-en">isinstance</span>(<span class="pl-s1">items</span>, <span class="pl-s1">list</span>):
        <span class="pl-s1">max_depth</span> <span class="pl-c1">=</span> <span class="pl-c1">1</span>
        <span class="pl-k">for</span> <span class="pl-s1">item</span> <span class="pl-c1">in</span> <span class="pl-s1">items</span>:
            <span class="pl-s1">max_depth</span> <span class="pl-c1">=</span> <span class="pl-en">max</span>(<span class="pl-en">list_depth</span>(<span class="pl-s1">item</span>) <span class="pl-c1">+</span> <span class="pl-c1">1</span>, <span class="pl-s1">max_depth</span>)
        <span class="pl-k">return</span> <span class="pl-s1">max_depth</span>
    <span class="pl-k">return</span> <span class="pl-c1">0</span></pre></div>
<blockquote>
<p><strong>点评</strong>：看到题目应该能够比较自然的想到使用递归的方式检查列表中的每个元素。</p>
</blockquote>
<h4><a id="user-content-题目48按照题目要求写出对应的装饰器" class="anchor" aria-hidden="true" href="#题目48按照题目要求写出对应的装饰器"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目48：按照题目要求写出对应的装饰器。</h4>
<blockquote>
<p><strong>要求</strong>：有一个通过网络获取数据的函数（可能会因为网络原因出现异常），写一个装饰器让这个函数在出现指定异常时可以重试指定的次数，并在每次重试之前随机延迟一段时间，最长延迟时间可以通过参数进行控制。</p>
</blockquote>
<p>方法一：</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">from</span> <span class="pl-s1">functools</span> <span class="pl-k">import</span> <span class="pl-s1">wraps</span>
<span class="pl-k">from</span> <span class="pl-s1">random</span> <span class="pl-k">import</span> <span class="pl-s1">random</span>
<span class="pl-k">from</span> <span class="pl-s1">time</span> <span class="pl-k">import</span> <span class="pl-s1">sleep</span>


<span class="pl-k">def</span> <span class="pl-en">retry</span>(*, <span class="pl-s1">retry_times</span><span class="pl-c1">=</span><span class="pl-c1">3</span>, <span class="pl-s1">max_wait_secs</span><span class="pl-c1">=</span><span class="pl-c1">5</span>, <span class="pl-s1">errors</span><span class="pl-c1">=</span>(<span class="pl-v">Exception</span>, )):

    <span class="pl-k">def</span> <span class="pl-en">decorate</span>(<span class="pl-s1">func</span>):

        <span class="pl-en">@<span class="pl-s1">wraps</span>(<span class="pl-s1">func</span>)</span>
        <span class="pl-k">def</span> <span class="pl-en">wrapper</span>(<span class="pl-c1">*</span><span class="pl-s1">args</span>, <span class="pl-c1">**</span><span class="pl-s1">kwargs</span>):
            <span class="pl-k">for</span> <span class="pl-s1">_</span> <span class="pl-c1">in</span> <span class="pl-en">range</span>(<span class="pl-s1">retry_times</span>):
                <span class="pl-k">try</span>:
                    <span class="pl-k">return</span> <span class="pl-en">func</span>(<span class="pl-c1">*</span><span class="pl-s1">args</span>, <span class="pl-c1">**</span><span class="pl-s1">kwargs</span>)
                <span class="pl-k">except</span> <span class="pl-s1">errors</span>:
                    <span class="pl-en">sleep</span>(<span class="pl-en">random</span>() <span class="pl-c1">*</span> <span class="pl-s1">max_wait_secs</span>)
            <span class="pl-k">return</span> <span class="pl-c1">None</span>

        <span class="pl-k">return</span> <span class="pl-s1">wrapper</span>

    <span class="pl-k">return</span> <span class="pl-s1">decorate</span></pre></div>
<p>方法二：</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">from</span> <span class="pl-s1">functools</span> <span class="pl-k">import</span> <span class="pl-s1">wraps</span>
<span class="pl-k">from</span> <span class="pl-s1">random</span> <span class="pl-k">import</span> <span class="pl-s1">random</span>
<span class="pl-k">from</span> <span class="pl-s1">time</span> <span class="pl-k">import</span> <span class="pl-s1">sleep</span>


<span class="pl-k">class</span> <span class="pl-v">Retry</span>(<span class="pl-s1">object</span>):

    <span class="pl-k">def</span> <span class="pl-en">__init__</span>(<span class="pl-s1">self</span>, *, <span class="pl-s1">retry_times</span><span class="pl-c1">=</span><span class="pl-c1">3</span>, <span class="pl-s1">max_wait_secs</span><span class="pl-c1">=</span><span class="pl-c1">5</span>, <span class="pl-s1">errors</span><span class="pl-c1">=</span>(<span class="pl-v">Exception</span>, )):
        <span class="pl-s1">self</span>.<span class="pl-s1">retry_times</span> <span class="pl-c1">=</span> <span class="pl-s1">retry_times</span>
        <span class="pl-s1">self</span>.<span class="pl-s1">max_wait_secs</span> <span class="pl-c1">=</span> <span class="pl-s1">max_wait_secs</span>
        <span class="pl-s1">self</span>.<span class="pl-s1">errors</span> <span class="pl-c1">=</span> <span class="pl-s1">errors</span>

    <span class="pl-k">def</span> <span class="pl-en">__call__</span>(<span class="pl-s1">self</span>, <span class="pl-s1">func</span>):

        <span class="pl-en">@<span class="pl-s1">wraps</span>(<span class="pl-s1">func</span>)</span>
        <span class="pl-k">def</span> <span class="pl-en">wrapper</span>(<span class="pl-c1">*</span><span class="pl-s1">args</span>, <span class="pl-c1">**</span><span class="pl-s1">kwargs</span>):
            <span class="pl-k">for</span> <span class="pl-s1">_</span> <span class="pl-c1">in</span> <span class="pl-en">range</span>(<span class="pl-s1">self</span>.<span class="pl-s1">retry_times</span>):
                <span class="pl-k">try</span>:
                    <span class="pl-k">return</span> <span class="pl-en">func</span>(<span class="pl-c1">*</span><span class="pl-s1">args</span>, <span class="pl-c1">**</span><span class="pl-s1">kwargs</span>)
                <span class="pl-k">except</span> <span class="pl-s1">self</span>.<span class="pl-s1">errors</span>:
                    <span class="pl-en">sleep</span>(<span class="pl-en">random</span>() <span class="pl-c1">*</span> <span class="pl-s1">self</span>.<span class="pl-s1">max_wait_secs</span>)
            <span class="pl-k">return</span> <span class="pl-c1">None</span>

        <span class="pl-k">return</span> <span class="pl-s1">wrapper</span></pre></div>
<blockquote>
<p><strong>点评</strong>：我们不止一次强调过，装饰器几乎是Python面试必问内容，这个题目比之前的题目稍微复杂一些，它需要的是一个参数化的装饰器。</p>
</blockquote>
<h4><a id="user-content-题目49写一个函数实现字符串反转尽可能写出你知道的所有方法" class="anchor" aria-hidden="true" href="#题目49写一个函数实现字符串反转尽可能写出你知道的所有方法"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目49：写一个函数实现字符串反转，尽可能写出你知道的所有方法。</h4>
<blockquote>
<p><strong>点评</strong>：烂大街的题目，基本上算是送人头的题目。</p>
</blockquote>
<p><strong>方法一</strong>：反向切片</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">def</span> <span class="pl-en">reverse_string</span>(<span class="pl-s1">content</span>):
    <span class="pl-k">return</span> <span class="pl-s1">content</span>[::<span class="pl-c1">-</span><span class="pl-c1">1</span>]</pre></div>
<p><strong>方法二</strong>：反转拼接</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">def</span> <span class="pl-en">reverse_string</span>(<span class="pl-s1">content</span>):
    <span class="pl-k">return</span> <span class="pl-s">''</span>.<span class="pl-en">join</span>(<span class="pl-en">reversed</span>(<span class="pl-s1">content</span>))</pre></div>
<p><strong>方法三</strong>：递归调用</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">def</span> <span class="pl-en">reverse_string</span>(<span class="pl-s1">content</span>):
    <span class="pl-k">if</span> <span class="pl-en">len</span>(<span class="pl-s1">content</span>) <span class="pl-c1">&lt;=</span> <span class="pl-c1">1</span>:
        <span class="pl-k">return</span> <span class="pl-s1">content</span>
    <span class="pl-k">return</span> <span class="pl-en">reverse_string</span>(<span class="pl-s1">content</span>[<span class="pl-c1">1</span>:]) <span class="pl-c1">+</span> <span class="pl-s1">content</span>[<span class="pl-c1">0</span>]</pre></div>
<p><strong>方法四</strong>：双端队列</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">from</span> <span class="pl-s1">collections</span> <span class="pl-k">import</span> <span class="pl-s1">deque</span>

<span class="pl-k">def</span> <span class="pl-en">reverse_string</span>(<span class="pl-s1">content</span>):
    <span class="pl-s1">q</span> <span class="pl-c1">=</span> <span class="pl-en">deque</span>()
    <span class="pl-s1">q</span>.<span class="pl-en">extendleft</span>(<span class="pl-s1">content</span>)
    <span class="pl-k">return</span> <span class="pl-s">''</span>.<span class="pl-en">join</span>(<span class="pl-s1">q</span>)</pre></div>
<p><strong>方法五</strong>：反向组装</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">from</span> <span class="pl-s1">io</span> <span class="pl-k">import</span> <span class="pl-v">StringIO</span>

<span class="pl-k">def</span> <span class="pl-en">reverse_string</span>(<span class="pl-s1">content</span>):
    <span class="pl-s1">buffer</span> <span class="pl-c1">=</span> <span class="pl-v">StringIO</span>()
    <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-en">range</span>(<span class="pl-en">len</span>(<span class="pl-s1">content</span>) <span class="pl-c1">-</span> <span class="pl-c1">1</span>, <span class="pl-c1">-</span><span class="pl-c1">1</span>, <span class="pl-c1">-</span><span class="pl-c1">1</span>):
        <span class="pl-s1">buffer</span>.<span class="pl-en">write</span>(<span class="pl-s1">content</span>[<span class="pl-s1">i</span>])
    <span class="pl-k">return</span> <span class="pl-s1">buffer</span>.<span class="pl-en">getvalue</span>()</pre></div>
<p><strong>方法六</strong>：反转拼接</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">def</span> <span class="pl-en">reverse_string</span>(<span class="pl-s1">content</span>):
    <span class="pl-k">return</span> <span class="pl-s">''</span>.<span class="pl-en">join</span>([<span class="pl-s1">content</span>[<span class="pl-s1">i</span>] <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-en">range</span>(<span class="pl-en">len</span>(<span class="pl-s1">content</span>) <span class="pl-c1">-</span> <span class="pl-c1">1</span>, <span class="pl-c1">-</span><span class="pl-c1">1</span>, <span class="pl-c1">-</span><span class="pl-c1">1</span>)])</pre></div>
<p><strong>方法七</strong>：半截交换</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">def</span> <span class="pl-en">reverse_string</span>(<span class="pl-s1">content</span>):
    <span class="pl-s1">length</span>, <span class="pl-s1">content</span><span class="pl-c1">=</span> <span class="pl-en">len</span>(<span class="pl-s1">content</span>), <span class="pl-en">list</span>(<span class="pl-s1">content</span>)
    <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-en">range</span>(<span class="pl-s1">length</span> <span class="pl-c1">//</span> <span class="pl-c1">2</span>):
        <span class="pl-s1">content</span>[<span class="pl-s1">i</span>], <span class="pl-s1">content</span>[<span class="pl-s1">length</span> <span class="pl-c1">-</span> <span class="pl-c1">1</span> <span class="pl-c1">-</span> <span class="pl-s1">i</span>] <span class="pl-c1">=</span> <span class="pl-s1">content</span>[<span class="pl-s1">length</span> <span class="pl-c1">-</span> <span class="pl-c1">1</span> <span class="pl-c1">-</span> <span class="pl-s1">i</span>], <span class="pl-s1">content</span>[<span class="pl-s1">i</span>]
    <span class="pl-k">return</span> <span class="pl-s">''</span>.<span class="pl-en">join</span>(<span class="pl-s1">content</span>)</pre></div>
<p><strong>方法八</strong>：对位交换</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">def</span> <span class="pl-en">reverse_string</span>(<span class="pl-s1">content</span>):
    <span class="pl-s1">length</span>, <span class="pl-s1">content</span><span class="pl-c1">=</span> <span class="pl-en">len</span>(<span class="pl-s1">content</span>), <span class="pl-en">list</span>(<span class="pl-s1">content</span>)
    <span class="pl-k">for</span> <span class="pl-s1">i</span>, <span class="pl-s1">j</span> <span class="pl-c1">in</span> <span class="pl-en">zip</span>(<span class="pl-en">range</span>(<span class="pl-s1">length</span> <span class="pl-c1">//</span> <span class="pl-c1">2</span>), <span class="pl-en">range</span>(<span class="pl-s1">length</span> <span class="pl-c1">-</span> <span class="pl-c1">1</span>, <span class="pl-s1">length</span> <span class="pl-c1">//</span> <span class="pl-c1">2</span> <span class="pl-c1">-</span> <span class="pl-c1">1</span>, <span class="pl-c1">-</span><span class="pl-c1">1</span>)):
        <span class="pl-s1">content</span>[<span class="pl-s1">i</span>], <span class="pl-s1">content</span>[<span class="pl-s1">j</span>] <span class="pl-c1">=</span> <span class="pl-s1">content</span>[<span class="pl-s1">j</span>], <span class="pl-s1">content</span>[<span class="pl-s1">i</span>]
    <span class="pl-k">return</span> <span class="pl-s">''</span>.<span class="pl-en">join</span>(<span class="pl-s1">content</span>)</pre></div>
<blockquote>
<p><strong>扩展</strong>：这些方法其实都是大同小异的，面试的时候能够给出几种有代表性的就足够了。给大家留一个思考题，上面这些方法，哪些做法的性能较好呢？我们之前提到过剖析代码性能的方法，大家可以用这些方法来检验下你给出的答案是否正确。</p>
</blockquote>
<h4><a id="user-content-题目50按照题目要求写出对应的函数" class="anchor" aria-hidden="true" href="#题目50按照题目要求写出对应的函数"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>题目50：按照题目要求写出对应的函数。</h4>
<blockquote>
<p><strong>要求</strong>：列表中有<code>1000000</code>个元素，取值范围是<code>[1000, 10000)</code>，设计一个函数找出列表中的重复元素。</p>
</blockquote>
<div class="highlight highlight-source-python"><pre><span class="pl-k">def</span> <span class="pl-en">find_dup</span>(<span class="pl-s1">items</span>: <span class="pl-s1">list</span>):
    <span class="pl-s1">dups</span> <span class="pl-c1">=</span> [<span class="pl-c1">0</span>] <span class="pl-c1">*</span> <span class="pl-c1">9000</span>
    <span class="pl-k">for</span> <span class="pl-s1">item</span> <span class="pl-c1">in</span> <span class="pl-s1">items</span>:
        <span class="pl-s1">dups</span>[<span class="pl-s1">item</span> <span class="pl-c1">-</span> <span class="pl-c1">1000</span>] <span class="pl-c1">+=</span> <span class="pl-c1">1</span>
    <span class="pl-k">for</span> <span class="pl-s1">idx</span>, <span class="pl-s1">val</span> <span class="pl-c1">in</span> <span class="pl-en">enumerate</span>(<span class="pl-s1">dups</span>):
        <span class="pl-k">if</span> <span class="pl-s1">val</span> <span class="pl-c1">&gt;</span> <span class="pl-c1">1</span>:
            <span class="pl-k">yield</span> <span class="pl-s1">idx</span> <span class="pl-c1">+</span> <span class="pl-c1">1000</span></pre></div>
<blockquote>
<p><strong>点评</strong>：这道题的解法和<a href="https://www.runoob.com/w3cnote/counting-sort.html" rel="nofollow">计数排序</a>的原理一致，虽然元素的数量非常多，但是取值范围<code>[1000, 10000)</code>并不是很大，只有9000个可能的取值，所以可以用一个能够保存9000个元素的<code>dups</code>列表来记录每个元素出现的次数，<code>dups</code>列表所有元素的初始值都是<code>0</code>，通过对<code>items</code>列表中元素的遍历，当出现某个元素时，将<code>dups</code>列表对应位置的值加1，最后<code>dups</code>列表中值大于1的元素对应的就是<code>items</code>列表中重复出现过的元素。</p>
</blockquote>
<p>更多的面试题，请移步到我的知乎专栏<a href="https://zhuanlan.zhihu.com/c_1228980105135497216" rel="nofollow">《Python面试宝典》</a>。</p>
</article>
  </div>

    </div>

  


  <details class="details-reset details-overlay details-overlay-dark" id="jumpto-line-details-dialog">
    <summary data-hotkey="l" aria-label="Jump to line"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast linejump" aria-label="Jump to line">
      <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-jump-to-line-form Box-body d-flex" action="" accept-charset="UTF-8" method="get">
        <input class="form-control flex-auto mr-3 linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
        <button type="submit" class="btn" data-close-dialog>Go</button>
</form>    </details-dialog>
  </details>




  </div>
</div>

    </main>
  </div>
  

  </div>

        
<div class="footer container-xl width-full p-responsive" role="contentinfo">
  <div class="position-relative d-flex flex-row-reverse flex-lg-row flex-wrap flex-lg-nowrap flex-justify-center flex-lg-justify-between pt-6 pb-2 mt-6 f6 text-gray border-top border-gray-light ">
    <ul class="list-style-none d-flex flex-wrap col-12 col-lg-5 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0">
      <li class="mr-3 mr-lg-0">&copy; 2020 GitHub, Inc.</li>
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to terms, text:terms" href="https://github.com/site/terms">Terms</a></li>
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to privacy, text:privacy" href="https://github.com/site/privacy">Privacy</a></li>
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to security, text:security" href="https://github.com/security">Security</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://githubstatus.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a data-ga-click="Footer, go to help, text:help" href="https://help.github.com">Help</a></li>

    </ul>

    <a aria-label="Homepage" title="GitHub" class="footer-octicon d-none d-lg-block mx-lg-4" href="https://github.com">
      <svg height="24" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>
</a>
   <ul class="list-style-none d-flex flex-wrap col-12 col-lg-5 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0">
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to contact, text:contact" href="https://github.com/contact">Contact GitHub</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://github.com/pricing" data-ga-click="Footer, go to Pricing, text:Pricing">Pricing</a></li>
      <li class="mr-3 mr-lg-0"><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3 mr-lg-0"><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://github.blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>
    </ul>
  </div>
  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 text-gray-light"></span>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path></svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg class="octicon octicon-x" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path></svg>
    </button>
    You can’t perform that action at this time.
  </div>


    <script crossorigin="anonymous" async="async" integrity="sha512-bn/3rKJzBl2H64K38R8KaVcT26vKK7BJQC59lwYc+9fjlHzmy0fwh+hzBtsgTdhIi13dxjzNKWhdSN8WTM9qUw==" type="application/javascript" id="js-conditional-compat" data-src="https://github.githubassets.com/assets/compat-bootstrap-6e7ff7ac.js"></script>
    <script crossorigin="anonymous" integrity="sha512-pUTnKCTI5AwDjCcoRca4GvqbIie8gPdp9KbzQU/NeHBalvs7YdiDc26EOOfICdPj0MmXFBzHkLn3bUyO7uPLeA==" type="application/javascript" src="https://github.githubassets.com/assets/environment-bootstrap-a544e728.js"></script>
    <script crossorigin="anonymous" async="async" integrity="sha512-Ncm8EEN+jdJqci1dTZ4/BCY+ueKmNOQiPQj6rcX2/6qKIdf1hJqQZnJJEjoFj18nEkD/hus03JOBTjmHB3jNMg==" type="application/javascript" src="https://github.githubassets.com/assets/vendor-35c9bc10.js"></script>
    <script crossorigin="anonymous" async="async" integrity="sha512-qB1YyRs4eXwCnazVr5D+s0S4LdcYRSpsVFvbzgktVac3EDP1vRdyOzpWjR742FlcCbPzWTc0YwccFd4dgJpHtg==" type="application/javascript" src="https://github.githubassets.com/assets/frameworks-a81d58c9.js"></script>
    
    <script crossorigin="anonymous" async="async" integrity="sha512-VwoDCPAbXzebH+BMCNCDqM8Ig+of50/dSndSx2DSoI4MbA73+v6w5Q5+141OuY5LeKjYBXkiBiBLL65hOO1h3A==" type="application/javascript" src="https://github.githubassets.com/assets/github-bootstrap-570a0308.js"></script>
    
      <script crossorigin="anonymous" async="async" integrity="sha512-TjmDUfspgN28WRWfc01tOL0BFS8pI/TAi8TQ665TcA3jG1C3QgfFu0YKa32Z03rlEL8dukbsy+amwBzgGyjESQ==" type="application/javascript" data-module-id="./Sortable.js" data-src="https://github.githubassets.com/assets/Sortable-4e398351.js"></script>
      <script crossorigin="anonymous" async="async" integrity="sha512-4GcSWGoe36+BoWho4gtJcByZe8j43w+lt2/PDe3rmBxRVSgD29YipDwuIywe8fvOd2b2CszBqaPGxSznUtE3Xg==" type="application/javascript" data-module-id="./drag-drop.js" data-src="https://github.githubassets.com/assets/drag-drop-e0671258.js"></script>
      <script crossorigin="anonymous" async="async" integrity="sha512-MttsTK6LRLl4AiQlvZ8MfNsDe0brgs9ubvDV/Ck6sVM+MnjEn+6tfF4hS8ENrXG1v+lBHFWmAS5j43gum0xsXw==" type="application/javascript" data-module-id="./gist-vendor.js" data-src="https://github.githubassets.com/assets/gist-vendor-32db6c4c.js"></script>
      <script crossorigin="anonymous" async="async" integrity="sha512-iLuC2weaJqL9mYAud2WDWjhd8cJe8dXVxw2KhCH2Rnj6WJvTzlZRmvTtL09wNWX6nRze/TDaQ7gq7BFLchaDYg==" type="application/javascript" data-module-id="./image-crop-element-loader.js" data-src="https://github.githubassets.com/assets/image-crop-element-loader-88bb82db.js"></script>
      <script crossorigin="anonymous" async="async" integrity="sha512-SzrmrFC6Li3booxqs0mRixus2NKXsmDzy81YKIdwyd4llzBUojVrUd87DAv4Gm3LlROU45cG5C6/noBz+/exMA==" type="application/javascript" data-module-id="./profile-pins-element.js" data-src="https://github.githubassets.com/assets/profile-pins-element-4b3ae6ac.js"></script>
      <script crossorigin="anonymous" async="async" integrity="sha512-qECv/jhsvLFN77eGNu0cjMR2+zvAlLyhQVTnmayJc5OLZoxMLjQZxZW1hK/dhcYro6Wec/aiF21HYf2N5OilYQ==" type="application/javascript" data-module-id="./randomColor.js" data-src="https://github.githubassets.com/assets/randomColor-a840affe.js"></script>
      <script crossorigin="anonymous" async="async" integrity="sha512-45AwxR1TB7Z8BL0dnYOrINtveNF4Du3OaUdubEdbdfYrswXjalLxzIFenU8e6CVEoL6pHMHLLzXRPFokwAWmsw==" type="application/javascript" data-module-id="./tweetsodium.js" data-src="https://github.githubassets.com/assets/tweetsodium-e39030c5.js"></script>
      <script crossorigin="anonymous" async="async" integrity="sha512-NM1W1VNDC9MWIx8L8lAk3+8egdBlekVtKpnfE7a4+8mG/3ESwpbgBtqL8m0n61t3lCBxQ49hXA66OpEfm196XA==" type="application/javascript" data-module-id="./user-status-submit.js" data-src="https://github.githubassets.com/assets/user-status-submit-34cd56d5.js"></script>
    
    
  <div class="js-stale-session-flash flash flash-warn flash-banner" hidden
    >
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path></svg>
    <span class="js-stale-session-flash-signed-in" hidden>You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="js-stale-session-flash-signed-out" hidden>You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <template id="site-details-dialog">
  <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark hx_rsm" open>
    <summary role="button" aria-label="Close dialog"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast hx_rsm-dialog hx_rsm-modal">
      <button class="Box-btn-octicon m-0 btn-octicon position-absolute right-0 top-0" type="button" aria-label="Close dialog" data-close-dialog>
        <svg class="octicon octicon-x" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path></svg>
      </button>
      <div class="octocat-spinner my-6 js-details-dialog-spinner"></div>
    </details-dialog>
  </details>
</template>

  <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box box-shadow-large" style="width:360px;">
  </div>
</div>


  </body>
</html>

