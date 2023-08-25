<template>
  <div class="sign-up-div"></div>
  <div class="sign-up-template col-lg-12"
       style="width: 30%;-webkit-box-shadow: 6px 9px 47px -5px rgba(100,17,63,1);
            -moz-box-shadow: 6px 9px 47px -5px rgba(100,17,63,1);
            box-shadow: 6px 9px 47px -5px rgba(100,17,63,1);">
    <div class="title">
      <img src="../assets/cloudlogo.png" alt="cloud" width="200">
      <h2 class="CompTitle" style="color: #64113F;">CyberLocksmith</h2>
    </div>
    <div class="form-div">
      <form @submit.prevent="signUp">
        <h3 class="FormTitle">Sign Up</h3>
        <div class="mb-3">
          <span style="float: left;color: grey">Email Address</span>
          <input type="email" class="form-control form-control-lg"
                 data-required-message="Enter your Email *" v-model="email"
                 required/>
        </div>
        <div class="mb-3">
          <span style="float: left;color: grey">Password</span>
          <input type="password" pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,16}$"
                 title="Must contain at least one number and one uppercase and lowercase letter,
                 and 8-16 characters"
                 class="form-control form-control-lg" v-model="password"
                 required/>
        </div>
        <button type="submit"
                class="btn btn-secondary bg-burgundy btn-lg btn-block">
          Sign Up
        </button>
        <p class="forgot-password text-right">
          <br>
          Already registered
          <router-link :to="{ name: 'login' }">sign in?</router-link>
        </p>
      </form>
    </div>
  </div>
</template>
<script>

import axios from 'axios';
// eslint-disable-next-line import/no-extraneous-dependencies
import Swal from 'sweetalert2';

export default {
  name: 'sign-up',
  components: {},
  computed: {},
  data() {
    return {
      email: '',
      password: '',
      emailError: '',
      passwordError: '',
    };
  },
  methods: {
    validateEmail() {
      const emailPattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      if (!this.email) {
        this.emailError = 'Email field cannot be empty.';
      } else if (!emailPattern.test(this.email)) {
        this.emailError = 'Please enter a valid email address.';
      } else {
        this.emailError = '';
      }
    },
    validatePassword() {
      if (!this.password) {
        this.passwordError = 'Password field cannot be empty.';
        return false;
      }
      if (this.password.length < 6) {
        this.passwordError = 'Password must be at least 6 characters long.';
        return false;
      }
      this.passwordError = '';
      return true;
    },

    signUp() {
      const isValidEmail = this.validateEmail();
      const isValidPassword = this.validatePassword();

      if (!isValidEmail || !isValidPassword) {
        this.showFailAlert();
      }
      const formData = new FormData();
      formData.append('email', this.email);
      formData.append('password', this.password);
      axios.post('http://127.0.0.1:5000/sign_up', formData)
        .then((response) => {
          if (response.data.is_success) {
            this.showSuccessAlert();
            this.$router.push('/sign_in');
          } else {
            this.showFailAlert();
          }
        });
    },

    showSuccessAlert() {
      Swal.fire({
        icon: 'success',
        title: 'Signed up successfully',
        timer: 5000,
        timerProgressBar: true,
        showConfirmButton: false,
        toast: true,
        position: 'top-end',
        onOpen: (toast) => {
          toast.addEventListener('mouseenter', Swal.stopTimer);
          toast.addEventListener('mouseleave', Swal.resumeTimer);
        },
      });
    },
    showFailAlert() {
      Swal.fire({
        icon: 'error',
        title: 'error',
        timer: 5000,
        timerProgressBar: true,
        showConfirmButton: false,
        toast: true,
        position: 'top-end',
        onOpen: (toast) => {
          toast.addEventListener('mouseenter', Swal.stopTimer);
          toast.addEventListener('mouseleave', Swal.resumeTimer);
        },
      });
    },
  },
};
</script>


<style lang="scss" scoped>

.burgundy {
  color: #64113F;
}

.bg-burgundy {
  background-color: #64113F;
}

.sign-up-template {
  margin: 10% auto;
  padding: 25px;
  text-align: center;
  border-radius: 20px;
}

.title {
  padding: 40px;
  padding-bottom: 20px;
}

.bi-cloud {
  background-image: url("../assets/fingerpint.png");
  background-size: 50% 50%, contain;
  background-position: center center;
  background-repeat: no-repeat;
}

.CompTitle {
  margin-top: 1rem;
  color: #64113F;
  text-align: center;
  font-family: Lora;
  font-size: 35px;
  font-style: normal;
  font-weight: 600;
  line-height: normal;
  flex-shrink: 0;
}

.FormTitle {
  padding-bottom: 15px;
  text-decoration: underline;
  font-weight: 400;
}

.form-div {
  margin: 0 25px;
}
</style>
