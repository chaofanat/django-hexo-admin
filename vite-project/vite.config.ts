import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import { ElementPlusResolver } from 'unplugin-vue-components/resolvers'
//import { resolve } from 'path'
import path from 'path'


// HTTP代理设置
const proxy = {
  '/api': {
    target: 'http://127.0.0.1:8081/hexoadmin', // Django服务器的地址
    changeOrigin: true, // 允许跨域
    rewrite: (path: string) => path.replace(/^\/api/, ""),
  },
} as Record<string, any>

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
    proxy
  },
  resolve: {
    // ↓路径别名
    alias: {
      "@": path.resolve(__dirname, './src')
    }
  },


})




