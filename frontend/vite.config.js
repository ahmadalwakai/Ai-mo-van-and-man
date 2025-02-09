import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  base: "/Ai-mo-van-and-man/",
  build: {
    rollupOptions: {
      input: "index.html",
      external: ["axios"], // ✅ Ensures axios is correctly resolved
    }
  },
  optimizeDeps: {
    include: ["axios"] // ✅ Ensures axios is included in the dependencies
  }
});
