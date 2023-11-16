<script>
	export let open = false;
</script>

<aside class="absolute top-12 h-full bg-slate-700 opacity-95" class:open>
	<nav class="p-12 text-xl">
		<a class="block" href="#about">About</a>
		<a class="block" href="#contact">Contact</a>
	</nav>
</aside>

<style>
	aside {
		left: -100%;
		transition: left 0.3s ease-in-out;
	}
	.open {
		left: 0;
	}
</style>
