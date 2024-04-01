import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import zhCn from "element-plus/es/locale/lang/zh-cn"//国际化
import 'bootstrap'
import "@popperjs/core";
import 'bootstrap/dist/css/bootstrap.min.css'
import axios from 'axios'

// 监听浏览器窗口关闭事件
// window.addEventListener('beforeunload', function() {
//   // 清除localStorage
//   localStorage.clear();
// });
const app = createApp(App);
//axios发送http请求的目标地址的基础路径
axios.defaults.baseURL = "/api"
app.config.globalProperties.$axios = axios
app.use(ElementPlus, { locale: zhCn }).use(router).mount('#app')

//全局注册图标组件
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}
