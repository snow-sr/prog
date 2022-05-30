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
    class="container-fluid w-full flex flex-wrap items-end justify-between px-10 py-10 bg-gray-900"
  >
    <ul class="flex">
      <li class="mr-6">
        <RouterLink class="text-blue-500 hover:text-blue-800" to="/"
          >Home</RouterLink
        >
      </li>
      <li class="mr-6">
        <RouterLink class="text-blue-500 hover:text-blue-800" to="/teams"
          >Times</RouterLink
        >
      </li>
      <li class="mr-6">
        <RouterLink class="text-blue-500 hover:text-blue-800" to="/players"
          >Jogadores</RouterLink
        >
      </li>
    </ul>
  </div>
</template>
