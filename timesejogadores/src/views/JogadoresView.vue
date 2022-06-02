<script>
import { useTeamsStore } from "../stores/teams.js";

export default {
  setup() {
    const store = useTeamsStore();

    return { getTeam: store.getTeam };
  },
};
</script>

<template>
  <div class="bg-slate-700 h-screen w-full flex justify-center">
    <div class="m-5">
      <h1 class="text-white text-4xl">
        Jogadores de {{ getTeam($route.params.lookingFor).name }}
      </h1>

       <div class="text-white text-center border m-5">
        <ul v-for="player in getTeam($route.params.lookingFor).players">
          <li class="underline mt-3 mb-3">
            {{player}}
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>
