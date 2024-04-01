import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";


 
// vue项目自带路由
const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "index",
    component: () => import("@/templates/index.vue"),
  },
  {
    path: "/register",
    name: "register",
    component: () => import   ("@/templates/register.vue"),
  },
  {
    path: "/login",
    name: "login",
    component: () => import("@/templates/login.vue"),
  },
  {
    path: "/about",
    name: "about",
    component: () => import("@/templates/about.vue"),
  },
  {
    path: "/blog",
    name: "blog",
    component: () => import("@/templates/blog.vue"),
  },
  {
    path: "/hexo_config",
    name: "hexo_config",
    component: () => import("@/templates/hexo_config.vue"),
  },
  {
    path: "/hexo_theme",
    name: "hexo_theme",
    component: () => import("@/templates/hexo_theme.vue"),
  }
];
 

 
const router = createRouter({
  history: createWebHistory(),
  routes: routes,
});
 

// 路由守卫，确保用户在未登录时无法访问受保护的路由
// 并自动重定向到登录页面
router.beforeEach((to, from, next) => {
  console.log(from);
  if (to.name !== "login" && to.name !== "register" && !localStorage.getItem("token")) {
    // 未登录且要跳转的页面不是登录页
    console.log("未登录");
    return next("/login");
    
  }
  next();
});
export default router;
 