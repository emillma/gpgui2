<script lang="ts">
    import type { PageData } from "./$types";
    import Connection from "$lib/Connection.svelte";
    import { onMount } from "svelte";
    import { SlideToggle } from "@skeletonlabs/skeleton";

    export let data: PageData;
    let terminal: HTMLElement;
    let scroll_pos: number;

    // user.set(Footer);

    async function onmessage(event: MessageEvent) {
        console.log(event.data);
    }

    function scroll_if_bottom(node: HTMLElement) {
        if (node.scrollTop + node.clientHeight > node.scrollHeight - 1000) {
            node.scroll({ top: node.scrollHeight, behavior: "smooth" });
        }
    }

    function toggle(thing: Event) {
        scroll_if_bottom(terminal);
        console.log("toggle");
    }
</script>

<svelte:head>
    <title>Mypage</title>
</svelte:head>

<Connection {onmessage} path_name={"cat"} />
<div class="page">
    <div
        bind:this={terminal}
        on:scroll={() => {
            console.log(terminal.scrollTop);
        }}
        class="overflow-scroll text-sm p-4 border-y-2 border-surface-800"
    >
        {#each Array(1000) as _, i}
            hello{i}{"\n"}
        {/each}
    </div>

    <div class="flex p-2 justify-center">
        <SlideToggle
            on:change={toggle}
            name="slider"
            active="bg-green-500"
            size="md"
        />
    </div>
</div>
