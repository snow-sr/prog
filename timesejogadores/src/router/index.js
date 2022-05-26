import { createRouter, createWebHistory } from "vue-router";
import TimesView from "../views/TimesView.vue";
import JogadoresView from "../views/JogadoresView.vue";
import Home from "../views/HomeView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "Home",
      component: Home,
    },
    {
      path: "/teams",
      name: "Times",
      component: TimesView,
    },
    {
      path: "/players",
      name: "Jogadores",
      component: JogadoresView,
    },
  ],
});

export default router;
