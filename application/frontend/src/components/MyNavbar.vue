<template>
  <div class="vue-template">
    <!-- Navigation -->
    <nav class="navbar  my-navigation" style="position: fixed; width: 100%">
      <router-link to="/home" style="text-decoration: none; color: #64113F">
        <div class="projectName">
          <img src="../assets/cloudlogo.png" alt="cloud" width="30">
          CyberLocksmith
        </div>
      </router-link>
      <div class="float-end" title="log out">
        <button class="btn btn-outline-dark" style="color: #64113F"
                @click.prevent="handleLogout">
          <font-awesome-icon icon="arrow-right-from-bracket"/>
        </button>
      </div>
    </nav>
  </div>
</template>

<style lang="scss">

.my-navigation {
  background-color: white;
  display: flex;
  border-bottom: 1px solid black;
  -webkit-box-shadow: 0px 5px 16px -3px rgba(0, 0, 0, 0.66);
  -moz-box-shadow: 0px 5px 16px -3px rgba(0, 0, 0, 0.66);
  box-shadow: 0px 5px 16px -3px rgba(0, 0, 0, 0.66);
}

.projectName {
  padding-left: 23px;

}

.float-end {
  padding-right: 23px;
  display: flex;
}


</style>
<script>
import axios from 'axios';

export default {
  components: {},
  methods: {
    handleLogout() {
      // eslint-disable-next-line no-console
      console.log('here');
      axios.post('http://127.0.0.1:5000/logout')
        .then((response) => {
          if (response.data.is_success) {
            this.$router.push('/logout');
          }
        });
    },
  },
};
</script>
