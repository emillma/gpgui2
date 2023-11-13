<script>
    /** @type {import('./$types').PageData} */
    export let data;

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

<h1>{data.title}</h1>
<p />
<div class="text-red-600">
    {@html data.content}
</div>
<p>The number is: {number}</p>
