import Vue from 'vue'
import Router from 'vue-router'
import index from '@/components/index'
import my_class from '@/components/my_class'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: index
    },
    {
      path: '/class',
      name: 'my_class',
      component: my_class,
    },
  ]
})
