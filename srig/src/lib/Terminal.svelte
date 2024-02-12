<script lang="ts">
    import Terminal from "$lib/Terminal.svelte";
    import { SlideToggle } from "@skeletonlabs/skeleton";
    import { afterUpdate } from "svelte";

    export let text: string = "";

    let auto_scroll = true;
    let term: HTMLElement;

    afterUpdate(() => {
        if (auto_scroll) {
            term.scroll({ top: term.scrollHeight, behavior: "smooth" });
        }
    });
</script>

<div bind:this={term} class="overflow-scroll grow text-sm border-surface-800">
    {#if text}
        <pre class="pre">{text}</pre>
    {/if}
</div>

<!-- <div class="flex p-4 justify-around justify-items-center">
        <SlideToggle
            bind:checked={auto_scroll}
            name="auto_scroll"
            active="bg-green-500"
            disabled={true}
        />
    </div> -->
