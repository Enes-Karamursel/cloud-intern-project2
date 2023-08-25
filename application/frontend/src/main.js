import { createApp } from 'vue';
import '@/assets/css/main.css';
import '@/assets/css/formalize.css';
import '@/assets/css/normalize.css';
import 'bootstrap/dist/css/bootstrap.min.css';
// eslint-disable-next-line import/no-extraneous-dependencies
import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faArrowRightFromBracket } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import App from './App.vue';
import store from './store';
import router from './router';

library.add(faArrowRightFromBracket);



createApp(App)
  .component('font-awesome-icon', FontAwesomeIcon)
  .use(store)
  .use(router)
  .use(VueSweetalert2)
  .mount('#app');
