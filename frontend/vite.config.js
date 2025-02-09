import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  
  // ✅ Ensures correct paths for GitHub Pages
  base: "/Ai-mo-van-and-man/",

  build: {
    outDir: "dist",
    assetsDir: "assets",
    rollupOptions: {
      output: {
        entryFileNames: "assets/[name]-[hash].js",
        chunkFileNames: "assets/[name]-[hash].js",
        assetFileNames: "assets/[name]-[hash][extname]",
      },
    },
  },

  server: {
    host: "0.0.0.0",
    port: 5173,
    open: true,
  },

  preview: {
    port: 5000,
    open: true,
  },

  optimizeDeps: {
    include: ["axios", "react", "react-dom", "react-router-dom"],
  },

  define: {
    "process.env": {},
  },
});
