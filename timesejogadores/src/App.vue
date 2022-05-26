<script>
import headerComponent from "./components/headerComponent.vue";
import footerComponent from "./components/footerComponent.vue";
export default {
  components: {
    headerComponent,
    footerComponent,
  },
};
</script>

<template>
  <headerComponent />
  <router-view></router-view>
  <footerComponent />
</template>
