import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    redirect: '/login'
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/Login/LoginView.vue'),
    meta: { requiresAuth: false }
  },
  {
    path: '/register',
    name: 'register',
    component: () => import('@/views/Login/RegisterView.vue'),
    meta: { requiresAuth: false }
  },
  {
    path: '/admin_index',
    name: 'admin_index',
    component: () => import("@/views/Admin/IndexView.vue"),
    meta: { requiresAuth: true },
    children: [
      {
        path: '/admin_index',
        redirect: '/admin_home'
      },
      {
        path: "/admin_home",
        name: "admin_home",
        component: () => import("@/views/Admin/Module/HomeView.vue"),
      },
      {
        path: "/admin_user",
        name: "admin_user",
        component: () => import("@/views/Admin/Module/UserView.vue"),
      },
      {
        path: "/admin_login_log",
        name: "admin_login_log",
        component: () => import("@/views/Admin/Module/LoginLogView.vue"),
      },
      {
        path: "/admin_card_record",
        name: "admin_card_record",
        component: () => import("@/views/Admin/Module/CardRecordView.vue"),
      },
    ]
  },
  {
    path: '/user_index',
    name: 'user_index',
    component: () => import("@/views/User/IndexView.vue"),
    meta: { requiresAuth: true },
    children: [
      {
        path: '/user_index',
        redirect: '/user_home'
      },
      {
        path: "/user_home",
        name: "user_home",
        component: () => import("@/views/User/Module/HomeView.vue"),
      },
      {
        path: "/user_mark_card",
        name: "user_mark_card",
        component: () => import("@/views/User/Module/MarkCodeView.vue"),
      },
      {
        path: "/user_card_record",
        name: "user_card_record",
        component: () => import("@/views/User/Module/CardRecordView.vue"),
      },
    ]
  }

]

const router = createRouter({
  history: createWebHistory('/liuyuhao/web'),
  routes
})

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('access_token');
  // 如果路由需要登录验证
  if (to.meta.requiresAuth) {
    // 如果用户未登录，则跳转到登录页面
    if (!token) {
      next('/login');
    } else {
      // 如果路由不需要登录验证，直接放行
      next();
    }
  } else {
    next();
  }
});

export default router
