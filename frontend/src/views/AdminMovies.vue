<template>
  <div>
    <UserNavBarComponent />
    <div class="container">
      <h2>Admin Movies</h2>

      <div class="movie-list">
        <div v-for="movie in movies" :key="movie.id" class="movie-card">
          <div class="movie-info">
            <h3>{{ movie.title }}</h3>
            <p>Start Time: {{ movie.start_timing }}</p>
            <p>End Time: {{ movie.end_timing }}</p>
            <p>Ticket Price: {{ movie.ticket_price }}</p>
            <div class="buttons">
              <button @click="showEditMovieModal(movie)">Edit</button>
              <button class="danger" @click="deleteMovie(movie.id)">Delete</button>
            </div>
          </div>
        </div>
      </div>

      <div v-if="showModal" class="edit-movie-form">
        <h3>Edit Movie</h3>
        <form @submit.prevent="editMovie">
          <div>
            <label for="movie-title">Movie Title:</label>
            <input type="text" id="movie-title" v-model="movie.title" required>
          </div>
          <div>
            <label for="movie-start-time">Start Time:</label>
            <input type="time" id="movie-start-time" v-model="movie.start_timing" required>
          </div>
          <div>
            <label for="movie-end-time">End Time:</label>
            <input type="time" id="movie-end-time" v-model="movie.end_timing" required>
          </div>
          <div>
            <label for="movie-ticket-price">Ticket Price:</label>
            <input type="number" id="movie-ticket-price" v-model="movie.ticket_price" required>
          </div>
          <button type="submit">Edit</button>
          <button @click="cancelEditMovie">Cancel</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "AdminHome",
  components: {
    UserNavBarComponent: () => import('../components/UserNavBarComponent.vue')
  },
  data() {
    return {
      movies: [], // Populate this array with movie data from API
      showModal: false,
      movie: {
        id: null,
        title: '',
        start_timing: '',
        end_timing: '',
        ticket_price: 0
      }
    };
  },
  async created() {
    await this.fetchMovies();
  },
  methods: {
    async fetchMovies() {
      const venueId = this.$route.params.id;
      const venueResponse = await axios.get(`http://localhost:5000/venues/${venueId}`);
      this.movies = venueResponse.data.movies;
    },
    showEditMovieModal(movie) {
      this.showModal = true;
      this.movie = movie;
    },
    cancelEditMovie() {
      this.showModal = false;
      this.movie = {
        id: null,
        title: '',
        start_timing: '',
        end_timing: '',
        ticket_price: 0
      };
    },
    async editMovie() {
      try {
        await axios.put(`http://localhost:5000/movies/${this.movie.id}`, this.movie);
        this.cancelEditMovie();
      } catch (error) {
        console.error('Error editing movie:', error);
        // You can also display an error message to the user, if needed
      }
    },
    async deleteMovie(movieId) {
      await axios.delete(`http://localhost:5000/movies/${movieId}`);
      this.movies = this.movies.filter(movie => movie.id !== movieId);
    }
  }
};
</script>

<style lang="scss">
// Global Styles
$primary-color: #3498db;
$secondary-color: #e74c3c;


// UserNavBarComponent
.user-nav-bar {
  background-color: $primary-color;
  color: white;
  padding: 1rem;

  a {
    color: white;
    text-decoration: none;

    &:hover {
      text-decoration: underline;
    }
  }
}

// Container
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;

  h2 {
    font-size: 24px;
    margin-bottom: 1rem;
  }

  .movie-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1rem;
    margin-top: 2rem;

    .movie-card {
      background-color: #f7f7f7;
      border: 1px solid #ddd;
      padding: 1rem;
      border-radius: 5px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
      transition: transform 0.2s ease;

      .movie-info {
        h3 {
          font-size: 20px;
          margin-bottom: 0.5rem;
        }

        p {
          margin-bottom: 0.25rem;
        }

        button {
          margin-top: 1rem;
          background-color: $primary-color;
          color: white;
          border: none;
          padding: 0.5rem 1rem;
          cursor: pointer;
          transition: background-color 0.3s ease;

          &:hover {
            background-color: darken($primary-color, 10%);
          }
        }
      }

      &:hover {
        transform: translateY(-5px);
      }
    }
  }

  .edit-movie-form {
    border: 1px solid #ddd;
    padding: 1rem;
    background-color: white;
    border-radius: 5px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);

    h3 {
      font-size: 20px;
      margin-bottom: 1rem;
    }

    label {
      display: block;
      margin-bottom: 0.5rem;
      font-weight: bold;
    }

    input[type="text"],
    input[type="time"],
    input[type="number"] {
      width: 100%;
      padding: 0.5rem;
      border: 1px solid #ddd;
      border-radius: 4px;
      margin-bottom: 1rem;
    }

    button[type="submit"],
    button[type="button"] {
      margin-right: 1rem;
      padding: 0.5rem 1rem;
      border: none;
      cursor: pointer;
      background-color: $primary-color;
      color: white;

      &:hover {
        background-color: darken($primary-color, 10%);
      }
    }
  }
}

.buttons {
  display: flex;
  justify-content: space-evenly;
}
</style>

