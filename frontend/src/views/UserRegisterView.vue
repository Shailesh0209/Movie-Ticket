<template>
    <div>
        <div class="container">
            <h2>User Registration</h2>
            <form @submit.prevent="registerUser">
            <div>
                <label for="name">Name:</label>
                <input type="text" id="name" v-model="name" required>
            </div>
            <div>
                <label for="email">Email:</label>
                <input type="email" id="email" v-model="email" required>
            </div>
            <div>
                <label for="password">Password:</label>
                <input type="password" id="password" v-model="password" required>
            </div>
            <button type="submit">Register</button>
        </form>
        </div>
    </div>
</template>
  
<script>
import axios from 'axios';

export default {
    data() {
        return {
            name: '',
            email: '',
            password: ''
        };
    },
    methods: {
        async registerUser() {
            try {
                const response = await axios.post('http://127.0.0.1:5000/users', {
                    name: this.name,
                    email: this.email,
                    password: this.password
                });
                this.$router.push('/login');
                console.log(response.data);
            } catch (error) {
                console.error('Error during registration:', error);
                alert('An error occurred during registration.');
            }
        }
    }
};
</script>
  
<style lang="scss">
// Global Styles
$primary-color: #3498db;

.container {
  max-width: 400px;
  margin: 0 auto;
  padding: 2rem;
  background-color: white;
  border: 1px solid #ddd;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);

  h2 {
    font-size: 24px;
    margin-bottom: 1rem;
    color: $primary-color;
  }

  form {
    label {
      display: block;
      margin-bottom: 0.5rem;
      font-weight: bold;
    }

    input {
      width: 100%;
      padding: 0.5rem;
      border: 1px solid #ddd;
      border-radius: 4px;
      margin-bottom: 1rem;
    }

    button[type="submit"] {
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
}
</style>

  