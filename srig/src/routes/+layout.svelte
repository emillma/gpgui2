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

	import { page } from "$app/stores";
</script>

<!-- App Shell -->
<AppShell>
	<svelte:fragment slot="header">
		<!-- App Bar -->
		<TabGroup
			active="variant-filled-secondary"
			flex="flex-grow"
			padding="py-4"
		>
			<TabAnchor href="/" selected={$page.url.pathname === "/"}>
				Home
			</TabAnchor>

			<TabAnchor href="/hello" selected={$page.url.pathname === "/hello"}>
				Hello
			</TabAnchor>
		</TabGroup>
	</svelte:fragment>
	<slot />
</AppShell>
