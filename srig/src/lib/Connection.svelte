<script lang="ts">
    import ReconnectingWebSocket from "reconnecting-websocket";
    import { onDestroy, onMount } from "svelte";
    import { page } from "$app/stores";

    export let onmessage: (event: MessageEvent) => Promise<void>;

    export let path_name: string = "/";
    export let port: string = "12102";

    let ws: ReconnectingWebSocket;

    onMount(() => {
        let url = new URL($page.url.toString());
        url.protocol = "ws:";
        url.port = port;
        url.pathname = path_name;

        ws = new ReconnectingWebSocket(url.toString(), [], {
            maxReconnectionDelay: 1000,
            minReconnectionDelay: 500,
            reconnectionDelayGrowFactor: 1,
            connectionTimeout: 1000,
            maxRetries: Infinity,
            debug: false,
        });
        ws.onmessage = onmessage;
    });

    onDestroy(() => {
        if (ws) {
            ws.close();
        }
    });
</script>
