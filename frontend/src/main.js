// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import highlightjs from 'highlight.js'; 
import * as custom from './libs/filters'


Vue.prototype.$http = axios;

//filters
Object.keys(custom).forEach(key => {
  Vue.filter(key, custom[key])
})

Vue.directive('highlight',function (el) {
    let blocks = el.querySelectorAll('pre code');
    blocks.forEach((block)=>{
      highlightjs.highlightBlock(block)
    })
})

Vue.config.productionTip = false;
axios.defaults.baseURL = 'http://127.0.0.1:8000/';

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
