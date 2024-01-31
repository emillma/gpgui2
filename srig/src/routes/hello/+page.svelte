<script>
    let count = 100;
</script>

{#each Array(count) as _, i}
    <div>Hello World {i+1}</div>
{/each}
