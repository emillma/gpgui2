<script lang="ts">
    import type { PageData } from "./$types";
    import Connection from "$lib/Connection.svelte";
    import { SlideToggle } from "@skeletonlabs/skeleton";
    import { afterUpdate, tick } from "svelte";

    export let data: PageData;
    let text: string = "";
    let term: HTMLElement;
    let scroll_pos: number;

    // user.set(Footer);

    async function onmessage(event: MessageEvent) {
        text = event.data;
    }

    afterUpdate(() => {
        const bottom = term.scrollTop + term.clientHeight;
        if (bottom > term.scrollHeight - 100)
            term.scroll({ top: term.scrollHeight, behavior: "smooth" });
    });
</script>

<svelte:head>
    <title>Mypage</title>
</svelte:head>

<Connection {onmessage} path_name={"cat"} />
<div class="page">
    <div
        bind:this={term}
        on:scroll={() => {
            console.log(term.scrollTop);
        }}
        class="overflow-scroll grow text-sm border-surface-800"
    >
        {#if text}
            <pre class="pre">{text}</pre>
        {/if}
    </div>

    <div class="flex p-4 justify-center">
        <SlideToggle
            name="slider"
            active="bg-green-500"
            size="md"
            disabled={true}
        />
    </div>
</div>
