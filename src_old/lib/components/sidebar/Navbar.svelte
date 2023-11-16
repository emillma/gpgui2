<script lang="ts">
	import Hamburger from "./Hamburger.svelte";
	export let sidebar = false;
</script>

<header class="h-12 flex justify-between bg-slate-700 p-2 items-center">
	<nav class="flex items-center">
		<Hamburger bind:open={sidebar} />
		Page
	</nav>
	<nav class="text-bold">
		<a href="/about" class="hoverlink">About</a>
		<a href="/contact" class="hoverlink ml-4">Contact</a>
	</nav>
</header>
