<script lang="ts">
    import Navbar from "$lib/components/sidebar/Navbar.svelte";
    import Sidebar from "$lib/components/sidebar/Sidebar.svelte";
    import Main from "$lib/components/sidebar/Main.svelte";

    let open = false;
</script>

<Sidebar bind:open />
<Navbar bind:sidebar={open} />
<Main />

<!-- {@debug navbar navbar.offsetHeight} -->

<style>
    :global(body) {
        padding: 0;
    }
</style>
