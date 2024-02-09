<script lang="ts">
    import Connection from "$lib/Connection.svelte";

    let jpeg_data: string;
    // user.set(Footer);

    async function onmessage(event: MessageEvent) {
        const blob: Blob = event.data;
        const jpegblob = new Blob([blob], { type: "image/jpeg" });
        const imageUrl = URL.createObjectURL(jpegblob);
        jpeg_data = imageUrl;
    }
</script>

<Connection {onmessage} path_name={"video"} />

<img class="w-1/2" src={jpeg_data} alt="image" aria-hidden="true" />
