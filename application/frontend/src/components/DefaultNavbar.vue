<template>
  <div class="vue-template">
    <!-- Navigation -->
    <nav class="navbar  my-navigation" style="position: fixed; width: 100%">
      <svg xmlns="http://www.w3.org/2000/svg" style="" width="35" height="35"
           fill="currentColor"
           class="bi-cloud" viewBox="0 0 16 16" id="IconChangeColor">
        <path
          d="M4.406 3.342A5.53 5.53 0 0 1 8 2c2.69
        0 4.923 2 5.166 4.579C14.758 6.804 16 8.137
        16 9.773 16 11.569 14.502 13 12.687 13H3.781C1.708
        13 0 11.366 0 9.318c0-1.763 1.266-3.223
        2.942-3.593.143-.863.698-1.723 1.464-2.383zm.653.757c-.757.653-1.153
        1.44-1.153 2.056v.448l-.445.049C2.064 6.805 1 7.952 1 9.318 1
        10.785 2.23 12 3.781 12h8.906C13.98 12 15 10.988 15
        9.773c0-1.216-1.02-2.228-2.313-2.228h-.5v-.5C12.188
        4.825 10.328 3 8 3a4.53 4.53 0 0 0-2.941 1.1z"
          id="mainIconPathAttribute" fill="#03989e"></path>
      </svg>
      <div class="projectName">
        CyberLocksmith
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
  color: #64113F;
  text-align: left;
  margin-right: 1355px;
}

.buttons {
  padding-right: 23px;
  display: flex;
}

.bi-cloud {
  background-image: url("../assets/fingerpint.png");
  background-size: 50% 50%, contain;
  background-position: center center;
  background-repeat: no-repeat;
}
</style>
<script setup>
</script>
