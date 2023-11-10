<script>
	let number_promise = get_number();

	async function get_number() {
		// const id = Math.floor(Math.random() * 60) + 1;
		const response = await fetch("/rand");
		const data = await response.text();
		return data;
	}
</script>

<div class="bg-slate-800 text-white h-screen">
	<div class=" rounded-lg px-6 py-8 ring-1 ring-slate-900/5 shadow-xl">
		<p>
			{#await number_promise}
				Loading planet...
			{:then planet}
				Your next planet is {planet}.
			{:catch someError}
				System error: {someError.message}.
			{/await}
		</p>

		<button on:click={() => (number_promise = get_number())}>
			Explore the next planet
		</button>
		<div>
			<span
				class="inline-flex items-center justify-center p-2 bg-indigo-500 rounded-md shadow-lg"
			>
				<svg
					class="h-6 w-6"
					xmlns="http://www.w3.org/2000/svg"
					fill="none"
					viewBox="0 0 24 24"
					stroke="currentColor"
					aria-hidden="true"><!-- ... --></svg
				>
			</span>
		</div>
		<h3 class="mt-5 text-base font-medium tracking-tight">
			Writes Upside-Down
		</h3>
		<p class="text-slate-400 mt-2 text-sm">
			The Zero Gravity Pen can be used to write in any orientation,
			including upside-down. It even works in outer space.
		</p>
	</div>
</div>
