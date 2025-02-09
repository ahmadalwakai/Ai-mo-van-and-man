import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  base: "/Ai-mo-van-and-man/",
  build: {
    rollupOptions: {
      external: [],  // ✅ Remove axios from external (to ensure it is bundled)
    },
  },
  optimizeDeps: {
    include: ["axios"], // ✅ Ensures axios is included in the dependency optimization step
  }
});
