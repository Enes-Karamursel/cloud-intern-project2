<template>
  <div class="sign-up-template bg-white col-lg-12"
       style="width: 30%;-webkit-box-shadow: 6px 9px 47px -5px rgba(100,17,63,1);
            -moz-box-shadow: 6px 9px 47px -5px rgba(100,17,63,1);
            box-shadow: 6px 9px 47px -5px rgba(100,17,63,1);">
    <div class="title">
      <img src="../assets/cloudlogo.png" alt="cloud" width="200">
      <h2 class="CompTitle" style="color: #64113F;">CyberLocksmith</h2>
    </div>
    <div class="form-div">
      <form @submit.prevent="signIn">
        <h3 class="FormTitle">Sign In</h3>
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
                 and  8-16 characters"
                 class="form-control form-control-lg" v-model="password"
                 required/>
        </div>
        <button type="submit"
                class="btn btn-secondary bg-burgundy btn-lg b tn-block">
          Sign In
        </button>
        <p class=" forgot-password text-right mt-2 mb-4
        ">
          <router-link to="/ForgotPassword">Forgot password?</router-link>
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
  components: {},
  computed: {},
  data() {
    return {
      email: '',
      password: '',
    };
  },
  methods: {
    signIn() {
      const formData = new FormData();
      formData.append('email', this.email);
      formData.append('password', this.password);
      return new Promise(() => {
        axios.post('/sign_in', formData)
          .then((response) => {
            if (response.data.is_success) {
              this.showSuccessAlert();
              // this.$store.commit('isLogin', true);
              this.$router.push('/home');
              // resolve(response);
            } else {
              this.showFailAlert();
            }
          })
          .catch((error) => {
            this.showFailAlert(error.message);
          })
          .finally(() => {
          });
      });
    },

    showSuccessAlert() {
      Swal.fire({
        icon: 'success',
        title: 'Signed in successfully',
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
    showFailAlert(title = 'error') {
      Swal.fire({
        icon: 'error',
        title,
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
  padding: 40px 40px 20px;
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
