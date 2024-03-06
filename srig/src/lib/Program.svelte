<script lang="ts">
    import Connection from "./Connection.svelte";
    import Terminal from "./Terminal.svelte";
    import { SlideToggle } from "@skeletonlabs/skeleton";

    export let cmd: string;
    let teminal_text: string = "";

    let toggle_on = false;
    let toggle_disabled = true;

    let ws: Connection;
    let update_debounce = true;

    async function message_cb(event: MessageEvent) {
        const msg = JSON.parse(event.data);
        if (msg.type === "message") teminal_text += msg.data;
        else if (msg.type === "status" && update_debounce) {
            toggle_on = msg.data === "True";
            toggle_disabled = false;
        }
    }

    async function toggle_change(event: Event) {
        if (toggle_on) ws.send("start");
        else ws.send("stop");
        toggle_disabled = true;
        update_debounce = false;
        setTimeout(() => {
            update_debounce = true;
        }, 1000);
    }
</script>

<Connection bind:this={ws} {message_cb} path_name={cmd} />

<div class="page">
    <Terminal bind:text={teminal_text} />
    <div class="flex p-4 justify-around justify-items-center">
        <SlideToggle
            bind:checked={toggle_on}
            bind:disabled={toggle_disabled}
            on:change={toggle_change}
            name="auto_scroll"
            active="bg-green-500"
        />
    </div>
</div>
