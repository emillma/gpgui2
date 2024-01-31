<script lang="ts">
    import { onDestroy, onMount } from "svelte";
    import ReconnectingWebSocket from "reconnecting-websocket";
    import Connection from "$lib/Connection.svelte";
    import Plotly from "plotly.js-dist";
    // import Plotly from "plotly.js";

    async function onmessage(event: MessageEvent) {
        // console.log(data);
        let elem = await Plotly.newPlot("elem_id", JSON.parse(event.data));

        elem.on("plotly_click", function (data: object) {
            console.log(data);
        });
        elem.on("plotly_hover", function (data: object) {
            console.log(data);
        });
        elem.on("plotly_animatingframe", function (data: object) {
            console.log(data);
        });

        console.log(elem);
    }
</script>

<div>Hello</div>
<Connection {onmessage} url={`ws://${location.hostname}:12102`} />

<div id="elem_id" style="height:40em;"></div>

<!-- <svelte:head>
    <script src="/plotly-latest.min.js" type="text/javascript"></script>
</svelte:head> -->
