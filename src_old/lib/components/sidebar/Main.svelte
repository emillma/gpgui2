<script lang="ts">
	let text: string[] = Array.from({ length: 200 }, (x, i) => `${i}`);
</script>

<main class="p-4 text-gray-300">
	<a href="#Anchorname">linked text</a>
	{#each text as t}
		<p>{t}</p>
	{/each}
</main>
