<script lang="ts">
  import { slide } from 'svelte/transition';
  import { mdiChevronDown } from '@mdi/js';

  import Button from '$lib/components/Button.svelte';
  import ButtonGroup from '$lib/components/ButtonGroup.svelte';
  import Dialog from '$lib/components/Dialog.svelte';
  import Drawer from '$lib/components/Drawer.svelte';
  import Menu from '$lib/components/Menu.svelte';
  import MenuItem from '$lib/components/MenuItem.svelte';
  import Preview from '$lib/components/Preview.svelte';
  import ToggleButton from '$lib/components/ToggleButton.svelte';
</script>

<h1>Examples</h1>

<h2>Dialog</h2>

<Preview>
  <ToggleButton let:on={open}>
    Open Dialog
    <Dialog slot="toggle" {open} on:close={toggle} let:toggle>
      <div slot="title">Are you sure you want to do that?</div>
      <div slot="actions">
        <Button variant="fill" color="accent">Close</Button>
      </div>
    </Dialog>
  </ToggleButton>
</Preview>

<h2>Drawer</h2>

<Preview>
  <ToggleButton>
    Open Drawer
    <Drawer slot="toggle" let:on={open} {open} on:close={toggleOff} class="w-[400px]" let:toggleOff>
      <h1>Contents</h1>
      <div
        class="fixed bottom-0 w-full flex justify-center bg-gray-500/25
      p-1 border-t border-gray-400"
      >
        <Button on:click={toggleOff}>Close</Button>
      </div>
    </Drawer>
  </ToggleButton>
</Preview>

<h2>slide transition</h2>

<Preview>
  <ToggleButton size="sm" transition={slide} let:on={showDetails}>
    {showDetails ? 'show less' : 'show more'}...
    <div slot="toggle" class="mt-2 border-t border-gray-100">
      {#each { length: 10 } as _, i}
        <div>{i}</div>
      {/each}
    </div>
  </ToggleButton>
</Preview>

<h2>slide transition (button after)</h2>

<Preview>
  <ToggleButton size="sm" transition={slide} let:on={showDetails} buttonPlacement="after">
    {showDetails ? 'show less' : 'show more'}...
    <div slot="toggle" class="mt-2 border-b border-gray-100">
      {#each { length: 10 } as _, i}
        <div>{i}</div>
      {/each}
    </div>
  </ToggleButton>
</Preview>

<h2>on by default</h2>

<Preview>
  <ToggleButton on size="sm" transition={slide} let:on={showDetails}>
    {showDetails ? 'show less' : 'show more'}...
    <div slot="toggle" class="mt-2 border-t border-b border-gray-100">
      {#each { length: 10 } as _, i}
        <div>{i}</div>
      {/each}
    </div>
  </ToggleButton>
</Preview>

<h2>ButtonGroup</h2>

<Preview>
  <ButtonGroup variant="outline">
    <Button>Click me</Button>
    <ToggleButton
      let:on={open}
      let:toggleOff
      icon={mdiChevronDown}
      iconOnly
      rounded
      class="px-1"
      transition={false}
    >
      <Menu {open} on:close={toggleOff} placement="bottom-start">
        <MenuItem>One</MenuItem>
        <MenuItem>Two</MenuItem>
        <MenuItem>Three</MenuItem>
      </Menu>
    </ToggleButton>
  </ButtonGroup>
</Preview>
