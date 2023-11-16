<script lang="ts">
    import type { PageData } from "./$types";
    export let data: PageData;

    let number = 0;

    let socket = null;

    import { onMount } from "svelte";
    onMount(() => {
        socket = new WebSocket("ws://localhost:8888/number");
        socket.onmessage = (event) => {
            number = event.data;
        };
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
