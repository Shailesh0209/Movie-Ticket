<!-- <template>
    
  <div class="admin-dashboard">
  
    <h2>Admin Dashboard</h2>
    <div class="dashboard-content">
      <b-button variant="primary" @click="addVenue">+</b-button>
      <div v-if="venues.length > 0">
        <h3>Venues</h3>
        <ul>
          <li v-for="venue in venues" :key="venue.id">{{ venue.name }}</li>
        </ul>
      </div>
    </div>
    </AdminNavBarComponent>
  </div>
</template> -->

<!-- <script>
export default {
  name: 'AdminHomeComponent',
  data() {
    return {
      venues: [],
    };
  },
  methods: {
    addVenue() {
      // Logic for adding a venue goes here
      const venueName = prompt('Enter venue name:');
      if (venueName) {
        const newVenue = { id: Date.now(), name: venueName };
        this.venues.push(newVenue);
      }
    },
  },
};
</script> -->

<!-- <style scoped>
.admin-dashboard {
  padding: 20px;
}

.dashboard-content {
  margin-top: 20px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 5px;
}
</style> -->
