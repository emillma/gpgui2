import { defineConfig } from 'vitest/config';
import { sveltekit } from '@sveltejs/kit/vite';
import { sveld } from './src/lib/plugins/vite';

export default defineConfig({
  plugins: [sveltekit(), sveld()],
  test: {
    include: ['src/**/*.{test,spec}.{js,ts}'],
  },
  server: {
    port: 12101,
    strictPort: true,
  },
  // define: {
  //   global: {}, //https://github.com/vitejs/vite/discussions/5912
  // }
});
