import Vue from 'vue'
import VueRouter from 'vue-router'

import month from '../views/month.vue'
import week from '../views/week.vue'
import list from '../views/list.vue'
import about from '../views/about.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'week',
        component: week
    },
    {
        path: '/month',
        name: 'month',
        component: month
    },
    {
        path: '/week',
        name: 'week',
        component: week
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
    base: process.env.BASE_URL,
    routes
})

export default router
