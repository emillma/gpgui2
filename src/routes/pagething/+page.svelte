<script lang="ts">
    import Page1 from "./Page1.svelte";
    import Page2 from "./Page2.svelte";

    let component: typeof Page1 | typeof Page2;

    let prop: number = 0;

    const page1 = () => {
        component = Page1;
        prop = 1;
    };

    const page2 = () => {
        component = Page2;
        prop = 2;
    };

    page1();
</script>

<button on:click={page1}>page1</button>
<button on:click={page2}>page2</button>

<svelte:component this={component} {prop} />
