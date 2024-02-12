<script lang="ts">
    import type { PageData } from "./$types";
    import Connection from "$lib/Connection.svelte";
    import Terminal from "$lib/Terminal.svelte";
    import { SlideToggle } from "@skeletonlabs/skeleton";

    export let data: PageData;
    let text: string = "";
    let checked = false;
    let disabled = true;
    let connection: Connection;
    let update_status = true;

    async function message_cb(event: MessageEvent) {
        const msg = JSON.parse(event.data);
        if (msg.type === "message") text += msg.data;
        else if (msg.type === "status" && update_status) {
            checked = msg.data === "True";
            disabled = false;
        }
    }

    async function toggle_change(event: Event) {
        if (checked) connection.send("start");
        else connection.send("stop");
        disabled = true;
        update_status = false;
        setTimeout(() => {
            update_status = true;
        }, 1000);
    }
</script>

<Connection bind:this={connection} {message_cb} path_name={"run_ls"} />

<div class="page">
    <Terminal bind:text />
    <div class="flex p-4 justify-around justify-items-center">
        <SlideToggle
            bind:checked
            bind:disabled
            on:change={toggle_change}
            name="auto_scroll"
            active="bg-green-500"
        />
    </div>
</div>
