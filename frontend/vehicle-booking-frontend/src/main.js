// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueResource from 'vue-resource'
import VueRouter from 'vue-router'
import store from './store/store'
import moment from 'moment'
// Import this component
import datePicker from 'vue-bootstrap-datetimepicker'
// Import date picker css
import 'eonasdan-bootstrap-datetimepicker/build/css/bootstrap-datetimepicker.css'

Vue.use(VueResource)
Vue.use(VueRouter)
Vue.use(datePicker)

// Vue.http.options.root = 'https://vuejs-http.firebaseio.com/'

Vue.http.options.root = 'http://127.0.0.1:8000/'

Vue.http.headers.common['Authorization'] = 'JWT ' + localStorage.getItem('token')

Vue.http.interceptors.push((request, next) => {
    if (request.method === 'POST') {
    // request.method = 'PUT'
    }
    next(response => {
        response.json = () => { return {messages: response.body} }
    })
})

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    store,
    moment,
    template: '<App/>',
    components: { App }
})
