import Vue from 'vue'
import Vuex from 'vuex'
// import axios from 'axios'
// import router from '../router'

Vue.use(Vuex)

export default new Vuex.Store({
  // global variables
  state: {
    actorData: {},
    actorNamesList: [],

    movies_list: {},
    movies_names_list: {},

    venues_list: {},
    venues_names_list: {}
  },

  getters: {
    
    // venue getters
    getVenueData: (state) => {
      return state.venues_list;
    },
    getVenueNamesList: (state) => {
      return state.venues_names_list;
    },
    
    
    //Movie show getters
    getMovieData: (state) => {
      return state.movies_list
    },
    getMovieNamesList: (state) => {
      return state.movies_names_list;
    },


    // 
    getActorData(state) {
      return state.actorData;
    },
    getActorNames(state) {
      return state.actorNamesList;
    },
  },


  mutations: {
    // user related mutations
    setUserData: (state, data) => {
      state.userData = data
    },

    // actor related mutations
    setActorData(state, payload) {
      state.actorData = payload;
    },
    setActorNames(state, payload) {
      state.actorNames = payload;
    },
    
    
    // movie related mutations
    setMovieData(state, payload) {
      state.movies_list = payload;
    },
    setMovieNamesList: (state, payload) => {
      state.movies_names_list = payload;
    },

    // venue related mutations
    setVenueData: (state, payload) => {
      state.venues_list = payload;
    },
    setVenueNamesList: (state, payload) => {
      state.venues_names_list = payload;
    }

  },


  actions: {

    // User related actions
    // async registerUser(_, payload) {
    //   try {
    //     const response = await axios.post("/users", payload);
    //     console.log("Registration successful", response.data);
    //     // Perform any additional actions or mutations
    //     console.log(response);
    //     router.push('/userHome')
    //   } catch (error) {
    //     console.error("Registration failed", error.response.data);
    //     // Handle the error, display a message, etc.
    //   }
    // },


    
    // Venue related actions
    //POST
    // async submitVenueDetails({ commit }, payload) {
    //   console.log("payload", payload);
    //   axios.post("http://127.0.0.1:5000/venues", payload)
    //     .then((response) => { 
    //       console.log(response);
    //       commit('setVenueData', response.data.venues_list)
    //       commit('setVenueNamesList', response.data.venues_names_list)
    //     })
    //     .catch((error) => {
    //       console.log(error.response.data);
    //     })
    // },

    // Edit venue
    // async editVenue({ commit }, payload) {
    //   console.log("payload", payload);
    //   axios.put("http://127.0.0.1:8000/api/editVenue", payload)
    //     .then((response) => {
    //       console.log(response);
    //       commit('setVenueData', response.data.venues_list)
    //       commit('setVenueNamesList', response.data.venues_names_list)
    //     })
    //     .catch((error) => {
    //       console.log(error.response.data);
    //     });
    // },

    //DELETE VENUE
    // async deleteVenue({ commit }, payload) {
    //   console.log("payload", payload);
    //   axios.delete(`http://127.0.0.1:8000/api/deleteVenueDetails/${payload.venueName}`)
    //     .then((response) => {
    //       commit('setVenueData', response.data.venues_list)
    //       console.log(response);
    //       commit('setVenueNamesList', response.data.venues_names_list)
    //     })
    //     .catch((error) => {
    //       console.log(error.response.data);
    //     })
    // },




    // Movie/show related actions
    // // Post request
    // async submitMovieDetails({ commit }, payload) {
    //   console.log("payload", payload);
    //   axios.post("http://127.0.0.1:8000/api/submitMovieDetails", payload)
    //     .then((response) => {
    //       console.log("response", response);
    //       commit('setMovieData', response.data.movies_list)
    //       commit('setMovieNames', response.data.movies_names_list);
    //     })
    //     .catch((error) => {
    //       console.error(error.response.data);
    //     });
    // },





  },



  modules: {
  }


})



