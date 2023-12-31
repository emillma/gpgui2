<script lang="ts">
  import { mdiHome, mdiMagnify, mdiMenu, mdiTrashCan } from '@mdi/js';
  import { faUser } from '@fortawesome/free-solid-svg-icons';

  import Button from '$lib/components/Button.svelte';
  import Preview from '$lib/components/Preview.svelte';
  import SectionDivider from '$lib/components/SectionDivider.svelte';
  import Tooltip from '$lib/components/Tooltip.svelte';
  import Toggle from '$lib/components/Toggle.svelte';
</script>

<h1>Examples</h1>

<h2>Basic</h2>

<Preview>
  <Button on:click={() => alert('Why did you do that?')}>Click me</Button>
</Preview>

<h2>Link</h2>

<Preview>
  <Button href="https://www.google.com" target="_blank">Open Google</Button>
</Preview>

<h2>Disabled</h2>

<Preview>
  <Button disabled>Click me</Button>
</Preview>

<h2>Loading</h2>

<Preview>
  <Button loading>Loading...</Button>
  <Button variant="outline" color="accent" loading>Loading...</Button>
  <Button variant="fill" color="accent" loading>Loading...</Button>
  <Button variant="fill-light" color="accent" loading>Loading...</Button>
  <Button variant="fill-outline" color="accent" loading>Loading...</Button>
  <Button variant="text" color="accent" loading>Loading...</Button>

  <div class="mt-2">
    <Toggle let:on={loading} let:toggle>
      <Button {loading} on:click={toggle}>Click me</Button>
    </Toggle>
    <Toggle let:on={loading} let:toggle>
      <Button variant="outline" color="accent" {loading} on:click={toggle}>Click me</Button>
    </Toggle>
    <Toggle let:on={loading} let:toggle>
      <Button variant="fill" color="accent" {loading} on:click={toggle}>Click me</Button>
    </Toggle>
    <Toggle let:on={loading} let:toggle>
      <Button variant="fill-light" color="accent" {loading} on:click={toggle}>Click me</Button>
    </Toggle>
    <Toggle let:on={loading} let:toggle>
      <Button variant="fill-outline" color="accent" {loading} on:click={toggle}>Click me</Button>
    </Toggle>
    <Toggle let:on={loading} let:toggle>
      <Button variant="text" color="accent" {loading} on:click={toggle}>Click me</Button>
    </Toggle>
  </div>

  <div class="mt-2">
    <Toggle let:on={loading} let:toggle>
      <Button icon={faUser} {loading} on:click={toggle}>Click me</Button>
    </Toggle>
    <Toggle let:on={loading} let:toggle>
      <Button icon={faUser} variant="outline" color="accent" {loading} on:click={toggle}
        >Click me</Button
      >
    </Toggle>
    <Toggle let:on={loading} let:toggle>
      <Button icon={faUser} variant="fill" color="accent" {loading} on:click={toggle}
        >Click me</Button
      >
    </Toggle>
    <Toggle let:on={loading} let:toggle>
      <Button icon={faUser} variant="fill-light" color="accent" {loading} on:click={toggle}
        >Click me</Button
      >
    </Toggle>
    <Toggle let:on={loading} let:toggle>
      <Button icon={faUser} variant="fill-outline" color="accent" {loading} on:click={toggle}
        >Click me</Button
      >
    </Toggle>
    <Toggle let:on={loading} let:toggle>
      <Button icon={faUser} variant="text" color="accent" {loading} on:click={toggle}
        >Click me</Button
      >
    </Toggle>
  </div>
</Preview>

<h2>Variants</h2>

<Preview>
  <div class="grid gap-2">
    <div>
      <Button>default</Button>
      <Button color="blue">default</Button>
      <Button color="red">default</Button>
      <Button color="green">default</Button>
      <Button color="gray">default</Button>
    </div>
    <div>
      <Button variant="outline">outline</Button>
      <Button variant="outline" color="blue">outline</Button>
      <Button variant="outline" color="red">outline</Button>
      <Button variant="outline" color="green">outline</Button>
      <Button variant="outline" color="gray">outline</Button>
    </div>
    <div>
      <Button variant="fill">fill</Button>
      <Button variant="fill" color="blue">fill</Button>
      <Button variant="fill" color="red">fill</Button>
      <Button variant="fill" color="green">fill</Button>
      <Button variant="fill" color="gray">fill</Button>
    </div>
    <div>
      <Button variant="fill-light">fill-light</Button>
      <Button variant="fill-light" color="blue">fill-light</Button>
      <Button variant="fill-light" color="red">fill-light</Button>
      <Button variant="fill-light" color="green">fill-light</Button>
      <Button variant="fill-light" color="gray">fill-light</Button>
    </div>
    <div>
      <Button variant="fill-outline">fill-outline</Button>
      <Button variant="fill-outline" color="blue">fill-outline</Button>
      <Button variant="fill-outline" color="red">fill-outline</Button>
      <Button variant="fill-outline" color="green">fill-outline</Button>
      <Button variant="fill-outline" color="gray">fill-outline</Button>
    </div>
    <div>
      <Button variant="text">text</Button>
      <Button variant="text" color="blue">text</Button>
      <Button variant="text" color="red">text</Button>
      <Button variant="text" color="green">text</Button>
      <Button variant="text" color="gray">text</Button>
    </div>
  </div>
</Preview>

<h2>`none` variant</h2>

<Preview>
  <Button variant="none">Click me</Button>
</Preview>

<h2>Size</h2>

<Preview>
  {#each ['sm', 'md', 'lg'] as size}
    <div class="[&:not(:first-child)]:mt-4">{size}</div>
    <div class="grid gap-2 ml-3">
      <div>
        <Button {size}>default</Button>
        <Button color="blue" {size}>default</Button>
        <Button color="red" {size}>default</Button>
        <Button color="green" {size}>default</Button>
        <Button color="gray" {size}>default</Button>
      </div>
      <div>
        <Button variant="outline" {size}>outline</Button>
        <Button variant="outline" {size} color="blue">outline</Button>
        <Button variant="outline" {size} color="red">outline</Button>
        <Button variant="outline" {size} color="green">outline</Button>
        <Button variant="outline" {size} color="gray">outline</Button>
      </div>
      <div>
        <Button variant="fill" {size}>fill</Button>
        <Button variant="fill" {size} color="blue">fill</Button>
        <Button variant="fill" {size} color="red">fill</Button>
        <Button variant="fill" {size} color="green">fill</Button>
        <Button variant="fill" {size} color="gray">fill</Button>
      </div>
      <div>
        <Button variant="fill-light" {size}>fill-light</Button>
        <Button variant="fill-light" {size} color="blue">fill-light</Button>
        <Button variant="fill-light" {size} color="red">fill-light</Button>
        <Button variant="fill-light" {size} color="green">fill-light</Button>
        <Button variant="fill-light" {size} color="gray">fill-light</Button>
      </div>
      <div>
        <Button variant="fill-outline" {size}>fill-outline</Button>
        <Button variant="fill-outline" {size} color="blue">fill-outline</Button>
        <Button variant="fill-outline" {size} color="red">fill-outline</Button>
        <Button variant="fill-outline" {size} color="green">fill-outline</Button>
        <Button variant="fill-outline" {size} color="gray">fill-outline</Button>
      </div>
      <div>
        <Button variant="text" {size}>text</Button>
        <Button variant="text" {size} color="blue">text</Button>
        <Button variant="text" {size} color="red">text</Button>
        <Button variant="text" {size} color="green">text</Button>
        <Button variant="text" {size} color="gray">text</Button>
      </div>
    </div>
  {/each}
</Preview>

<h2>Rounded</h2>

<Preview>
  <div class="grid gap-2">
    <div>
      <Button>default</Button>
      <Button rounded>rounded</Button>
      <Button rounded="full">full</Button>
      <Button rounded={false}>false</Button>
    </div>
    <div>
      <Button variant="outline" color="accent">default</Button>
      <Button variant="outline" color="accent" rounded>rounded</Button>
      <Button variant="outline" color="accent" rounded="full">full</Button>
      <Button variant="outline" color="accent" rounded={false}>false</Button>
    </div>
    <div>
      <Button variant="fill" color="accent">default</Button>
      <Button variant="fill" color="accent" rounded>rounded</Button>
      <Button variant="fill" color="accent" rounded="full">full</Button>
      <Button variant="fill" color="accent" rounded={false}>false</Button>
    </div>
    <div>
      <Button variant="fill-light" color="accent">default</Button>
      <Button variant="fill-light" color="accent" rounded>rounded</Button>
      <Button variant="fill-light" color="accent" rounded="full">full</Button>
      <Button variant="fill-light" color="accent" rounded={false}>false</Button>
    </div>
    <div>
      <Button variant="fill-outline" color="accent">default</Button>
      <Button variant="fill-outline" color="accent" rounded>rounded</Button>
      <Button variant="fill-outline" color="accent" rounded="full">full</Button>
      <Button variant="fill-outline" color="accent" rounded={false}>false</Button>
    </div>
  </div>
</Preview>

<h2>Uppercase</h2>

<Preview>
  <Button class="uppercase">default</Button>
  <Button class="uppercase" variant="outline" color="accent">outline</Button>
  <Button class="uppercase" variant="fill" color="accent">fill</Button>
  <Button class="uppercase" variant="fill-light" color="accent">fill-light</Button>
  <Button class="uppercase" variant="fill-outline" color="accent">fill-outline</Button>
  <Button class="uppercase" variant="text" color="accent">text</Button>
</Preview>

<h2>Tooltip</h2>

<Preview>
  <Tooltip title="Really, do it!" placement="right" offset={2}>
    <Button>Click me</Button>
  </Tooltip>
</Preview>

<h2>Tooltip (disabled)</h2>

<Preview>
  <Tooltip title="Really, do it!" placement="right" offset={2}>
    <Button disabled>Click me</Button>
  </Tooltip>
</Preview>

<h2>Text with icon</h2>

<Preview>
  <div class="flex items-center">
    <Button icon={mdiTrashCan} color="red">Delete</Button>
    <Button icon={mdiMagnify} class="flex-row-reverse">Search</Button>
    <Button icon={mdiHome} class="flex-col">Home</Button>
    <Button icon={mdiHome} class="flex-col-reverse">Home</Button>
    <Button icon={faUser}>Profile</Button>
  </div>
</Preview>

<h2>Pass props to Icon</h2>

<Preview>
  <Button icon={{ data: mdiTrashCan, size: '2rem', style: 'color:#b91c1c' }} color="red"
    >Delete</Button
  >
</Preview>

<SectionDivider class="mt-12">Icon only</SectionDivider>

<h2>Icon-only button</h2>

<Preview>
  <Button icon={mdiMenu} />
</Preview>

<h2>Icon-only size</h2>

<Preview>
  <Button icon={mdiMenu} size="sm" />
  <Button icon={mdiMenu} size="md" />
  <Button icon={mdiMenu} size="lg" />
</Preview>

<h2>Icon-only button with custom padding</h2>

<Preview>
  <Button icon={mdiMenu} class="p-2" />
</Preview>

<h2>Icon via url</h2>

<Preview>
  <Button icon="https://api.iconify.design/mdi:account.svg" class="p-2" />
</Preview>

<h2>Icon via SVG string</h2>

<Preview>
  <Button
    icon={'<svg width="32" height="32" viewBox="0 0 24 24"><path fill="currentColor" d="M12 4a4 4 0 0 1 4 4a4 4 0 0 1-4 4a4 4 0 0 1-4-4a4 4 0 0 1 4-4m0 10c4.42 0 8 1.79 8 4v2H4v-2c0-2.21 3.58-4 8-4Z"/></svg>'}
    class="p-2"
  />
</Preview>

<h2>Icon-only button variants and color</h2>

<Preview>
  <div>
    <Button icon={mdiMenu} />
    <Button icon={mdiMenu} color="accent" />
  </div>
  <div>
    <Button icon={mdiMenu} variant="outline" />
    <Button icon={mdiMenu} variant="outline" color="accent" />
  </div>
  <div>
    <Button icon={mdiMenu} variant="fill" />
    <Button icon={mdiMenu} variant="fill" color="accent" />
  </div>
  <div>
    <Button icon={mdiMenu} variant="fill-light" />
    <Button icon={mdiMenu} variant="fill-light" color="accent" />
  </div>
  <div>
    <Button icon={mdiMenu} variant="fill-outline" />
    <Button icon={mdiMenu} variant="fill-outline" color="accent" />
  </div>
  <div>
    <Button icon={mdiMenu} variant="text" />
    <Button icon={mdiMenu} variant="text" color="accent" />
  </div>
</Preview>
