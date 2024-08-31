import { fileURLToPath, URL } from "node:url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

// https://vitejs.dev/config/
export default defineConfig(({ command, mode, ssrBuild }) => {
  const config = {
    plugins: [vue()],
    server: { port: 3000, strictPort: true },
    resolve: {
      alias: {
        "@": fileURLToPath(new URL("./src", import.meta.url)),
      },
    },
    // base: '/dist'
  };

  let buildConfig = {
    outDir: "../static/",
    emptyOutDir: true,
    rollupOptions: {
      input: "main.js",
    },
  };

  buildConfig.rollupOptions.output = {
    entryFileNames: "[name].js",
    assetFileNames: "assets/[name].[ext]",
  };

  return {
    ...config,
    build: buildConfig,
  };
});
