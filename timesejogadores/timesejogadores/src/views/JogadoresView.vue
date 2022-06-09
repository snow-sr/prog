<script>
import { useTeamsStore } from "../stores/teams.js";
import { mapState, mapStores, mapActions} from 'pinia'

export default {
  setup() {
    const store = useTeamsStore();

    return { store, getTeam: store.getTeam };
  },
  data() {
    return {
      InputTeam: "",
      InputUser: "",
    }
  },
  computed: {
    ...mapState(useTeamsStore, ['teams', 'getTeam'])
    
  },
  methods: {
    ...mapStores(useTeamsStore),
    ...mapActions(useTeamsStore, ["addPlayer"]),

      addToTeam(){
          if(this.InputTeam == null || this.InputUser == null){
            return 0;
          }
          this.addPlayer(this.InputUser, this.InputTeam)
          
      }
  },
};
</script>

<template>
  <div class="bg-slate-700 h-full w-full flex flex-col items-center">
    <div class="m-5">
      <h1 class="text-white text-4xl">
        Jogadores de {{ getTeam($route.params.lookingFor).name }}
      </h1>
    

      <div class="text-white text-center border m-5">
        <ul v-for="player in getTeam($route.params.lookingFor).players">
          <li class="underline mt-3 mb-3">
            {{ player }}
          </li>
        </ul>
      </div>
    </div>
  </div>

  <div class="bg-slate-700 h-screen w-full flex flex-col justify-center">
    <div class="relative flex py-5 items-center">
      <div class="flex-grow border-t border-gray-400"></div>
      <span class="flex-shrink mx-4 text-gray-400">Cadastrar Jogadores</span>
      <div class="flex-grow border-t border-gray-400"></div>
    </div>

    <div class="m-5 text-center flex flex-col justify-center items-center">
      <label
        for="exampleFormControlInput2"
        class="form-label inline-block mb-2 text-gray-200 text-xl"
        >Gerenciamento de times</label
      >

      <div class="flex justify-center">
        <div class="mb-3 xl:w-96">
          <select
            class="form-select appearance-none block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding bg-no-repeat border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
            aria-label="Default select example"
            v-model="InputTeam"
          >
            <option selected disabled>Escolha um time:</option>
            <option v-for="team in teams" >{{team.name}}</option>
            </select>
        </div>
      </div>

      <input
        type="text"
        class="form-control block w-full px-3 py-1.5 mt-6 w-96 text-xl font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
        id="exampleFormControlInput2"
        placeholder="Insira o nome do jogador"
        v-model="InputUser"
      />
      <button
        type="button"
        class="inline-block mt-3 px-6 py-2.5 bg-purple-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-purple-700 hover:shadow-lg focus:bg-purple-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-purple-800 active:shadow-lg transition duration-150 ease-in-out"
        @click="addToTeam()"
      >
        Salvar
      </button>
    </div>
  </div>
</template>
