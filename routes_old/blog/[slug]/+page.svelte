<script lang="ts">
    import type { PageData } from "./$types";
    import { onDestroy, onMount } from "svelte";
    export let data: PageData;

    let number = 0;

    let socket: WebSocket | null = null;

    onMount(() => {
        socket = new WebSocket(`ws://${location.host}/ws`);
        socket.onmessage = (event) => {
            number = event.data;
        };
        socket.onclose = () => {
            socket = null;
        };
    });

    onDestroy(() => {
        if (socket) {
            socket.close();
        }
    });
</script>

<svelte:head>
    <title>Mypage</title>
</svelte:head>

<h1>{data.title}</h1>
<p />
<div>
    {@html data.content}
</div>
<p>The number is: {number}</p>
