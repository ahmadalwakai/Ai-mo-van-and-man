import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  base: "/Ai-mo-van-and-man/",
  build: {
    rollupOptions: {
      external: [],  // ✅ Ensures axios is bundled properly
    },
  },
  optimizeDeps: {
    include: ["axios"], // ✅ Forces axios to be included in the build
  }
});
