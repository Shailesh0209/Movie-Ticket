import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './registerServiceWorker'
import '@fortawesome/fontawesome-free/css/all.css'



// import AdminActorComponent from '@/components/AdminActorComponent.vue'
// import AdminHomeComponent from '@/components/AdminHomeComponent.vue'
import AdminNavBarComponent from '@/components/AdminNavBarComponent.vue'
import VenueNavBarComponent from '@/components/VenueNavBarComponent.vue'

// import UserHomeComponent from '@/components/UserHomeComponent.vue'
import UserNavBarComponent from '@/components/UserNavBarComponent.vue'


// Vue.component('AdminActorComponent', AdminActorComponent)
// Vue.component('AdminHomeComponent', AdminHomeComponent)
Vue.component('AdminNavBarComponent', AdminNavBarComponent)
Vue.component('VenueNavBarComponent', VenueNavBarComponent)

// Vue.component('UserHomeComponent', UserHomeComponent)
Vue.component('UserNavBarComponent', UserNavBarComponent)


Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
