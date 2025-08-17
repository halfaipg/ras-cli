<!doctype html>
<html class="">
	<head>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no" />
		<meta name="description" content="We’re on a journey to advance and democratize artificial intelligence through open source and open science." />
		<meta property="fb:app_id" content="1321688464574422" />
		<meta name="twitter:card" content="summary_large_image" />
		<meta name="twitter:site" content="@huggingface" />
		<meta name="twitter:image" content="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/Qwen/Qwen3-Coder-30B-A3B-Instruct.png" />
		<meta property="og:title" content="qwen3coder_tool_parser.py · Qwen/Qwen3-Coder-30B-A3B-Instruct at main" />
		<meta property="og:type" content="website" />
		<meta property="og:url" content="https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct/blob/main/qwen3coder_tool_parser.py" />
		<meta property="og:image" content="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/Qwen/Qwen3-Coder-30B-A3B-Instruct.png" />

		<link rel="stylesheet" href="/front/build/kube-9d7efdc/style.css" />

		<link rel="preconnect" href="https://fonts.gstatic.com" />
		<link
			href="https://fonts.googleapis.com/css2?family=Source+Sans+Pro:ital,wght@0,200;0,300;0,400;0,600;0,700;1,200;1,300;1,400;1,600;1,700&display=swap"
			rel="stylesheet"
		/>
		<link
			href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600;700&display=swap"
			rel="stylesheet"
		/>

		<link
			rel="preload"
			href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.12.0/katex.min.css"
			as="style"
			onload="this.onload=null;this.rel='stylesheet'"
		/>
		<noscript>
			<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.12.0/katex.min.css" />
		</noscript>

		<script>const guestTheme = document.cookie.match(/theme=(\w+)/)?.[1]; document.documentElement.classList.toggle('dark', guestTheme === 'dark' || ( (!guestTheme || guestTheme === 'system') && window.matchMedia('(prefers-color-scheme: dark)').matches));</script>
<link rel="canonical" href="https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct/blob/main/qwen3coder_tool_parser.py">  <!-- HEAD_svelte-1oal594_START --><style>.blob-line-num::before {
			content: attr(data-line-num);
		}
	</style><!-- HEAD_svelte-1oal594_END -->

		<title>qwen3coder_tool_parser.py · Qwen/Qwen3-Coder-30B-A3B-Instruct at main</title>

		<script
			defer
			data-domain="huggingface.co"
			event-loggedIn="false"
			src="/js/script.pageview-props.js"
		></script>
		<script>
			window.plausible =
				window.plausible ||
				function () {
					(window.plausible.q = window.plausible.q || []).push(arguments);
				};
		</script>
		<script>
			window.hubConfig = {"features":{"signupDisabled":false},"sshGitUrl":"git@hf.co","moonHttpUrl":"https:\/\/huggingface.co","captchaApiKey":"bd5f2066-93dc-4bdd-a64b-a24646ca3859","captchaDisabledOnSignup":true,"datasetViewerPublicUrl":"https:\/\/datasets-server.huggingface.co","stripePublicKey":"pk_live_x2tdjFXBCvXo2FFmMybezpeM00J6gPCAAc","environment":"production","userAgent":"HuggingFace (production)","spacesIframeDomain":"hf.space","spacesApiUrl":"https:\/\/api.hf.space","docSearchKey":"ece5e02e57300e17d152c08056145326e90c4bff3dd07d7d1ae40cf1c8d39cb6","logoDev":{"apiUrl":"https:\/\/img.logo.dev\/","apiKey":"pk_UHS2HZOeRnaSOdDp7jbd5w"}};
		</script>
		<script type="text/javascript" src="https://de5282c3ca0c.edge.sdk.awswaf.com/de5282c3ca0c/526cf06acb0d/challenge.js" defer></script> 
	</head>
	<body class="flex flex-col min-h-dvh bg-white dark:bg-gray-950 text-black ViewerBlobPage">
		<div class="flex min-h-dvh flex-col"><div class="SVELTE_HYDRATER contents" data-target="SystemThemeMonitor" data-props="{&quot;isLoggedIn&quot;:false}"></div>

	<div class="SVELTE_HYDRATER contents" data-target="MainHeader" data-props="{&quot;classNames&quot;:&quot;&quot;,&quot;isWide&quot;:false,&quot;isZh&quot;:false,&quot;isPro&quot;:false}"><header class="border-b border-gray-100 "><div class="w-full px-4 container flex h-16 items-center"><div class="flex flex-1 items-center"><a class="mr-5 flex flex-none items-center lg:mr-6" href="/"><img alt="Hugging Face's logo" class="w-7 md:mr-2" src="/front/assets/huggingface_logo-noborder.svg">
				<span class="hidden whitespace-nowrap text-lg font-bold md:block">Hugging Face</span></a>
			<div class="relative flex-1 lg:max-w-sm mr-2 sm:mr-4 md:mr-3 xl:mr-6"><input autocomplete="off" class="w-full dark:bg-gray-950 pl-8 form-input-alt h-9 pr-3 focus:shadow-xl " name="" placeholder="Search models, datasets, users..."   spellcheck="false" type="text" value="">
	<svg class="absolute left-2.5 text-gray-400 top-1/2 transform -translate-y-1/2" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M30 28.59L22.45 21A11 11 0 1 0 21 22.45L28.59 30zM5 14a9 9 0 1 1 9 9a9 9 0 0 1-9-9z" fill="currentColor"></path></svg>
	</div>
			<div class="flex flex-none items-center justify-center p-0.5 place-self-stretch lg:hidden"><button class="relative z-40 flex h-6 w-8 items-center justify-center" type="button"><svg width="1em" height="1em" viewBox="0 0 10 10" class="text-xl" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" preserveAspectRatio="xMidYMid meet" fill="currentColor"><path fill-rule="evenodd" clip-rule="evenodd" d="M1.65039 2.9999C1.65039 2.8066 1.80709 2.6499 2.00039 2.6499H8.00039C8.19369 2.6499 8.35039 2.8066 8.35039 2.9999C8.35039 3.1932 8.19369 3.3499 8.00039 3.3499H2.00039C1.80709 3.3499 1.65039 3.1932 1.65039 2.9999ZM1.65039 4.9999C1.65039 4.8066 1.80709 4.6499 2.00039 4.6499H8.00039C8.19369 4.6499 8.35039 4.8066 8.35039 4.9999C8.35039 5.1932 8.19369 5.3499 8.00039 5.3499H2.00039C1.80709 5.3499 1.65039 5.1932 1.65039 4.9999ZM2.00039 6.6499C1.80709 6.6499 1.65039 6.8066 1.65039 6.9999C1.65039 7.1932 1.80709 7.3499 2.00039 7.3499H8.00039C8.19369 7.3499 8.35039 7.1932 8.35039 6.9999C8.35039 6.8066 8.19369 6.6499 8.00039 6.6499H2.00039Z"></path></svg>
		</button>

	</div></div>
		<nav aria-label="Main" class="ml-auto hidden lg:block"><ul class="flex items-center gap-x-1 2xl:gap-x-2"><li class="hover:text-indigo-700"><a class="group flex items-center px-2 py-0.5 dark:text-gray-300 dark:hover:text-gray-100" href="/models"><svg class="mr-1.5 text-gray-400 group-hover:text-indigo-500" style="" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-quaternary" d="M20.23 7.24L12 12L3.77 7.24a1.98 1.98 0 0 1 .7-.71L11 2.76c.62-.35 1.38-.35 2 0l6.53 3.77c.29.173.531.418.7.71z" opacity=".25" fill="currentColor"></path><path class="uim-tertiary" d="M12 12v9.5a2.09 2.09 0 0 1-.91-.21L4.5 17.48a2.003 2.003 0 0 1-1-1.73v-7.5a2.06 2.06 0 0 1 .27-1.01L12 12z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M20.5 8.25v7.5a2.003 2.003 0 0 1-1 1.73l-6.62 3.82c-.275.13-.576.198-.88.2V12l8.23-4.76c.175.308.268.656.27 1.01z" fill="currentColor"></path></svg>
						Models</a>
				</li><li class="hover:text-red-700"><a class="group flex items-center px-2 py-0.5 dark:text-gray-300 dark:hover:text-gray-100" href="/datasets"><svg class="mr-1.5 text-gray-400 group-hover:text-red-500" style="" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 25 25"><ellipse cx="12.5" cy="5" fill="currentColor" fill-opacity="0.25" rx="7.5" ry="2"></ellipse><path d="M12.5 15C16.6421 15 20 14.1046 20 13V20C20 21.1046 16.6421 22 12.5 22C8.35786 22 5 21.1046 5 20V13C5 14.1046 8.35786 15 12.5 15Z" fill="currentColor" opacity="0.5"></path><path d="M12.5 7C16.6421 7 20 6.10457 20 5V11.5C20 12.6046 16.6421 13.5 12.5 13.5C8.35786 13.5 5 12.6046 5 11.5V5C5 6.10457 8.35786 7 12.5 7Z" fill="currentColor" opacity="0.5"></path><path d="M5.23628 12C5.08204 12.1598 5 12.8273 5 13C5 14.1046 8.35786 15 12.5 15C16.6421 15 20 14.1046 20 13C20 12.8273 19.918 12.1598 19.7637 12C18.9311 12.8626 15.9947 13.5 12.5 13.5C9.0053 13.5 6.06886 12.8626 5.23628 12Z" fill="currentColor"></path></svg>
						Datasets</a>
				</li><li class="hover:text-blue-700"><a class="group flex items-center px-2 py-0.5 dark:text-gray-300 dark:hover:text-gray-100" href="/spaces"><svg class="mr-1.5 text-gray-400 group-hover:text-blue-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" viewBox="0 0 25 25"><path opacity=".5" d="M6.016 14.674v4.31h4.31v-4.31h-4.31ZM14.674 14.674v4.31h4.31v-4.31h-4.31ZM6.016 6.016v4.31h4.31v-4.31h-4.31Z" fill="currentColor"></path><path opacity=".75" fill-rule="evenodd" clip-rule="evenodd" d="M3 4.914C3 3.857 3.857 3 4.914 3h6.514c.884 0 1.628.6 1.848 1.414a5.171 5.171 0 0 1 7.31 7.31c.815.22 1.414.964 1.414 1.848v6.514A1.914 1.914 0 0 1 20.086 22H4.914A1.914 1.914 0 0 1 3 20.086V4.914Zm3.016 1.102v4.31h4.31v-4.31h-4.31Zm0 12.968v-4.31h4.31v4.31h-4.31Zm8.658 0v-4.31h4.31v4.31h-4.31Zm0-10.813a2.155 2.155 0 1 1 4.31 0 2.155 2.155 0 0 1-4.31 0Z" fill="currentColor"></path><path opacity=".25" d="M16.829 6.016a2.155 2.155 0 1 0 0 4.31 2.155 2.155 0 0 0 0-4.31Z" fill="currentColor"></path></svg>
						Spaces</a>
				</li><li class="max-xl:hidden relative"><div class="relative ">
	<button class="group flex items-center px-2 py-0.5 dark:text-gray-300 hover:text-yellow-700 dark:hover:text-gray-100 " type="button">
		<svg class="mr-1.5 mr-1.5 text-gray-400 text-yellow-500! group-hover:text-yellow-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M20.6081 3C21.7684 3 22.8053 3.49196 23.5284 4.38415C23.9756 4.93678 24.4428 5.82749 24.4808 7.16133C24.9674 7.01707 25.4353 6.93643 25.8725 6.93643C26.9833 6.93643 27.9865 7.37587 28.696 8.17411C29.6075 9.19872 30.0124 10.4579 29.8361 11.7177C29.7523 12.3177 29.5581 12.8555 29.2678 13.3534C29.8798 13.8646 30.3306 14.5763 30.5485 15.4322C30.719 16.1032 30.8939 17.5006 29.9808 18.9403C30.0389 19.0342 30.0934 19.1319 30.1442 19.2318C30.6932 20.3074 30.7283 21.5229 30.2439 22.6548C29.5093 24.3704 27.6841 25.7219 24.1397 27.1727C21.9347 28.0753 19.9174 28.6523 19.8994 28.6575C16.9842 29.4379 14.3477 29.8345 12.0653 29.8345C7.87017 29.8345 4.8668 28.508 3.13831 25.8921C0.356375 21.6797 0.754104 17.8269 4.35369 14.1131C6.34591 12.058 7.67023 9.02782 7.94613 8.36275C8.50224 6.39343 9.97271 4.20438 12.4172 4.20438H12.4179C12.6236 4.20438 12.8314 4.2214 13.0364 4.25468C14.107 4.42854 15.0428 5.06476 15.7115 6.02205C16.4331 5.09583 17.134 4.359 17.7682 3.94323C18.7242 3.31737 19.6794 3 20.6081 3ZM20.6081 5.95917C20.2427 5.95917 19.7963 6.1197 19.3039 6.44225C17.7754 7.44319 14.8258 12.6772 13.7458 14.7131C13.3839 15.3952 12.7655 15.6837 12.2086 15.6837C11.1036 15.6837 10.2408 14.5497 12.1076 13.1085C14.9146 10.9402 13.9299 7.39584 12.5898 7.1776C12.5311 7.16799 12.4731 7.16355 12.4172 7.16355C11.1989 7.16355 10.6615 9.33114 10.6615 9.33114C10.6615 9.33114 9.0863 13.4148 6.38031 16.206C3.67434 18.998 3.5346 21.2388 5.50675 24.2246C6.85185 26.2606 9.42666 26.8753 12.0653 26.8753C14.8021 26.8753 17.6077 26.2139 19.1799 25.793C19.2574 25.7723 28.8193 22.984 27.6081 20.6107C27.4046 20.212 27.0693 20.0522 26.6471 20.0522C24.9416 20.0522 21.8393 22.6726 20.5057 22.6726C20.2076 22.6726 19.9976 22.5416 19.9116 22.222C19.3433 20.1173 28.552 19.2325 27.7758 16.1839C27.639 15.6445 27.2677 15.4256 26.746 15.4263C24.4923 15.4263 19.4358 19.5181 18.3759 19.5181C18.2949 19.5181 18.2368 19.4937 18.2053 19.4419C17.6743 18.557 17.9653 17.9394 21.7082 15.6009C25.4511 13.2617 28.0783 11.8545 26.5841 10.1752C26.4121 9.98141 26.1684 9.8956 25.8725 9.8956C23.6001 9.89634 18.2311 14.9403 18.2311 14.9403C18.2311 14.9403 16.7821 16.496 15.9057 16.496C15.7043 16.496 15.533 16.4139 15.4169 16.2112C14.7956 15.1296 21.1879 10.1286 21.5484 8.06535C21.7928 6.66715 21.3771 5.95917 20.6081 5.95917Z" fill="#FF9D00"></path><path d="M5.50686 24.2246C3.53472 21.2387 3.67446 18.9979 6.38043 16.206C9.08641 13.4147 10.6615 9.33111 10.6615 9.33111C10.6615 9.33111 11.2499 6.95933 12.59 7.17757C13.93 7.39581 14.9139 10.9401 12.1069 13.1084C9.29997 15.276 12.6659 16.7489 13.7459 14.713C14.8258 12.6772 17.7747 7.44316 19.304 6.44221C20.8326 5.44128 21.9089 6.00204 21.5484 8.06532C21.188 10.1286 14.795 15.1295 15.4171 16.2118C16.0391 17.2934 18.2312 14.9402 18.2312 14.9402C18.2312 14.9402 25.0907 8.49588 26.5842 10.1752C28.0776 11.8545 25.4512 13.2616 21.7082 15.6008C17.9646 17.9393 17.6744 18.557 18.2054 19.4418C18.7372 20.3266 26.9998 13.1351 27.7759 16.1838C28.5513 19.2324 19.3434 20.1173 19.9117 22.2219C20.48 24.3274 26.3979 18.2382 27.6082 20.6107C28.8193 22.9839 19.2574 25.7722 19.18 25.7929C16.0914 26.62 8.24723 28.3726 5.50686 24.2246Z" fill="#FFD21E"></path></svg>
			Community
		</button>
	
	
	</div>
				</li><li class="hover:text-yellow-700"><a class="group flex items-center px-2 py-0.5 dark:text-gray-300 dark:hover:text-gray-100" href="/docs"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" class="mr-1.5 text-gray-400 group-hover:text-yellow-500" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><path d="m2.28 3.7-.3.16a.67.67 0 0 0-.34.58v8.73l.01.04.02.07.01.04.03.06.02.04.02.03.04.06.05.05.04.04.06.04.06.04.08.04.08.02h.05l.07.02h.11l.04-.01.07-.02.03-.01.07-.03.22-.12a5.33 5.33 0 0 1 5.15.1.67.67 0 0 0 .66 0 5.33 5.33 0 0 1 5.33 0 .67.67 0 0 0 1-.58V4.36a.67.67 0 0 0-.34-.5l-.3-.17v7.78a.63.63 0 0 1-.87.59 4.9 4.9 0 0 0-4.35.35l-.65.39a.29.29 0 0 1-.15.04.29.29 0 0 1-.16-.04l-.65-.4a4.9 4.9 0 0 0-4.34-.34.63.63 0 0 1-.87-.59V3.7Z" fill="currentColor" class="dark:opacity-40"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M8 3.1a5.99 5.99 0 0 0-5.3-.43.66.66 0 0 0-.42.62v8.18c0 .45.46.76.87.59a4.9 4.9 0 0 1 4.34.35l.65.39c.05.03.1.04.16.04.05 0 .1-.01.15-.04l.65-.4a4.9 4.9 0 0 1 4.35-.34.63.63 0 0 0 .86-.59V3.3a.67.67 0 0 0-.41-.62 5.99 5.99 0 0 0-5.3.43l-.3.17L8 3.1Zm.73 1.87a.43.43 0 1 0-.86 0v5.48a.43.43 0 0 0 .86 0V4.97Z" fill="currentColor" class="opacity-40 dark:opacity-100"></path><path d="M8.73 4.97a.43.43 0 1 0-.86 0v5.48a.43.43 0 1 0 .86 0V4.96Z" fill="currentColor" class="dark:opacity-40"></path></svg>
						Docs</a>
				</li><li class="hover:text-black dark:hover:text-white max-2xl:hidden"><a class="group flex items-center px-2 py-0.5 dark:text-gray-300 dark:hover:text-gray-100" href="/enterprise"><svg class="mr-1.5 text-gray-400 group-hover:text-black dark:group-hover:text-white" xmlns="http://www.w3.org/2000/svg" fill="none" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 12 12"><path fill-rule="evenodd" clip-rule="evenodd" d="M4.9 1.35a3.16 3.16 0 0 0-2.8 2.07L.37 8.58C0 9.71.7 10.65 1.86 10.65H7.3a3.2 3.2 0 0 0 2.84-2.07l1.67-5.16c.36-1.13-.3-2.07-1.46-2.07H4.91Zm.4 2.07L3.57 8.47h3.57l.36-1.12H5.4l.28-.91h1.75l.4-1.1H6.07l.3-.83h2l.36-1.1H5.27h.04Z" fill="currentColor"></path></svg>
						Enterprise</a>
				</li>

		<li><a class="group flex items-center px-2 py-0.5 dark:text-gray-300 dark:hover:text-gray-100" href="/pricing">Pricing
			</a></li>

		<li><div class="relative group">
	<button class="px-2 py-0.5 hover:text-gray-500 dark:hover:text-gray-600 flex items-center " type="button">
		<svg class=" text-gray-500 w-5 group-hover:text-gray-400 dark:text-gray-300 dark:group-hover:text-gray-100" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" viewBox="0 0 32 18" preserveAspectRatio="xMidYMid meet"><path fill-rule="evenodd" clip-rule="evenodd" d="M14.4504 3.30221C14.4504 2.836 14.8284 2.45807 15.2946 2.45807H28.4933C28.9595 2.45807 29.3374 2.836 29.3374 3.30221C29.3374 3.76842 28.9595 4.14635 28.4933 4.14635H15.2946C14.8284 4.14635 14.4504 3.76842 14.4504 3.30221Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M14.4504 9.00002C14.4504 8.53382 14.8284 8.15588 15.2946 8.15588H28.4933C28.9595 8.15588 29.3374 8.53382 29.3374 9.00002C29.3374 9.46623 28.9595 9.84417 28.4933 9.84417H15.2946C14.8284 9.84417 14.4504 9.46623 14.4504 9.00002Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M14.4504 14.6978C14.4504 14.2316 14.8284 13.8537 15.2946 13.8537H28.4933C28.9595 13.8537 29.3374 14.2316 29.3374 14.6978C29.3374 15.164 28.9595 15.542 28.4933 15.542H15.2946C14.8284 15.542 14.4504 15.164 14.4504 14.6978Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M1.94549 6.87377C2.27514 6.54411 2.80962 6.54411 3.13928 6.87377L6.23458 9.96907L9.32988 6.87377C9.65954 6.54411 10.194 6.54411 10.5237 6.87377C10.8533 7.20343 10.8533 7.73791 10.5237 8.06756L6.23458 12.3567L1.94549 8.06756C1.61583 7.73791 1.61583 7.20343 1.94549 6.87377Z" fill="currentColor"></path></svg>
			
		</button>
	
	
	</div></li>
		<li><hr class="h-5 w-0.5 border-none bg-gray-100 dark:bg-gray-800"></li>
		<li><a class="block cursor-pointer whitespace-nowrap px-2 py-0.5 hover:text-gray-500 dark:text-gray-300 dark:hover:text-gray-100" href="/login">Log In
				</a></li>
			<li><a class="whitespace-nowrap rounded-full border border-transparent bg-gray-900 px-3 py-1 leading-none text-white hover:border-black hover:bg-white hover:text-black" href="/join">Sign Up
					</a></li></ul></nav></div></header></div>
	
	
	
	<div class="SVELTE_HYDRATER contents" data-target="SSOBanner" data-props="{}"></div>
	


	

	<main class="flex flex-1 flex-col">
	<div class="SVELTE_HYDRATER contents" data-target="ModelHeader" data-props="{&quot;activeTab&quot;:&quot;files&quot;,&quot;author&quot;:{&quot;_id&quot;:&quot;64c8b5837fe12ecd0a7e92eb&quot;,&quot;avatarUrl&quot;:&quot;https://cdn-avatars.huggingface.co/v1/production/uploads/620760a26e3b7210c2ff1943/-s1gyJfvbE1RgO5iBeNOi.png&quot;,&quot;fullname&quot;:&quot;Qwen&quot;,&quot;name&quot;:&quot;Qwen&quot;,&quot;type&quot;:&quot;org&quot;,&quot;isHf&quot;:false,&quot;isHfAdmin&quot;:false,&quot;isMod&quot;:false,&quot;isEnterprise&quot;:true,&quot;followerCount&quot;:44431},&quot;canReadRepoSettings&quot;:false,&quot;canWriteRepoContent&quot;:false,&quot;canDisable&quot;:false,&quot;model&quot;:{&quot;author&quot;:&quot;Qwen&quot;,&quot;cardData&quot;:{&quot;library_name&quot;:&quot;transformers&quot;,&quot;license&quot;:&quot;apache-2.0&quot;,&quot;license_link&quot;:&quot;https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct/blob/main/LICENSE&quot;,&quot;pipeline_tag&quot;:&quot;text-generation&quot;},&quot;cardExists&quot;:true,&quot;config&quot;:{&quot;architectures&quot;:[&quot;Qwen3MoeForCausalLM&quot;],&quot;model_type&quot;:&quot;qwen3_moe&quot;,&quot;tokenizer_config&quot;:{&quot;bos_token&quot;:null,&quot;chat_template&quot;:&quot;{% macro render_extra_keys(json_dict, handled_keys) %}\n    {%- if json_dict is mapping %}\n        {%- for json_key in json_dict if json_key not in handled_keys %}\n            {%- if json_dict[json_key] is mapping %}\n                {{- '\\n<' ~ json_key ~ '>' ~ (json_dict[json_key] | tojson | safe) ~ '</' ~ json_key ~ '>' }}\n            {%- else %}\n                {{-'\\n<' ~ json_key ~ '>' ~ (json_dict[json_key] | string) ~ '</' ~ json_key ~ '>' }}\n            {%- endif %}\n        {%- endfor %}\n    {%- endif %}\n{% endmacro %}\n\n{%- if messages[0][\&quot;role\&quot;] == \&quot;system\&quot; %}\n    {%- set system_message = messages[0][\&quot;content\&quot;] %}\n    {%- set loop_messages = messages[1:] %}\n{%- else %}\n    {%- set loop_messages = messages %}\n{%- endif %}\n\n{%- if not tools is defined %}\n    {%- set tools = [] %}\n{%- endif %}\n\n{%- if system_message is defined %}\n    {{- \&quot;<|im_start|>system\\n\&quot; + system_message }}\n{%- else %}\n    {%- if tools is iterable and tools | length > 0 %}\n        {{- \&quot;<|im_start|>system\\nYou are Qwen, a helpful AI assistant that can interact with a computer to solve tasks.\&quot; }}\n    {%- endif %}\n{%- endif %}\n{%- if tools is iterable and tools | length > 0 %}\n    {{- \&quot;\\n\\nYou have access to the following functions:\\n\\n\&quot; }}\n    {{- \&quot;<tools>\&quot; }}\n    {%- for tool in tools %}\n        {%- if tool.function is defined %}\n            {%- set tool = tool.function %}\n        {%- endif %}\n        {{- \&quot;\\n<function>\\n<name>\&quot; ~ tool.name ~ \&quot;</name>\&quot; }}\n        {%- if tool.description is defined %}\n            {{- '\\n<description>' ~ (tool.description | trim) ~ '</description>' }}\n        {%- endif %}\n        {{- '\\n<parameters>' }}\n        {%- if tool.parameters is defined and tool.parameters is mapping and tool.parameters.properties is defined and tool.parameters.properties is mapping %}\n            {%- for param_name, param_fields in tool.parameters.properties|items %}\n                {{- '\\n<parameter>' }}\n                {{- '\\n<name>' ~ param_name ~ '</name>' }}\n                {%- if param_fields.type is defined %}\n                    {{- '\\n<type>' ~ (param_fields.type | string) ~ '</type>' }}\n                {%- endif %}\n                {%- if param_fields.description is defined %}\n                    {{- '\\n<description>' ~ (param_fields.description | trim) ~ '</description>' }}\n                {%- endif %}\n                {%- set handled_keys = ['name', 'type', 'description'] %}\n                {{- render_extra_keys(param_fields, handled_keys) }}\n                {{- '\\n</parameter>' }}\n            {%- endfor %}\n        {%- endif %}\n        {% set handled_keys = ['type', 'properties'] %}\n        {{- render_extra_keys(tool.parameters, handled_keys) }}\n        {{- '\\n</parameters>' }}\n        {%- set handled_keys = ['type', 'name', 'description', 'parameters'] %}\n        {{- render_extra_keys(tool, handled_keys) }}\n        {{- '\\n</function>' }}\n    {%- endfor %}\n    {{- \&quot;\\n</tools>\&quot; }}\n    {{- '\\n\\nIf you choose to call a function ONLY reply in the following format with NO suffix:\\n\\n<tool_call>\\n<function=example_function_name>\\n<parameter=example_parameter_1>\\nvalue_1\\n</parameter>\\n<parameter=example_parameter_2>\\nThis is the value for the second parameter\\nthat can span\\nmultiple lines\\n</parameter>\\n</function>\\n</tool_call>\\n\\n<IMPORTANT>\\nReminder:\\n- Function calls MUST follow the specified format: an inner <function=...></function> block must be nested within <tool_call></tool_call> XML tags\\n- Required parameters MUST be specified\\n- You may provide optional reasoning for your function call in natural language BEFORE the function call, but NOT after\\n- If there is no function call available, answer the question like normal with your current knowledge and do not tell the user about function calls\\n</IMPORTANT>' }}\n{%- endif %}\n{%- if system_message is defined %}\n    {{- '<|im_end|>\\n' }}\n{%- else %}\n    {%- if tools is iterable and tools | length > 0 %}\n        {{- '<|im_end|>\\n' }}\n    {%- endif %}\n{%- endif %}\n{%- for message in loop_messages %}\n    {%- if message.role == \&quot;assistant\&quot; and message.tool_calls is defined and message.tool_calls is iterable and message.tool_calls | length > 0 %}\n        {{- '<|im_start|>' + message.role }}\n        {%- if message.content is defined and message.content is string and message.content | trim | length > 0 %}\n            {{- '\\n' + message.content | trim + '\\n' }}\n        {%- endif %}\n        {%- for tool_call in message.tool_calls %}\n            {%- if tool_call.function is defined %}\n                {%- set tool_call = tool_call.function %}\n            {%- endif %}\n            {{- '\\n<tool_call>\\n<function=' + tool_call.name + '>\\n' }}\n            {%- if tool_call.arguments is defined %}\n                {%- for args_name, args_value in tool_call.arguments|items %}\n                    {{- '<parameter=' + args_name + '>\\n' }}\n                    {%- set args_value = args_value | tojson | safe if args_value is mapping else args_value | string %}\n                    {{- args_value }}\n                    {{- '\\n</parameter>\\n' }}\n                {%- endfor %}\n            {%- endif %}\n            {{- '</function>\\n</tool_call>' }}\n        {%- endfor %}\n        {{- '<|im_end|>\\n' }}\n    {%- elif message.role == \&quot;user\&quot; or message.role == \&quot;system\&quot; or message.role == \&quot;assistant\&quot; %}\n        {{- '<|im_start|>' + message.role + '\\n' + message.content + '<|im_end|>' + '\\n' }}\n    {%- elif message.role == \&quot;tool\&quot; %}\n        {%- if loop.previtem and loop.previtem.role != \&quot;tool\&quot; %}\n            {{- '<|im_start|>user\\n' }}\n        {%- endif %}\n        {{- '<tool_response>\\n' }}\n        {{- message.content }}\n        {{- '\\n</tool_response>\\n' }}\n        {%- if not loop.last and loop.nextitem.role != \&quot;tool\&quot; %}\n            {{- '<|im_end|>\\n' }}\n        {%- elif loop.last %}\n            {{- '<|im_end|>\\n' }}\n        {%- endif %}\n    {%- else %}\n        {{- '<|im_start|>' + message.role + '\\n' + message.content + '<|im_end|>\\n' }}\n    {%- endif %}\n{%- endfor %}\n{%- if add_generation_prompt %}\n    {{- '<|im_start|>assistant\\n' }}\n{%- endif %}\n&quot;,&quot;eos_token&quot;:&quot;<|im_end|>&quot;,&quot;pad_token&quot;:&quot;<|endoftext|>&quot;,&quot;unk_token&quot;:null}},&quot;createdAt&quot;:&quot;2025-07-31T07:04:55.000Z&quot;,&quot;discussionsDisabled&quot;:false,&quot;downloads&quot;:196373,&quot;downloadsAllTime&quot;:196373,&quot;id&quot;:&quot;Qwen/Qwen3-Coder-30B-A3B-Instruct&quot;,&quot;isLikedByUser&quot;:false,&quot;availableInferenceProviders&quot;:[{&quot;provider&quot;:&quot;fireworks-ai&quot;,&quot;modelStatus&quot;:&quot;live&quot;,&quot;providerStatus&quot;:&quot;live&quot;,&quot;providerId&quot;:&quot;accounts/fireworks/models/qwen3-coder-30b-a3b-instruct&quot;,&quot;task&quot;:&quot;conversational&quot;,&quot;adapterWeightsPath&quot;:&quot;model-00001-of-00016.safetensors&quot;,&quot;features&quot;:{&quot;structuredOutput&quot;:false,&quot;toolCalling&quot;:true}}],&quot;inference&quot;:&quot;warm&quot;,&quot;lastModified&quot;:&quot;2025-08-07T07:08:04.000Z&quot;,&quot;likes&quot;:471,&quot;pipeline_tag&quot;:&quot;text-generation&quot;,&quot;library_name&quot;:&quot;transformers&quot;,&quot;librariesOther&quot;:[],&quot;trackDownloads&quot;:true,&quot;model-index&quot;:null,&quot;private&quot;:false,&quot;repoType&quot;:&quot;model&quot;,&quot;gated&quot;:false,&quot;pwcLink&quot;:{&quot;error&quot;:&quot;Unknown error, can't generate link to Papers With Code.&quot;},&quot;tags&quot;:[&quot;transformers&quot;,&quot;safetensors&quot;,&quot;qwen3_moe&quot;,&quot;text-generation&quot;,&quot;conversational&quot;,&quot;arxiv:2505.09388&quot;,&quot;license:apache-2.0&quot;,&quot;autotrain_compatible&quot;,&quot;endpoints_compatible&quot;,&quot;region:us&quot;],&quot;tag_objs&quot;:[{&quot;id&quot;:&quot;text-generation&quot;,&quot;label&quot;:&quot;Text Generation&quot;,&quot;type&quot;:&quot;pipeline_tag&quot;,&quot;subType&quot;:&quot;nlp&quot;},{&quot;id&quot;:&quot;transformers&quot;,&quot;label&quot;:&quot;Transformers&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;safetensors&quot;,&quot;label&quot;:&quot;Safetensors&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;qwen3_moe&quot;,&quot;label&quot;:&quot;qwen3_moe&quot;,&quot;type&quot;:&quot;other&quot;},{&quot;id&quot;:&quot;conversational&quot;,&quot;label&quot;:&quot;conversational&quot;,&quot;type&quot;:&quot;other&quot;},{&quot;id&quot;:&quot;autotrain_compatible&quot;,&quot;label&quot;:&quot;AutoTrain Compatible&quot;,&quot;type&quot;:&quot;other&quot;},{&quot;id&quot;:&quot;endpoints_compatible&quot;,&quot;label&quot;:&quot;Inference Endpoints&quot;,&quot;type&quot;:&quot;other&quot;},{&quot;id&quot;:&quot;arxiv:2505.09388&quot;,&quot;label&quot;:&quot;arxiv:2505.09388&quot;,&quot;type&quot;:&quot;arxiv&quot;,&quot;extra&quot;:{&quot;paperTitle&quot;:&quot;Qwen3 Technical Report&quot;}},{&quot;id&quot;:&quot;license:apache-2.0&quot;,&quot;label&quot;:&quot;apache-2.0&quot;,&quot;type&quot;:&quot;license&quot;},{&quot;type&quot;:&quot;region&quot;,&quot;label&quot;:&quot;🇺🇸 Region: US&quot;,&quot;id&quot;:&quot;region:us&quot;}],&quot;transformersInfo&quot;:{&quot;auto_model&quot;:&quot;AutoModelForCausalLM&quot;,&quot;pipeline_tag&quot;:&quot;text-generation&quot;,&quot;processor&quot;:&quot;AutoTokenizer&quot;},&quot;widgetData&quot;:[{&quot;text&quot;:&quot;Hi, what can you help me with?&quot;},{&quot;text&quot;:&quot;What is 84 * 3 / 2?&quot;},{&quot;text&quot;:&quot;Tell me an interesting fact about the universe!&quot;},{&quot;text&quot;:&quot;Explain quantum computing in simple terms.&quot;}],&quot;safetensors&quot;:{&quot;parameters&quot;:{&quot;BF16&quot;:30532122624},&quot;total&quot;:30532122624,&quot;sharded&quot;:true},&quot;hasBlockedOids&quot;:false,&quot;region&quot;:&quot;us&quot;,&quot;isQuantized&quot;:false,&quot;xetEnabled&quot;:true},&quot;discussionsStats&quot;:{&quot;closed&quot;:3,&quot;open&quot;:13,&quot;total&quot;:16},&quot;query&quot;:{},&quot;inferenceContextData&quot;:{&quot;billableEntities&quot;:[],&quot;entityName2Providers&quot;:{},&quot;defaultProviders&quot;:[{&quot;name&quot;:&quot;fireworks-ai&quot;,&quot;enabled&quot;:true,&quot;position&quot;:0,&quot;isReleased&quot;:true,&quot;accuratePricing&quot;:true}]}}"><header class="bg-linear-to-t border-b border-gray-100 pt-6 sm:pt-9 from-purple-500/8 dark:from-purple-500/20 to-white to-70%  dark:to-gray-950"><div class="container relative "><h1 class="flex flex-wrap items-center max-md:leading-tight mb-3 text-lg max-sm:gap-y-1.5 md:text-xl">
			<div class="group flex flex-none items-center"><div class="relative mr-1 flex items-center">

			

<span class="inline-block "><span class="contents"><a href="/Qwen" class="text-gray-400 hover:text-blue-600"><img alt="" class="size-3.5 rounded-sm  flex-none" src="https://cdn-avatars.huggingface.co/v1/production/uploads/620760a26e3b7210c2ff1943/-s1gyJfvbE1RgO5iBeNOi.png" crossorigin="anonymous"></a></span>
	</span></div>
		

<span class="inline-block "><span class="contents"><a href="/Qwen" class="text-gray-400 hover:text-blue-600">Qwen</a></span>
	</span>
		<div class="mx-0.5 text-gray-300">/</div></div>

<div class="max-w-full "><a class="break-words font-mono font-semibold hover:text-blue-600 " href="/Qwen/Qwen3-Coder-30B-A3B-Instruct">Qwen3-Coder-30B-A3B-Instruct</a>
	<button class="text-sm mr-4 focus:outline-hidden inline-flex cursor-pointer items-center text-sm  mx-0.5   text-gray-600 " title="Copy model name to clipboard" type="button"><svg class="" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" fill="currentColor" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M28,10V28H10V10H28m0-2H10a2,2,0,0,0-2,2V28a2,2,0,0,0,2,2H28a2,2,0,0,0,2-2V10a2,2,0,0,0-2-2Z" transform="translate(0)"></path><path d="M4,18H2V4A2,2,0,0,1,4,2H18V4H4Z" transform="translate(0)"></path><rect fill="none" width="32" height="32"></rect></svg>
		</button></div>
			<div class="inline-flex items-center overflow-hidden whitespace-nowrap rounded-md border bg-white text-sm leading-none text-gray-500  mr-2"><button class="relative flex items-center overflow-hidden from-red-50 to-transparent dark:from-red-900 px-1.5 py-1 hover:bg-linear-to-t focus:outline-hidden"  title="Like"><svg class="left-1.5 absolute" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" fill="currentColor"><path d="M22.45,6a5.47,5.47,0,0,1,3.91,1.64,5.7,5.7,0,0,1,0,8L16,26.13,5.64,15.64a5.7,5.7,0,0,1,0-8,5.48,5.48,0,0,1,7.82,0L16,10.24l2.53-2.58A5.44,5.44,0,0,1,22.45,6m0-2a7.47,7.47,0,0,0-5.34,2.24L16,7.36,14.89,6.24a7.49,7.49,0,0,0-10.68,0,7.72,7.72,0,0,0,0,10.82L16,29,27.79,17.06a7.72,7.72,0,0,0,0-10.82A7.49,7.49,0,0,0,22.45,4Z"></path></svg>

		
		<span class="ml-4 pl-0.5 ">like</span></button>
	<button class="focus:outline-hidden flex items-center border-l px-1.5 py-1 text-gray-400 hover:bg-gray-50 focus:bg-gray-100 dark:hover:bg-gray-900 dark:focus:bg-gray-800" title="See users who liked this repository">471</button></div>




			<div class="relative flex items-center gap-1.5  "><div class="mr-2 inline-flex h-6 items-center overflow-hidden whitespace-nowrap rounded-md border text-sm text-gray-500"><button class="focus:outline-hidden relative flex h-full max-w-56 items-center gap-1.5 overflow-hidden px-1.5 hover:bg-gray-50 focus:bg-gray-100 dark:hover:bg-gray-900 dark:focus:bg-gray-800" type="button" ><div class="flex h-full flex-1 items-center justify-center ">Follow</div>
		<img alt="" class="rounded-xs size-3 flex-none" src="https://cdn-avatars.huggingface.co/v1/production/uploads/620760a26e3b7210c2ff1943/-s1gyJfvbE1RgO5iBeNOi.png">
		<span class="truncate">Qwen</span></button>
	<button class="focus:outline-hidden flex h-full items-center border-l pl-1.5 pr-1.5 text-gray-400 hover:bg-gray-50 focus:bg-gray-100 dark:hover:bg-gray-900 dark:focus:bg-gray-800" title="Show Qwen's followers" type="button">44.4k</button></div>

		</div>
			
	</h1>
		<div class="mb-3 flex flex-wrap md:mb-4"><a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/models?pipeline_tag=text-generation"><div class="tag   tag-white "><div class="tag-ico -ml-2 tag-ico-red"><svg class="-mr-0.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" fill="currentColor" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 18 18"><path d="M16.2607 8.08202L14.468 6.28928C14.3063 6.12804 14.0873 6.03749 13.859 6.03749C13.6307 6.03749 13.4117 6.12804 13.25 6.28928L5.6375 13.904V16.9125H8.64607L16.2607 9.30002C16.422 9.13836 16.5125 8.91935 16.5125 8.69102C16.5125 8.4627 16.422 8.24369 16.2607 8.08202V8.08202ZM8.1953 15.825H6.725V14.3547L11.858 9.22118L13.3288 10.6915L8.1953 15.825ZM14.0982 9.92262L12.6279 8.45232L13.8606 7.21964L15.3309 8.68994L14.0982 9.92262Z"></path><path d="M6.18125 9.84373H7.26875V6.03748H8.9V4.94998H4.55V6.03748H6.18125V9.84373Z"></path><path d="M4.55 11.475H2.375V2.775H11.075V4.95H12.1625V2.775C12.1625 2.48658 12.0479 2.20997 11.844 2.00602C11.64 1.80208 11.3634 1.6875 11.075 1.6875H2.375C2.08658 1.6875 1.80997 1.80208 1.60602 2.00602C1.40207 2.20997 1.2875 2.48658 1.2875 2.775V11.475C1.2875 11.7634 1.40207 12.04 1.60602 12.244C1.80997 12.4479 2.08658 12.5625 2.375 12.5625H4.55V11.475Z"></path></svg></div>

	

	<span>Text Generation</span>
	

	</div></a><a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/models?library=transformers"><div class="tag   tag-white "><svg class="text-black inline-block text-sm" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" preserveAspectRatio="xMidYMid meet" width="1em" height="1em" viewBox="0 0 95 88"><path fill="#fff" d="M94.25 70.08a8.28 8.28 0 0 1-.43 6.46 10.57 10.57 0 0 1-3 3.6 25.18 25.18 0 0 1-5.7 3.2 65.74 65.74 0 0 1-7.56 2.65 46.67 46.67 0 0 1-11.42 1.68c-5.42.05-10.09-1.23-13.4-4.5a40.4 40.4 0 0 1-10.14.03c-3.34 3.25-7.99 4.52-13.39 4.47a46.82 46.82 0 0 1-11.43-1.68 66.37 66.37 0 0 1-7.55-2.65c-2.28-.98-4.17-2-5.68-3.2a10.5 10.5 0 0 1-3.02-3.6c-.99-2-1.18-4.3-.42-6.46a8.54 8.54 0 0 1-.33-5.63c.25-.95.66-1.83 1.18-2.61a8.67 8.67 0 0 1 2.1-8.47 8.23 8.23 0 0 1 2.82-2.07 41.75 41.75 0 1 1 81.3-.12 8.27 8.27 0 0 1 3.11 2.19 8.7 8.7 0 0 1 2.1 8.47c.52.78.93 1.66 1.18 2.61a8.61 8.61 0 0 1-.32 5.63Z"></path><path fill="#FFD21E" d="M47.21 76.5a34.75 34.75 0 1 0 0-69.5 34.75 34.75 0 0 0 0 69.5Z"></path><path fill="#FF9D0B" d="M81.96 41.75a34.75 34.75 0 1 0-69.5 0 34.75 34.75 0 0 0 69.5 0Zm-73.5 0a38.75 38.75 0 1 1 77.5 0 38.75 38.75 0 0 1-77.5 0Z"></path><path fill="#3A3B45" d="M58.5 32.3c1.28.44 1.78 3.06 3.07 2.38a5 5 0 1 0-6.76-2.07c.61 1.15 2.55-.72 3.7-.32ZM34.95 32.3c-1.28.44-1.79 3.06-3.07 2.38a5 5 0 1 1 6.76-2.07c-.61 1.15-2.56-.72-3.7-.32Z"></path><path fill="#FF323D" d="M46.96 56.29c9.83 0 13-8.76 13-13.26 0-2.34-1.57-1.6-4.09-.36-2.33 1.15-5.46 2.74-8.9 2.74-7.19 0-13-6.88-13-2.38s3.16 13.26 13 13.26Z"></path><path fill="#3A3B45" fill-rule="evenodd" d="M39.43 54a8.7 8.7 0 0 1 5.3-4.49c.4-.12.81.57 1.24 1.28.4.68.82 1.37 1.24 1.37.45 0 .9-.68 1.33-1.35.45-.7.89-1.38 1.32-1.25a8.61 8.61 0 0 1 5 4.17c3.73-2.94 5.1-7.74 5.1-10.7 0-2.34-1.57-1.6-4.09-.36l-.14.07c-2.31 1.15-5.39 2.67-8.77 2.67s-6.45-1.52-8.77-2.67c-2.6-1.29-4.23-2.1-4.23.29 0 3.05 1.46 8.06 5.47 10.97Z" clip-rule="evenodd"></path><path fill="#FF9D0B" d="M70.71 37a3.25 3.25 0 1 0 0-6.5 3.25 3.25 0 0 0 0 6.5ZM24.21 37a3.25 3.25 0 1 0 0-6.5 3.25 3.25 0 0 0 0 6.5ZM17.52 48c-1.62 0-3.06.66-4.07 1.87a5.97 5.97 0 0 0-1.33 3.76 7.1 7.1 0 0 0-1.94-.3c-1.55 0-2.95.59-3.94 1.66a5.8 5.8 0 0 0-.8 7 5.3 5.3 0 0 0-1.79 2.82c-.24.9-.48 2.8.8 4.74a5.22 5.22 0 0 0-.37 5.02c1.02 2.32 3.57 4.14 8.52 6.1 3.07 1.22 5.89 2 5.91 2.01a44.33 44.33 0 0 0 10.93 1.6c5.86 0 10.05-1.8 12.46-5.34 3.88-5.69 3.33-10.9-1.7-15.92-2.77-2.78-4.62-6.87-5-7.77-.78-2.66-2.84-5.62-6.25-5.62a5.7 5.7 0 0 0-4.6 2.46c-1-1.26-1.98-2.25-2.86-2.82A7.4 7.4 0 0 0 17.52 48Zm0 4c.51 0 1.14.22 1.82.65 2.14 1.36 6.25 8.43 7.76 11.18.5.92 1.37 1.31 2.14 1.31 1.55 0 2.75-1.53.15-3.48-3.92-2.93-2.55-7.72-.68-8.01.08-.02.17-.02.24-.02 1.7 0 2.45 2.93 2.45 2.93s2.2 5.52 5.98 9.3c3.77 3.77 3.97 6.8 1.22 10.83-1.88 2.75-5.47 3.58-9.16 3.58-3.81 0-7.73-.9-9.92-1.46-.11-.03-13.45-3.8-11.76-7 .28-.54.75-.76 1.34-.76 2.38 0 6.7 3.54 8.57 3.54.41 0 .7-.17.83-.6.79-2.85-12.06-4.05-10.98-8.17.2-.73.71-1.02 1.44-1.02 3.14 0 10.2 5.53 11.68 5.53.11 0 .2-.03.24-.1.74-1.2.33-2.04-4.9-5.2-5.21-3.16-8.88-5.06-6.8-7.33.24-.26.58-.38 1-.38 3.17 0 10.66 6.82 10.66 6.82s2.02 2.1 3.25 2.1c.28 0 .52-.1.68-.38.86-1.46-8.06-8.22-8.56-11.01-.34-1.9.24-2.85 1.31-2.85Z"></path><path fill="#FFD21E" d="M38.6 76.69c2.75-4.04 2.55-7.07-1.22-10.84-3.78-3.77-5.98-9.3-5.98-9.3s-.82-3.2-2.69-2.9c-1.87.3-3.24 5.08.68 8.01 3.91 2.93-.78 4.92-2.29 2.17-1.5-2.75-5.62-9.82-7.76-11.18-2.13-1.35-3.63-.6-3.13 2.2.5 2.79 9.43 9.55 8.56 11-.87 1.47-3.93-1.71-3.93-1.71s-9.57-8.71-11.66-6.44c-2.08 2.27 1.59 4.17 6.8 7.33 5.23 3.16 5.64 4 4.9 5.2-.75 1.2-12.28-8.53-13.36-4.4-1.08 4.11 11.77 5.3 10.98 8.15-.8 2.85-9.06-5.38-10.74-2.18-1.7 3.21 11.65 6.98 11.76 7.01 4.3 1.12 15.25 3.49 19.08-2.12Z"></path><path fill="#FF9D0B" d="M77.4 48c1.62 0 3.07.66 4.07 1.87a5.97 5.97 0 0 1 1.33 3.76 7.1 7.1 0 0 1 1.95-.3c1.55 0 2.95.59 3.94 1.66a5.8 5.8 0 0 1 .8 7 5.3 5.3 0 0 1 1.78 2.82c.24.9.48 2.8-.8 4.74a5.22 5.22 0 0 1 .37 5.02c-1.02 2.32-3.57 4.14-8.51 6.1-3.08 1.22-5.9 2-5.92 2.01a44.33 44.33 0 0 1-10.93 1.6c-5.86 0-10.05-1.8-12.46-5.34-3.88-5.69-3.33-10.9 1.7-15.92 2.78-2.78 4.63-6.87 5.01-7.77.78-2.66 2.83-5.62 6.24-5.62a5.7 5.7 0 0 1 4.6 2.46c1-1.26 1.98-2.25 2.87-2.82A7.4 7.4 0 0 1 77.4 48Zm0 4c-.51 0-1.13.22-1.82.65-2.13 1.36-6.25 8.43-7.76 11.18a2.43 2.43 0 0 1-2.14 1.31c-1.54 0-2.75-1.53-.14-3.48 3.91-2.93 2.54-7.72.67-8.01a1.54 1.54 0 0 0-.24-.02c-1.7 0-2.45 2.93-2.45 2.93s-2.2 5.52-5.97 9.3c-3.78 3.77-3.98 6.8-1.22 10.83 1.87 2.75 5.47 3.58 9.15 3.58 3.82 0 7.73-.9 9.93-1.46.1-.03 13.45-3.8 11.76-7-.29-.54-.75-.76-1.34-.76-2.38 0-6.71 3.54-8.57 3.54-.42 0-.71-.17-.83-.6-.8-2.85 12.05-4.05 10.97-8.17-.19-.73-.7-1.02-1.44-1.02-3.14 0-10.2 5.53-11.68 5.53-.1 0-.19-.03-.23-.1-.74-1.2-.34-2.04 4.88-5.2 5.23-3.16 8.9-5.06 6.8-7.33-.23-.26-.57-.38-.98-.38-3.18 0-10.67 6.82-10.67 6.82s-2.02 2.1-3.24 2.1a.74.74 0 0 1-.68-.38c-.87-1.46 8.05-8.22 8.55-11.01.34-1.9-.24-2.85-1.31-2.85Z"></path><path fill="#FFD21E" d="M56.33 76.69c-2.75-4.04-2.56-7.07 1.22-10.84 3.77-3.77 5.97-9.3 5.97-9.3s.82-3.2 2.7-2.9c1.86.3 3.23 5.08-.68 8.01-3.92 2.93.78 4.92 2.28 2.17 1.51-2.75 5.63-9.82 7.76-11.18 2.13-1.35 3.64-.6 3.13 2.2-.5 2.79-9.42 9.55-8.55 11 .86 1.47 3.92-1.71 3.92-1.71s9.58-8.71 11.66-6.44c2.08 2.27-1.58 4.17-6.8 7.33-5.23 3.16-5.63 4-4.9 5.2.75 1.2 12.28-8.53 13.36-4.4 1.08 4.11-11.76 5.3-10.97 8.15.8 2.85 9.05-5.38 10.74-2.18 1.69 3.21-11.65 6.98-11.76 7.01-4.31 1.12-15.26 3.49-19.08-2.12Z"></path></svg>

	

	<span>Transformers</span>
	

	</div></a><a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/models?library=safetensors"><div class="tag   tag-white "><svg class="text-black inline-block text-sm" viewBox="0 0 57 44" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet"><path d="M36.816 20.1474L54.9918 27.4409C55.5142 27.6506 55.9623 28.0112 56.2788 28.4766C56.5954 28.9421 56.7661 29.4913 56.7691 30.0542C56.7722 30.6171 56.6074 31.1682 56.2959 31.637C55.9844 32.1059 55.5402 32.4713 55.0201 32.6866L29.953 43.0646C29.2593 43.3518 28.4799 43.3518 27.7862 43.0646L2.71624 32.6894C2.19613 32.4741 1.75197 32.1087 1.44044 31.6398C1.12892 31.171 0.964165 30.62 0.967204 30.057C0.970244 29.4941 1.14094 28.9449 1.45751 28.4794C1.77408 28.014 2.22216 27.6534 2.74456 27.4437L21.2404 20.0227C22.2997 19.5979 25.6477 20.8441 28.8682 20.8555C32.3096 20.8668 35.6292 19.6715 36.816 20.1474ZM11.3042 30.1119L28.8682 37.3828L46.435 30.1119L28.8682 23.0619L11.3042 30.1119ZM29.9247 0.388251L54.9918 10.4462C55.5142 10.6559 55.9623 11.0165 56.2788 11.482C56.5954 11.9474 56.7661 12.4967 56.7691 13.0596C56.7722 13.6225 56.6074 14.1735 56.2959 14.6424C55.9844 15.1112 55.5402 15.4766 55.0201 15.6919L29.953 26.07C29.2593 26.3572 28.4799 26.3572 27.7862 26.07L2.71624 15.6948C2.19613 15.4795 1.75197 15.1141 1.44044 14.6452C1.12892 14.1763 0.964165 13.6253 0.967204 13.0624C0.970244 12.4995 1.14094 11.9503 1.45751 11.4848C1.77408 11.0193 2.22216 10.6588 2.74456 10.4491L27.8117 0.388251C28.4896 0.1157 29.2467 0.1157 29.9247 0.388251ZM11.3042 13.1172L28.8682 20.3881L46.435 13.1172L28.8682 6.06729L11.3042 13.1172Z" fill="currentColor"></path></svg>

	

	<span>Safetensors</span>
	

	</div></a><a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/models?other=qwen3_moe"><div class="tag   tag-white ">

	

	<span>qwen3_moe</span>
	

	</div></a><a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/models?other=conversational"><div class="tag   tag-white ">

	

	<span>conversational</span>
	

	</div></a>

	<div class="relative inline-block ">
	<button class="group mr-1 mb-1 md:mr-1.5 md:mb-1.5  rounded-full rounded-br-none " type="button">
		<div slot="button"><div class="tag rounded-full  tag-white relative rounded-br-none pr-2.5">
		<svg class="-mr-1 text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" viewBox="0 0 12 12" preserveAspectRatio="xMidYMid meet" fill="none"><path fill="currentColor" fill-rule="evenodd" d="M8.007 1.814a1.176 1.176 0 0 0-.732-.266H3.088c-.64 0-1.153.512-1.153 1.152v6.803c0 .64.513 1.152 1.153 1.152h5.54c.632 0 1.144-.511 1.144-1.152V3.816c0-.338-.137-.658-.412-.887L8.007 1.814Zm-1.875 1.81c0 .695.55 1.253 1.244 1.253h.983a.567.567 0 0 1 .553.585v4.041c0 .165-.119.302-.283.302h-5.55c-.156 0-.275-.137-.275-.302V2.7a.284.284 0 0 1 .284-.301h2.468a.574.574 0 0 1 .434.19.567.567 0 0 1 .142.395v.64Z" clip-rule="evenodd"></path><path fill="currentColor" fill-opacity=".2" fill-rule="evenodd" d="M6.132 3.624c0 .695.55 1.253 1.244 1.253h.97a.567.567 0 0 1 .566.585v4.041c0 .165-.119.302-.283.302h-5.55c-.156 0-.275-.137-.275-.302V2.7a.284.284 0 0 1 .284-.301h2.468a.567.567 0 0 1 .576.585v.64Z" clip-rule="evenodd"></path></svg>

	

	<span class="-mr-2 text-gray-400">arxiv:</span>
		<span>2505.09388</span>
	

	<div class="border-br-gray-200 absolute bottom-0.5 right-0.5 h-1 w-1 border-[3px] border-l-transparent border-t-transparent border-b-gray-200 border-r-gray-200 group-hover:border-b-gray-400 group-hover:border-r-gray-400 dark:border-b-gray-700 dark:border-r-gray-700 group-hover:dark:border-b-gray-400 group-hover:dark:border-r-gray-400"></div></div></div>
		</button>
	
	
	</div><div class="relative inline-block ">
	<button class="group mr-1 mb-1 md:mr-1.5 md:mb-1.5  rounded-full rounded-br-none " type="button">
		<div slot="button"><div class="tag rounded-full  tag-white relative rounded-br-none pr-2.5">
		<svg class="text-xs text-gray-900" width="1em" height="1em" viewBox="0 0 10 10" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M1.46009 5.0945V6.88125C1.46009 7.25201 1.75937 7.55129 2.13012 7.55129C2.50087 7.55129 2.80016 7.25201 2.80016 6.88125V5.0945C2.80016 4.72375 2.50087 4.42446 2.13012 4.42446C1.75937 4.42446 1.46009 4.72375 1.46009 5.0945ZM4.14022 5.0945V6.88125C4.14022 7.25201 4.4395 7.55129 4.81026 7.55129C5.18101 7.55129 5.48029 7.25201 5.48029 6.88125V5.0945C5.48029 4.72375 5.18101 4.42446 4.81026 4.42446C4.4395 4.42446 4.14022 4.72375 4.14022 5.0945ZM1.23674 9.78473H8.38377C8.75452 9.78473 9.0538 9.48545 9.0538 9.1147C9.0538 8.74395 8.75452 8.44466 8.38377 8.44466H1.23674C0.865993 8.44466 0.566711 8.74395 0.566711 9.1147C0.566711 9.48545 0.865993 9.78473 1.23674 9.78473ZM6.82036 5.0945V6.88125C6.82036 7.25201 7.11964 7.55129 7.49039 7.55129C7.86114 7.55129 8.16042 7.25201 8.16042 6.88125V5.0945C8.16042 4.72375 7.86114 4.42446 7.49039 4.42446C7.11964 4.42446 6.82036 4.72375 6.82036 5.0945ZM4.39484 0.623142L0.865993 2.48137C0.682851 2.57517 0.566711 2.76725 0.566711 2.97273C0.566711 3.28094 0.816857 3.53109 1.12507 3.53109H8.49991C8.80365 3.53109 9.0538 3.28094 9.0538 2.97273C9.0538 2.76725 8.93766 2.57517 8.75452 2.48137L5.22568 0.623142C4.9666 0.484669 4.65391 0.484669 4.39484 0.623142V0.623142Z" fill="currentColor"></path></svg>

	<span class="-mr-1 text-gray-400">License:</span>

	<span>apache-2.0</span>
	

	<div class="border-br-gray-200 absolute bottom-0.5 right-0.5 h-1 w-1 border-[3px] border-l-transparent border-t-transparent border-b-gray-200 border-r-gray-200 group-hover:border-b-gray-400 group-hover:border-r-gray-400 dark:border-b-gray-700 dark:border-r-gray-700 group-hover:dark:border-b-gray-400 group-hover:dark:border-r-gray-400"></div></div></div>
		</button>
	
	
	</div></div>

		<div class="flex flex-col-reverse lg:flex-row lg:items-center lg:justify-between"><div class="-mb-px flex h-12 items-center overflow-x-auto overflow-y-hidden ">
	<a class="tab-alternate" href="/Qwen/Qwen3-Coder-30B-A3B-Instruct"><svg class="mr-1.5 text-gray-400 flex-none" style="" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-quaternary" d="M20.23 7.24L12 12L3.77 7.24a1.98 1.98 0 0 1 .7-.71L11 2.76c.62-.35 1.38-.35 2 0l6.53 3.77c.29.173.531.418.7.71z" opacity=".25" fill="currentColor"></path><path class="uim-tertiary" d="M12 12v9.5a2.09 2.09 0 0 1-.91-.21L4.5 17.48a2.003 2.003 0 0 1-1-1.73v-7.5a2.06 2.06 0 0 1 .27-1.01L12 12z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M20.5 8.25v7.5a2.003 2.003 0 0 1-1 1.73l-6.62 3.82c-.275.13-.576.198-.88.2V12l8.23-4.76c.175.308.268.656.27 1.01z" fill="currentColor"></path></svg>
	Model card
	

	
		</a><a class="tab-alternate active" href="/Qwen/Qwen3-Coder-30B-A3B-Instruct/tree/main"><svg class="mr-1.5 text-gray-400 flex-none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-tertiary" d="M21 19h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2zm0-4h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2zm0-8h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2zm0 4h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M9 19a1 1 0 0 1-1-1V6a1 1 0 0 1 2 0v12a1 1 0 0 1-1 1zm-6-4.333a1 1 0 0 1-.64-1.769L3.438 12l-1.078-.898a1 1 0 0 1 1.28-1.538l2 1.667a1 1 0 0 1 0 1.538l-2 1.667a.999.999 0 0 1-.64.231z" fill="currentColor"></path></svg>
	<span class="xl:hidden">Files</span>
		<span class="hidden xl:inline">Files and versions</span>
	

	

<span class="inline-block "><span class="contents"><div slot="anchor" class="shadow-purple-500/10 ml-2 inline-flex -translate-y-px items-center gap-0.5 rounded-md border bg-white px-1 py-0.5 align-middle text-xs font-semibold leading-none text-gray-800 shadow-sm dark:border-gray-700 dark:bg-gradient-to-b dark:from-gray-925 dark:to-gray-925 dark:text-gray-300"><svg class="size-3 " xmlns="http://www.w3.org/2000/svg" aria-hidden="true" fill="currentColor" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 12 12"><path fill-rule="evenodd" clip-rule="evenodd" d="M6.14 3.64 5.1 4.92 2.98 2.28h2.06l1.1 1.36Zm0 4.72-1.1 1.36H2.98l2.13-2.64 1.03 1.28Zm4.9 1.36L8.03 6l3-3.72H8.96L5.97 6l3 3.72h2.06Z" fill="#7875FF"></path><path d="M4.24 6 2.6 8.03.97 6 2.6 3.97 4.24 6Z" fill="#FF7F41" opacity="1"></path></svg>
						<span>xet</span>
					</div></span>
	</span>
		</a><a class="tab-alternate" href="/Qwen/Qwen3-Coder-30B-A3B-Instruct/discussions"><svg class="mr-1.5 text-gray-400 flex-none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M20.6081 3C21.7684 3 22.8053 3.49196 23.5284 4.38415C23.9756 4.93678 24.4428 5.82749 24.4808 7.16133C24.9674 7.01707 25.4353 6.93643 25.8725 6.93643C26.9833 6.93643 27.9865 7.37587 28.696 8.17411C29.6075 9.19872 30.0124 10.4579 29.8361 11.7177C29.7523 12.3177 29.5581 12.8555 29.2678 13.3534C29.8798 13.8646 30.3306 14.5763 30.5485 15.4322C30.719 16.1032 30.8939 17.5006 29.9808 18.9403C30.0389 19.0342 30.0934 19.1319 30.1442 19.2318C30.6932 20.3074 30.7283 21.5229 30.2439 22.6548C29.5093 24.3704 27.6841 25.7219 24.1397 27.1727C21.9347 28.0753 19.9174 28.6523 19.8994 28.6575C16.9842 29.4379 14.3477 29.8345 12.0653 29.8345C7.87017 29.8345 4.8668 28.508 3.13831 25.8921C0.356375 21.6797 0.754104 17.8269 4.35369 14.1131C6.34591 12.058 7.67023 9.02782 7.94613 8.36275C8.50224 6.39343 9.97271 4.20438 12.4172 4.20438H12.4179C12.6236 4.20438 12.8314 4.2214 13.0364 4.25468C14.107 4.42854 15.0428 5.06476 15.7115 6.02205C16.4331 5.09583 17.134 4.359 17.7682 3.94323C18.7242 3.31737 19.6794 3 20.6081 3ZM20.6081 5.95917C20.2427 5.95917 19.7963 6.1197 19.3039 6.44225C17.7754 7.44319 14.8258 12.6772 13.7458 14.7131C13.3839 15.3952 12.7655 15.6837 12.2086 15.6837C11.1036 15.6837 10.2408 14.5497 12.1076 13.1085C14.9146 10.9402 13.9299 7.39584 12.5898 7.1776C12.5311 7.16799 12.4731 7.16355 12.4172 7.16355C11.1989 7.16355 10.6615 9.33114 10.6615 9.33114C10.6615 9.33114 9.0863 13.4148 6.38031 16.206C3.67434 18.998 3.5346 21.2388 5.50675 24.2246C6.85185 26.2606 9.42666 26.8753 12.0653 26.8753C14.8021 26.8753 17.6077 26.2139 19.1799 25.793C19.2574 25.7723 28.8193 22.984 27.6081 20.6107C27.4046 20.212 27.0693 20.0522 26.6471 20.0522C24.9416 20.0522 21.8393 22.6726 20.5057 22.6726C20.2076 22.6726 19.9976 22.5416 19.9116 22.222C19.3433 20.1173 28.552 19.2325 27.7758 16.1839C27.639 15.6445 27.2677 15.4256 26.746 15.4263C24.4923 15.4263 19.4358 19.5181 18.3759 19.5181C18.2949 19.5181 18.2368 19.4937 18.2053 19.4419C17.6743 18.557 17.9653 17.9394 21.7082 15.6009C25.4511 13.2617 28.0783 11.8545 26.5841 10.1752C26.4121 9.98141 26.1684 9.8956 25.8725 9.8956C23.6001 9.89634 18.2311 14.9403 18.2311 14.9403C18.2311 14.9403 16.7821 16.496 15.9057 16.496C15.7043 16.496 15.533 16.4139 15.4169 16.2112C14.7956 15.1296 21.1879 10.1286 21.5484 8.06535C21.7928 6.66715 21.3771 5.95917 20.6081 5.95917Z" fill="#FF9D00"></path><path d="M5.50686 24.2246C3.53472 21.2387 3.67446 18.9979 6.38043 16.206C9.08641 13.4147 10.6615 9.33111 10.6615 9.33111C10.6615 9.33111 11.2499 6.95933 12.59 7.17757C13.93 7.39581 14.9139 10.9401 12.1069 13.1084C9.29997 15.276 12.6659 16.7489 13.7459 14.713C14.8258 12.6772 17.7747 7.44316 19.304 6.44221C20.8326 5.44128 21.9089 6.00204 21.5484 8.06532C21.188 10.1286 14.795 15.1295 15.4171 16.2118C16.0391 17.2934 18.2312 14.9402 18.2312 14.9402C18.2312 14.9402 25.0907 8.49588 26.5842 10.1752C28.0776 11.8545 25.4512 13.2616 21.7082 15.6008C17.9646 17.9393 17.6744 18.557 18.2054 19.4418C18.7372 20.3266 26.9998 13.1351 27.7759 16.1838C28.5513 19.2324 19.3434 20.1173 19.9117 22.2219C20.48 24.3274 26.3979 18.2382 27.6082 20.6107C28.8193 22.9839 19.2574 25.7722 19.18 25.7929C16.0914 26.62 8.24723 28.3726 5.50686 24.2246Z" fill="#FFD21E"></path></svg>
	Community
	<div class="ml-1.5 flex h-4 min-w-[1rem] items-center justify-center rounded px-1 text-xs leading-none shadow-sm bg-black text-white dark:bg-gray-800 dark:text-gray-200">16</div>

	
		</a></div>
	
			


<div class="relative mb-1.5 flex flex-wrap gap-1.5 sm:flex-nowrap lg:mb-0"><div class="order-last sm:order-first"><div class="relative ">
	<button class="btn px-1.5 py-1.5 " type="button">
		
			<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" class="p-0.5" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><circle cx="16" cy="7" r="3" fill="currentColor"></circle><circle cx="16" cy="16" r="3" fill="currentColor"></circle><circle cx="16" cy="25" r="3" fill="currentColor"></circle></svg>
		
		</button>
	
	
	</div></div>














	<div class="flex-none w-full sm:w-auto"><div class="relative ">
	<button class="text-sm btn btn w-full cursor-pointer text-sm" type="button">
		<svg class="mr-1.5 " xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M12.1 2a9.8 9.8 0 0 0-5.4 1.6l6.4 6.4a2.1 2.1 0 0 1 .2 3a2.1 2.1 0 0 1-3-.2L3.7 6.4A9.84 9.84 0 0 0 2 12.1a10.14 10.14 0 0 0 10.1 10.1a10.9 10.9 0 0 0 2.6-.3l6.7 6.7a5 5 0 0 0 7.1-7.1l-6.7-6.7a10.9 10.9 0 0 0 .3-2.6A10 10 0 0 0 12.1 2zm8 10.1a7.61 7.61 0 0 1-.3 2.1l-.3 1.1l.8.8l6.7 6.7a2.88 2.88 0 0 1 .9 2.1A2.72 2.72 0 0 1 27 27a2.9 2.9 0 0 1-4.2 0l-6.7-6.7l-.8-.8l-1.1.3a7.61 7.61 0 0 1-2.1.3a8.27 8.27 0 0 1-5.7-2.3A7.63 7.63 0 0 1 4 12.1a8.33 8.33 0 0 1 .3-2.2l4.4 4.4a4.14 4.14 0 0 0 5.9.2a4.14 4.14 0 0 0-.2-5.9L10 4.2a6.45 6.45 0 0 1 2-.3a8.27 8.27 0 0 1 5.7 2.3a8.49 8.49 0 0 1 2.4 5.9z" fill="currentColor"></path></svg>
			Train
		<svg class="-mr-1 text-gray-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M16.293 9.293L12 13.586L7.707 9.293l-1.414 1.414L12 16.414l5.707-5.707z" fill="currentColor"></path></svg></button>
	
	
	</div>
		


		

</div>
		<div class="flex-none w-full sm:w-auto"><div class="relative ">
	<button class="text-sm btn btn w-full cursor-pointer text-sm" type="button">
		<svg class="mr-1.5 " xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" fill="currentColor" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><rect x="6.34" y="19" width="11.31" height="2" transform="translate(-10.63 14.34) rotate(-45)"></rect><path d="M17,30a1,1,0,0,1-.37-.07,1,1,0,0,1-.62-.79l-1-7,2-.28.75,5.27L21,24.52V17a1,1,0,0,1,.29-.71l4.07-4.07A8.94,8.94,0,0,0,28,5.86V4H26.14a8.94,8.94,0,0,0-6.36,2.64l-4.07,4.07A1,1,0,0,1,15,11H7.48L4.87,14.26l5.27.75-.28,2-7-1a1,1,0,0,1-.79-.62,1,1,0,0,1,.15-1l4-5A1,1,0,0,1,7,9h7.59l3.77-3.78A10.92,10.92,0,0,1,26.14,2H28a2,2,0,0,1,2,2V5.86a10.92,10.92,0,0,1-3.22,7.78L23,17.41V25a1,1,0,0,1-.38.78l-5,4A1,1,0,0,1,17,30Z"></path></svg>
			Deploy
		<svg class="-mr-1 text-gray-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M16.293 9.293L12 13.586L7.707 9.293l-1.414 1.414L12 16.414l5.707-5.707z" fill="currentColor"></path></svg></button>
	
	
	</div>

		





		



		


		



		

</div>
		

<div class="relative flex-auto sm:flex-none">
	<button class="from-gray-800! to-black! text-white! gap-1! border-gray-800! dark:border-gray-900!  btn w-full cursor-pointer text-sm" type="button">
		<svg class="mr-1.5 mr-0.5! " xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path fill="currentColor" d="M28 4H4a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h8v4H8v2h16v-2h-4v-4h8a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2ZM18 28h-4v-4h4Zm10-6H4V6h24Z"></path></svg>
			Use this model
		<svg class="-mr-1 text-gray-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M16.293 9.293L12 13.586L7.707 9.293l-1.414 1.414L12 16.414l5.707-5.707z" fill="currentColor"></path></svg></button>
	
	
	</div>

</div>
	</div></div></header>


</div>
	
<div class="container relative flex flex-col md:grid md:space-y-0 w-full md:grid-cols-12  space-y-4 md:gap-6 mb-16"><section class="pt-8 border-gray-100 col-span-full"><div class="SVELTE_HYDRATER contents" data-target="ViewerHeader" data-props="{&quot;context&quot;:{&quot;repo&quot;:{&quot;name&quot;:&quot;Qwen/Qwen3-Coder-30B-A3B-Instruct&quot;,&quot;type&quot;:&quot;model&quot;},&quot;rev&quot;:&quot;main&quot;,&quot;path&quot;:&quot;qwen3coder_tool_parser.py&quot;,&quot;subpaths&quot;:[{&quot;dir&quot;:&quot;qwen3coder_tool_parser.py&quot;}]},&quot;refs&quot;:{&quot;branches&quot;:[{&quot;name&quot;:&quot;main&quot;,&quot;ref&quot;:&quot;refs/heads/main&quot;,&quot;targetCommit&quot;:&quot;8110d98ad896c995124f3bc44b2f8dd695a4d252&quot;}],&quot;tags&quot;:[],&quot;converts&quot;:[]},&quot;view&quot;:&quot;blob&quot;}"><header class="flex flex-wrap items-center justify-start pb-2 md:justify-end lg:flex-nowrap"><div class="grow max-md:flex max-md:w-full max-md:items-start max-md:justify-between"><div class="relative mr-4 flex min-w-0 basis-auto flex-wrap items-center md:grow md:basis-full lg:basis-auto lg:flex-nowrap"><div class="relative mr-3 mb-2">
	<button class="text-sm md:text-base btn w-full cursor-pointer text-sm" type="button">
		<svg class="mr-1.5 text-gray-700 dark:text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24" style="transform: rotate(360deg);"><path d="M13 14c-3.36 0-4.46 1.35-4.82 2.24C9.25 16.7 10 17.76 10 19a3 3 0 0 1-3 3a3 3 0 0 1-3-3c0-1.31.83-2.42 2-2.83V7.83A2.99 2.99 0 0 1 4 5a3 3 0 0 1 3-3a3 3 0 0 1 3 3c0 1.31-.83 2.42-2 2.83v5.29c.88-.65 2.16-1.12 4-1.12c2.67 0 3.56-1.34 3.85-2.23A3.006 3.006 0 0 1 14 7a3 3 0 0 1 3-3a3 3 0 0 1 3 3c0 1.34-.88 2.5-2.09 2.86C17.65 11.29 16.68 14 13 14m-6 4a1 1 0 0 0-1 1a1 1 0 0 0 1 1a1 1 0 0 0 1-1a1 1 0 0 0-1-1M7 4a1 1 0 0 0-1 1a1 1 0 0 0 1 1a1 1 0 0 0 1-1a1 1 0 0 0-1-1m10 2a1 1 0 0 0-1 1a1 1 0 0 0 1 1a1 1 0 0 0 1-1a1 1 0 0 0-1-1z" fill="currentColor"></path></svg>
			main
		<svg class="-mr-1 text-gray-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M16.293 9.293L12 13.586L7.707 9.293l-1.414 1.414L12 16.414l5.707-5.707z" fill="currentColor"></path></svg></button>
	
	
	</div>
			<div class="relative mb-2 flex flex-wrap items-center"><a class="truncate text-gray-800 hover:underline" href="/Qwen/Qwen3-Coder-30B-A3B-Instruct/tree/main">Qwen3-Coder-30B-A3B-Instruct</a>
				<span class="mx-1 text-gray-300">/</span>
					<span class="dark:text-gray-300">qwen3coder_tool_parser.py</span>
					<button class="text-xs ml-2 focus:outline-hidden inline-flex cursor-pointer items-center text-sm  mx-0.5   text-gray-600 " title="Copy path" type="button"><svg class="" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" fill="currentColor" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M28,10V28H10V10H28m0-2H10a2,2,0,0,0-2,2V28a2,2,0,0,0,2,2H28a2,2,0,0,0,2-2V10a2,2,0,0,0-2-2Z" transform="translate(0)"></path><path d="M4,18H2V4A2,2,0,0,1,4,2H18V4H4Z" transform="translate(0)"></path><rect fill="none" width="32" height="32"></rect></svg>
		</button></div></div>
		</div>
	
	</header></div>
			<div class="SVELTE_HYDRATER contents" data-target="LastCommit" data-props="{&quot;commitLast&quot;:{&quot;date&quot;:&quot;2025-07-31T07:17:24.000Z&quot;,&quot;verified&quot;:&quot;verified&quot;,&quot;subject&quot;:&quot;Upload folder using huggingface_hub&quot;,&quot;authors&quot;:[{&quot;_id&quot;:&quot;62430a8522549d0917bfeb5a&quot;,&quot;avatar&quot;:&quot;https://cdn-avatars.huggingface.co/v1/production/uploads/62430a8522549d0917bfeb5a/l8jr2cvCp9YBK41XaV27R.jpeg&quot;,&quot;isHf&quot;:false,&quot;user&quot;:&quot;littlebird13&quot;}],&quot;commit&quot;:{&quot;id&quot;:&quot;703eb35446d63a053064b2812c37c385b41f269f&quot;,&quot;parentIds&quot;:[&quot;87fefa3b0acba13e79fe3481ed808601c4e87e80&quot;]},&quot;title&quot;:&quot;Upload folder using huggingface_hub&quot;},&quot;repo&quot;:{&quot;name&quot;:&quot;Qwen/Qwen3-Coder-30B-A3B-Instruct&quot;,&quot;type&quot;:&quot;model&quot;}}"><div class="from-gray-100-to-white bg-linear-to-t flex flex-wrap items-baseline gap-y-1 rounded-t-lg border border-b-0 px-3 py-2 dark:border-gray-800"><img class="mr-2.5 mt-0.5 h-4 w-4 self-center rounded-full" alt="littlebird13's picture" src="https://cdn-avatars.huggingface.co/v1/production/uploads/62430a8522549d0917bfeb5a/l8jr2cvCp9YBK41XaV27R.jpeg">
			<div class="mr-4 flex flex-none items-center truncate"><a class="hover:underline" href="/littlebird13">littlebird13
					</a>
				
			</div>
		<div class="mr-4 truncate font-mono text-xs text-gray-500 hover:prose-a:underline sm:text-sm"><!-- HTML_TAG_START -->Upload folder using huggingface_hub<!-- HTML_TAG_END --></div>
		<a class="rounded-sm border bg-gray-50 px-1.5 text-sm hover:underline dark:border-gray-800 dark:bg-gray-900" href="/Qwen/Qwen3-Coder-30B-A3B-Instruct/commit/703eb35446d63a053064b2812c37c385b41f269f">703eb35</a>
		<span class="mx-2 text-green-500 dark:text-green-600 px-1.5 border-green-100 dark:border-green-800 rounded-full border text-xs uppercase" title="This commit is signed and the signature is verified">verified</span>
		<time class="ml-auto hidden flex-none truncate pl-2 text-gray-500 dark:text-gray-400 lg:block" datetime="2025-07-31T07:17:24" title="Thu, 31 Jul 2025 07:17:24 GMT">18 days ago</time></div></div>
			<div class="relative flex flex-wrap items-center border px-3 py-1.5 text-sm text-gray-800 dark:border-gray-800 dark:bg-gray-900 ">
				<a class="my-1 mr-4 flex items-center hover:underline " href="/Qwen/Qwen3-Coder-30B-A3B-Instruct/raw/main/qwen3coder_tool_parser.py"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" style="transform: rotate(360deg);"><path d="M31 16l-7 7l-1.41-1.41L28.17 16l-5.58-5.59L24 9l7 7z" fill="currentColor"></path><path d="M1 16l7-7l1.41 1.41L3.83 16l5.58 5.59L8 23l-7-7z" fill="currentColor"></path><path d="M12.419 25.484L17.639 6l1.932.518L14.35 26z" fill="currentColor"></path></svg>
							raw
						</a><div class="SVELTE_HYDRATER contents" data-target="CopyButton" data-props="{&quot;value&quot;:&quot;https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct/resolve/main/qwen3coder_tool_parser.py&quot;,&quot;style&quot;:&quot;blank&quot;,&quot;label&quot;:&quot;Copy download link&quot;,&quot;classNames&quot;:&quot;my-1 mr-4 flex items-center no-underline hover:underline&quot;}"><button class="my-1 mr-4 flex items-center no-underline hover:underline       " title="Copy download link" type="button"><svg class="" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" fill="currentColor" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M28,10V28H10V10H28m0-2H10a2,2,0,0,0-2,2V28a2,2,0,0,0,2,2H28a2,2,0,0,0,2-2V10a2,2,0,0,0-2-2Z" transform="translate(0)"></path><path d="M4,18H2V4A2,2,0,0,1,4,2H18V4H4Z" transform="translate(0)"></path><rect fill="none" width="32" height="32"></rect></svg>
		<span class="ml-1.5 ">Copy download link</span></button></div><a class="my-1 mr-4 flex items-center hover:underline " href="/Qwen/Qwen3-Coder-30B-A3B-Instruct/commits/main/qwen3coder_tool_parser.py"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" style="transform: rotate(360deg);"><path d="M16 4C9.383 4 4 9.383 4 16s5.383 12 12 12s12-5.383 12-12S22.617 4 16 4zm0 2c5.535 0 10 4.465 10 10s-4.465 10-10 10S6 21.535 6 16S10.465 6 16 6zm-1 2v9h7v-2h-5V8z" fill="currentColor"></path></svg>
							history
						</a><a class="my-1 mr-4 flex items-center hover:underline " href="/Qwen/Qwen3-Coder-30B-A3B-Instruct/blame/main/qwen3coder_tool_parser.py"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" style="transform: rotate(360deg);"><path d="M16 2a14 14 0 1 0 14 14A14 14 0 0 0 16 2zm0 26a12 12 0 1 1 12-12a12 12 0 0 1-12 12z" fill="currentColor"></path><path d="M11.5 11a2.5 2.5 0 1 0 2.5 2.5a2.48 2.48 0 0 0-2.5-2.5z" fill="currentColor"></path><path d="M20.5 11a2.5 2.5 0 1 0 2.5 2.5a2.48 2.48 0 0 0-2.5-2.5z" fill="currentColor"></path></svg>
							blame
						</a><a class="my-1 mr-4 flex items-center hover:underline text-green-600 dark:text-green-500" href="/Qwen/Qwen3-Coder-30B-A3B-Instruct/edit/main/qwen3coder_tool_parser.py"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M2 26h28v2H2z" fill="currentColor"></path><path d="M25.4 9c.8-.8.8-2 0-2.8l-3.6-3.6c-.8-.8-2-.8-2.8 0l-15 15V24h6.4l15-15zm-5-5L24 7.6l-3 3L17.4 7l3-3zM6 22v-3.6l10-10l3.6 3.6l-10 10H6z" fill="currentColor"></path></svg>
							contribute
						</a><a class="my-1 mr-4 flex items-center hover:underline " href="/Qwen/Qwen3-Coder-30B-A3B-Instruct/delete/main/qwen3coder_tool_parser.py"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M12 12h2v12h-2z" fill="currentColor"></path><path d="M18 12h2v12h-2z" fill="currentColor"></path><path d="M4 6v2h2v20a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8h2V6zm4 22V8h16v20z" fill="currentColor"></path><path d="M12 2h8v2h-8z" fill="currentColor"></path></svg>
							delete
						</a>

				<div class="mr-4 flex items-center"><div class="SVELTE_HYDRATER contents" data-target="ScanStatusBadge" data-props="{&quot;classNames&quot;:&quot;mr-2&quot;,&quot;scanStatus&quot;:{&quot;status&quot;:&quot;safe&quot;,&quot;protectAiScan&quot;:{&quot;status&quot;:&quot;unscanned&quot;,&quot;message&quot;:null,&quot;reportLink&quot;:&quot;https://protectai.com/insights/models/Qwen/Qwen3-Coder-30B-A3B-Instruct/8110d98ad896c995124f3bc44b2f8dd695a4d252/files?blob-id=774f4bbf588d764cd190b4b0ca339b7eefb0daa2&amp;utm_source=huggingface&quot;},&quot;avScan&quot;:{&quot;status&quot;:&quot;safe&quot;,&quot;version&quot;:&quot;1.4.3/27734&quot;},&quot;pickleImportScan&quot;:{&quot;status&quot;:&quot;unscanned&quot;,&quot;pickleImports&quot;:[],&quot;version&quot;:&quot;0.0.0&quot;},&quot;jFrogScan&quot;:{&quot;status&quot;:&quot;unscanned&quot;,&quot;message&quot;:&quot;Not a machine-learning model&quot;,&quot;reportLink&quot;:&quot;&quot;,&quot;reportLabel&quot;:&quot;&quot;}},&quot;repo&quot;:{&quot;name&quot;:&quot;Qwen/Qwen3-Coder-30B-A3B-Instruct&quot;,&quot;type&quot;:&quot;model&quot;},&quot;revision&quot;:&quot;main&quot;,&quot;filePath&quot;:&quot;qwen3coder_tool_parser.py&quot;,&quot;openByDefault&quot;:false}"><div class="sm:relative mr-2"><button class="flex h-[1.125rem] select-none items-center gap-0.5 rounded border pl-0.5 pr-0.5 text-xs leading-tight text-gray-400 hover:cursor-pointer text-gray-400 hover:border-gray-200 hover:bg-gray-50 hover:text-gray-500 dark:border-gray-800 dark:hover:bg-gray-800 dark:hover:text-gray-200 "><svg class="flex-none" width="1em" height="1em" viewBox="0 0 22 28" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M15.3634 10.3639C15.8486 10.8491 15.8486 11.6357 15.3634 12.1209L10.9292 16.5551C10.6058 16.8785 10.0814 16.8785 9.7579 16.5551L7.03051 13.8277C6.54532 13.3425 6.54532 12.5558 7.03051 12.0707C7.51569 11.5855 8.30234 11.5855 8.78752 12.0707L9.7579 13.041C10.0814 13.3645 10.6058 13.3645 10.9292 13.041L13.6064 10.3639C14.0916 9.8787 14.8782 9.8787 15.3634 10.3639Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M10.6666 27.12C4.93329 25.28 0 19.2267 0 12.7867V6.52001C0 5.40001 0.693334 4.41334 1.73333 4.01334L9.73333 1.01334C10.3333 0.786673 11 0.786673 11.6 1.02667L19.6 4.02667C20.1083 4.21658 20.5465 4.55701 20.8562 5.00252C21.1659 5.44803 21.3324 5.97742 21.3333 6.52001V12.7867C21.3333 19.24 16.4 25.28 10.6666 27.12Z" fill="currentColor" fill-opacity="0.22"></path><path d="M10.0845 1.94967L10.0867 1.94881C10.4587 1.8083 10.8666 1.81036 11.2286 1.95515L11.2387 1.95919L11.2489 1.963L19.2489 4.963L19.25 4.96342C19.5677 5.08211 19.8416 5.29488 20.0351 5.57333C20.2285 5.85151 20.3326 6.18203 20.3333 6.52082C20.3333 6.52113 20.3333 6.52144 20.3333 6.52176L20.3333 12.7867C20.3333 18.6535 15.8922 24.2319 10.6666 26.0652C5.44153 24.2316 1 18.6409 1 12.7867V6.52001C1 5.82357 1.42893 5.20343 2.08883 4.94803L10.0845 1.94967Z" stroke="currentColor" stroke-opacity="0.30" stroke-width="2"></path></svg>

			<span class="mr-0.5 max-sm:hidden">Safe</span></button>

	</div></div>
						</div>

				<div class="flex items-center gap-x-3 dark:text-gray-300 sm:ml-auto"><div class="SVELTE_HYDRATER contents" data-target="LineWrapButton" data-props="{&quot;classNames&quot;:&quot;text-xs&quot;,&quot;lineSelectorClass&quot;:&quot;blob-line&quot;}">

<button class="text-xs focus:outline-hidden inline-flex cursor-pointer items-center justify-center text-sm  mx-0.5  " type="button"><svg class="opacity-40" width="1em" height="1em" viewBox="0 0 12 11" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M0.75 1.25H11.25M0.75 5H9C9.75 5 11.25 5.375 11.25 6.875C11.25 8.375 9.99975 8.75 9.375 8.75H6M6 8.75L7.5 7.25M6 8.75L7.5 10.25M0.75 8.75H3.75" stroke="currentColor" stroke-width="1.125" stroke-linecap="round" stroke-linejoin="round"></path></svg></button></div>
					28.9 kB</div></div>

			<div class="relative min-h-[100px] overflow-hidden rounded-b-lg border border-t-0 leading-tight dark:border-gray-800 dark:bg-gray-925">
				<div class="py-3"><div class="SVELTE_HYDRATER contents" data-target="BlobContent" data-props="{&quot;lines&quot;:[&quot;<span class=\&quot;hljs-comment\&quot;># SPDX-License-Identifier: Apache-2.0</span>&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>import</span> json&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>import</span> re&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>import</span> uuid&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>from</span> collections.abc <span class=\&quot;hljs-keyword\&quot;>import</span> <span class=\&quot;hljs-type\&quot;>Sequence</span>&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>from</span> typing <span class=\&quot;hljs-keyword\&quot;>import</span> <span class=\&quot;hljs-type\&quot;>Union</span>, <span class=\&quot;hljs-type\&quot;>Optional</span>, <span class=\&quot;hljs-type\&quot;>Any</span>, <span class=\&quot;hljs-type\&quot;>List</span>, <span class=\&quot;hljs-type\&quot;>Dict</span>&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>from</span> enum <span class=\&quot;hljs-keyword\&quot;>import</span> Enum&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>from</span> vllm.entrypoints.openai.protocol <span class=\&quot;hljs-keyword\&quot;>import</span> (&quot;,&quot;    ChatCompletionRequest,&quot;,&quot;    ChatCompletionToolsParam,&quot;,&quot;    DeltaMessage,&quot;,&quot;    DeltaToolCall,&quot;,&quot;    DeltaFunctionCall,&quot;,&quot;    ExtractedToolCallInformation,&quot;,&quot;    FunctionCall,&quot;,&quot;    ToolCall,&quot;,&quot;)&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>from</span> vllm.entrypoints.openai.tool_parsers.abstract_tool_parser <span class=\&quot;hljs-keyword\&quot;>import</span> (&quot;,&quot;    ToolParser,&quot;,&quot;    ToolParserManager,&quot;,&quot;)&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>from</span> vllm.logger <span class=\&quot;hljs-keyword\&quot;>import</span> init_logger&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>from</span> vllm.transformers_utils.tokenizer <span class=\&quot;hljs-keyword\&quot;>import</span> AnyTokenizer&quot;,&quot;&quot;,&quot;logger = init_logger(__name__)&quot;,&quot;&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-meta\&quot;>@ToolParserManager.register_module(<span class=\&quot;hljs-params\&quot;><span class=\&quot;hljs-string\&quot;>&amp;quot;qwen3_xml&amp;quot;</span></span>)</span>&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>class</span> <span class=\&quot;hljs-title class_\&quot;>Qwen3XMLToolParser</span>(<span class=\&quot;hljs-title class_ inherited__\&quot;>ToolParser</span>):&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>__init__</span>(<span class=\&quot;hljs-params\&quot;>self, tokenizer: AnyTokenizer</span>):&quot;,&quot;        <span class=\&quot;hljs-built_in\&quot;>super</span>().__init__(tokenizer)&quot;,&quot;&quot;,&quot;        self.current_tool_name_sent: <span class=\&quot;hljs-built_in\&quot;>bool</span> = <span class=\&quot;hljs-literal\&quot;>False</span>&quot;,&quot;        self.prev_tool_call_arr: <span class=\&quot;hljs-built_in\&quot;>list</span>[<span class=\&quot;hljs-built_in\&quot;>dict</span>] = []&quot;,&quot;        self.current_tool_id: <span class=\&quot;hljs-built_in\&quot;>int</span> = -<span class=\&quot;hljs-number\&quot;>1</span>&quot;,&quot;        self.streamed_args_for_tool: <span class=\&quot;hljs-built_in\&quot;>list</span>[<span class=\&quot;hljs-built_in\&quot;>str</span>] = []&quot;,&quot;&quot;,&quot;        <span class=\&quot;hljs-comment\&quot;># Sentinel tokens for streaming mode</span>&quot;,&quot;        self.tool_call_start_token: <span class=\&quot;hljs-built_in\&quot;>str</span> = <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;lt;tool_call&amp;gt;&amp;quot;</span>&quot;,&quot;        self.tool_call_end_token: <span class=\&quot;hljs-built_in\&quot;>str</span> = <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;lt;/tool_call&amp;gt;&amp;quot;</span>&quot;,&quot;        self.tool_call_prefix: <span class=\&quot;hljs-built_in\&quot;>str</span> = <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;lt;function=&amp;quot;</span>&quot;,&quot;        self.function_end_token: <span class=\&quot;hljs-built_in\&quot;>str</span> = <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;lt;/function&amp;gt;&amp;quot;</span>&quot;,&quot;        self.parameter_prefix: <span class=\&quot;hljs-built_in\&quot;>str</span> = <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;lt;parameter=&amp;quot;</span>&quot;,&quot;        self.parameter_end_token: <span class=\&quot;hljs-built_in\&quot;>str</span> = <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;lt;/parameter&amp;gt;&amp;quot;</span>&quot;,&quot;        self.is_tool_call_started: <span class=\&quot;hljs-built_in\&quot;>bool</span> = <span class=\&quot;hljs-literal\&quot;>False</span>&quot;,&quot;        self.failed_count: <span class=\&quot;hljs-built_in\&quot;>int</span> = <span class=\&quot;hljs-number\&quot;>0</span>&quot;,&quot;&quot;,&quot;        <span class=\&quot;hljs-comment\&quot;># Enhanced streaming state - reset for each new message</span>&quot;,&quot;        self._reset_streaming_state()&quot;,&quot;&quot;,&quot;        <span class=\&quot;hljs-comment\&quot;># Regex patterns</span>&quot;,&quot;        self.tool_call_complete_regex = re.<span class=\&quot;hljs-built_in\&quot;>compile</span>(&quot;,&quot;            <span class=\&quot;hljs-string\&quot;>r&amp;quot;&amp;lt;tool_call&amp;gt;(.*?)&amp;lt;/tool_call&amp;gt;&amp;quot;</span>, re.DOTALL&quot;,&quot;        )&quot;,&quot;        self.tool_call_regex = re.<span class=\&quot;hljs-built_in\&quot;>compile</span>(&quot;,&quot;            <span class=\&quot;hljs-string\&quot;>r&amp;quot;&amp;lt;tool_call&amp;gt;(.*?)&amp;lt;/tool_call&amp;gt;|&amp;lt;tool_call&amp;gt;(.*?)$&amp;quot;</span>, re.DOTALL&quot;,&quot;        )&quot;,&quot;        self.tool_call_function_regex = re.<span class=\&quot;hljs-built_in\&quot;>compile</span>(&quot;,&quot;            <span class=\&quot;hljs-string\&quot;>r&amp;quot;&amp;lt;function=(.*?)&amp;lt;/function&amp;gt;|&amp;lt;function=(.*)$&amp;quot;</span>, re.DOTALL&quot;,&quot;        )&quot;,&quot;        self.tool_call_parameter_regex = re.<span class=\&quot;hljs-built_in\&quot;>compile</span>(&quot;,&quot;            <span class=\&quot;hljs-string\&quot;>r&amp;quot;&amp;lt;parameter=(.*?)&amp;lt;/parameter&amp;gt;|&amp;lt;parameter=(.*?)$&amp;quot;</span>, re.DOTALL&quot;,&quot;        )&quot;,&quot;&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>if</span> <span class=\&quot;hljs-keyword\&quot;>not</span> self.model_tokenizer:&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>raise</span> ValueError(&quot;,&quot;                <span class=\&quot;hljs-string\&quot;>&amp;quot;The model tokenizer must be passed to the ToolParser &amp;quot;</span>&quot;,&quot;                <span class=\&quot;hljs-string\&quot;>&amp;quot;constructor during construction.&amp;quot;</span>&quot;,&quot;            )&quot;,&quot;&quot;,&quot;        self.tool_call_start_token_id = self.vocab.get(self.tool_call_start_token)&quot;,&quot;        self.tool_call_end_token_id = self.vocab.get(self.tool_call_end_token)&quot;,&quot;&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>if</span> self.tool_call_start_token_id <span class=\&quot;hljs-keyword\&quot;>is</span> <span class=\&quot;hljs-literal\&quot;>None</span> <span class=\&quot;hljs-keyword\&quot;>or</span> self.tool_call_end_token_id <span class=\&quot;hljs-keyword\&quot;>is</span> <span class=\&quot;hljs-literal\&quot;>None</span>:&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>raise</span> RuntimeError(&quot;,&quot;                <span class=\&quot;hljs-string\&quot;>&amp;quot;Qwen3 XML Tool parser could not locate tool call start/end &amp;quot;</span>&quot;,&quot;                <span class=\&quot;hljs-string\&quot;>&amp;quot;tokens in the tokenizer!&amp;quot;</span>&quot;,&quot;            )&quot;,&quot;&quot;,&quot;        logger.info(<span class=\&quot;hljs-string\&quot;>f&amp;quot;vLLM Successfully import tool parser <span class=\&quot;hljs-subst\&quot;>{self.__class__.__name__}</span> !&amp;quot;</span>)&quot;,&quot;&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>_generate_tool_call_id</span>(<span class=\&quot;hljs-params\&quot;>self</span>) -&amp;gt; <span class=\&quot;hljs-built_in\&quot;>str</span>:&quot;,&quot;        <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;&amp;quot;Generate a unique tool call ID.&amp;quot;&amp;quot;&amp;quot;</span>&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>return</span> <span class=\&quot;hljs-string\&quot;>f&amp;quot;call_<span class=\&quot;hljs-subst\&quot;>{uuid.uuid4().<span class=\&quot;hljs-built_in\&quot;>hex</span>[:<span class=\&quot;hljs-number\&quot;>24</span>]}</span>&amp;quot;</span>&quot;,&quot;&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>_reset_streaming_state</span>(<span class=\&quot;hljs-params\&quot;>self</span>):&quot;,&quot;        <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;&amp;quot;Reset all streaming state.&amp;quot;&amp;quot;&amp;quot;</span>&quot;,&quot;        self.current_tool_index = <span class=\&quot;hljs-number\&quot;>0</span>&quot;,&quot;        self.is_tool_call_started = <span class=\&quot;hljs-literal\&quot;>False</span>&quot;,&quot;        self.header_sent = <span class=\&quot;hljs-literal\&quot;>False</span>&quot;,&quot;        self.current_tool_id = <span class=\&quot;hljs-literal\&quot;>None</span>&quot;,&quot;        self.current_function_name = <span class=\&quot;hljs-literal\&quot;>None</span>&quot;,&quot;        self.current_param_name = <span class=\&quot;hljs-literal\&quot;>None</span>&quot;,&quot;        self.current_param_value = <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;</span>&quot;,&quot;        self.param_count = <span class=\&quot;hljs-number\&quot;>0</span>&quot;,&quot;        self.in_param = <span class=\&quot;hljs-literal\&quot;>False</span>&quot;,&quot;        self.in_function = <span class=\&quot;hljs-literal\&quot;>False</span>&quot;,&quot;        self.accumulated_text = <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;</span>&quot;,&quot;        self.json_started = <span class=\&quot;hljs-literal\&quot;>False</span>&quot;,&quot;        self.json_closed = <span class=\&quot;hljs-literal\&quot;>False</span>&quot;,&quot;&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>_parse_xml_function_call</span>(<span class=\&quot;hljs-params\&quot;></span>&quot;,&quot;<span class=\&quot;hljs-params\&quot;>        self, function_call_str: <span class=\&quot;hljs-built_in\&quot;>str</span>, tools: <span class=\&quot;hljs-type\&quot;>Optional</span>[<span class=\&quot;hljs-built_in\&quot;>list</span>[ChatCompletionToolsParam]]</span>&quot;,&quot;<span class=\&quot;hljs-params\&quot;>    </span>) -&amp;gt; <span class=\&quot;hljs-type\&quot;>Optional</span>[ToolCall]:&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>get_arguments_config</span>(<span class=\&quot;hljs-params\&quot;>func_name: <span class=\&quot;hljs-built_in\&quot;>str</span></span>) -&amp;gt; <span class=\&quot;hljs-built_in\&quot;>dict</span>:&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>if</span> tools <span class=\&quot;hljs-keyword\&quot;>is</span> <span class=\&quot;hljs-literal\&quot;>None</span>:&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>return</span> {}&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>for</span> config <span class=\&quot;hljs-keyword\&quot;>in</span> tools:&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>if</span> <span class=\&quot;hljs-keyword\&quot;>not</span> <span class=\&quot;hljs-built_in\&quot;>hasattr</span>(config, <span class=\&quot;hljs-string\&quot;>&amp;quot;type&amp;quot;</span>) <span class=\&quot;hljs-keyword\&quot;>or</span> <span class=\&quot;hljs-keyword\&quot;>not</span> (&quot;,&quot;                    <span class=\&quot;hljs-built_in\&quot;>hasattr</span>(config, <span class=\&quot;hljs-string\&quot;>&amp;quot;function&amp;quot;</span>) <span class=\&quot;hljs-keyword\&quot;>and</span> <span class=\&quot;hljs-built_in\&quot;>hasattr</span>(config.function, <span class=\&quot;hljs-string\&quot;>&amp;quot;name&amp;quot;</span>)&quot;,&quot;                ):&quot;,&quot;                    <span class=\&quot;hljs-keyword\&quot;>continue</span>&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>if</span> config.<span class=\&quot;hljs-built_in\&quot;>type</span> == <span class=\&quot;hljs-string\&quot;>&amp;quot;function&amp;quot;</span> <span class=\&quot;hljs-keyword\&quot;>and</span> config.function.name == func_name:&quot;,&quot;                    <span class=\&quot;hljs-keyword\&quot;>if</span> <span class=\&quot;hljs-keyword\&quot;>not</span> <span class=\&quot;hljs-built_in\&quot;>hasattr</span>(config.function, <span class=\&quot;hljs-string\&quot;>&amp;quot;parameters&amp;quot;</span>):&quot;,&quot;                        <span class=\&quot;hljs-keyword\&quot;>return</span> {}&quot;,&quot;                    params = config.function.parameters&quot;,&quot;                    <span class=\&quot;hljs-keyword\&quot;>if</span> <span class=\&quot;hljs-built_in\&quot;>isinstance</span>(params, <span class=\&quot;hljs-built_in\&quot;>dict</span>) <span class=\&quot;hljs-keyword\&quot;>and</span> <span class=\&quot;hljs-string\&quot;>&amp;quot;properties&amp;quot;</span> <span class=\&quot;hljs-keyword\&quot;>in</span> params:&quot;,&quot;                        <span class=\&quot;hljs-keyword\&quot;>return</span> params[<span class=\&quot;hljs-string\&quot;>&amp;quot;properties&amp;quot;</span>]&quot;,&quot;                    <span class=\&quot;hljs-keyword\&quot;>elif</span> <span class=\&quot;hljs-built_in\&quot;>isinstance</span>(params, <span class=\&quot;hljs-built_in\&quot;>dict</span>):&quot;,&quot;                        <span class=\&quot;hljs-keyword\&quot;>return</span> params&quot;,&quot;                    <span class=\&quot;hljs-keyword\&quot;>else</span>:&quot;,&quot;                        <span class=\&quot;hljs-keyword\&quot;>return</span> {}&quot;,&quot;            logger.warning(<span class=\&quot;hljs-string\&quot;>f&amp;quot;Tool &amp;#x27;<span class=\&quot;hljs-subst\&quot;>{func_name}</span>&amp;#x27; is not defined in the tools list.&amp;quot;</span>)&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>return</span> {}&quot;,&quot;&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>convert_param_value</span>(<span class=\&quot;hljs-params\&quot;></span>&quot;,&quot;<span class=\&quot;hljs-params\&quot;>            param_value: <span class=\&quot;hljs-built_in\&quot;>str</span>, param_name: <span class=\&quot;hljs-built_in\&quot;>str</span>, param_config: <span class=\&quot;hljs-built_in\&quot;>dict</span>, func_name: <span class=\&quot;hljs-built_in\&quot;>str</span></span>&quot;,&quot;<span class=\&quot;hljs-params\&quot;>        </span>) -&amp;gt; <span class=\&quot;hljs-type\&quot;>Any</span>:&quot;,&quot;            <span class=\&quot;hljs-comment\&quot;># Handle null value for any type</span>&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>if</span> param_value.lower() == <span class=\&quot;hljs-string\&quot;>&amp;quot;null&amp;quot;</span>:&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>return</span> <span class=\&quot;hljs-literal\&quot;>None</span>&quot;,&quot;&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>if</span> param_name <span class=\&quot;hljs-keyword\&quot;>not</span> <span class=\&quot;hljs-keyword\&quot;>in</span> param_config:&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>if</span> param_config != {}:&quot;,&quot;                    logger.warning(&quot;,&quot;                        <span class=\&quot;hljs-string\&quot;>f&amp;quot;Parsed parameter &amp;#x27;<span class=\&quot;hljs-subst\&quot;>{param_name}</span>&amp;#x27; is not defined in the tool &amp;quot;</span>&quot;,&quot;                        <span class=\&quot;hljs-string\&quot;>f&amp;quot;parameters for tool &amp;#x27;<span class=\&quot;hljs-subst\&quot;>{func_name}</span>&amp;#x27;, directly returning the string value.&amp;quot;</span>&quot;,&quot;                    )&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>return</span> param_value&quot;,&quot;&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>if</span> (&quot;,&quot;                <span class=\&quot;hljs-built_in\&quot;>isinstance</span>(param_config[param_name], <span class=\&quot;hljs-built_in\&quot;>dict</span>)&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>and</span> <span class=\&quot;hljs-string\&quot;>&amp;quot;type&amp;quot;</span> <span class=\&quot;hljs-keyword\&quot;>in</span> param_config[param_name]&quot;,&quot;            ):&quot;,&quot;                param_type = <span class=\&quot;hljs-built_in\&quot;>str</span>(param_config[param_name][<span class=\&quot;hljs-string\&quot;>&amp;quot;type&amp;quot;</span>]).strip().lower()&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>else</span>:&quot;,&quot;                param_type = <span class=\&quot;hljs-string\&quot;>&amp;quot;string&amp;quot;</span>&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>if</span> param_type <span class=\&quot;hljs-keyword\&quot;>in</span> [<span class=\&quot;hljs-string\&quot;>&amp;quot;string&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;str&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;text&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;varchar&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;char&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;enum&amp;quot;</span>]:&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>return</span> param_value&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>elif</span> (&quot;,&quot;                param_type.startswith(<span class=\&quot;hljs-string\&quot;>&amp;quot;int&amp;quot;</span>)&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>or</span> param_type.startswith(<span class=\&quot;hljs-string\&quot;>&amp;quot;uint&amp;quot;</span>)&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>or</span> param_type.startswith(<span class=\&quot;hljs-string\&quot;>&amp;quot;long&amp;quot;</span>)&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>or</span> param_type.startswith(<span class=\&quot;hljs-string\&quot;>&amp;quot;short&amp;quot;</span>)&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>or</span> param_type.startswith(<span class=\&quot;hljs-string\&quot;>&amp;quot;unsigned&amp;quot;</span>)&quot;,&quot;            ):&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>try</span>:&quot;,&quot;                    param_value = <span class=\&quot;hljs-built_in\&quot;>int</span>(param_value)&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>except</span>:&quot;,&quot;                    logger.warning(&quot;,&quot;                        <span class=\&quot;hljs-string\&quot;>f&amp;quot;Parsed value &amp;#x27;<span class=\&quot;hljs-subst\&quot;>{param_value}</span>&amp;#x27; of parameter &amp;#x27;<span class=\&quot;hljs-subst\&quot;>{param_name}</span>&amp;#x27; is not an integer in tool &amp;quot;</span>&quot;,&quot;                        <span class=\&quot;hljs-string\&quot;>f&amp;quot;&amp;#x27;<span class=\&quot;hljs-subst\&quot;>{func_name}</span>&amp;#x27;, degenerating to string.&amp;quot;</span>&quot;,&quot;                    )&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>return</span> param_value&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>elif</span> param_type.startswith(<span class=\&quot;hljs-string\&quot;>&amp;quot;num&amp;quot;</span>) <span class=\&quot;hljs-keyword\&quot;>or</span> param_type.startswith(<span class=\&quot;hljs-string\&quot;>&amp;quot;float&amp;quot;</span>):&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>try</span>:&quot;,&quot;                    float_param_value = <span class=\&quot;hljs-built_in\&quot;>float</span>(param_value)&quot;,&quot;                    param_value = float_param_value <span class=\&quot;hljs-keyword\&quot;>if</span> float_param_value - <span class=\&quot;hljs-built_in\&quot;>int</span>(float_param_value) != <span class=\&quot;hljs-number\&quot;>0</span> <span class=\&quot;hljs-keyword\&quot;>else</span> <span class=\&quot;hljs-built_in\&quot;>int</span>(float_param_value)&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>except</span>:&quot;,&quot;                    logger.warning(&quot;,&quot;                        <span class=\&quot;hljs-string\&quot;>f&amp;quot;Parsed value &amp;#x27;<span class=\&quot;hljs-subst\&quot;>{param_value}</span>&amp;#x27; of parameter &amp;#x27;<span class=\&quot;hljs-subst\&quot;>{param_name}</span>&amp;#x27; is not a float in tool &amp;quot;</span>&quot;,&quot;                        <span class=\&quot;hljs-string\&quot;>f&amp;quot;&amp;#x27;<span class=\&quot;hljs-subst\&quot;>{func_name}</span>&amp;#x27;, degenerating to string.&amp;quot;</span>&quot;,&quot;                    )&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>return</span> param_value&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>elif</span> param_type <span class=\&quot;hljs-keyword\&quot;>in</span> [<span class=\&quot;hljs-string\&quot;>&amp;quot;boolean&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;bool&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;binary&amp;quot;</span>]:&quot;,&quot;                param_value = param_value.lower()&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>if</span> param_value <span class=\&quot;hljs-keyword\&quot;>not</span> <span class=\&quot;hljs-keyword\&quot;>in</span> [<span class=\&quot;hljs-string\&quot;>&amp;quot;true&amp;quot;</span>, <span class=\&quot;hljs-string\&quot;>&amp;quot;false&amp;quot;</span>]:&quot;,&quot;                    logger.warning(&quot;,&quot;                        <span class=\&quot;hljs-string\&quot;>f&amp;quot;Parsed value &amp;#x27;<span class=\&quot;hljs-subst\&quot;>{param_value}</span>&amp;#x27; of parameter &amp;#x27;<span class=\&quot;hljs-subst\&quot;>{param_name}</span>&amp;#x27; is not a boolean (`true` of `false`) in tool &amp;#x27;<span class=\&quot;hljs-subst\&quot;>{func_name}</span>&amp;#x27;, degenerating to false.&amp;quot;</span>&quot;,&quot;                    )&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>return</span> param_value == <span class=\&quot;hljs-string\&quot;>&amp;quot;true&amp;quot;</span>&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>else</span>:&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>if</span> param_type == <span class=\&quot;hljs-string\&quot;>&amp;quot;object&amp;quot;</span> <span class=\&quot;hljs-keyword\&quot;>or</span> param_type.startswith(<span class=\&quot;hljs-string\&quot;>&amp;quot;dict&amp;quot;</span>):&quot;,&quot;                    <span class=\&quot;hljs-keyword\&quot;>try</span>:&quot;,&quot;                        param_value = json.loads(param_value)&quot;,&quot;                        <span class=\&quot;hljs-keyword\&quot;>return</span> param_value&quot;,&quot;                    <span class=\&quot;hljs-keyword\&quot;>except</span>:&quot;,&quot;                        logger.warning(&quot;,&quot;                            <span class=\&quot;hljs-string\&quot;>f&amp;quot;Parsed value &amp;#x27;<span class=\&quot;hljs-subst\&quot;>{param_value}</span>&amp;#x27; of parameter &amp;#x27;<span class=\&quot;hljs-subst\&quot;>{param_name}</span>&amp;#x27; is not a valid JSON object in tool &amp;quot;</span>&quot;,&quot;                            <span class=\&quot;hljs-string\&quot;>f&amp;quot;&amp;#x27;<span class=\&quot;hljs-subst\&quot;>{func_name}</span>&amp;#x27;, will try other methods to parse it.&amp;quot;</span>&quot;,&quot;                        )&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>try</span>:&quot;,&quot;                    param_value = <span class=\&quot;hljs-built_in\&quot;>eval</span>(param_value)&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>except</span>:&quot;,&quot;                    logger.warning(&quot;,&quot;                        <span class=\&quot;hljs-string\&quot;>f&amp;quot;Parsed value &amp;#x27;<span class=\&quot;hljs-subst\&quot;>{param_value}</span>&amp;#x27; of parameter &amp;#x27;<span class=\&quot;hljs-subst\&quot;>{param_name}</span>&amp;#x27; cannot be converted via Python `eval()` in tool &amp;#x27;<span class=\&quot;hljs-subst\&quot;>{func_name}</span>&amp;#x27;, degenerating to string.&amp;quot;</span>&quot;,&quot;                    )&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>return</span> param_value&quot;,&quot;&quot;,&quot;        <span class=\&quot;hljs-comment\&quot;># Extract function name</span>&quot;,&quot;        end_index = function_call_str.index(<span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;gt;&amp;quot;</span>)&quot;,&quot;        function_name = function_call_str[:end_index]&quot;,&quot;        param_config = get_arguments_config(function_name)&quot;,&quot;        parameters = function_call_str[end_index + <span class=\&quot;hljs-number\&quot;>1</span> :]&quot;,&quot;        param_dict = {}&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>for</span> <span class=\&quot;hljs-keyword\&quot;>match</span> <span class=\&quot;hljs-keyword\&quot;>in</span> self.tool_call_parameter_regex.findall(parameters):&quot;,&quot;            match_text = <span class=\&quot;hljs-keyword\&quot;>match</span>[<span class=\&quot;hljs-number\&quot;>0</span>] <span class=\&quot;hljs-keyword\&quot;>if</span> <span class=\&quot;hljs-keyword\&quot;>match</span>[<span class=\&quot;hljs-number\&quot;>0</span>] <span class=\&quot;hljs-keyword\&quot;>else</span> <span class=\&quot;hljs-keyword\&quot;>match</span>[<span class=\&quot;hljs-number\&quot;>1</span>]&quot;,&quot;            idx = match_text.index(<span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;gt;&amp;quot;</span>)&quot;,&quot;            param_name = match_text[:idx]&quot;,&quot;            param_value = <span class=\&quot;hljs-built_in\&quot;>str</span>(match_text[idx + <span class=\&quot;hljs-number\&quot;>1</span> :])&quot;,&quot;            <span class=\&quot;hljs-comment\&quot;># Remove prefix and trailing \\n</span>&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>if</span> param_value.startswith(<span class=\&quot;hljs-string\&quot;>&amp;quot;\\n&amp;quot;</span>):&quot;,&quot;                param_value = param_value[<span class=\&quot;hljs-number\&quot;>1</span>:]&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>if</span> param_value.endswith(<span class=\&quot;hljs-string\&quot;>&amp;quot;\\n&amp;quot;</span>):&quot;,&quot;                param_value = param_value[:-<span class=\&quot;hljs-number\&quot;>1</span>]&quot;,&quot;&quot;,&quot;            param_dict[param_name] = convert_param_value(&quot;,&quot;                param_value, param_name, param_config, function_name&quot;,&quot;            )&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>return</span> ToolCall(&quot;,&quot;            <span class=\&quot;hljs-built_in\&quot;>type</span>=<span class=\&quot;hljs-string\&quot;>&amp;quot;function&amp;quot;</span>,&quot;,&quot;            function=FunctionCall(&quot;,&quot;                name=function_name, arguments=json.dumps(param_dict, ensure_ascii=<span class=\&quot;hljs-literal\&quot;>False</span>)&quot;,&quot;            ),&quot;,&quot;        )&quot;,&quot;&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>_get_function_calls</span>(<span class=\&quot;hljs-params\&quot;>self, model_output: <span class=\&quot;hljs-built_in\&quot;>str</span></span>) -&amp;gt; <span class=\&quot;hljs-type\&quot;>List</span>[<span class=\&quot;hljs-built_in\&quot;>str</span>]:&quot;,&quot;        <span class=\&quot;hljs-comment\&quot;># Find all tool calls</span>&quot;,&quot;        matched_ranges = self.tool_call_regex.findall(model_output)&quot;,&quot;        raw_tool_calls = [&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>match</span>[<span class=\&quot;hljs-number\&quot;>0</span>] <span class=\&quot;hljs-keyword\&quot;>if</span> <span class=\&quot;hljs-keyword\&quot;>match</span>[<span class=\&quot;hljs-number\&quot;>0</span>] <span class=\&quot;hljs-keyword\&quot;>else</span> <span class=\&quot;hljs-keyword\&quot;>match</span>[<span class=\&quot;hljs-number\&quot;>1</span>] <span class=\&quot;hljs-keyword\&quot;>for</span> <span class=\&quot;hljs-keyword\&quot;>match</span> <span class=\&quot;hljs-keyword\&quot;>in</span> matched_ranges&quot;,&quot;        ]&quot;,&quot;&quot;,&quot;        <span class=\&quot;hljs-comment\&quot;># Back-off strategy if no tool_call tags found</span>&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>if</span> <span class=\&quot;hljs-built_in\&quot;>len</span>(raw_tool_calls) == <span class=\&quot;hljs-number\&quot;>0</span>:&quot;,&quot;            raw_tool_calls = [model_output]&quot;,&quot;&quot;,&quot;        raw_function_calls = []&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>for</span> tool_call <span class=\&quot;hljs-keyword\&quot;>in</span> raw_tool_calls:&quot;,&quot;            raw_function_calls.extend(self.tool_call_function_regex.findall(tool_call))&quot;,&quot;&quot;,&quot;        function_calls = [&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>match</span>[<span class=\&quot;hljs-number\&quot;>0</span>] <span class=\&quot;hljs-keyword\&quot;>if</span> <span class=\&quot;hljs-keyword\&quot;>match</span>[<span class=\&quot;hljs-number\&quot;>0</span>] <span class=\&quot;hljs-keyword\&quot;>else</span> <span class=\&quot;hljs-keyword\&quot;>match</span>[<span class=\&quot;hljs-number\&quot;>1</span>] <span class=\&quot;hljs-keyword\&quot;>for</span> <span class=\&quot;hljs-keyword\&quot;>match</span> <span class=\&quot;hljs-keyword\&quot;>in</span> raw_function_calls&quot;,&quot;        ]&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>return</span> function_calls&quot;,&quot;&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>extract_tool_calls</span>(<span class=\&quot;hljs-params\&quot;></span>&quot;,&quot;<span class=\&quot;hljs-params\&quot;>        self,</span>&quot;,&quot;<span class=\&quot;hljs-params\&quot;>        model_output: <span class=\&quot;hljs-built_in\&quot;>str</span>,</span>&quot;,&quot;<span class=\&quot;hljs-params\&quot;>        request: ChatCompletionRequest,</span>&quot;,&quot;<span class=\&quot;hljs-params\&quot;>    </span>) -&amp;gt; ExtractedToolCallInformation:&quot;,&quot;        <span class=\&quot;hljs-comment\&quot;># Quick check to avoid unnecessary processing</span>&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>if</span> self.tool_call_prefix <span class=\&quot;hljs-keyword\&quot;>not</span> <span class=\&quot;hljs-keyword\&quot;>in</span> model_output:&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>return</span> ExtractedToolCallInformation(&quot;,&quot;                tools_called=<span class=\&quot;hljs-literal\&quot;>False</span>, tool_calls=[], content=model_output&quot;,&quot;            )&quot;,&quot;&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>try</span>:&quot;,&quot;            function_calls = self._get_function_calls(model_output)&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>if</span> <span class=\&quot;hljs-built_in\&quot;>len</span>(function_calls) == <span class=\&quot;hljs-number\&quot;>0</span>:&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>return</span> ExtractedToolCallInformation(&quot;,&quot;                    tools_called=<span class=\&quot;hljs-literal\&quot;>False</span>, tool_calls=[], content=model_output&quot;,&quot;                )&quot;,&quot;&quot;,&quot;            tool_calls = [&quot;,&quot;                self._parse_xml_function_call(function_call_str, request.tools)&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>for</span> function_call_str <span class=\&quot;hljs-keyword\&quot;>in</span> function_calls&quot;,&quot;            ]&quot;,&quot;&quot;,&quot;            <span class=\&quot;hljs-comment\&quot;># Populate prev_tool_call_arr for serving layer to set finish_reason</span>&quot;,&quot;            self.prev_tool_call_arr.clear()  <span class=\&quot;hljs-comment\&quot;># Clear previous calls</span>&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>for</span> tool_call <span class=\&quot;hljs-keyword\&quot;>in</span> tool_calls:&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>if</span> tool_call:&quot;,&quot;                    self.prev_tool_call_arr.append(&quot;,&quot;                        {&quot;,&quot;                            <span class=\&quot;hljs-string\&quot;>&amp;quot;name&amp;quot;</span>: tool_call.function.name,&quot;,&quot;                            <span class=\&quot;hljs-string\&quot;>&amp;quot;arguments&amp;quot;</span>: tool_call.function.arguments,&quot;,&quot;                        }&quot;,&quot;                    )&quot;,&quot;&quot;,&quot;            <span class=\&quot;hljs-comment\&quot;># Extract content before tool calls</span>&quot;,&quot;            content_index = model_output.find(self.tool_call_start_token)&quot;,&quot;            content_index = (&quot;,&quot;                content_index&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>if</span> content_index &amp;gt;= <span class=\&quot;hljs-number\&quot;>0</span>&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>else</span> model_output.find(self.tool_call_prefix)&quot;,&quot;            )&quot;,&quot;            content = model_output[:content_index]  <span class=\&quot;hljs-comment\&quot;># .rstrip()</span>&quot;,&quot;&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>return</span> ExtractedToolCallInformation(&quot;,&quot;                tools_called=(<span class=\&quot;hljs-built_in\&quot;>len</span>(tool_calls) &amp;gt; <span class=\&quot;hljs-number\&quot;>0</span>),&quot;,&quot;                tool_calls=tool_calls,&quot;,&quot;                content=content <span class=\&quot;hljs-keyword\&quot;>if</span> content <span class=\&quot;hljs-keyword\&quot;>else</span> <span class=\&quot;hljs-literal\&quot;>None</span>,&quot;,&quot;            )&quot;,&quot;&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>except</span> Exception:&quot;,&quot;            logger.exception(<span class=\&quot;hljs-string\&quot;>&amp;quot;Error in extracting tool call from response.&amp;quot;</span>)&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>return</span> ExtractedToolCallInformation(&quot;,&quot;                tools_called=<span class=\&quot;hljs-literal\&quot;>False</span>, tool_calls=[], content=model_output&quot;,&quot;            )&quot;,&quot;&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>extract_tool_calls_streaming</span>(<span class=\&quot;hljs-params\&quot;></span>&quot;,&quot;<span class=\&quot;hljs-params\&quot;>        self,</span>&quot;,&quot;<span class=\&quot;hljs-params\&quot;>        previous_text: <span class=\&quot;hljs-built_in\&quot;>str</span>,</span>&quot;,&quot;<span class=\&quot;hljs-params\&quot;>        current_text: <span class=\&quot;hljs-built_in\&quot;>str</span>,</span>&quot;,&quot;<span class=\&quot;hljs-params\&quot;>        delta_text: <span class=\&quot;hljs-built_in\&quot;>str</span>,</span>&quot;,&quot;<span class=\&quot;hljs-params\&quot;>        previous_token_ids: <span class=\&quot;hljs-type\&quot;>Sequence</span>[<span class=\&quot;hljs-built_in\&quot;>int</span>],</span>&quot;,&quot;<span class=\&quot;hljs-params\&quot;>        current_token_ids: <span class=\&quot;hljs-type\&quot;>Sequence</span>[<span class=\&quot;hljs-built_in\&quot;>int</span>],</span>&quot;,&quot;<span class=\&quot;hljs-params\&quot;>        delta_token_ids: <span class=\&quot;hljs-type\&quot;>Sequence</span>[<span class=\&quot;hljs-built_in\&quot;>int</span>],</span>&quot;,&quot;<span class=\&quot;hljs-params\&quot;>        request: ChatCompletionRequest,</span>&quot;,&quot;<span class=\&quot;hljs-params\&quot;>    </span>) -&amp;gt; <span class=\&quot;hljs-type\&quot;>Union</span>[DeltaMessage, <span class=\&quot;hljs-literal\&quot;>None</span>]:&quot;,&quot;        <span class=\&quot;hljs-comment\&quot;># If no delta text, return None unless it&amp;#x27;s an EOS token after tool calls</span>&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>if</span> <span class=\&quot;hljs-keyword\&quot;>not</span> delta_text:&quot;,&quot;            <span class=\&quot;hljs-comment\&quot;># Check if this is an EOS token after all tool calls are complete</span>&quot;,&quot;            <span class=\&quot;hljs-comment\&quot;># We check for tool calls in the text even if is_tool_call_started is False</span>&quot;,&quot;            <span class=\&quot;hljs-comment\&quot;># because it might have been reset after processing all tools</span>&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>if</span> delta_token_ids <span class=\&quot;hljs-keyword\&quot;>and</span> self.tool_call_end_token_id <span class=\&quot;hljs-keyword\&quot;>not</span> <span class=\&quot;hljs-keyword\&quot;>in</span> delta_token_ids:&quot;,&quot;                <span class=\&quot;hljs-comment\&quot;># Count complete tool calls</span>&quot;,&quot;                complete_calls = <span class=\&quot;hljs-built_in\&quot;>len</span>(&quot;,&quot;                    self.tool_call_complete_regex.findall(current_text)&quot;,&quot;                )&quot;,&quot;&quot;,&quot;                <span class=\&quot;hljs-comment\&quot;># If we have completed tool calls and populated prev_tool_call_arr</span>&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>if</span> complete_calls &amp;gt; <span class=\&quot;hljs-number\&quot;>0</span> <span class=\&quot;hljs-keyword\&quot;>and</span> <span class=\&quot;hljs-built_in\&quot;>len</span>(self.prev_tool_call_arr) &amp;gt; <span class=\&quot;hljs-number\&quot;>0</span>:&quot;,&quot;                    <span class=\&quot;hljs-comment\&quot;># Check if all tool calls are closed</span>&quot;,&quot;                    open_calls = current_text.count(&quot;,&quot;                        self.tool_call_start_token&quot;,&quot;                    ) - current_text.count(self.tool_call_end_token)&quot;,&quot;                    <span class=\&quot;hljs-keyword\&quot;>if</span> open_calls == <span class=\&quot;hljs-number\&quot;>0</span>:&quot;,&quot;                        <span class=\&quot;hljs-comment\&quot;># Return empty delta message to allow finish_reason processing</span>&quot;,&quot;                        <span class=\&quot;hljs-keyword\&quot;>return</span> DeltaMessage(content=<span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;</span>)&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>elif</span> <span class=\&quot;hljs-keyword\&quot;>not</span> self.is_tool_call_started <span class=\&quot;hljs-keyword\&quot;>and</span> current_text:&quot;,&quot;                    <span class=\&quot;hljs-comment\&quot;># This is a regular content response that&amp;#x27;s now complete</span>&quot;,&quot;                    <span class=\&quot;hljs-keyword\&quot;>return</span> DeltaMessage(content=<span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;</span>)&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>return</span> <span class=\&quot;hljs-literal\&quot;>None</span>&quot;,&quot;&quot;,&quot;        <span class=\&quot;hljs-comment\&quot;># Check if this is the first call (reset state if needed)</span>&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>if</span> <span class=\&quot;hljs-keyword\&quot;>not</span> previous_text:&quot;,&quot;            self._reset_streaming_state()&quot;,&quot;&quot;,&quot;        <span class=\&quot;hljs-comment\&quot;># Update accumulated text</span>&quot;,&quot;        self.accumulated_text = current_text&quot;,&quot;&quot;,&quot;        <span class=\&quot;hljs-comment\&quot;># Check if we need to advance to next tool</span>&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>if</span> self.json_closed <span class=\&quot;hljs-keyword\&quot;>and</span> <span class=\&quot;hljs-keyword\&quot;>not</span> self.in_function:&quot;,&quot;            <span class=\&quot;hljs-comment\&quot;># Check if this tool call has ended</span>&quot;,&quot;            tool_ends = current_text.count(self.tool_call_end_token)&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>if</span> tool_ends &amp;gt; self.current_tool_index:&quot;,&quot;                <span class=\&quot;hljs-comment\&quot;># This tool has ended, advance to next</span>&quot;,&quot;                self.current_tool_index += <span class=\&quot;hljs-number\&quot;>1</span>&quot;,&quot;                self.header_sent = <span class=\&quot;hljs-literal\&quot;>False</span>&quot;,&quot;                self.param_count = <span class=\&quot;hljs-number\&quot;>0</span>&quot;,&quot;                self.json_started = <span class=\&quot;hljs-literal\&quot;>False</span>&quot;,&quot;                self.json_closed = <span class=\&quot;hljs-literal\&quot;>False</span>&quot;,&quot;&quot;,&quot;                <span class=\&quot;hljs-comment\&quot;># Check if there are more tool calls</span>&quot;,&quot;                tool_starts = current_text.count(self.tool_call_start_token)&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>if</span> self.current_tool_index &amp;gt;= tool_starts:&quot;,&quot;                    <span class=\&quot;hljs-comment\&quot;># No more tool calls</span>&quot;,&quot;                    self.is_tool_call_started = <span class=\&quot;hljs-literal\&quot;>False</span>&quot;,&quot;                <span class=\&quot;hljs-comment\&quot;># Continue processing next tool</span>&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>return</span> <span class=\&quot;hljs-literal\&quot;>None</span>&quot;,&quot;&quot;,&quot;        <span class=\&quot;hljs-comment\&quot;># Handle normal content before tool calls</span>&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>if</span> <span class=\&quot;hljs-keyword\&quot;>not</span> self.is_tool_call_started:&quot;,&quot;            <span class=\&quot;hljs-comment\&quot;># Check if tool call is starting</span>&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>if</span> (&quot;,&quot;                self.tool_call_start_token_id <span class=\&quot;hljs-keyword\&quot;>in</span> delta_token_ids&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>or</span> self.tool_call_start_token <span class=\&quot;hljs-keyword\&quot;>in</span> delta_text&quot;,&quot;            ):&quot;,&quot;                self.is_tool_call_started = <span class=\&quot;hljs-literal\&quot;>True</span>&quot;,&quot;                <span class=\&quot;hljs-comment\&quot;># Return any content before the tool call</span>&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>if</span> self.tool_call_start_token <span class=\&quot;hljs-keyword\&quot;>in</span> delta_text:&quot;,&quot;                    content_before = delta_text[&quot;,&quot;                        : delta_text.index(self.tool_call_start_token)&quot;,&quot;                    ]&quot;,&quot;                    <span class=\&quot;hljs-keyword\&quot;>if</span> content_before:&quot;,&quot;                        <span class=\&quot;hljs-keyword\&quot;>return</span> DeltaMessage(content=content_before)&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>return</span> <span class=\&quot;hljs-literal\&quot;>None</span>&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>else</span>:&quot;,&quot;                <span class=\&quot;hljs-comment\&quot;># Check if we&amp;#x27;re between tool calls - skip whitespace</span>&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>if</span> current_text.rstrip().endswith(self.tool_call_end_token):&quot;,&quot;                    <span class=\&quot;hljs-comment\&quot;># We just ended a tool call, skip whitespace</span>&quot;,&quot;                    <span class=\&quot;hljs-keyword\&quot;>if</span> delta_text.strip() == <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;</span>:&quot;,&quot;                        <span class=\&quot;hljs-keyword\&quot;>return</span> <span class=\&quot;hljs-literal\&quot;>None</span>&quot;,&quot;                <span class=\&quot;hljs-comment\&quot;># Normal content, no tool call</span>&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>return</span> DeltaMessage(content=delta_text)&quot;,&quot;&quot;,&quot;        <span class=\&quot;hljs-comment\&quot;># Check if we&amp;#x27;re between tool calls (waiting for next one)</span>&quot;,&quot;        <span class=\&quot;hljs-comment\&quot;># Count tool calls we&amp;#x27;ve seen vs processed</span>&quot;,&quot;        tool_starts_count = current_text.count(self.tool_call_start_token)&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>if</span> self.current_tool_index &amp;gt;= tool_starts_count:&quot;,&quot;            <span class=\&quot;hljs-comment\&quot;># We&amp;#x27;re past all tool calls, shouldn&amp;#x27;t be here</span>&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>return</span> <span class=\&quot;hljs-literal\&quot;>None</span>&quot;,&quot;&quot;,&quot;        <span class=\&quot;hljs-comment\&quot;># We&amp;#x27;re in a tool call, find the current tool call portion</span>&quot;,&quot;        <span class=\&quot;hljs-comment\&quot;># Need to find the correct tool call based on current_tool_index</span>&quot;,&quot;        tool_starts = []&quot;,&quot;        idx = <span class=\&quot;hljs-number\&quot;>0</span>&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>while</span> <span class=\&quot;hljs-literal\&quot;>True</span>:&quot;,&quot;            idx = current_text.find(self.tool_call_start_token, idx)&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>if</span> idx == -<span class=\&quot;hljs-number\&quot;>1</span>:&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>break</span>&quot;,&quot;            tool_starts.append(idx)&quot;,&quot;            idx += <span class=\&quot;hljs-built_in\&quot;>len</span>(self.tool_call_start_token)&quot;,&quot;&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>if</span> self.current_tool_index &amp;gt;= <span class=\&quot;hljs-built_in\&quot;>len</span>(tool_starts):&quot;,&quot;            <span class=\&quot;hljs-comment\&quot;># No more tool calls to process yet</span>&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>return</span> <span class=\&quot;hljs-literal\&quot;>None</span>&quot;,&quot;&quot;,&quot;        tool_start_idx = tool_starts[self.current_tool_index]&quot;,&quot;        <span class=\&quot;hljs-comment\&quot;># Find where this tool call ends (or current position if not ended yet)</span>&quot;,&quot;        tool_end_idx = current_text.find(self.tool_call_end_token, tool_start_idx)&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>if</span> tool_end_idx == -<span class=\&quot;hljs-number\&quot;>1</span>:&quot;,&quot;            tool_text = current_text[tool_start_idx:]&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>else</span>:&quot;,&quot;            tool_text = current_text[&quot;,&quot;                tool_start_idx : tool_end_idx + <span class=\&quot;hljs-built_in\&quot;>len</span>(self.tool_call_end_token)&quot;,&quot;            ]&quot;,&quot;&quot;,&quot;        <span class=\&quot;hljs-comment\&quot;># Looking for function header</span>&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>if</span> <span class=\&quot;hljs-keyword\&quot;>not</span> self.header_sent:&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>if</span> self.tool_call_prefix <span class=\&quot;hljs-keyword\&quot;>in</span> tool_text:&quot;,&quot;                func_start = tool_text.find(self.tool_call_prefix) + <span class=\&quot;hljs-built_in\&quot;>len</span>(&quot;,&quot;                    self.tool_call_prefix&quot;,&quot;                )&quot;,&quot;                func_end = tool_text.find(<span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;gt;&amp;quot;</span>, func_start)&quot;,&quot;&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>if</span> func_end != -<span class=\&quot;hljs-number\&quot;>1</span>:&quot;,&quot;                    <span class=\&quot;hljs-comment\&quot;># Found complete function name</span>&quot;,&quot;                    self.current_function_name = tool_text[func_start:func_end]&quot;,&quot;                    self.current_tool_id = self._generate_tool_call_id()&quot;,&quot;                    self.header_sent = <span class=\&quot;hljs-literal\&quot;>True</span>&quot;,&quot;                    self.in_function = <span class=\&quot;hljs-literal\&quot;>True</span>&quot;,&quot;&quot;,&quot;                    <span class=\&quot;hljs-comment\&quot;># IMPORTANT: Add to prev_tool_call_arr immediately when we detect a tool call</span>&quot;,&quot;                    <span class=\&quot;hljs-comment\&quot;># This ensures finish_reason=&amp;quot;tool_calls&amp;quot; even if parsing isn&amp;#x27;t complete</span>&quot;,&quot;                    already_added = <span class=\&quot;hljs-built_in\&quot;>any</span>(&quot;,&quot;                        tool.get(<span class=\&quot;hljs-string\&quot;>&amp;quot;name&amp;quot;</span>) == self.current_function_name&quot;,&quot;                        <span class=\&quot;hljs-keyword\&quot;>for</span> tool <span class=\&quot;hljs-keyword\&quot;>in</span> self.prev_tool_call_arr&quot;,&quot;                    )&quot;,&quot;                    <span class=\&quot;hljs-keyword\&quot;>if</span> <span class=\&quot;hljs-keyword\&quot;>not</span> already_added:&quot;,&quot;                        self.prev_tool_call_arr.append(&quot;,&quot;                            {&quot;,&quot;                                <span class=\&quot;hljs-string\&quot;>&amp;quot;name&amp;quot;</span>: self.current_function_name,&quot;,&quot;                                <span class=\&quot;hljs-string\&quot;>&amp;quot;arguments&amp;quot;</span>: <span class=\&quot;hljs-string\&quot;>&amp;quot;{}&amp;quot;</span>,  <span class=\&quot;hljs-comment\&quot;># Placeholder, will be updated later</span>&quot;,&quot;                            }&quot;,&quot;                        )&quot;,&quot;&quot;,&quot;                    <span class=\&quot;hljs-comment\&quot;># Send header with function info</span>&quot;,&quot;                    <span class=\&quot;hljs-keyword\&quot;>return</span> DeltaMessage(&quot;,&quot;                        tool_calls=[&quot;,&quot;                            DeltaToolCall(&quot;,&quot;                                index=self.current_tool_index,&quot;,&quot;                                <span class=\&quot;hljs-built_in\&quot;>id</span>=self.current_tool_id,&quot;,&quot;                                function=DeltaFunctionCall(&quot;,&quot;                                    name=self.current_function_name, arguments=<span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;</span>&quot;,&quot;                                ),&quot;,&quot;                                <span class=\&quot;hljs-built_in\&quot;>type</span>=<span class=\&quot;hljs-string\&quot;>&amp;quot;function&amp;quot;</span>,&quot;,&quot;                            )&quot;,&quot;                        ]&quot;,&quot;                    )&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>return</span> <span class=\&quot;hljs-literal\&quot;>None</span>&quot;,&quot;&quot;,&quot;        <span class=\&quot;hljs-comment\&quot;># We&amp;#x27;ve sent header, now handle function body</span>&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>if</span> self.in_function:&quot;,&quot;            <span class=\&quot;hljs-comment\&quot;># Send opening brace if not sent yet</span>&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>if</span> <span class=\&quot;hljs-keyword\&quot;>not</span> self.json_started <span class=\&quot;hljs-keyword\&quot;>and</span> <span class=\&quot;hljs-keyword\&quot;>not</span> self.parameter_prefix <span class=\&quot;hljs-keyword\&quot;>in</span> delta_text:&quot;,&quot;                self.json_started = <span class=\&quot;hljs-literal\&quot;>True</span>&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>return</span> DeltaMessage(&quot;,&quot;                    tool_calls=[&quot;,&quot;                        DeltaToolCall(&quot;,&quot;                            index=self.current_tool_index,&quot;,&quot;                            function=DeltaFunctionCall(arguments=<span class=\&quot;hljs-string\&quot;>&amp;quot;{&amp;quot;</span>),&quot;,&quot;                        )&quot;,&quot;                    ]&quot;,&quot;                )&quot;,&quot;&quot;,&quot;            <span class=\&quot;hljs-comment\&quot;># Make sure json_started is set if we&amp;#x27;re processing parameters</span>&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>if</span> <span class=\&quot;hljs-keyword\&quot;>not</span> self.json_started:&quot;,&quot;                self.json_started = <span class=\&quot;hljs-literal\&quot;>True</span>&quot;,&quot;&quot;,&quot;            <span class=\&quot;hljs-comment\&quot;># Check for function end in accumulated text</span>&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>if</span> <span class=\&quot;hljs-keyword\&quot;>not</span> self.json_closed <span class=\&quot;hljs-keyword\&quot;>and</span> self.function_end_token <span class=\&quot;hljs-keyword\&quot;>in</span> tool_text:&quot;,&quot;                <span class=\&quot;hljs-comment\&quot;># Close JSON</span>&quot;,&quot;                self.json_closed = <span class=\&quot;hljs-literal\&quot;>True</span>&quot;,&quot;&quot;,&quot;                <span class=\&quot;hljs-comment\&quot;># Extract the complete tool call to update prev_tool_call_arr with final arguments</span>&quot;,&quot;                <span class=\&quot;hljs-comment\&quot;># Find the function content</span>&quot;,&quot;                func_start = tool_text.find(self.tool_call_prefix) + <span class=\&quot;hljs-built_in\&quot;>len</span>(&quot;,&quot;                    self.tool_call_prefix&quot;,&quot;                )&quot;,&quot;                func_content_end = tool_text.find(self.function_end_token, func_start)&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>if</span> func_content_end != -<span class=\&quot;hljs-number\&quot;>1</span>:&quot;,&quot;                    func_content = tool_text[func_start:func_content_end]&quot;,&quot;                    <span class=\&quot;hljs-comment\&quot;># Parse to get the complete arguments</span>&quot;,&quot;                    <span class=\&quot;hljs-keyword\&quot;>try</span>:&quot;,&quot;                        parsed_tool = self._parse_xml_function_call(&quot;,&quot;                            func_content, request.tools <span class=\&quot;hljs-keyword\&quot;>if</span> request <span class=\&quot;hljs-keyword\&quot;>else</span> <span class=\&quot;hljs-literal\&quot;>None</span>&quot;,&quot;                        )&quot;,&quot;                        <span class=\&quot;hljs-keyword\&quot;>if</span> parsed_tool:&quot;,&quot;                            <span class=\&quot;hljs-comment\&quot;># Update existing entry in prev_tool_call_arr with complete arguments</span>&quot;,&quot;                            <span class=\&quot;hljs-keyword\&quot;>for</span> i, tool <span class=\&quot;hljs-keyword\&quot;>in</span> <span class=\&quot;hljs-built_in\&quot;>enumerate</span>(self.prev_tool_call_arr):&quot;,&quot;                                <span class=\&quot;hljs-keyword\&quot;>if</span> tool.get(<span class=\&quot;hljs-string\&quot;>&amp;quot;name&amp;quot;</span>) == parsed_tool.function.name:&quot;,&quot;                                    self.prev_tool_call_arr[i][<span class=\&quot;hljs-string\&quot;>&amp;quot;arguments&amp;quot;</span>] = (&quot;,&quot;                                        parsed_tool.function.arguments&quot;,&quot;                                    )&quot;,&quot;                                    <span class=\&quot;hljs-keyword\&quot;>break</span>&quot;,&quot;                    <span class=\&quot;hljs-keyword\&quot;>except</span> Exception:&quot;,&quot;                        <span class=\&quot;hljs-keyword\&quot;>pass</span>  <span class=\&quot;hljs-comment\&quot;># Ignore parsing errors during streaming</span>&quot;,&quot;&quot;,&quot;                result = DeltaMessage(&quot;,&quot;                    tool_calls=[&quot;,&quot;                        DeltaToolCall(&quot;,&quot;                            index=self.current_tool_index,&quot;,&quot;                            function=DeltaFunctionCall(arguments=<span class=\&quot;hljs-string\&quot;>&amp;quot;}&amp;quot;</span>),&quot;,&quot;                        )&quot;,&quot;                    ]&quot;,&quot;                )&quot;,&quot;&quot;,&quot;                <span class=\&quot;hljs-comment\&quot;># Reset state for next tool</span>&quot;,&quot;                self.in_function = <span class=\&quot;hljs-literal\&quot;>False</span>&quot;,&quot;                self.json_closed = <span class=\&quot;hljs-literal\&quot;>True</span>&quot;,&quot;&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>return</span> result&quot;,&quot;&quot;,&quot;            <span class=\&quot;hljs-comment\&quot;># Look for parameters</span>&quot;,&quot;            <span class=\&quot;hljs-comment\&quot;># Count how many complete parameters we have processed</span>&quot;,&quot;            complete_params = tool_text.count(self.parameter_end_token)&quot;,&quot;&quot;,&quot;            <span class=\&quot;hljs-comment\&quot;># Check if we should start a new parameter</span>&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>if</span> <span class=\&quot;hljs-keyword\&quot;>not</span> self.in_param <span class=\&quot;hljs-keyword\&quot;>and</span> self.param_count &amp;lt; complete_params:&quot;,&quot;                <span class=\&quot;hljs-comment\&quot;># Find the unprocessed parameter</span>&quot;,&quot;                <span class=\&quot;hljs-comment\&quot;># Count parameter starts</span>&quot;,&quot;                param_starts = []&quot;,&quot;                idx = <span class=\&quot;hljs-number\&quot;>0</span>&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>while</span> <span class=\&quot;hljs-literal\&quot;>True</span>:&quot;,&quot;                    idx = tool_text.find(self.parameter_prefix, idx)&quot;,&quot;                    <span class=\&quot;hljs-keyword\&quot;>if</span> idx == -<span class=\&quot;hljs-number\&quot;>1</span>:&quot;,&quot;                        <span class=\&quot;hljs-keyword\&quot;>break</span>&quot;,&quot;                    param_starts.append(idx)&quot;,&quot;                    idx += <span class=\&quot;hljs-built_in\&quot;>len</span>(self.parameter_prefix)&quot;,&quot;&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>if</span> <span class=\&quot;hljs-built_in\&quot;>len</span>(param_starts) &amp;gt; self.param_count:&quot;,&quot;                    <span class=\&quot;hljs-comment\&quot;># Process the next parameter</span>&quot;,&quot;                    param_idx = param_starts[self.param_count]&quot;,&quot;                    param_start = param_idx + <span class=\&quot;hljs-built_in\&quot;>len</span>(self.parameter_prefix)&quot;,&quot;                    remaining = tool_text[param_start:]&quot;,&quot;&quot;,&quot;                    <span class=\&quot;hljs-keyword\&quot;>if</span> <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;gt;&amp;quot;</span> <span class=\&quot;hljs-keyword\&quot;>in</span> remaining:&quot;,&quot;                        <span class=\&quot;hljs-comment\&quot;># We have the complete parameter name</span>&quot;,&quot;                        name_end = remaining.find(<span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;gt;&amp;quot;</span>)&quot;,&quot;                        self.current_param_name = remaining[:name_end]&quot;,&quot;&quot;,&quot;                        <span class=\&quot;hljs-comment\&quot;># Find the parameter value</span>&quot;,&quot;                        value_start = param_start + name_end + <span class=\&quot;hljs-number\&quot;>1</span>&quot;,&quot;                        value_text = tool_text[value_start:]&quot;,&quot;                        <span class=\&quot;hljs-keyword\&quot;>if</span> value_text.startswith(<span class=\&quot;hljs-string\&quot;>&amp;quot;\\n&amp;quot;</span>):&quot;,&quot;                            value_text = value_text[<span class=\&quot;hljs-number\&quot;>1</span>:]&quot;,&quot;&quot;,&quot;                        <span class=\&quot;hljs-comment\&quot;># Find where this parameter ends</span>&quot;,&quot;                        param_end_idx = value_text.find(self.parameter_end_token)&quot;,&quot;                        <span class=\&quot;hljs-keyword\&quot;>if</span> param_end_idx != -<span class=\&quot;hljs-number\&quot;>1</span>:&quot;,&quot;                            <span class=\&quot;hljs-comment\&quot;># Complete parameter found</span>&quot;,&quot;                            param_value = value_text[:param_end_idx]&quot;,&quot;                            <span class=\&quot;hljs-keyword\&quot;>if</span> param_value.endswith(<span class=\&quot;hljs-string\&quot;>&amp;quot;\\n&amp;quot;</span>):&quot;,&quot;                                param_value = param_value[:-<span class=\&quot;hljs-number\&quot;>1</span>]&quot;,&quot;&quot;,&quot;                            <span class=\&quot;hljs-comment\&quot;># Build complete JSON fragment for this parameter</span>&quot;,&quot;                            <span class=\&quot;hljs-keyword\&quot;>if</span> self.param_count == <span class=\&quot;hljs-number\&quot;>0</span>:&quot;,&quot;                                json_fragment = (&quot;,&quot;                                    <span class=\&quot;hljs-string\&quot;>&amp;#x27;&amp;quot;&amp;#x27;</span>&quot;,&quot;                                    + self.current_param_name&quot;,&quot;                                    + <span class=\&quot;hljs-string\&quot;>&amp;#x27;&amp;quot;: &amp;quot;&amp;#x27;</span>&quot;,&quot;                                    + json.dumps(param_value)[<span class=\&quot;hljs-number\&quot;>1</span>:-<span class=\&quot;hljs-number\&quot;>1</span>]&quot;,&quot;                                    + <span class=\&quot;hljs-string\&quot;>&amp;#x27;&amp;quot;&amp;#x27;</span>&quot;,&quot;                                )&quot;,&quot;                            <span class=\&quot;hljs-keyword\&quot;>else</span>:&quot;,&quot;                                json_fragment = (&quot;,&quot;                                    <span class=\&quot;hljs-string\&quot;>&amp;#x27;, &amp;quot;&amp;#x27;</span>&quot;,&quot;                                    + self.current_param_name&quot;,&quot;                                    + <span class=\&quot;hljs-string\&quot;>&amp;#x27;&amp;quot;: &amp;quot;&amp;#x27;</span>&quot;,&quot;                                    + json.dumps(param_value)[<span class=\&quot;hljs-number\&quot;>1</span>:-<span class=\&quot;hljs-number\&quot;>1</span>]&quot;,&quot;                                    + <span class=\&quot;hljs-string\&quot;>&amp;#x27;&amp;quot;&amp;#x27;</span>&quot;,&quot;                                )&quot;,&quot;&quot;,&quot;                            self.param_count += <span class=\&quot;hljs-number\&quot;>1</span>&quot;,&quot;&quot;,&quot;                            <span class=\&quot;hljs-keyword\&quot;>return</span> DeltaMessage(&quot;,&quot;                                tool_calls=[&quot;,&quot;                                    DeltaToolCall(&quot;,&quot;                                        index=self.current_tool_index,&quot;,&quot;                                        function=DeltaFunctionCall(&quot;,&quot;                                            arguments=json_fragment&quot;,&quot;                                        ),&quot;,&quot;                                    )&quot;,&quot;                                ]&quot;,&quot;                            )&quot;,&quot;&quot;,&quot;            <span class=\&quot;hljs-comment\&quot;># Continue parameter value</span>&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>if</span> self.in_param:&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>if</span> self.parameter_end_token <span class=\&quot;hljs-keyword\&quot;>in</span> delta_text:&quot;,&quot;                    <span class=\&quot;hljs-comment\&quot;># End of parameter</span>&quot;,&quot;                    end_idx = delta_text.find(self.parameter_end_token)&quot;,&quot;                    value_chunk = delta_text[:end_idx]&quot;,&quot;&quot;,&quot;                    <span class=\&quot;hljs-comment\&quot;># Skip past &amp;gt; if at start</span>&quot;,&quot;                    <span class=\&quot;hljs-keyword\&quot;>if</span> <span class=\&quot;hljs-keyword\&quot;>not</span> self.current_param_value <span class=\&quot;hljs-keyword\&quot;>and</span> <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;gt;&amp;quot;</span> <span class=\&quot;hljs-keyword\&quot;>in</span> value_chunk:&quot;,&quot;                        gt_idx = value_chunk.find(<span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;gt;&amp;quot;</span>)&quot;,&quot;                        value_chunk = value_chunk[gt_idx + <span class=\&quot;hljs-number\&quot;>1</span> :]&quot;,&quot;&quot;,&quot;                    <span class=\&quot;hljs-keyword\&quot;>if</span> <span class=\&quot;hljs-keyword\&quot;>not</span> self.current_param_value <span class=\&quot;hljs-keyword\&quot;>and</span> value_chunk.startswith(<span class=\&quot;hljs-string\&quot;>&amp;quot;\\n&amp;quot;</span>):&quot;,&quot;                        value_chunk = value_chunk[<span class=\&quot;hljs-number\&quot;>1</span>:]&quot;,&quot;&quot;,&quot;                    <span class=\&quot;hljs-comment\&quot;># Calculate incremental JSON</span>&quot;,&quot;                    full_value = self.current_param_value + value_chunk&quot;,&quot;                    prev_escaped = (&quot;,&quot;                        json.dumps(self.current_param_value)[<span class=\&quot;hljs-number\&quot;>1</span>:-<span class=\&quot;hljs-number\&quot;>1</span>]&quot;,&quot;                        <span class=\&quot;hljs-keyword\&quot;>if</span> self.current_param_value&quot;,&quot;                        <span class=\&quot;hljs-keyword\&quot;>else</span> <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;</span>&quot;,&quot;                    )&quot;,&quot;                    full_escaped = json.dumps(full_value)[<span class=\&quot;hljs-number\&quot;>1</span>:-<span class=\&quot;hljs-number\&quot;>1</span>]&quot;,&quot;                    delta_escaped = full_escaped[<span class=\&quot;hljs-built_in\&quot;>len</span>(prev_escaped) :]&quot;,&quot;&quot;,&quot;                    self.in_param = <span class=\&quot;hljs-literal\&quot;>False</span>&quot;,&quot;                    self.current_param_value = <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;</span>&quot;,&quot;&quot;,&quot;                    <span class=\&quot;hljs-keyword\&quot;>return</span> DeltaMessage(&quot;,&quot;                        tool_calls=[&quot;,&quot;                            DeltaToolCall(&quot;,&quot;                                index=self.current_tool_index,&quot;,&quot;                                function=DeltaFunctionCall(&quot;,&quot;                                    arguments=delta_escaped + <span class=\&quot;hljs-string\&quot;>&amp;#x27;&amp;quot;&amp;#x27;</span>&quot;,&quot;                                ),&quot;,&quot;                            )&quot;,&quot;                        ]&quot;,&quot;                    )&quot;,&quot;                <span class=\&quot;hljs-keyword\&quot;>else</span>:&quot;,&quot;                    <span class=\&quot;hljs-comment\&quot;># Continue accumulating value</span>&quot;,&quot;                    value_chunk = delta_text&quot;,&quot;&quot;,&quot;                    <span class=\&quot;hljs-comment\&quot;># Handle first chunk after param name</span>&quot;,&quot;                    <span class=\&quot;hljs-keyword\&quot;>if</span> <span class=\&quot;hljs-keyword\&quot;>not</span> self.current_param_value <span class=\&quot;hljs-keyword\&quot;>and</span> <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;gt;&amp;quot;</span> <span class=\&quot;hljs-keyword\&quot;>in</span> value_chunk:&quot;,&quot;                        gt_idx = value_chunk.find(<span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;gt;&amp;quot;</span>)&quot;,&quot;                        value_chunk = value_chunk[gt_idx + <span class=\&quot;hljs-number\&quot;>1</span> :]&quot;,&quot;&quot;,&quot;                    <span class=\&quot;hljs-keyword\&quot;>if</span> <span class=\&quot;hljs-keyword\&quot;>not</span> self.current_param_value <span class=\&quot;hljs-keyword\&quot;>and</span> value_chunk.startswith(<span class=\&quot;hljs-string\&quot;>&amp;quot;\\n&amp;quot;</span>):&quot;,&quot;                        value_chunk = value_chunk[<span class=\&quot;hljs-number\&quot;>1</span>:]&quot;,&quot;&quot;,&quot;                    <span class=\&quot;hljs-keyword\&quot;>if</span> value_chunk:&quot;,&quot;                        <span class=\&quot;hljs-comment\&quot;># Stream the escaped delta</span>&quot;,&quot;                        prev_escaped = (&quot;,&quot;                            json.dumps(self.current_param_value)[<span class=\&quot;hljs-number\&quot;>1</span>:-<span class=\&quot;hljs-number\&quot;>1</span>]&quot;,&quot;                            <span class=\&quot;hljs-keyword\&quot;>if</span> self.current_param_value&quot;,&quot;                            <span class=\&quot;hljs-keyword\&quot;>else</span> <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;</span>&quot;,&quot;                        )&quot;,&quot;                        self.current_param_value += value_chunk&quot;,&quot;                        full_escaped = json.dumps(self.current_param_value)[<span class=\&quot;hljs-number\&quot;>1</span>:-<span class=\&quot;hljs-number\&quot;>1</span>]&quot;,&quot;                        delta_escaped = full_escaped[<span class=\&quot;hljs-built_in\&quot;>len</span>(prev_escaped) :]&quot;,&quot;&quot;,&quot;                        <span class=\&quot;hljs-keyword\&quot;>if</span> delta_escaped:&quot;,&quot;                            <span class=\&quot;hljs-keyword\&quot;>return</span> DeltaMessage(&quot;,&quot;                                tool_calls=[&quot;,&quot;                                    DeltaToolCall(&quot;,&quot;                                        index=self.current_tool_index,&quot;,&quot;                                        function=DeltaFunctionCall(&quot;,&quot;                                            arguments=delta_escaped&quot;,&quot;                                        ),&quot;,&quot;                                    )&quot;,&quot;                                ]&quot;,&quot;                            )&quot;,&quot;&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>return</span> <span class=\&quot;hljs-literal\&quot;>None</span>&quot;,&quot;&quot;],&quot;lineSelectorClass&quot;:&quot;blob-line&quot;,&quot;context&quot;:{&quot;repo&quot;:{&quot;name&quot;:&quot;Qwen/Qwen3-Coder-30B-A3B-Instruct&quot;,&quot;type&quot;:&quot;model&quot;},&quot;rev&quot;:&quot;main&quot;,&quot;path&quot;:&quot;qwen3coder_tool_parser.py&quot;,&quot;subpaths&quot;:[{&quot;dir&quot;:&quot;qwen3coder_tool_parser.py&quot;}]}}">

<div class="@container relative"><div class="@max-3xl:text-xs overflow-x-auto text-sm"><table class="min-w-full border-collapse font-mono"><tbody>
					<tr class="" id="L1">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="1">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-comment"># SPDX-License-Identifier: Apache-2.0</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L2">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="2">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L3">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="3">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-keyword">import</span> json<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L4">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="4">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-keyword">import</span> re<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L5">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="5">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-keyword">import</span> uuid<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L6">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="6">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-keyword">from</span> collections.abc <span class="hljs-keyword">import</span> <span class="hljs-type">Sequence</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L7">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="7">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-keyword">from</span> typing <span class="hljs-keyword">import</span> <span class="hljs-type">Union</span>, <span class="hljs-type">Optional</span>, <span class="hljs-type">Any</span>, <span class="hljs-type">List</span>, <span class="hljs-type">Dict</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L8">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="8">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-keyword">from</span> enum <span class="hljs-keyword">import</span> Enum<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L9">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="9">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L10">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="10">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-keyword">from</span> vllm.entrypoints.openai.protocol <span class="hljs-keyword">import</span> (<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L11">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="11">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->    ChatCompletionRequest,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L12">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="12">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->    ChatCompletionToolsParam,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L13">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="13">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->    DeltaMessage,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L14">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="14">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->    DeltaToolCall,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L15">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="15">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->    DeltaFunctionCall,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L16">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="16">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->    ExtractedToolCallInformation,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L17">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="17">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->    FunctionCall,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L18">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="18">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->    ToolCall,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L19">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="19">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L20">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="20">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-keyword">from</span> vllm.entrypoints.openai.tool_parsers.abstract_tool_parser <span class="hljs-keyword">import</span> (<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L21">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="21">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->    ToolParser,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L22">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="22">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->    ToolParserManager,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L23">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="23">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L24">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="24">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-keyword">from</span> vllm.logger <span class="hljs-keyword">import</span> init_logger<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L25">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="25">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-keyword">from</span> vllm.transformers_utils.tokenizer <span class="hljs-keyword">import</span> AnyTokenizer<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L26">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="26">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L27">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="27">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->logger = init_logger(__name__)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L28">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="28">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L29">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="29">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L30">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="30">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-meta">@ToolParserManager.register_module(<span class="hljs-params"><span class="hljs-string">&quot;qwen3_xml&quot;</span></span>)</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L31">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="31">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-keyword">class</span> <span class="hljs-title class_">Qwen3XMLToolParser</span>(<span class="hljs-title class_ inherited__">ToolParser</span>):<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L32">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="32">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->    <span class="hljs-keyword">def</span> <span class="hljs-title function_">__init__</span>(<span class="hljs-params">self, tokenizer: AnyTokenizer</span>):<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L33">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="33">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-built_in">super</span>().__init__(tokenizer)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L34">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="34">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L35">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="35">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.current_tool_name_sent: <span class="hljs-built_in">bool</span> = <span class="hljs-literal">False</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L36">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="36">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.prev_tool_call_arr: <span class="hljs-built_in">list</span>[<span class="hljs-built_in">dict</span>] = []<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L37">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="37">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.current_tool_id: <span class="hljs-built_in">int</span> = -<span class="hljs-number">1</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L38">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="38">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.streamed_args_for_tool: <span class="hljs-built_in">list</span>[<span class="hljs-built_in">str</span>] = []<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L39">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="39">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L40">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="40">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-comment"># Sentinel tokens for streaming mode</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L41">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="41">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.tool_call_start_token: <span class="hljs-built_in">str</span> = <span class="hljs-string">&quot;&lt;tool_call&gt;&quot;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L42">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="42">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.tool_call_end_token: <span class="hljs-built_in">str</span> = <span class="hljs-string">&quot;&lt;/tool_call&gt;&quot;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L43">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="43">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.tool_call_prefix: <span class="hljs-built_in">str</span> = <span class="hljs-string">&quot;&lt;function=&quot;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L44">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="44">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.function_end_token: <span class="hljs-built_in">str</span> = <span class="hljs-string">&quot;&lt;/function&gt;&quot;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L45">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="45">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.parameter_prefix: <span class="hljs-built_in">str</span> = <span class="hljs-string">&quot;&lt;parameter=&quot;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L46">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="46">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.parameter_end_token: <span class="hljs-built_in">str</span> = <span class="hljs-string">&quot;&lt;/parameter&gt;&quot;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L47">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="47">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.is_tool_call_started: <span class="hljs-built_in">bool</span> = <span class="hljs-literal">False</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L48">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="48">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.failed_count: <span class="hljs-built_in">int</span> = <span class="hljs-number">0</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L49">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="49">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L50">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="50">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-comment"># Enhanced streaming state - reset for each new message</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L51">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="51">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self._reset_streaming_state()<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L52">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="52">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L53">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="53">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-comment"># Regex patterns</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L54">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="54">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.tool_call_complete_regex = re.<span class="hljs-built_in">compile</span>(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L55">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="55">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-string">r&quot;&lt;tool_call&gt;(.*?)&lt;/tool_call&gt;&quot;</span>, re.DOTALL<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L56">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="56">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L57">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="57">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.tool_call_regex = re.<span class="hljs-built_in">compile</span>(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L58">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="58">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-string">r&quot;&lt;tool_call&gt;(.*?)&lt;/tool_call&gt;|&lt;tool_call&gt;(.*?)$&quot;</span>, re.DOTALL<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L59">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="59">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L60">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="60">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.tool_call_function_regex = re.<span class="hljs-built_in">compile</span>(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L61">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="61">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-string">r&quot;&lt;function=(.*?)&lt;/function&gt;|&lt;function=(.*)$&quot;</span>, re.DOTALL<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L62">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="62">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L63">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="63">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.tool_call_parameter_regex = re.<span class="hljs-built_in">compile</span>(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L64">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="64">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-string">r&quot;&lt;parameter=(.*?)&lt;/parameter&gt;|&lt;parameter=(.*?)$&quot;</span>, re.DOTALL<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L65">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="65">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L66">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="66">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L67">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="67">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> self.model_tokenizer:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L68">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="68">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">raise</span> ValueError(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L69">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="69">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-string">&quot;The model tokenizer must be passed to the ToolParser &quot;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L70">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="70">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-string">&quot;constructor during construction.&quot;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L71">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="71">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L72">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="72">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L73">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="73">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.tool_call_start_token_id = self.vocab.get(self.tool_call_start_token)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L74">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="74">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.tool_call_end_token_id = self.vocab.get(self.tool_call_end_token)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L75">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="75">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L76">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="76">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">if</span> self.tool_call_start_token_id <span class="hljs-keyword">is</span> <span class="hljs-literal">None</span> <span class="hljs-keyword">or</span> self.tool_call_end_token_id <span class="hljs-keyword">is</span> <span class="hljs-literal">None</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L77">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="77">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">raise</span> RuntimeError(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L78">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="78">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-string">&quot;Qwen3 XML Tool parser could not locate tool call start/end &quot;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L79">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="79">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-string">&quot;tokens in the tokenizer!&quot;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L80">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="80">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L81">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="81">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L82">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="82">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        logger.info(<span class="hljs-string">f&quot;vLLM Successfully import tool parser <span class="hljs-subst">{self.__class__.__name__}</span> !&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L83">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="83">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L84">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="84">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->    <span class="hljs-keyword">def</span> <span class="hljs-title function_">_generate_tool_call_id</span>(<span class="hljs-params">self</span>) -&gt; <span class="hljs-built_in">str</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L85">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="85">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-string">&quot;&quot;&quot;Generate a unique tool call ID.&quot;&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L86">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="86">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">return</span> <span class="hljs-string">f&quot;call_<span class="hljs-subst">{uuid.uuid4().<span class="hljs-built_in">hex</span>[:<span class="hljs-number">24</span>]}</span>&quot;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L87">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="87">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L88">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="88">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->    <span class="hljs-keyword">def</span> <span class="hljs-title function_">_reset_streaming_state</span>(<span class="hljs-params">self</span>):<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L89">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="89">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-string">&quot;&quot;&quot;Reset all streaming state.&quot;&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L90">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="90">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.current_tool_index = <span class="hljs-number">0</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L91">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="91">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.is_tool_call_started = <span class="hljs-literal">False</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L92">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="92">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.header_sent = <span class="hljs-literal">False</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L93">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="93">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.current_tool_id = <span class="hljs-literal">None</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L94">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="94">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.current_function_name = <span class="hljs-literal">None</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L95">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="95">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.current_param_name = <span class="hljs-literal">None</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L96">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="96">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.current_param_value = <span class="hljs-string">&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L97">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="97">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.param_count = <span class="hljs-number">0</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L98">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="98">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.in_param = <span class="hljs-literal">False</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L99">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="99">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.in_function = <span class="hljs-literal">False</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L100">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="100">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.accumulated_text = <span class="hljs-string">&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L101">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="101">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.json_started = <span class="hljs-literal">False</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L102">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="102">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.json_closed = <span class="hljs-literal">False</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L103">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="103">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L104">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="104">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->    <span class="hljs-keyword">def</span> <span class="hljs-title function_">_parse_xml_function_call</span>(<span class="hljs-params"></span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L105">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="105">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-params">        self, function_call_str: <span class="hljs-built_in">str</span>, tools: <span class="hljs-type">Optional</span>[<span class="hljs-built_in">list</span>[ChatCompletionToolsParam]]</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L106">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="106">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-params">    </span>) -&gt; <span class="hljs-type">Optional</span>[ToolCall]:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L107">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="107">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">def</span> <span class="hljs-title function_">get_arguments_config</span>(<span class="hljs-params">func_name: <span class="hljs-built_in">str</span></span>) -&gt; <span class="hljs-built_in">dict</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L108">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="108">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">if</span> tools <span class="hljs-keyword">is</span> <span class="hljs-literal">None</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L109">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="109">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">return</span> {}<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L110">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="110">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">for</span> config <span class="hljs-keyword">in</span> tools:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L111">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="111">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> <span class="hljs-built_in">hasattr</span>(config, <span class="hljs-string">&quot;type&quot;</span>) <span class="hljs-keyword">or</span> <span class="hljs-keyword">not</span> (<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L112">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="112">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-built_in">hasattr</span>(config, <span class="hljs-string">&quot;function&quot;</span>) <span class="hljs-keyword">and</span> <span class="hljs-built_in">hasattr</span>(config.function, <span class="hljs-string">&quot;name&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L113">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="113">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                ):<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L114">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="114">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-keyword">continue</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L115">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="115">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">if</span> config.<span class="hljs-built_in">type</span> == <span class="hljs-string">&quot;function&quot;</span> <span class="hljs-keyword">and</span> config.function.name == func_name:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L116">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="116">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> <span class="hljs-built_in">hasattr</span>(config.function, <span class="hljs-string">&quot;parameters&quot;</span>):<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L117">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="117">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        <span class="hljs-keyword">return</span> {}<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L118">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="118">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    params = config.function.parameters<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L119">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="119">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-keyword">if</span> <span class="hljs-built_in">isinstance</span>(params, <span class="hljs-built_in">dict</span>) <span class="hljs-keyword">and</span> <span class="hljs-string">&quot;properties&quot;</span> <span class="hljs-keyword">in</span> params:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L120">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="120">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        <span class="hljs-keyword">return</span> params[<span class="hljs-string">&quot;properties&quot;</span>]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L121">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="121">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-keyword">elif</span> <span class="hljs-built_in">isinstance</span>(params, <span class="hljs-built_in">dict</span>):<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L122">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="122">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        <span class="hljs-keyword">return</span> params<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L123">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="123">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-keyword">else</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L124">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="124">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        <span class="hljs-keyword">return</span> {}<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L125">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="125">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            logger.warning(<span class="hljs-string">f&quot;Tool &#x27;<span class="hljs-subst">{func_name}</span>&#x27; is not defined in the tools list.&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L126">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="126">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">return</span> {}<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L127">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="127">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L128">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="128">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">def</span> <span class="hljs-title function_">convert_param_value</span>(<span class="hljs-params"></span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L129">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="129">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-params">            param_value: <span class="hljs-built_in">str</span>, param_name: <span class="hljs-built_in">str</span>, param_config: <span class="hljs-built_in">dict</span>, func_name: <span class="hljs-built_in">str</span></span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L130">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="130">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-params">        </span>) -&gt; <span class="hljs-type">Any</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L131">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="131">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-comment"># Handle null value for any type</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L132">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="132">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">if</span> param_value.lower() == <span class="hljs-string">&quot;null&quot;</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L133">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="133">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">return</span> <span class="hljs-literal">None</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L134">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="134">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L135">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="135">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">if</span> param_name <span class="hljs-keyword">not</span> <span class="hljs-keyword">in</span> param_config:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L136">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="136">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">if</span> param_config != {}:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L137">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="137">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    logger.warning(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L138">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="138">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        <span class="hljs-string">f&quot;Parsed parameter &#x27;<span class="hljs-subst">{param_name}</span>&#x27; is not defined in the tool &quot;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L139">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="139">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        <span class="hljs-string">f&quot;parameters for tool &#x27;<span class="hljs-subst">{func_name}</span>&#x27;, directly returning the string value.&quot;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L140">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="140">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L141">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="141">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">return</span> param_value<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L142">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="142">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L143">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="143">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">if</span> (<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L144">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="144">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-built_in">isinstance</span>(param_config[param_name], <span class="hljs-built_in">dict</span>)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L145">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="145">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">and</span> <span class="hljs-string">&quot;type&quot;</span> <span class="hljs-keyword">in</span> param_config[param_name]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L146">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="146">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            ):<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L147">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="147">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                param_type = <span class="hljs-built_in">str</span>(param_config[param_name][<span class="hljs-string">&quot;type&quot;</span>]).strip().lower()<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L148">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="148">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">else</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L149">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="149">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                param_type = <span class="hljs-string">&quot;string&quot;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L150">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="150">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">if</span> param_type <span class="hljs-keyword">in</span> [<span class="hljs-string">&quot;string&quot;</span>, <span class="hljs-string">&quot;str&quot;</span>, <span class="hljs-string">&quot;text&quot;</span>, <span class="hljs-string">&quot;varchar&quot;</span>, <span class="hljs-string">&quot;char&quot;</span>, <span class="hljs-string">&quot;enum&quot;</span>]:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L151">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="151">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">return</span> param_value<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L152">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="152">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">elif</span> (<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L153">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="153">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                param_type.startswith(<span class="hljs-string">&quot;int&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L154">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="154">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">or</span> param_type.startswith(<span class="hljs-string">&quot;uint&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L155">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="155">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">or</span> param_type.startswith(<span class="hljs-string">&quot;long&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L156">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="156">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">or</span> param_type.startswith(<span class="hljs-string">&quot;short&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L157">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="157">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">or</span> param_type.startswith(<span class="hljs-string">&quot;unsigned&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L158">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="158">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            ):<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L159">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="159">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">try</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L160">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="160">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    param_value = <span class="hljs-built_in">int</span>(param_value)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L161">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="161">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">except</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L162">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="162">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    logger.warning(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L163">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="163">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        <span class="hljs-string">f&quot;Parsed value &#x27;<span class="hljs-subst">{param_value}</span>&#x27; of parameter &#x27;<span class="hljs-subst">{param_name}</span>&#x27; is not an integer in tool &quot;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L164">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="164">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        <span class="hljs-string">f&quot;&#x27;<span class="hljs-subst">{func_name}</span>&#x27;, degenerating to string.&quot;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L165">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="165">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L166">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="166">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">return</span> param_value<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L167">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="167">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">elif</span> param_type.startswith(<span class="hljs-string">&quot;num&quot;</span>) <span class="hljs-keyword">or</span> param_type.startswith(<span class="hljs-string">&quot;float&quot;</span>):<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L168">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="168">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">try</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L169">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="169">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    float_param_value = <span class="hljs-built_in">float</span>(param_value)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L170">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="170">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    param_value = float_param_value <span class="hljs-keyword">if</span> float_param_value - <span class="hljs-built_in">int</span>(float_param_value) != <span class="hljs-number">0</span> <span class="hljs-keyword">else</span> <span class="hljs-built_in">int</span>(float_param_value)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L171">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="171">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">except</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L172">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="172">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    logger.warning(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L173">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="173">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        <span class="hljs-string">f&quot;Parsed value &#x27;<span class="hljs-subst">{param_value}</span>&#x27; of parameter &#x27;<span class="hljs-subst">{param_name}</span>&#x27; is not a float in tool &quot;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L174">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="174">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        <span class="hljs-string">f&quot;&#x27;<span class="hljs-subst">{func_name}</span>&#x27;, degenerating to string.&quot;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L175">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="175">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L176">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="176">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">return</span> param_value<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L177">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="177">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">elif</span> param_type <span class="hljs-keyword">in</span> [<span class="hljs-string">&quot;boolean&quot;</span>, <span class="hljs-string">&quot;bool&quot;</span>, <span class="hljs-string">&quot;binary&quot;</span>]:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L178">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="178">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                param_value = param_value.lower()<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L179">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="179">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">if</span> param_value <span class="hljs-keyword">not</span> <span class="hljs-keyword">in</span> [<span class="hljs-string">&quot;true&quot;</span>, <span class="hljs-string">&quot;false&quot;</span>]:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L180">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="180">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    logger.warning(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L181">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="181">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        <span class="hljs-string">f&quot;Parsed value &#x27;<span class="hljs-subst">{param_value}</span>&#x27; of parameter &#x27;<span class="hljs-subst">{param_name}</span>&#x27; is not a boolean (`true` of `false`) in tool &#x27;<span class="hljs-subst">{func_name}</span>&#x27;, degenerating to false.&quot;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L182">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="182">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L183">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="183">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">return</span> param_value == <span class="hljs-string">&quot;true&quot;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L184">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="184">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">else</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L185">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="185">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">if</span> param_type == <span class="hljs-string">&quot;object&quot;</span> <span class="hljs-keyword">or</span> param_type.startswith(<span class="hljs-string">&quot;dict&quot;</span>):<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L186">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="186">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-keyword">try</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L187">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="187">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        param_value = json.loads(param_value)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L188">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="188">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        <span class="hljs-keyword">return</span> param_value<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L189">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="189">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-keyword">except</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L190">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="190">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        logger.warning(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L191">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="191">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                            <span class="hljs-string">f&quot;Parsed value &#x27;<span class="hljs-subst">{param_value}</span>&#x27; of parameter &#x27;<span class="hljs-subst">{param_name}</span>&#x27; is not a valid JSON object in tool &quot;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L192">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="192">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                            <span class="hljs-string">f&quot;&#x27;<span class="hljs-subst">{func_name}</span>&#x27;, will try other methods to parse it.&quot;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L193">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="193">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L194">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="194">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">try</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L195">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="195">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    param_value = <span class="hljs-built_in">eval</span>(param_value)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L196">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="196">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">except</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L197">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="197">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    logger.warning(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L198">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="198">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        <span class="hljs-string">f&quot;Parsed value &#x27;<span class="hljs-subst">{param_value}</span>&#x27; of parameter &#x27;<span class="hljs-subst">{param_name}</span>&#x27; cannot be converted via Python `eval()` in tool &#x27;<span class="hljs-subst">{func_name}</span>&#x27;, degenerating to string.&quot;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L199">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="199">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L200">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="200">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">return</span> param_value<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L201">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="201">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L202">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="202">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-comment"># Extract function name</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L203">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="203">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        end_index = function_call_str.index(<span class="hljs-string">&quot;&gt;&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L204">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="204">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        function_name = function_call_str[:end_index]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L205">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="205">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        param_config = get_arguments_config(function_name)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L206">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="206">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        parameters = function_call_str[end_index + <span class="hljs-number">1</span> :]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L207">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="207">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        param_dict = {}<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L208">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="208">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">for</span> <span class="hljs-keyword">match</span> <span class="hljs-keyword">in</span> self.tool_call_parameter_regex.findall(parameters):<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L209">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="209">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            match_text = <span class="hljs-keyword">match</span>[<span class="hljs-number">0</span>] <span class="hljs-keyword">if</span> <span class="hljs-keyword">match</span>[<span class="hljs-number">0</span>] <span class="hljs-keyword">else</span> <span class="hljs-keyword">match</span>[<span class="hljs-number">1</span>]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L210">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="210">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            idx = match_text.index(<span class="hljs-string">&quot;&gt;&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L211">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="211">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            param_name = match_text[:idx]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L212">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="212">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            param_value = <span class="hljs-built_in">str</span>(match_text[idx + <span class="hljs-number">1</span> :])<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L213">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="213">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-comment"># Remove prefix and trailing \n</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L214">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="214">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">if</span> param_value.startswith(<span class="hljs-string">&quot;\n&quot;</span>):<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L215">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="215">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                param_value = param_value[<span class="hljs-number">1</span>:]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L216">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="216">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">if</span> param_value.endswith(<span class="hljs-string">&quot;\n&quot;</span>):<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L217">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="217">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                param_value = param_value[:-<span class="hljs-number">1</span>]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L218">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="218">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L219">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="219">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            param_dict[param_name] = convert_param_value(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L220">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="220">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                param_value, param_name, param_config, function_name<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L221">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="221">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L222">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="222">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">return</span> ToolCall(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L223">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="223">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-built_in">type</span>=<span class="hljs-string">&quot;function&quot;</span>,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L224">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="224">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            function=FunctionCall(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L225">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="225">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                name=function_name, arguments=json.dumps(param_dict, ensure_ascii=<span class="hljs-literal">False</span>)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L226">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="226">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            ),<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L227">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="227">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L228">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="228">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L229">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="229">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->    <span class="hljs-keyword">def</span> <span class="hljs-title function_">_get_function_calls</span>(<span class="hljs-params">self, model_output: <span class="hljs-built_in">str</span></span>) -&gt; <span class="hljs-type">List</span>[<span class="hljs-built_in">str</span>]:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L230">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="230">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-comment"># Find all tool calls</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L231">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="231">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        matched_ranges = self.tool_call_regex.findall(model_output)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L232">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="232">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        raw_tool_calls = [<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L233">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="233">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">match</span>[<span class="hljs-number">0</span>] <span class="hljs-keyword">if</span> <span class="hljs-keyword">match</span>[<span class="hljs-number">0</span>] <span class="hljs-keyword">else</span> <span class="hljs-keyword">match</span>[<span class="hljs-number">1</span>] <span class="hljs-keyword">for</span> <span class="hljs-keyword">match</span> <span class="hljs-keyword">in</span> matched_ranges<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L234">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="234">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        ]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L235">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="235">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L236">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="236">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-comment"># Back-off strategy if no tool_call tags found</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L237">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="237">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">if</span> <span class="hljs-built_in">len</span>(raw_tool_calls) == <span class="hljs-number">0</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L238">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="238">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            raw_tool_calls = [model_output]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L239">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="239">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L240">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="240">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        raw_function_calls = []<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L241">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="241">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">for</span> tool_call <span class="hljs-keyword">in</span> raw_tool_calls:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L242">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="242">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            raw_function_calls.extend(self.tool_call_function_regex.findall(tool_call))<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L243">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="243">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L244">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="244">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        function_calls = [<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L245">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="245">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">match</span>[<span class="hljs-number">0</span>] <span class="hljs-keyword">if</span> <span class="hljs-keyword">match</span>[<span class="hljs-number">0</span>] <span class="hljs-keyword">else</span> <span class="hljs-keyword">match</span>[<span class="hljs-number">1</span>] <span class="hljs-keyword">for</span> <span class="hljs-keyword">match</span> <span class="hljs-keyword">in</span> raw_function_calls<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L246">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="246">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        ]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L247">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="247">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">return</span> function_calls<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L248">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="248">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L249">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="249">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->    <span class="hljs-keyword">def</span> <span class="hljs-title function_">extract_tool_calls</span>(<span class="hljs-params"></span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L250">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="250">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-params">        self,</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L251">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="251">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-params">        model_output: <span class="hljs-built_in">str</span>,</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L252">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="252">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-params">        request: ChatCompletionRequest,</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L253">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="253">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-params">    </span>) -&gt; ExtractedToolCallInformation:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L254">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="254">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-comment"># Quick check to avoid unnecessary processing</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L255">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="255">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">if</span> self.tool_call_prefix <span class="hljs-keyword">not</span> <span class="hljs-keyword">in</span> model_output:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L256">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="256">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">return</span> ExtractedToolCallInformation(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L257">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="257">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                tools_called=<span class="hljs-literal">False</span>, tool_calls=[], content=model_output<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L258">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="258">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L259">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="259">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L260">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="260">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">try</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L261">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="261">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            function_calls = self._get_function_calls(model_output)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L262">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="262">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">if</span> <span class="hljs-built_in">len</span>(function_calls) == <span class="hljs-number">0</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L263">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="263">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">return</span> ExtractedToolCallInformation(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L264">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="264">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    tools_called=<span class="hljs-literal">False</span>, tool_calls=[], content=model_output<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L265">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="265">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L266">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="266">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L267">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="267">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            tool_calls = [<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L268">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="268">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                self._parse_xml_function_call(function_call_str, request.tools)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L269">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="269">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">for</span> function_call_str <span class="hljs-keyword">in</span> function_calls<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L270">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="270">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            ]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L271">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="271">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L272">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="272">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-comment"># Populate prev_tool_call_arr for serving layer to set finish_reason</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L273">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="273">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            self.prev_tool_call_arr.clear()  <span class="hljs-comment"># Clear previous calls</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L274">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="274">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">for</span> tool_call <span class="hljs-keyword">in</span> tool_calls:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L275">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="275">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">if</span> tool_call:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L276">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="276">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    self.prev_tool_call_arr.append(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L277">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="277">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        {<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L278">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="278">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                            <span class="hljs-string">&quot;name&quot;</span>: tool_call.function.name,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L279">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="279">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                            <span class="hljs-string">&quot;arguments&quot;</span>: tool_call.function.arguments,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L280">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="280">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        }<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L281">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="281">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L282">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="282">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L283">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="283">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-comment"># Extract content before tool calls</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L284">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="284">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            content_index = model_output.find(self.tool_call_start_token)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L285">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="285">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            content_index = (<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L286">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="286">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                content_index<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L287">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="287">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">if</span> content_index &gt;= <span class="hljs-number">0</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L288">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="288">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">else</span> model_output.find(self.tool_call_prefix)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L289">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="289">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L290">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="290">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            content = model_output[:content_index]  <span class="hljs-comment"># .rstrip()</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L291">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="291">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L292">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="292">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">return</span> ExtractedToolCallInformation(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L293">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="293">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                tools_called=(<span class="hljs-built_in">len</span>(tool_calls) &gt; <span class="hljs-number">0</span>),<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L294">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="294">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                tool_calls=tool_calls,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L295">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="295">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                content=content <span class="hljs-keyword">if</span> content <span class="hljs-keyword">else</span> <span class="hljs-literal">None</span>,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L296">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="296">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L297">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="297">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L298">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="298">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">except</span> Exception:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L299">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="299">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            logger.exception(<span class="hljs-string">&quot;Error in extracting tool call from response.&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L300">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="300">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">return</span> ExtractedToolCallInformation(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L301">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="301">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                tools_called=<span class="hljs-literal">False</span>, tool_calls=[], content=model_output<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L302">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="302">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L303">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="303">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L304">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="304">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->    <span class="hljs-keyword">def</span> <span class="hljs-title function_">extract_tool_calls_streaming</span>(<span class="hljs-params"></span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L305">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="305">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-params">        self,</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L306">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="306">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-params">        previous_text: <span class="hljs-built_in">str</span>,</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L307">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="307">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-params">        current_text: <span class="hljs-built_in">str</span>,</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L308">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="308">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-params">        delta_text: <span class="hljs-built_in">str</span>,</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L309">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="309">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-params">        previous_token_ids: <span class="hljs-type">Sequence</span>[<span class="hljs-built_in">int</span>],</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L310">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="310">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-params">        current_token_ids: <span class="hljs-type">Sequence</span>[<span class="hljs-built_in">int</span>],</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L311">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="311">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-params">        delta_token_ids: <span class="hljs-type">Sequence</span>[<span class="hljs-built_in">int</span>],</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L312">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="312">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-params">        request: ChatCompletionRequest,</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L313">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="313">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START --><span class="hljs-params">    </span>) -&gt; <span class="hljs-type">Union</span>[DeltaMessage, <span class="hljs-literal">None</span>]:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L314">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="314">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-comment"># If no delta text, return None unless it&#x27;s an EOS token after tool calls</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L315">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="315">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> delta_text:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L316">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="316">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-comment"># Check if this is an EOS token after all tool calls are complete</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L317">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="317">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-comment"># We check for tool calls in the text even if is_tool_call_started is False</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L318">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="318">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-comment"># because it might have been reset after processing all tools</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L319">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="319">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">if</span> delta_token_ids <span class="hljs-keyword">and</span> self.tool_call_end_token_id <span class="hljs-keyword">not</span> <span class="hljs-keyword">in</span> delta_token_ids:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L320">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="320">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-comment"># Count complete tool calls</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L321">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="321">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                complete_calls = <span class="hljs-built_in">len</span>(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L322">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="322">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    self.tool_call_complete_regex.findall(current_text)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L323">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="323">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L324">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="324">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L325">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="325">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-comment"># If we have completed tool calls and populated prev_tool_call_arr</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L326">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="326">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">if</span> complete_calls &gt; <span class="hljs-number">0</span> <span class="hljs-keyword">and</span> <span class="hljs-built_in">len</span>(self.prev_tool_call_arr) &gt; <span class="hljs-number">0</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L327">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="327">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-comment"># Check if all tool calls are closed</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L328">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="328">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    open_calls = current_text.count(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L329">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="329">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        self.tool_call_start_token<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L330">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="330">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    ) - current_text.count(self.tool_call_end_token)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L331">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="331">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-keyword">if</span> open_calls == <span class="hljs-number">0</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L332">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="332">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        <span class="hljs-comment"># Return empty delta message to allow finish_reason processing</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L333">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="333">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        <span class="hljs-keyword">return</span> DeltaMessage(content=<span class="hljs-string">&quot;&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L334">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="334">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">elif</span> <span class="hljs-keyword">not</span> self.is_tool_call_started <span class="hljs-keyword">and</span> current_text:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L335">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="335">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-comment"># This is a regular content response that&#x27;s now complete</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L336">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="336">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-keyword">return</span> DeltaMessage(content=<span class="hljs-string">&quot;&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L337">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="337">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">return</span> <span class="hljs-literal">None</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L338">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="338">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L339">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="339">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-comment"># Check if this is the first call (reset state if needed)</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L340">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="340">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> previous_text:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L341">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="341">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            self._reset_streaming_state()<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L342">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="342">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L343">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="343">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-comment"># Update accumulated text</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L344">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="344">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        self.accumulated_text = current_text<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L345">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="345">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L346">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="346">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-comment"># Check if we need to advance to next tool</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L347">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="347">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">if</span> self.json_closed <span class="hljs-keyword">and</span> <span class="hljs-keyword">not</span> self.in_function:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L348">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="348">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-comment"># Check if this tool call has ended</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L349">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="349">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            tool_ends = current_text.count(self.tool_call_end_token)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L350">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="350">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">if</span> tool_ends &gt; self.current_tool_index:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L351">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="351">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-comment"># This tool has ended, advance to next</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L352">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="352">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                self.current_tool_index += <span class="hljs-number">1</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L353">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="353">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                self.header_sent = <span class="hljs-literal">False</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L354">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="354">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                self.param_count = <span class="hljs-number">0</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L355">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="355">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                self.json_started = <span class="hljs-literal">False</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L356">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="356">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                self.json_closed = <span class="hljs-literal">False</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L357">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="357">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L358">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="358">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-comment"># Check if there are more tool calls</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L359">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="359">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                tool_starts = current_text.count(self.tool_call_start_token)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L360">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="360">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">if</span> self.current_tool_index &gt;= tool_starts:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L361">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="361">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-comment"># No more tool calls</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L362">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="362">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    self.is_tool_call_started = <span class="hljs-literal">False</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L363">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="363">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-comment"># Continue processing next tool</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L364">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="364">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">return</span> <span class="hljs-literal">None</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L365">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="365">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L366">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="366">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-comment"># Handle normal content before tool calls</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L367">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="367">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> self.is_tool_call_started:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L368">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="368">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-comment"># Check if tool call is starting</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L369">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="369">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">if</span> (<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L370">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="370">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                self.tool_call_start_token_id <span class="hljs-keyword">in</span> delta_token_ids<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L371">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="371">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">or</span> self.tool_call_start_token <span class="hljs-keyword">in</span> delta_text<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L372">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="372">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            ):<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L373">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="373">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                self.is_tool_call_started = <span class="hljs-literal">True</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L374">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="374">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-comment"># Return any content before the tool call</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L375">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="375">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">if</span> self.tool_call_start_token <span class="hljs-keyword">in</span> delta_text:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L376">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="376">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    content_before = delta_text[<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L377">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="377">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        : delta_text.index(self.tool_call_start_token)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L378">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="378">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    ]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L379">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="379">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-keyword">if</span> content_before:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L380">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="380">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        <span class="hljs-keyword">return</span> DeltaMessage(content=content_before)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L381">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="381">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">return</span> <span class="hljs-literal">None</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L382">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="382">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">else</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L383">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="383">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-comment"># Check if we&#x27;re between tool calls - skip whitespace</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L384">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="384">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">if</span> current_text.rstrip().endswith(self.tool_call_end_token):<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L385">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="385">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-comment"># We just ended a tool call, skip whitespace</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L386">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="386">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-keyword">if</span> delta_text.strip() == <span class="hljs-string">&quot;&quot;</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L387">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="387">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        <span class="hljs-keyword">return</span> <span class="hljs-literal">None</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L388">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="388">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-comment"># Normal content, no tool call</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L389">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="389">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">return</span> DeltaMessage(content=delta_text)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L390">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="390">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L391">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="391">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-comment"># Check if we&#x27;re between tool calls (waiting for next one)</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L392">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="392">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-comment"># Count tool calls we&#x27;ve seen vs processed</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L393">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="393">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        tool_starts_count = current_text.count(self.tool_call_start_token)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L394">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="394">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">if</span> self.current_tool_index &gt;= tool_starts_count:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L395">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="395">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-comment"># We&#x27;re past all tool calls, shouldn&#x27;t be here</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L396">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="396">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">return</span> <span class="hljs-literal">None</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L397">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="397">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L398">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="398">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-comment"># We&#x27;re in a tool call, find the current tool call portion</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L399">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="399">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-comment"># Need to find the correct tool call based on current_tool_index</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L400">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="400">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        tool_starts = []<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L401">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="401">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        idx = <span class="hljs-number">0</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L402">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="402">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">while</span> <span class="hljs-literal">True</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L403">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="403">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            idx = current_text.find(self.tool_call_start_token, idx)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L404">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="404">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">if</span> idx == -<span class="hljs-number">1</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L405">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="405">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">break</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L406">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="406">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            tool_starts.append(idx)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L407">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="407">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            idx += <span class="hljs-built_in">len</span>(self.tool_call_start_token)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L408">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="408">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L409">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="409">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">if</span> self.current_tool_index &gt;= <span class="hljs-built_in">len</span>(tool_starts):<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L410">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="410">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-comment"># No more tool calls to process yet</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L411">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="411">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">return</span> <span class="hljs-literal">None</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L412">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="412">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L413">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="413">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        tool_start_idx = tool_starts[self.current_tool_index]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L414">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="414">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-comment"># Find where this tool call ends (or current position if not ended yet)</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L415">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="415">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        tool_end_idx = current_text.find(self.tool_call_end_token, tool_start_idx)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L416">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="416">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">if</span> tool_end_idx == -<span class="hljs-number">1</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L417">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="417">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            tool_text = current_text[tool_start_idx:]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L418">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="418">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">else</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L419">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="419">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            tool_text = current_text[<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L420">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="420">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                tool_start_idx : tool_end_idx + <span class="hljs-built_in">len</span>(self.tool_call_end_token)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L421">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="421">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            ]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L422">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="422">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L423">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="423">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-comment"># Looking for function header</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L424">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="424">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> self.header_sent:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L425">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="425">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">if</span> self.tool_call_prefix <span class="hljs-keyword">in</span> tool_text:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L426">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="426">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                func_start = tool_text.find(self.tool_call_prefix) + <span class="hljs-built_in">len</span>(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L427">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="427">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    self.tool_call_prefix<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L428">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="428">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L429">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="429">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                func_end = tool_text.find(<span class="hljs-string">&quot;&gt;&quot;</span>, func_start)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L430">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="430">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L431">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="431">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">if</span> func_end != -<span class="hljs-number">1</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L432">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="432">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-comment"># Found complete function name</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L433">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="433">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    self.current_function_name = tool_text[func_start:func_end]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L434">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="434">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    self.current_tool_id = self._generate_tool_call_id()<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L435">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="435">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    self.header_sent = <span class="hljs-literal">True</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L436">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="436">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    self.in_function = <span class="hljs-literal">True</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L437">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="437">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L438">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="438">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-comment"># IMPORTANT: Add to prev_tool_call_arr immediately when we detect a tool call</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L439">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="439">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-comment"># This ensures finish_reason=&quot;tool_calls&quot; even if parsing isn&#x27;t complete</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L440">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="440">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    already_added = <span class="hljs-built_in">any</span>(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L441">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="441">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        tool.get(<span class="hljs-string">&quot;name&quot;</span>) == self.current_function_name<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L442">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="442">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        <span class="hljs-keyword">for</span> tool <span class="hljs-keyword">in</span> self.prev_tool_call_arr<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L443">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="443">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L444">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="444">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> already_added:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L445">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="445">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        self.prev_tool_call_arr.append(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L446">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="446">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                            {<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L447">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="447">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                <span class="hljs-string">&quot;name&quot;</span>: self.current_function_name,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L448">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="448">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                <span class="hljs-string">&quot;arguments&quot;</span>: <span class="hljs-string">&quot;{}&quot;</span>,  <span class="hljs-comment"># Placeholder, will be updated later</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L449">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="449">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                            }<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L450">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="450">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L451">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="451">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L452">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="452">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-comment"># Send header with function info</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L453">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="453">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-keyword">return</span> DeltaMessage(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L454">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="454">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        tool_calls=[<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L455">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="455">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                            DeltaToolCall(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L456">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="456">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                index=self.current_tool_index,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L457">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="457">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                <span class="hljs-built_in">id</span>=self.current_tool_id,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L458">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="458">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                function=DeltaFunctionCall(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L459">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="459">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                    name=self.current_function_name, arguments=<span class="hljs-string">&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L460">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="460">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                ),<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L461">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="461">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                <span class="hljs-built_in">type</span>=<span class="hljs-string">&quot;function&quot;</span>,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L462">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="462">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                            )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L463">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="463">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        ]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L464">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="464">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L465">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="465">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">return</span> <span class="hljs-literal">None</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L466">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="466">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L467">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="467">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-comment"># We&#x27;ve sent header, now handle function body</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L468">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="468">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">if</span> self.in_function:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L469">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="469">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-comment"># Send opening brace if not sent yet</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L470">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="470">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> self.json_started <span class="hljs-keyword">and</span> <span class="hljs-keyword">not</span> self.parameter_prefix <span class="hljs-keyword">in</span> delta_text:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L471">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="471">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                self.json_started = <span class="hljs-literal">True</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L472">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="472">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">return</span> DeltaMessage(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L473">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="473">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    tool_calls=[<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L474">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="474">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        DeltaToolCall(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L475">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="475">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                            index=self.current_tool_index,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L476">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="476">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                            function=DeltaFunctionCall(arguments=<span class="hljs-string">&quot;{&quot;</span>),<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L477">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="477">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L478">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="478">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    ]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L479">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="479">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L480">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="480">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L481">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="481">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-comment"># Make sure json_started is set if we&#x27;re processing parameters</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L482">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="482">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> self.json_started:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L483">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="483">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                self.json_started = <span class="hljs-literal">True</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L484">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="484">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L485">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="485">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-comment"># Check for function end in accumulated text</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L486">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="486">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> self.json_closed <span class="hljs-keyword">and</span> self.function_end_token <span class="hljs-keyword">in</span> tool_text:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L487">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="487">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-comment"># Close JSON</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L488">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="488">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                self.json_closed = <span class="hljs-literal">True</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L489">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="489">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L490">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="490">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-comment"># Extract the complete tool call to update prev_tool_call_arr with final arguments</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L491">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="491">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-comment"># Find the function content</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L492">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="492">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                func_start = tool_text.find(self.tool_call_prefix) + <span class="hljs-built_in">len</span>(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L493">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="493">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    self.tool_call_prefix<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L494">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="494">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L495">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="495">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                func_content_end = tool_text.find(self.function_end_token, func_start)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L496">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="496">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">if</span> func_content_end != -<span class="hljs-number">1</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L497">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="497">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    func_content = tool_text[func_start:func_content_end]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L498">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="498">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-comment"># Parse to get the complete arguments</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L499">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="499">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-keyword">try</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L500">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="500">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        parsed_tool = self._parse_xml_function_call(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L501">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="501">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                            func_content, request.tools <span class="hljs-keyword">if</span> request <span class="hljs-keyword">else</span> <span class="hljs-literal">None</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L502">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="502">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L503">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="503">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        <span class="hljs-keyword">if</span> parsed_tool:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L504">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="504">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                            <span class="hljs-comment"># Update existing entry in prev_tool_call_arr with complete arguments</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L505">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="505">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                            <span class="hljs-keyword">for</span> i, tool <span class="hljs-keyword">in</span> <span class="hljs-built_in">enumerate</span>(self.prev_tool_call_arr):<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L506">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="506">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                <span class="hljs-keyword">if</span> tool.get(<span class="hljs-string">&quot;name&quot;</span>) == parsed_tool.function.name:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L507">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="507">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                    self.prev_tool_call_arr[i][<span class="hljs-string">&quot;arguments&quot;</span>] = (<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L508">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="508">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                        parsed_tool.function.arguments<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L509">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="509">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                    )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L510">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="510">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                    <span class="hljs-keyword">break</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L511">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="511">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-keyword">except</span> Exception:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L512">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="512">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        <span class="hljs-keyword">pass</span>  <span class="hljs-comment"># Ignore parsing errors during streaming</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L513">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="513">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L514">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="514">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                result = DeltaMessage(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L515">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="515">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    tool_calls=[<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L516">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="516">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        DeltaToolCall(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L517">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="517">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                            index=self.current_tool_index,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L518">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="518">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                            function=DeltaFunctionCall(arguments=<span class="hljs-string">&quot;}&quot;</span>),<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L519">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="519">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L520">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="520">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    ]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L521">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="521">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L522">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="522">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L523">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="523">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-comment"># Reset state for next tool</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L524">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="524">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                self.in_function = <span class="hljs-literal">False</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L525">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="525">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                self.json_closed = <span class="hljs-literal">True</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L526">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="526">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L527">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="527">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">return</span> result<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L528">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="528">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L529">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="529">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-comment"># Look for parameters</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L530">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="530">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-comment"># Count how many complete parameters we have processed</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L531">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="531">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            complete_params = tool_text.count(self.parameter_end_token)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L532">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="532">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L533">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="533">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-comment"># Check if we should start a new parameter</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L534">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="534">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> self.in_param <span class="hljs-keyword">and</span> self.param_count &lt; complete_params:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L535">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="535">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-comment"># Find the unprocessed parameter</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L536">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="536">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-comment"># Count parameter starts</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L537">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="537">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                param_starts = []<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L538">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="538">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                idx = <span class="hljs-number">0</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L539">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="539">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">while</span> <span class="hljs-literal">True</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L540">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="540">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    idx = tool_text.find(self.parameter_prefix, idx)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L541">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="541">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-keyword">if</span> idx == -<span class="hljs-number">1</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L542">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="542">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        <span class="hljs-keyword">break</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L543">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="543">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    param_starts.append(idx)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L544">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="544">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    idx += <span class="hljs-built_in">len</span>(self.parameter_prefix)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L545">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="545">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L546">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="546">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">if</span> <span class="hljs-built_in">len</span>(param_starts) &gt; self.param_count:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L547">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="547">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-comment"># Process the next parameter</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L548">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="548">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    param_idx = param_starts[self.param_count]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L549">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="549">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    param_start = param_idx + <span class="hljs-built_in">len</span>(self.parameter_prefix)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L550">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="550">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    remaining = tool_text[param_start:]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L551">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="551">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L552">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="552">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-keyword">if</span> <span class="hljs-string">&quot;&gt;&quot;</span> <span class="hljs-keyword">in</span> remaining:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L553">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="553">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        <span class="hljs-comment"># We have the complete parameter name</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L554">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="554">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        name_end = remaining.find(<span class="hljs-string">&quot;&gt;&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L555">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="555">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        self.current_param_name = remaining[:name_end]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L556">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="556">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L557">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="557">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        <span class="hljs-comment"># Find the parameter value</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L558">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="558">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        value_start = param_start + name_end + <span class="hljs-number">1</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L559">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="559">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        value_text = tool_text[value_start:]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L560">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="560">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        <span class="hljs-keyword">if</span> value_text.startswith(<span class="hljs-string">&quot;\n&quot;</span>):<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L561">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="561">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                            value_text = value_text[<span class="hljs-number">1</span>:]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L562">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="562">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L563">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="563">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        <span class="hljs-comment"># Find where this parameter ends</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L564">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="564">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        param_end_idx = value_text.find(self.parameter_end_token)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L565">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="565">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        <span class="hljs-keyword">if</span> param_end_idx != -<span class="hljs-number">1</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L566">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="566">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                            <span class="hljs-comment"># Complete parameter found</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L567">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="567">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                            param_value = value_text[:param_end_idx]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L568">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="568">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                            <span class="hljs-keyword">if</span> param_value.endswith(<span class="hljs-string">&quot;\n&quot;</span>):<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L569">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="569">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                param_value = param_value[:-<span class="hljs-number">1</span>]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L570">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="570">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L571">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="571">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                            <span class="hljs-comment"># Build complete JSON fragment for this parameter</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L572">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="572">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                            <span class="hljs-keyword">if</span> self.param_count == <span class="hljs-number">0</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L573">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="573">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                json_fragment = (<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L574">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="574">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                    <span class="hljs-string">&#x27;&quot;&#x27;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L575">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="575">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                    + self.current_param_name<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L576">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="576">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                    + <span class="hljs-string">&#x27;&quot;: &quot;&#x27;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L577">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="577">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                    + json.dumps(param_value)[<span class="hljs-number">1</span>:-<span class="hljs-number">1</span>]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L578">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="578">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                    + <span class="hljs-string">&#x27;&quot;&#x27;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L579">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="579">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L580">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="580">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                            <span class="hljs-keyword">else</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L581">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="581">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                json_fragment = (<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L582">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="582">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                    <span class="hljs-string">&#x27;, &quot;&#x27;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L583">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="583">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                    + self.current_param_name<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L584">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="584">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                    + <span class="hljs-string">&#x27;&quot;: &quot;&#x27;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L585">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="585">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                    + json.dumps(param_value)[<span class="hljs-number">1</span>:-<span class="hljs-number">1</span>]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L586">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="586">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                    + <span class="hljs-string">&#x27;&quot;&#x27;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L587">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="587">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L588">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="588">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L589">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="589">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                            self.param_count += <span class="hljs-number">1</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L590">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="590">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L591">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="591">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                            <span class="hljs-keyword">return</span> DeltaMessage(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L592">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="592">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                tool_calls=[<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L593">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="593">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                    DeltaToolCall(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L594">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="594">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                        index=self.current_tool_index,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L595">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="595">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                        function=DeltaFunctionCall(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L596">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="596">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                            arguments=json_fragment<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L597">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="597">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                        ),<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L598">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="598">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                    )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L599">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="599">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                ]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L600">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="600">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                            )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L601">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="601">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L602">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="602">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-comment"># Continue parameter value</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L603">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="603">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->            <span class="hljs-keyword">if</span> self.in_param:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L604">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="604">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">if</span> self.parameter_end_token <span class="hljs-keyword">in</span> delta_text:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L605">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="605">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-comment"># End of parameter</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L606">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="606">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    end_idx = delta_text.find(self.parameter_end_token)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L607">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="607">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    value_chunk = delta_text[:end_idx]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L608">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="608">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L609">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="609">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-comment"># Skip past &gt; if at start</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L610">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="610">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> self.current_param_value <span class="hljs-keyword">and</span> <span class="hljs-string">&quot;&gt;&quot;</span> <span class="hljs-keyword">in</span> value_chunk:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L611">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="611">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        gt_idx = value_chunk.find(<span class="hljs-string">&quot;&gt;&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L612">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="612">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        value_chunk = value_chunk[gt_idx + <span class="hljs-number">1</span> :]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L613">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="613">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L614">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="614">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> self.current_param_value <span class="hljs-keyword">and</span> value_chunk.startswith(<span class="hljs-string">&quot;\n&quot;</span>):<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L615">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="615">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        value_chunk = value_chunk[<span class="hljs-number">1</span>:]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L616">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="616">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L617">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="617">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-comment"># Calculate incremental JSON</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L618">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="618">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    full_value = self.current_param_value + value_chunk<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L619">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="619">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    prev_escaped = (<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L620">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="620">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        json.dumps(self.current_param_value)[<span class="hljs-number">1</span>:-<span class="hljs-number">1</span>]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L621">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="621">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        <span class="hljs-keyword">if</span> self.current_param_value<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L622">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="622">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        <span class="hljs-keyword">else</span> <span class="hljs-string">&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L623">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="623">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L624">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="624">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    full_escaped = json.dumps(full_value)[<span class="hljs-number">1</span>:-<span class="hljs-number">1</span>]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L625">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="625">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    delta_escaped = full_escaped[<span class="hljs-built_in">len</span>(prev_escaped) :]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L626">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="626">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L627">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="627">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    self.in_param = <span class="hljs-literal">False</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L628">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="628">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    self.current_param_value = <span class="hljs-string">&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L629">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="629">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L630">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="630">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-keyword">return</span> DeltaMessage(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L631">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="631">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        tool_calls=[<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L632">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="632">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                            DeltaToolCall(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L633">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="633">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                index=self.current_tool_index,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L634">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="634">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                function=DeltaFunctionCall(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L635">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="635">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                    arguments=delta_escaped + <span class="hljs-string">&#x27;&quot;&#x27;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L636">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="636">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                ),<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L637">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="637">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                            )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L638">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="638">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        ]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L639">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="639">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L640">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="640">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                <span class="hljs-keyword">else</span>:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L641">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="641">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-comment"># Continue accumulating value</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L642">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="642">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    value_chunk = delta_text<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L643">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="643">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L644">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="644">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-comment"># Handle first chunk after param name</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L645">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="645">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> self.current_param_value <span class="hljs-keyword">and</span> <span class="hljs-string">&quot;&gt;&quot;</span> <span class="hljs-keyword">in</span> value_chunk:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L646">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="646">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        gt_idx = value_chunk.find(<span class="hljs-string">&quot;&gt;&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L647">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="647">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        value_chunk = value_chunk[gt_idx + <span class="hljs-number">1</span> :]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L648">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="648">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L649">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="649">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> self.current_param_value <span class="hljs-keyword">and</span> value_chunk.startswith(<span class="hljs-string">&quot;\n&quot;</span>):<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L650">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="650">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        value_chunk = value_chunk[<span class="hljs-number">1</span>:]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L651">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="651">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L652">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="652">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                    <span class="hljs-keyword">if</span> value_chunk:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L653">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="653">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        <span class="hljs-comment"># Stream the escaped delta</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L654">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="654">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        prev_escaped = (<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L655">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="655">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                            json.dumps(self.current_param_value)[<span class="hljs-number">1</span>:-<span class="hljs-number">1</span>]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L656">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="656">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                            <span class="hljs-keyword">if</span> self.current_param_value<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L657">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="657">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                            <span class="hljs-keyword">else</span> <span class="hljs-string">&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L658">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="658">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L659">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="659">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        self.current_param_value += value_chunk<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L660">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="660">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        full_escaped = json.dumps(self.current_param_value)[<span class="hljs-number">1</span>:-<span class="hljs-number">1</span>]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L661">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="661">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        delta_escaped = full_escaped[<span class="hljs-built_in">len</span>(prev_escaped) :]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L662">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="662">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L663">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="663">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                        <span class="hljs-keyword">if</span> delta_escaped:<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L664">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="664">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                            <span class="hljs-keyword">return</span> DeltaMessage(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L665">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="665">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                tool_calls=[<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L666">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="666">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                    DeltaToolCall(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L667">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="667">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                        index=self.current_tool_index,<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L668">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="668">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                        function=DeltaFunctionCall(<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L669">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="669">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                            arguments=delta_escaped<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L670">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="670">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                        ),<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L671">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="671">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                    )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L672">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="672">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                                ]<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L673">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="673">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->                            )<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L674">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="674">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L675">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="675">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->        <span class="hljs-keyword">return</span> <span class="hljs-literal">None</span><!-- HTML_TAG_END --></td>
					</tr>
					<tr class="" id="L676">
						
						<td class="blob-line-num sticky left-0 w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-400/80 hover:text-black dark:text-gray-500 dark:hover:text-white bg-white dark:bg-gray-950" data-line-num="676">
							<div class="absolute inset-y-0 right-0 border-r"></div></td>
						<td class="blob-line overflow-visible px-3 whitespace-pre"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr></tbody></table></div>
	</div></div></div>
				</div></section></div></main>

	</div>

		<script>
			import("\/front\/build\/kube-9d7efdc\/index.js");
			window.moonSha = "kube-9d7efdc\/";
			window.__hf_deferred = {};
		</script>

		<!-- Stripe -->
		<script>
			if (["hf.co", "huggingface.co"].includes(window.location.hostname)) {
				const script = document.createElement("script");
				script.src = "https://js.stripe.com/v3/";
				script.async = true;
				document.head.appendChild(script);
			}
		</script>
	</body>
</html>
