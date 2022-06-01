<script>
export default {
  data() {
    return {
      teams: [
        { name: "teste", jogadores: ["a", "b", "c"] },
        { name: "teste2", jogadores: ["a2", "b2", "c2"] },
        { name: "teste3", jogadores: ["a3", "b3", "c3"] },
        { name: "teste4", jogadores: ["a4", "b4", "c4"] },
      ],
    };
  },
};
</script>

<template>
  <div class="bg-slate-700 h-screen w-full flex justify-center">
    <div class="m-5">
      <h1 class="text-white text-4xl">Ver times e jogadores de cada time!</h1>

      <div class="text-white text-center border m-5">
        <ul v-for="team in teams">
          <li class="underline mt-3 mb-3">
            {{ team.name }}
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>
