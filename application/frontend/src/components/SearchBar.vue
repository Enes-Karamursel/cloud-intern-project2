<template>
  <div class="searchbar_form">
    <input type="text" autocomplete="off" required v-model="searchKeyword" name="keyword"
           style="text-indent:17px;"
           placeholder="Write your domain or keyword" class="searchbar" @keyup.enter="fetchDomain">
    <button type="submit" value="Submit" class="search_btn" @click="fetchDomain">Search</button>
  </div>
</template>
<script>

import axios from 'axios';
import { mapGetters } from 'vuex';

export default {
  name: 'SearchBar',
  data() {
    return {
      searchKeyword: '',
      buton_count: 0,
      ofs: 0,
      lim: 15,
    };
  },
  computed: {
    ...mapGetters([
      'limit', 'offset', 'active_button_page_number', 'keyword', 'lastLineCount', 'firstLineCount',
    ]),
  },
  methods: {
    fetchDomain() {
      const formData = new FormData();
      formData.append('keyword', this.searchKeyword);
      this.$store.commit('active_button_page_number', '1');
      if (this.searchKeyword) {
        axios.post('http://localhost:5000/home', formData)
          .then((response) => {
            this.buton_count = Math.ceil(response.data.counter / this.limit);
            this.$store.commit('buttonCount', this.buton_count);
            this.$store.commit('offset', response.data.last_page_number);
            this.$store.commit('domainRows', response.data.domain_info);
            this.$store.commit('domainRowsCount', response.data.counter);
            this.$store.commit('keyword', this.searchKeyword);
            this.$store.commit('lastLineCount', response.data.last_page_number);
            this.$store.commit('firstLineCount', response.data.first_page_number);
            this.$router.push('/result');
          })
          .catch();
      }
    },
  },

};
</script>

<style scoped lang="scss">
.searchbar_form {
  position: relative;
  display: inline-block;
  width: fit-content;
}

.searchbar {
  background: url('../assets/searchicon.png') no-repeat scroll 15px 20px;
  background-size: 20px;
  padding-left: 25px;
  padding-right: 180px; /* Adjust this value as needed */
  border: 0;
  border-radius: 60px;
  color: black;
  width: 860px;
  height: 65px;
  border: 1px solid #64113F;
  transform: translateZ(0) scale(1);
  transition: transform .2s;
}

.searchbar:focus {
  border-color: #9C27B0;
}

.searchbar::placeholder {
  color: rgba(0, 0, 0, 0.61);
}

.search_btn {
  border: 0;
  border-top-right-radius: 33px;
  border-bottom-right-radius: 33px;
  color: white;
  padding: 15px 40px;
  background: #64113F;
  position: absolute;
  top: 0;
  right: 0;
  cursor: pointer;
  width: 143px;
  height: 65px;
}
.search_btn:not(:disabled):hover {
  transform: scale(1.05);
}
</style>
