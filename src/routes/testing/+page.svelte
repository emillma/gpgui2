<script lang="ts">
    import Button from "svelte-ux";
    import Preview from "svelte-ux";
    import ScrollContainer from "svelte-ux";
</script>

<h1>Examples</h1>

<h2>Basic</h2>

<Preview>
    <ScrollContainer class="scroll-mt-6 scroll-mb-6" let:scrollIntoView>
        <Button
            variant="fill"
            color="accent"
            on:click={() => scrollIntoView({ block: "end" })}
            >Scroll to bottom</Button
        >
        {#each { length: 100 } as _, i}
            <div>Item: {i + 1}</div>
        {/each}
        <Button variant="fill" color="accent" on:click={() => scrollIntoView()}
            >Scroll to top</Button
        >
    </ScrollContainer>
</Preview>
