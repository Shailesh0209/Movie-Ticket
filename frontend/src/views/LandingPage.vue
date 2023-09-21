<template>
  <div>
    <UserNavBarComponent />
    <div class="container">
      <div class="venue-container">
        <div v-for="venue in venues" :key="venue.id" class="venue-card">
          <div @click="viewVenueMovies(venue.id)" class="venue-info">
            <h3>{{ venue.name }}</h3>
            <p>{{ venue.address }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "LandingPage",
  components: {
    UserNavBarComponent: () => import('../components/UserNavBarComponent.vue')
  },
  data() {
    return {
      venues: [],
    };
  },
  mounted() {
    this.fetchVenues();
  },
  methods: {
    async fetchVenues() {
      const response = await axios.get('http://localhost:5000/venues');
      this.venues = response.data;
    },
    viewVenueMovies(venueId) {
      this.$router.push(`/venues/${venueId}`);
    }
  },
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

  .venue-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;

    .venue-card {
      background-color: #f7f7f7;
      border: 1px solid #ddd;
      padding: 1rem;
      border-radius: 5px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
      transition: transform 0.2s ease;

      .venue-info {
        cursor: pointer;

        h3 {
          font-size: 20px;
          margin-bottom: 0.5rem;
        }

        p {
          margin-bottom: 0.25rem;
        }
      }

      &:hover {
        transform: translateY(-5px);
      }
    }
  }
}
</style>
