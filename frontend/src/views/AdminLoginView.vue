<!-- <template>
  <div class="admin-login-view">
    <h1>Admin Login</h1>
    <form @submit.prevent="login">
      <div class="form-group">
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="username" required>
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" required>
      </div>
      <div class="form-group">
        <label for="email">email</label>
        <input type="email" id="email" v-model="email" required>
      </div>
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'AdminLoginView',
  data() {
    return {
      username: '',
      password: '',
      email: ''
    };
  },
  methods: {
    
    login() {
      axios.post('http://localhost:8000/login?include_auth_token', {
      username: this.username,
      password: this.password,
      email: this.email
    })
      .then(response => {
       response.json();
      })
      .then((data) => {
              const token=data.response.user.authentication_token;
              localStorage.setItem("token", token);
              this.$router.push({ name: 'AdminDashboard' });
              })
      .catch(error => {
        console.log(error);
      });
      // Perform login logic here, e.g. send a request to the server
      // with the username and password
      // Example:
      // if (this.username === 'admin' && this.password === 'password') {
      //   // Successful login
      //   console.log('Login successful');
      //   // Redirect to the admin dashboard or perform other actions
      // } else {
      //   // Failed login
      //   console.log('Invalid credentials');
      //   // Show error message or perform other actions
      // }
    }
  }
};
</script>

<style scoped>
.admin-login-view {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
}
.form-group {
  margin-bottom: 20px;
}
label {
  display: block;
  font-weight: bold;
}
input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 8px;
}
button {
  padding: 8px 16px;
  background-color: #007bff;
  color: #fff;
  border: none;
  cursor: pointer;
}
</style> -->
