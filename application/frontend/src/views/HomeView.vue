<template>
  <div>
    <div>
      <my-navbar/>
    </div>
    <div class="home" style=" display: block; margin-top: 130px">
      <img src="../assets/cloudlogo.png" alt="cloud" width="200">
      <HelloWorld msg="CyberLocksmith" slogan="Some keys open huge doors!"
                  style="text-align: -webkit-center"/>
      <SearchBar/>
    </div>
    <small class="footer">Copyright © 2023 &nbsp;<a class="link" href="https://socradar.io/"
                                                    target="_blank">
      SOCRadar® </a> &nbsp;All rights reserved.
    </small>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue';
import SearchBar from '@/components/SearchBar.vue';
import MyNavbar from '@/components/MyNavbar.vue';
import { mapGetters } from 'vuex';
import axios from 'axios';


export default {
  name: 'HomeView',
  components: {
    MyNavbar,
    SearchBar,
    HelloWorld,
  },
  computed: {
    ...mapGetters([]),
  },
  methods: {
    firstReq() {
      const formData = new FormData();
      formData.append('keyword', 'asdfg');
      axios.post('/home', formData).then((response) => {
        // eslint-disable-next-line no-console
        console.log(response);
      }).catch(() => {
        this.$router.push('/protected');
      });
    },
  },
  beforeMount() {
    this.firstReq();
  },
};
</script>

<style scoped lang="scss">
.home {
  text-align: center;
  display: inline-block;
  height: 100%;
}

.bi-cloud {
  background-image: url("../assets/fingerpint.png");
  background-size: 50% 50%, contain;
  background-position: center center;
  background-repeat: no-repeat;
}

.footer {
  margin-top: auto;
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
}

.link {
  text-decoration: none;
  font-weight: bolder;
  color: #64113F;
}
</style>
