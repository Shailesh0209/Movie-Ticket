
// import HomeView from '../views/HomeView.vue'

import Vue from 'vue'
import VueRouter from 'vue-router'
import axios from 'axios'
import store from '../store'

// import AdminLoginView from '../views/AdminLoginView.vue'
// import AdminHomeComponent from '@/components/AdminHomeComponent.vue'
// import AdminActorComponent from '@/components/AdminActorComponent.vue'
// import AdminMovies from '@/views/AdminMovies.vue'
// import AdminVenues from '../views/AdminVenues.vue'


// Admin
import AdminHome from '../views/AdminHome.vue'



import UserLoginView from '../views/UserLoginView.vue'
import UserRegisterView from '../views/UserRegisterView.vue'
// import UserHomePage from '../views/UserHomePage.vue'
import UserProfilePage from '../views/UserProfilePage.vue'
import UserBookingPage from '../views/UserBookingPage.vue'

// import UserHomeComponent from '@/components/UserHomeComponent.vue'

import LandingPage from '../views/LandingPage.vue'

Vue.use(VueRouter)


const routes = [
  {
    path: '/adminHome',
    name: 'AdminHome',
    component: AdminHome,
    beforeEnter: (to, from, next) => {
      axios.get("http://127.0.0.1:5000/venues")
        .then(response => {
          store.commit('setVenueData', response.data)
          console.log("Ramayan", response.data.movies_names_list)
          next()
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  {
    path: '/',
    name: 'LandingPage',
    component: LandingPage
  },
  
  {
    path: '/login',
    name: 'UserLoginView',
    component: UserLoginView
  },

  {
    path: '/Signup',
    name: 'UserRegisterView',
    component: UserRegisterView,
  },
  

  {
    path: '/profile',
    name: 'UserProfilePage',
    component: UserProfilePage
  },

  {
    path: '/bookings',
    name: 'UserBookingPage',
    component: UserBookingPage
  },
  {
    path: '/adminHome/movies/:id',
    name: 'AdminMovies',
    component: () => import('../views/AdminMovies.vue'),
  },
  {
    path: '/venues/:id',
    name: 'VenuesPage',
    component: () => import('../views/VenuesPage.vue'), 
  },
  {
    path: '/register',
    name: 'UserRegisterView',
    component: UserRegisterView
  },

  {
    path: '/trigger-daily-reminder',
    name: 'TriggerDailyReminder',
    beforeEnter: (to, from, next) => {
      axios.get("http://127.0.0.1:5000/trigger-daily-reminder")  // Call your Flask route that triggers the daily_reminder Celery task
        .then(response => {
          console.log("Daily Reminder Task Response:", response.data);
          next();
        })
        .catch(error => {
          console.log(error);
          next();
        });
    }
  },
  {
    path: '/trigger-monthly-report',
    name: 'TriggerMonthlyReport',
    beforeEnter: (to, from, next) => {
      axios.get("http://127.0.0.1:5000/trigger-monthly-report")  // Call your Flask route that triggers the monthly_report Celery task
        .then(response => {
          console.log("Monthly Report Task Response:", response.data);
          next();
        })
        .catch(error => {
          console.log(error);
          next();
        });
    }
  }


]


const router = new VueRouter({
  routes
})

export default router








