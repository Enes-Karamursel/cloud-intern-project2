<template>
  <div class="sign-up-template col-lg-12"
       style="width: 30%;-webkit-box-shadow: 6px 9px 47px -5px rgba(100,17,63,1);
            -moz-box-shadow: 6px 9px 47px -5px rgba(100,17,63,1);
            box-shadow: 6px 9px 47px -5px rgba(100,17,63,1);">
    <div class="title">
      <img src="../assets/cloudlogo.png" alt="cloud" width="200">
      <h2 class="CompTitle" style="color: #64113F;">CyberLocksmith</h2>
    </div>
    <div class="form-div">
      <form>
        <h3 class="FormTitle">You must logged in to access this page!</h3>
        <div class="mb-3">
          <button class="logout-Button">
            <router-link to="/sign_in"
                         class="btn btn-secondary bg-burgundy btn-lg btn-block"
                         role="button"
                         aria-pressed="true" @click="signIn">Please Sign In!
            </router-link>
          </button>
        </div>
      </form>
    </div>
  </div>
</template>


<script>
export default {
  data() {
    return {
      signIn: false,
    };
  },
};
</script>

<style>

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
