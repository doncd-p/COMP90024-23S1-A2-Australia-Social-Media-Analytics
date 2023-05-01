import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import Element from 'element-ui';
import './assets/css/element-variables.scss';
import locale from 'element-ui/lib/locale/lang/en'
// Git test commit
Vue.use(ElementUI, { locale })
Vue.use(Element);
Vue.use(ElementUI);
Vue.prototype.$axios = axios;

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
