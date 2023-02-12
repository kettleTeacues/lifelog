import Vue from 'vue'
import VueRouter from 'vue-router'

import index from '../views/index.vue'
import list from '../views/list.vue'
import about from '../views/about.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'index',
        component: index
    },
    {
        path: '/list',
        name: 'list',
        component: list
    },
    {
        path: '/about',
        name: 'about',
        component: about
    },
]

const router = new VueRouter({
    mode: 'history',
    base: '/',
    routes
})

export default router
