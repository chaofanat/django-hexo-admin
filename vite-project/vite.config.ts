import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

import AutoImport from "unplugin-auto-import/vite";
import Components from "unplugin-vue-components/vite";
import { ElementPlusResolver } from "unplugin-vue-components/resolvers";
//import { resolve } from 'path'
import path from "path";

// HTTP代理设置
const proxy = {
  "/api": {
    target: "http://127.0.0.1:8081/hexoadmin", // Django服务器api的地址
    changeOrigin: true, // 允许跨域
    rewrite: (path: string) => path.replace(/^\/api/, ""), // 重写路径
  },
} as Record<string, any>;

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    AutoImport({
      resolvers: [ElementPlusResolver()],
    }),
    Components({
      resolvers: [ElementPlusResolver()],
    }),
  ],
  server: {
    proxy,
  },
  resolve: {
    // ↓路径别名
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },

  build: {
    outDir: "dist", // 生成输出的根目录。如果该目录存在，则会在生成之前将其删除。 默认文件夹名称为dist
    target: "ESNext",
    terserOptions: {
      compress: {
        drop_console: true, // 生产环境去掉控制台 console
        drop_debugger: true, // 生产环境去掉控制台 debugger 默认就是true
        dead_code: true, // 删除无法访问的代码 默认就是true
      },
    },
    chunkSizeWarningLimit: 2000, // 调整区块大小警告限制
  },
});
