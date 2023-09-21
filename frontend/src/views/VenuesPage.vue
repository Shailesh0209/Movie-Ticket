<template>
    <div>
        <UserNavBarComponent />
        <div class="container">
            <h2>{{ venue.name }}</h2>
            <div class="movie-list">
                <div v-for="movie in movies" :key="movie.id" class="movie-card">
                    <div class="movie-info">
                        <h3>{{ movie.title }}</h3>
                        <p>Start Time: {{ movie.start_timing }}</p>
                        <p>End Time: {{ movie.end_timing }}</p>
                        <p>Ticket Price: {{ movie.ticket_price }}</p>
                        <form @submit.prevent="bookShow(movie.id)" class="input-button-container">
                            <input type="number" v-model="bookingInput" min="1" placeholder="No of seats ">
                            <button>Submit</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'VenuesPage',
    components: {
        UserNavBarComponent: () => import('../components/UserNavBarComponent.vue')
    },
    data() {
        return {
            venue: {},
            movies: [],
            bookingInput: 0,
            isLoggedIn: false,
        };
    },
    created() {
        this.isLoggedIn = localStorage.getItem('access_token')==null?false:true;
    },
    mounted() {
        this.fetchVenues();
    },
    methods: {
        bookShow(movieId) {
            // Perform the action you want when the "Book Show" button is clicked
            // You can use this.$router.push() to navigate to a new route, or show a modal, etc.
            // For example, navigating to a booking page:
            if(!this.isLoggedIn){
                this.$router.push('/login');
                return;
            }
            const user = JSON.parse(localStorage.getItem('user'));
            const response = axios.post(`http://localhost:5000/bookings?user_id=${user.id}&movie_id=${movieId}`, {
                seats: this.bookingInput
            });
            console.log(response);
            alert("Booking Successful");
            this.$router.push('/');
        },
        async fetchVenues() {
            const venueResponse = await axios.get(`http://localhost:5000/venues/${this.$route.params.id}`);
            console.log(venueResponse.data);
            this.venue = venueResponse.data;
            this.movies = venueResponse.data.movies;

        },
        viewVenueMovies(venueId) {
            this.$router.push(`/venues/${venueId}`);
        }
    },
}
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
        gap: 1.5rem;
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
            }

            &:hover {
                transform: translateY(-5px);
            }
        }
    }
}
</style>
