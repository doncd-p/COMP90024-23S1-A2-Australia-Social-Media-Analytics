import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect: '/home',
    name: 'Layout',
    component: () => import(/* webpackChunkName: "about" */ '../layout/index'),
    children: [
      {
        path: 'home',
        name: 'Home',
        component: () => import('../views/home/Home.vue')
      },
      {
        path: 'dashboard',
        name: 'Dashboard',
        redirect: '/dashboard/ranking',
        component: () => import('../views/dashboard/index.vue'),
        children: [
          {
            path: 'distribution',
            name: 'Distribution',
            component: () => import('../views/dashboard/Distribution.vue')
          },
          {
            path: 'ranking',
            name: 'Ranking',
            component: () => import('../views/dashboard/Ranking.vue')
          },
        ]
      },
      {
        path: 'about',
        name: 'Aboout',
        component: () => import('../views/about/About.vue')
      },
      {
        path: 'map',
        name: 'Map',
        component: () => import('../views/map/Map.vue')
      }
    ]
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
