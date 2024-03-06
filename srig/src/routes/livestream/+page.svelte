<script lang="ts">
    import Connection from "$lib/Connection.svelte";

    let jpeg_data: string;
    // user.set(Footer);

    async function message_cb(event: MessageEvent) {
        const blob: Blob = event.data;
        const jpegblob = new Blob([blob], { type: "image/jpeg" });
        const imageUrl = URL.createObjectURL(jpegblob);
        jpeg_data = imageUrl;
    }
</script>

<Connection {message_cb} path_name={"video"} />

{#if jpeg_data}
    <img class="w-1/2" src={jpeg_data} alt="image" aria-hidden="true" />
{/if}
