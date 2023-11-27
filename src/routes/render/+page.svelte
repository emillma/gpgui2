<script lang="ts">
    import { onDestroy, onMount } from "svelte";

    let soc: WebSocket;
    let jpeg_data: string | null = null;
    let data: string | null = null;

    async function onmessage(event: MessageEvent) {
        const blob: Blob = event.data;
        const jpegblob = new Blob([blob], { type: "image/jpeg" });
        const imageUrl = URL.createObjectURL(jpegblob);
        jpeg_data = imageUrl;
    }
    function connect() {
        soc = new WebSocket(`ws://${location.hostname}:5170/ws`);
        soc.onmessage = onmessage;
        const timer = setTimeout(() => soc.close(), 2000);
        soc.onopen = (event) => clearTimeout(timer);
        soc.onclose = (event) => setTimeout(connect, 1000);
        soc.onerror = (event) => soc.close();
    }
    onMount(connect);

    onDestroy(() => {
        if (soc) {
            soc.close();
        }
    });
</script>

<img src={jpeg_data} alt="image" aria-hidden="true" />
{@debug soc}
