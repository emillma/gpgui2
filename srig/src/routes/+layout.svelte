<script lang="ts">
	import "../app.postcss";
	import { AppShell, TabAnchor, TabGroup } from "@skeletonlabs/skeleton";

	// Highlight JS
	import hljs from "highlight.js/lib/core";
	import "highlight.js/styles/github-dark.css";
	import { storeHighlightJs } from "@skeletonlabs/skeleton";
	import xml from "highlight.js/lib/languages/xml"; // for HTML
	import css from "highlight.js/lib/languages/css";
	import javascript from "highlight.js/lib/languages/javascript";
	import typescript from "highlight.js/lib/languages/typescript";

	hljs.registerLanguage("xml", xml); // for HTML
	hljs.registerLanguage("css", css);
	hljs.registerLanguage("javascript", javascript);
	hljs.registerLanguage("typescript", typescript);
	storeHighlightJs.set(hljs);

	// Floating UI for Popups
	import {
		computePosition,
		autoUpdate,
		flip,
		shift,
		offset,
		arrow,
	} from "@floating-ui/dom";
	import { storePopup } from "@skeletonlabs/skeleton";
	storePopup.set({ computePosition, autoUpdate, flip, shift, offset, arrow });

	// Emil's stuff
	import { page } from "$app/stores";
	import { setContext } from "svelte";

	const pages = [
		{ name: "Home", path: "/" },
		// { name: "ls", path: "/hello" },
		{ name: "Ptp", path: "/ptp" },
		{ name: "Video", path: "/livestream" },
	];
</script>

<TabGroup
	class="h-10 top-0"
	active="variant-filled-secondary"
	flex="flex-1"
	padding="py-2"
>
	{#each pages as p}
		<TabAnchor href={p.path} selected={$page.url.pathname === p.path}>
			{p.name}
		</TabAnchor>
	{/each}
</TabGroup>
<slot />
