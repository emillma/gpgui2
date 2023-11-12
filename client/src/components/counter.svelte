<script>
    let count = 0;
</script>

<button
    class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
    on:click={() => (count += 1)}
>
    Clicked {count} times
</button>

<style>
</style>
