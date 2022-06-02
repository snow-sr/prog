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
      <li class="mr-3">
        <RouterLink class="text-pink-500 hover:text-pink-800" :to="{name: 'Home'}"
          >Home</RouterLink
        >
      </li>
      <p class="mr-3 text-pink-500">
        |
      </p>
      <li class="mr-3">
        <RouterLink class="text-pink-500 hover:text-pink-800" :to="{name: 'Times'}"
          >Time</RouterLink
        >
      </li>
      <p class="mr-3 text-pink-500">
        |
      </p>
      <li class="mr-6">
        <RouterLink class="text-pink-500 hover:text-pink-800" :to="{name: 'Jogadores'}"
          >Jogadores</RouterLink
        >
      </li>
    </ul>

    <ul class="flex justify-end align-end">
      <li class="mr-3">
        <RouterLink class="text-pink-500 hover:text-pink-800" to="/"
          >Sair</RouterLink
        >
      </li> 
    </ul>
  </div>
</template>
