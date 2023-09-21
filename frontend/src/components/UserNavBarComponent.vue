<template>
  <div class="navbar">
    <router-link to="/" class="logo">Booking App</router-link>
    <div class="greet">
      <span v-if="isLoggedIn && !isAdmin">Welcome, {{ user.name }}</span>
      <span v-else-if="isLoggedIn && isAdmin"
        >Welcome, {{ user.name }} (Admin)</span>
    </div>
    <div class="nav-links">
      <!-- <button v-if="isLoggedIn" @click="exportTheatreCSV">CSV</button> -->
      <form @submit.prevent="search">
        <input type="text" v-model="searchQuery" placeholder="Search" />
      </form>
      <button v-if="!isLoggedIn" @click="showLogin">Login</button>
      <button v-if="!isLoggedIn" @click="showRegister">Register</button>


      <button v-else @click="logout">Logout</button>
      
    </div>
    <!-- Show searh results -->
    <div class="searchResult" v-if="showSearchResults">
      <h3>Movies</h3>
      <ul>
        <li v-for="movie in movies" :key="movie.id">
          <router-link :to="{ name: 'movie', params: { id: movie.id } }">
            {{ movie.title }}
          </router-link>
        </li>
      </ul>
      <h3>Venues</h3>
      <ul>
        <li v-for="venue in venues" :key="venue.id">
          <router-link :to="{ name: 'venue', params: { id: venue.id } }">
            {{ venue.name }}
          </router-link>
        </li>
      </ul>
    </div>
  </div>

</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      searchQuery: '',
      isLoggedIn: false, // Set this to true when the user is logged in
      user: {},
      isAdmin: false,
      movies: [],
      venues: [],
      showSearchResults: false,
    };
  },
  created() {
    // Check if the user is logged in
    this.isLoggedIn = localStorage.getItem('access_token') ? true : false;
    this.user = JSON.parse(localStorage.getItem('user'));
    console.log('Is logged in:', this.isLoggedIn)
    this.isAdmin = this.user.role === 'admin' ? true : false;
    // If so, set isLoggedIn to true
    // Otherwise, set it to false
  },
  methods: {
    async search() {
      const response = await axios.get(`http://localhost:5000/search?name=${this.searchQuery}`);
      console.log("data",response.data);
      this.movies = response.data.movie;
      this.venues = response.data.venue;
      this.showSearchResults = true;
    },  
    handleSearch() {
      // Implement your search functionality here
      console.log('Search:', this.searchQuery);
    },
    showLogin() {
      // Implement your login logic here
      this.$router.push('/login');
      console.log('Show login form');
    },
    showRegister() {
      // Implement your register logic here
      this.$router.push('/register');
      console.log('Show register form');
    },

    // async exportTheatreCSV() {
    //   try {
    //     // Call the backend API to trigger the export CSV task
    //     const response = await axios.post(
    //       `http://localhost:5000/export_theatre_csv/${theatreId}`,
    //       null,
    //       {
    //         headers: {
    //           Authorization: `Bearer ${localStorage.getItem('access_token')}`,
    //         },
    //       }
    //     );
    //     console.log(response.data);
    //     // Show a success message or alert
    //   } catch (error) {
    //     console.error('Error exporting theatre as CSV:', error);
    //     // Show an error message or alert
    //   }
    // },

    logout() {
      // Implement your logout logic here
      localStorage.removeItem('access_token');
      localStorage.removeItem('user');
      this.$router.push('/');
      this.isLoggedIn = false;
    },
  },
};
</script>

<style lang="scss">
$primary-color: #3498db;
$secondary-color: #e74c3c;


.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
  background-color: #333;
  color: white;

  .logo {
    font-size: 24px;
    font-weight: bold;
    text-decoration: none;
    color: white;

    &:hover {
      text-decoration: none;
      color: white;
    }
  }

  .greet {
    font-size: 16px;
    margin-right: 10px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .nav-links {
    display: flex;
    align-items: center;

    input {
      padding: 5px;
      margin-right: 10px;
      border: 1px solid #777;
      border-radius: 4px;
      background-color: #444;
      color: white;

      &:focus {
        outline: none;
        border-color: $primary-color;
        background-color: white;
        color: black;
      }
    }

    button {
      padding: 5px 10px;
      border: none;
      background-color: #555;
      color: white;
      cursor: pointer;
      transition: background-color 0.3s ease;

      &:hover {
        background-color: #777;
      }
    }
  }
  .searchResult{
    position: absolute;
    top: 100%;
    left: 0;
    width: 100%;
    background-color: #333;
    color: white;
    padding: 10px;
    z-index: 1;
    ul{
      list-style: none;
      padding: 0;
      margin: 0;
      li{
        margin: 5px 0;
        a{
          color: white;
          text-decoration: none;
          &:hover{
            text-decoration: underline;
          }
        }
      }
    }
  }
}
</style>

