<script lang="ts">
    import { onDestroy, onMount } from "svelte";

    let soc: WebSocket;
    let jpeg_data: string | null = null;
    let data: string | null = null;
    async function onmessage(event: MessageEvent) {
        data = event.data;
        // const data = await event.data.arrayBuffer();
        // jpeg_data = btoa(String.fromCharCode(...new Uint8Array(data)));
    }
    function connect() {
        soc = new WebSocket(`ws://${location.hostname}:5170/ws`);
        soc.onmessage = onmessage;
        const timer = setTimeout(() => soc.close(), 1000);
        soc.onopen = () => clearTimeout(timer);
        soc.onclose = () => setTimeout(connect, 1000);
        soc.onerror = () => soc.close();
    }
    connect();
    onMount(() => console.log("mounted"));

    onDestroy(() => {
        if (soc) {
            soc.close();
        }
    });
</script>

{data}
