<script lang="ts">
    import { onMount } from "svelte";

    var dir_handle: FileSystemDirectoryHandle;
    var content: string = "";

    async function getDir() {
        dir_handle = await (window as any).showDirectoryPicker();
    }
    async function write_to_file() {
        const file_handle = await dir_handle.getFileHandle("test.txt", {
            create: true,
        });
        const writable = await file_handle.createWritable();
        await writable.write(content);
        await writable.close();
    }
</script>

<input type="text" bind:value={content} />
<p>{content}</p>
// Display the content in a paragraph

<button on:click={getDir}>set dir</button>
<button on:click={write_to_file}>write to file</button>
