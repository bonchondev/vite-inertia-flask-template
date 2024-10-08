import "./app.css"
import { createApp, h } from 'vue';
// import type { App } from 'vue';
import { createInertiaApp } from '@inertiajs/inertia-vue3';
import { VueQueryPlugin } from "@tanstack/vue-query";

// type StrOrNum = string | number

// declare global {
//   interface Window {
//     reverseUrl(urlName: string, args?: Record<string, unknown> | StrOrNum | StrOrNum[]): string
//   }
// }
//
// create a plugin to use window.reverseUrl in our Components
const routePlugin = {
  install: (app, _options) => {
    app.config.globalProperties.$route = window.reverseUrl;
  }
}

createInertiaApp({
  resolve: async name => {
    const page = await import(`./src/pages/${name}.vue`);
    return page.default;
  },
  setup({ el, app, props, plugin }) {
    const vueApp = createApp({ render: () => h(app, props) });
    vueApp.use(plugin);
    vueApp.use(routePlugin);
    vueApp.use(VueQueryPlugin);
    vueApp.mount(el);
  }
})
