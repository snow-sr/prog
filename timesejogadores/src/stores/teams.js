import { defineStore } from "pinia";

export const useTeamsStore = defineStore("Teams", {
  state: () => ({
    teams: [
      { name: "teste", players: ["adilson", "bernardo", "cássio"] },
      { name: "teste2", players: ["david", "elias", "fábio"] },
      { name: "teste3", players: ["guilherme", "h", "j"] },
      { name: "teste4", players: ["kaik", "lui", "marco"] },
    ],
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
  },
});
