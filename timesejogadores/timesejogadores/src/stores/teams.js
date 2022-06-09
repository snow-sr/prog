import { defineStore } from "pinia";
import { v4 as uuidv4 } from 'uuid';

export const useTeamsStore = defineStore("Teams", {
  state: () => ({
    teams: [
      { name: "teste", players: ["adilson", "bernardo", "cássio"], id: uuidv4() },
      { name: "teste2", players: ["david", "elias", "fábio"], id: uuidv4() },
      { name: "teste3", players: ["guilherme", "hariel", "joão"], id: uuidv4() },
      { name: "teste4", players: ["kaik", "lui", "marco"], id: uuidv4() },
    ],
    selectedTeam: "",
  }),
  getters: {
    getTeam: (state) => {
      return (teamName) => state.teams.find((team) => team.name === teamName);
    },
    getAllTeams: (state) => {
      return (state.teams)
    },
  },
  actions: {
    addTeam(x) {
      this.teams.push(x);
      return "Added";
    },
    addPlayer(x, y){
      let arr = this.getTeam(y);
      console.log(arr)
      arr.players.push(x)
      console.log(arr, this.teams) 
    }
  }
});
