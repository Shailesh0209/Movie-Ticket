<!-- <template>
  <div>
    <h1 class="title">Creating a new Venue</h1>

    <b-modal ref="venueModalRef" id="venueModal" size="xl" hide-footer>
      <template v-slot:modal-title>
        <h3 class="text-center">Add new venue details</h3>
      </template>
      <div class="d-block text-center">
        <b-form @submit="onSubmit" v-if="show">
          <b-form-group id="input-group-1" label="Venue Name:" label-for="input-1">
            <b-form-input
              id="input-1"
              v-model="form.venueName"
              type="text"
              placeholder="Enter Venue Name"
              required
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-2" label="Place:" label-for="input-2">
            <b-form-input
              id="input-2"
              v-model="form.place"
              type="text"
              placeholder="Enter Place"
              required
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-3" label="Location (State of India):" label-for="input-3">
            <b-form-input
              id="input-3"
              v-model="form.location"
              type="text"
              placeholder="Enter Location"
              required
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-4" label="Capacity:" label-for="input-4">
            <b-form-input
              id="input-4"
              v-model="form.capacity"
              type="number"
              placeholder="Enter Capacity"
              required
            ></b-form-input>
          </b-form-group>

          <b-button type="submit" variant="primary">Submit</b-button>
        </b-form>
      </div>
    </b-modal>

    <b-modal v-model="showModalDialog" title="Delete the Venue!!!" hide-footer>
      
        <h3>Are you sure you want to delete the venue?</h3>
        <b-button class="mt-3" variant="danger" @click="deleteVenue()">Yes</b-button>
        <b-button class="mt-3" variant="secondary" @click="closeModalDialog">No</b-button>
      
    </b-modal>

  </div>
</template>


<script>
import { mapGetters } from "vuex";

// import axios from 'axios';

export default {
  name: "AdminVenues",
  data() {
    return {
      showModalDialog: false,
      venueName: "",
      form: {
        venueName: '',
        place: '',
        location: '',
        capacity: null
      },
      show: true
    }
  },
  methods: {

    async onSubmit() {
      this.$store.dispatch("submitVenueDetails", {
        venue_name: this.form.venueName,
        place: this.form.place,
        location: this.form.location,
        capacity: this.form.capacity,
      }, {
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
        }
      })
        .then((response) => {
          console.log("Venue created successfully", response.data);
          this.$router.push({ name: "AdminHome" });
        })
        .catch(error => {
          console.error("Venue creation failed", error);
        });
    },

    showDeleteModal(venueName) {
      console.log("showDeleteModal", venueName);
      this.showModalDialog = true;
      this.venueName = venueName;
    },
    closeModalDialog() {
      this.showModalDialog = false;
    },
    deleteVenue() {
      console.log("deleting venue", this.venueName);
      this.$store.dispatch("deleteVenue", {
        venueName: this.venueName,
      });
      this.showModalDialog = false;
    }



  },

  computed: {
    ...mapGetters(["getVenueNamesList"]),
    venueData() {
      return this.getVenueNamesList;
    }
  },
}
</script>




<style scoped>
/* Add any custom styles for your component here */
</style>
 -->
