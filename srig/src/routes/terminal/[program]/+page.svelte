<script lang="ts">
    import type { PageData } from "./$types";
    import Connection from "$lib/Connection.svelte";
    import { SlideToggle } from "@skeletonlabs/skeleton";
    import { afterUpdate, tick } from "svelte";

    export let data: PageData;
    let text: string = "";
    let term: HTMLElement;
    let scroll_pos: number;
    let auto_scroll = true;
    let running = false;
    // user.set(Footer);

    async function onmessage(event: MessageEvent) {
        text = text + event.data;
    }

    afterUpdate(() => {
        // const bottom = term.scrollTop + term.clientHeight;
        if (auto_scroll) {
            term.scroll({ top: term.scrollHeight, behavior: "smooth" });
        }
    });
</script>

<svelte:head>
    <title>Mypage</title>
</svelte:head>

<Connection {onmessage} path_name={"run_ls"} />

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

    <div class="flex p-4 justify-around justify-items-center">
        <SlideToggle
            bind:checked={running}
            name="auto_scroll"
            active="bg-green-500"
            disabled={true}
        />
        <SlideToggle
            bind:checked={auto_scroll}
            name="auto_scroll"
            active="bg-green-500"
        />
    </div>
</div>
