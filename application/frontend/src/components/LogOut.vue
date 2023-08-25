<script setup>

</script>

<template>
  <div class="sign-up-template col-lg-12"
       style="width: 30%;-webkit-box-shadow: 6px 9px 47px -5px rgba(100,17,63,1);
            -moz-box-shadow: 6px 9px 47px -5px rgba(100,17,63,1);
            box-shadow: 6px 9px 47px -5px rgba(100,17,63,1);">
    <div class="title">
      <img src="../assets/cloudlogo.png" alt="cloud" width="200">
      <h2 class="CompTitle" style="color: #64113F;">CyberLocksmith</h2>
    </div>
    <h1 class="FormTitle">Logged Out!</h1>
    <p> Thank you for using <b>CyberLocksmith!</b></p>
    <br>
    <button class="logout-Button">
      <router-link to="/sign_in" class="btn btn-primary btn-lg active bg-burgundy btn-lg btn-block"
                   role="button"
                   aria-pressed="true" >Sign In Again
      </router-link>
    </button>
  </div>
</template>

<style scoped lang="scss">
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

.FormTitle {
  padding-bottom: 15px;
  font-weight: bold;
}

.logout-Button {

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
</style>
