<template>
  <div id="app">
    <nav-bar class="header-container"></nav-bar>
    <router-view/>
  </div>
</template>

<script>
import NavBar from "./layout/navbar/index.vue";

export default {
  name: "App",
  components: {
    NavBar
  },
  data() {
    return {};
  },

  mounted() {},

  methods: {},
};
</script>

<style lang="scss" scoped>
.header-container {
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 9999;
}

</style>