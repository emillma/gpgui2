<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  import { mdiMinus, mdiPlus } from '@mdi/js';

  import { Button, TextField } from '.';
  import { selectOnFocus } from '$lib/actions/input';
  import { getComponentTheme } from './theme';
  import { cls } from '$lib/utils/styles';

  export let value: number = 0;
  export let min: number | undefined = undefined;
  export let max: number | undefined = undefined;

  const theme = getComponentTheme('NumberStepper');

  const dispatch = createEventDispatcher();

  $: dispatch('change', { value });
</script>

<TextField
  type="integer"
  bind:value
  align="center"
  class={cls('NumberStepper w-24', theme.root, $$props.class)}
  actions={(node) => [selectOnFocus(node)]}
  {...$$restProps}
>
  <div slot="prepend" class="flex">
    <Button
      icon={mdiMinus}
      on:click={() => (value -= 1)}
      size="sm"
      disabled={min != null && value <= min}
    />
  </div>
  <div slot="append" class="flex">
    <Button
      icon={mdiPlus}
      on:click={() => (value += 1)}
      size="sm"
      disabled={max != null && value >= max}
    />
  </div>
</TextField>
