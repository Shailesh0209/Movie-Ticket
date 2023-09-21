<template>
  
  <div class="login-page">
    <h1>Login</h1>
    
    <form @submit.prevent="loginUser">
      
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required>
      </div>
      
      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" required>
      </div>
      
      <div class="form-actions">
        <button type="submit" class="btn btn-primary" >Login</button>
      </div>
    </form>
  
  </div>

</template>


<script>
import axios from 'axios';
import jwtDecode from 'jwt-decode';

export default {
  name: "UserLoginView",

  data() {
    return {
      email: '',
      password: ''
    };
  },

  methods: {
    async loginUser() {
      try{
      const response = await axios.post('http://127.0.0.1:5000/login', {
        email: this.email,
        password: this.password
      });
      const token = response.data.access_token;
      localStorage.setItem('access_token', token);
      const decodeToken = jwtDecode(token);
      const user_response = await axios.get(`http://localhost:5000/users/${decodeToken.sub}`, {
        headers: {
          Authorization: `Bearer ${token}`
        }
      });
      // console.log(user_response.data);
      localStorage.setItem('user', JSON.stringify(user_response.data));
      if (user_response.data.role === 'admin') {
        this.$router.push('/adminHome');
      } else {
        this.$router.push('/');
      } 
      } catch (error) {
        console.error('Error during login:', error);
        alert('invalid credentials');
      }
    },

    goToRegister() {
      // Redirect to the user registration page or perform other actions
      // Example:
      this.$router.push({ name: 'UserRegisterView' });
    }
  }
};
</script>

<style scoped>
.login-page {
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
input[type="email"],
input[type="password"] {
  width: 100%;
  padding: 8px;
}
.form-actions {
  display: flex;
  justify-content: space-between;
}
</style>
