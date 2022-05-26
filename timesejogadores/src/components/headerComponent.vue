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
        <RouterLink class="text-blue-500 hover:text-blue-800" To="/Home"
          >Active</RouterLink
        >
      </li>
      <li class="mr-6">
        <RouterLink class="text-blue-500 hover:text-blue-800" To="/teams"
          >Times</RouterLink
        >
      </li>
      <li class="mr-6">
        <RouterLink class="text-blue-500 hover:text-blue-800" To="/players"
          >Jogadores</RouterLink
        >
      </li>
    </ul>
  </div>
</template>
