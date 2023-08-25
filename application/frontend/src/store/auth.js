export default {
  state: {
    isLogin: false,
  },
  getters: {
    isLogin: (state) => state.isLogin,
  },
  mutations: {
    isAuthenticated(state, value) {
      state.isAuthenticated = value;
    },
    isLogin(state, payload) {
      state.isLogin = payload;
    },
  },
  actions: {
    login({ commit }) {
      // Simulate successful login
      commit('setIsAuthenticated', true);
      // this.$router.push('/home');
    },
    /*    logout({ commit }) {
      // Simulate logout
      commit('IsAuthenticated', false);
    },
    checkAuth() { */

  },
  // },

};
