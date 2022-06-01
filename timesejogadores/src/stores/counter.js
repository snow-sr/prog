import { defineStore } from 'pinia'

export const useTeamsStore = defineStore({
  id: 'Teams',
  state: () => ({
    teams: []
  }),
  actions: {
    increment(x) {
      this.teams.push(x)
    }
  }
})
