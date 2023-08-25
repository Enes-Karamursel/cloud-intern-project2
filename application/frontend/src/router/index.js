import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import ResultView from '@/views/ResultView.vue';


const routes = [
  {
    path: '/',
    name: '',
    component: () => import('../components/SignupComponent.vue'),
  },
  {
    path: '/protected',
    name: 'protected',
    component: () => import('../components/ProtectedPages.vue'),
  },
  {
    path: '/home',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/result',
    name: 'result',
    component: ResultView,
  },
  {
    path: '/signup',
    name: 'Signup',
    component: () => import('../components/SignupComponent.vue'),
  },
  {
    path: '/sign_in',
    name: 'login',
    component: () => import('../components/LoginComponent.vue'),
  },
  {
    path: '/ForgotPassword',
    name: 'ForgotPassword',
    component: () => import('../components/ForgotPassword.vue'),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// router.beforeEach((to, from, next) => {
//   const loggedIn = auth.getters.isLogin;
//   if (to.matched.some((record) => record.meta.requiresAuth)) {
//     if (loggedIn) {
//       next();
//       return;
//     }
//     next('/sign_in');
//   } else {
//     next();
//   }
// });

export default router;
