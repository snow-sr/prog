<script>
import { RouterLink } from "vue-router";

export default {
  components: {
    RouterLink,
  },
};
</script>

<template>
  <div
    class="container-fluid w-full flex flex-wrap items-center justify-between px-12 py-8 bg-purple-800"
  >
    <ul class="flex">
      <li class="mr-6">
        <RouterLink class="text-pink-500 hover:text-pink-800" to="/"
          >Home</RouterLink
        >
      </li>
      <li class="mr-6">
        <RouterLink class="text-pink-500 hover:text-pink-800" to="/teams"
          >Times</RouterLink
        >
      </li>
      <li class="mr-6">
        <RouterLink class="text-pink-500 hover:text-pink-800" to="/players"
          >Jogadores</RouterLink
        >
      </li>
    </ul>
  </div>
</template>
