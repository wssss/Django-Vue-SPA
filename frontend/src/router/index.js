import Vue from 'vue'
import Router from 'vue-router'
import index from '@/pages/index'
import post from '@/pages/post'

Vue.use(Router)

export default new Router({
	routes: [
		{
			path: '/',
			name: 'index',
			component: index
		},
		{
			path: '/post/:id',
			name: 'post',
			component: post
		}
	]
})
