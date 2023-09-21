<template>
    <div>
        <UserNavBarComponent />
        <div class="container">
            <h2>Admin Home</h2>
            <button @click="showAddVenueModal">Add Venue</button>

            <!-- Add Venue Form -->
            <div v-if="showAddVenueForm" class="add-venue-form">
                <h3>Add Venue</h3>
                <form @submit.prevent="addVenue">
                    <div>
                        <label for="venue-name">Venue Name:</label>
                        <input type="text" id="venue-name" v-model="newVenue.name" required>
                    </div>
                    <div>
                        <label for="venue-address">Venue Address:</label>
                        <input type="text" id="venue-address" v-model="newVenue.address" required>
                    </div>
                    <button type="submit">Add</button>
                    <button @click="cancelAddVenue">Cancel</button>
                </form>
            </div>

            <!-- Venue List -->
            <div class="venue-list">
                <div v-for="venue in venues" :key="venue.id" class="venue-card">
                    <div @click="viewVenueMovies(venue.id)" class="venue-info">
                        <h3>{{ venue.name }}</h3>
                        <p>{{ venue.address }}</p>
                    </div>
                    <button @click="showEditVenueModal(venue)">Edit</button>
                    <button @click="deleteVenue(venue.id)">Delete</button>
                    <button @click="addMovie(venue)">Add Movies</button>
                </div>
            </div>

            <div v-if="showModal" class="edit-venue-form">
                <h3>Edit Venue</h3>
                <form @submit.prevent="editVenue">
                    <div>
                        <label for="venue-name">Venue Name:</label>
                        <input type="text" id="venue-name" v-model="venue.name" required>
                    </div>
                    <div>
                        <label for="venue-address">Venue Address:</label>
                        <input type="text" id="venue-address" v-model="venue.address" required>
                    </div>
                    <button type="submit">Edit</button>
                    <button @click="cancelEditVenue">Cancel</button>
                </form>
            </div>

            <!-- add movie form -->
            <div v-if="showAddMovieForm" class="add-movie-form">
                <h3>Add Movie</h3>
                <form @submit.prevent="addMovieToVenue">
                    <div>
                        <label for="movie-title">Movie Title:</label>
                        <input type="text" id="movie-title" v-model="newMovie.title" required>
                    </div>
                    <div>
                        <label for="start-timing">Start Timing:</label>
                        <input type="time" id="start-timing" v-model="newMovie.start_timing" required>
                    </div>
                    <div>
                        <label for="end-timing">End Timing:</label>
                        <input type="time" id="end-timing" v-model="newMovie.end_timing" required>
                    </div>
                    <div>
                        <label for="ticket-price">Ticket Price:</label>
                        <input type="text" id="ticket-price" v-model="newMovie.ticket_price" required>
                    </div>
                    <button type="submit">Add Movie</button>
                    <button @click="cancelAddMovie">Cancel</button>
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
            venues: [], // Populate this array with venue data from API
            showModal: false,
            showAddVenueForm: false,
            showAddMovieForm: false,
            newVenue: {
                name: '',
                address: ''
            },
            newMovie: {
                title: '',
                start_timing: '',
                end_timing: '',
                ticket_price: 0
            },
            venue: {
                id: null,
                name: '',
                address: ''
            }
        };
    },
    async created() {
        const response = await axios.get('http://localhost:5000/venues');
        this.venues = response.data;
    },
    methods: {
        showAddVenueModal() {
            this.showAddVenueForm = true;
        },
        cancelAddVenue() {
            this.showAddVenueForm = false;
            this.newVenue.name = '';
            this.newVenue.address = '';
        },
        cancelEditVenue() {
            this.showModal = false;
            this.venue.name = '';
            this.venue.address = '';
        },
        async addVenue() {
            const response = await axios.post('http://localhost:5000/venues', {
                name: this.newVenue.name,
                address: this.newVenue.address
            });
            this.venues.push(response.data);
            this.cancelAddVenue();
        },
        async editVenue() {
            const response = await axios.put(`http://localhost:5000/venues/${this.venue.id}`, {
                name: this.venue.name,
                address: this.venue.address
            });
            this.venues = this.venues.map(venue => {
                if (venue.id === response.data.id) {
                    return response.data;
                }
                return venue;
            });
            this.cancelEditVenue();
        },
        showEditVenueModal(venue) {
            this.showModal = true;
            this.venue = venue;

            // Implement logic to show the edit modal
        },
        async deleteVenue(venueId) {
            await axios.delete(`http://localhost:5000/venues/${venueId}`);
            this.venues = this.venues.filter(venue => venue.id !== venueId);
            console.log(venueId);
            // Implement logic to delete the venue
        },
        addMovie(venue) {
            this.showAddMovieForm = true;
            this.venue = venue;
        },
        cancelAddMovie() {
            this.showAddMovieForm = false;
            this.newMovie.title = '';
            this.newMovie.start_timing = '';
            this.newMovie.end_timing = '';
            this.newMovie.ticket_price = 0;
            this.newMovie.venue_id = 0;
        },
        async addMovieToVenue() {
            console.log(this.newMovie);
            const movie_response = await axios.post(`http://localhost:5000/movies?venue_id=${this.venue.id}`, {
                title: this.newMovie.title,
                start_timing: this.newMovie.start_timing,
                end_timing: this.newMovie.end_timing,
                ticket_price: this.newMovie.ticket_price,
            });
            console.log(movie_response.data);
            this.cancelAddMovie();
        },
        viewVenueMovies(id) {
            this.$router.push(`/adminHome/movies/${id}`);
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

  button {
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

  .add-venue-form, .edit-venue-form, .add-movie-form {
    border: 1px solid #ddd;
    padding: 1rem;
    margin: 1rem 0;
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

    input, select {
      width: 100%;
      padding: 0.5rem;
      border: 1px solid #ddd;
      border-radius: 4px;
      margin-bottom: 1rem;
    }

    button[type="submit"] {
      background-color: $primary-color;
      color: white;
    }

    button[type="submit"], button[type="button"] {
      margin-right: 1rem;
      padding: 0.5rem 1rem;
      border: none;
      cursor: pointer;
    }
  }

  .venue-list {
    display: flex;
    flex-wrap: wrap;
    margin-top: 2rem;

    .venue-card {
      background-color: #f7f7f7;
      border: 1px solid #ddd;
      padding: 1rem;
      margin: 1rem;
      border-radius: 5px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
      transition: transform 0.2s ease;

      &:hover {
        transform: translateY(-5px);
      }

      .venue-info {
        cursor: pointer;
      }

      button {
        margin: 0.5rem 0.25rem;
      }
    }
  }
}
</style>

  