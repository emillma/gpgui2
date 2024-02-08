<script lang="ts">
    import type { PageData } from "./$types";
    import Connection from "$lib/Connection.svelte";

    async function onmessage(event: MessageEvent) {
        console.log(event.data);
    }
</script>

<svelte:head>
    <title>Mypage</title>
</svelte:head>

<Connection {onmessage} path_name={"cat"} />
Hello
