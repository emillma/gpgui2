<script lang="ts">
    import { onDestroy, onMount } from "svelte";
    import ReconnectingWebSocket from "reconnecting-websocket";
    let ws: ReconnectingWebSocket;
    let jpeg_data: string | null = null;
    let data: string | null = null;

    async function onmessage(event: MessageEvent) {
        const blob: Blob = event.data;
        const jpegblob = new Blob([blob], { type: "image/jpeg" });
        const imageUrl = URL.createObjectURL(jpegblob);
        jpeg_data = imageUrl;
    }

    onMount(() => {
        ws = new ReconnectingWebSocket(
            `ws://${location.hostname}:5170/ws`,
            [],
            {
                maxReconnectionDelay: 1000,
                minReconnectionDelay: 500,
                reconnectionDelayGrowFactor: 1,
                connectionTimeout: 500,
                maxRetries: Infinity,
                debug: false,
            },
        );
        ws.onmessage = onmessage;
    });

    onDestroy(() => {
        if (ws) {
            ws.close();
        }
    });
</script>

<img src={jpeg_data} alt="image" aria-hidden="true" />
{@debug ws}
