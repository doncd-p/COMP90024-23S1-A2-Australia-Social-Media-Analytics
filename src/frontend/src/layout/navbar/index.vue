<template>
  <div class="navbar-container">
    <div class="navbar-header">
      <button
        type="button"
        class="navbar-toggle"
        data-toggle="collapse"
        data-target="#bs-example-navbar-collapse-1"
      >
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <h1><a to="#">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ELEFEEL&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a></h1>
    </div>
    <el-menu
      :default-active="activeMenu"
      class="header-container"
      mode="horizontal"
      background-color="#333"
      text-color="#fff"
      active-text-color="#ffd04b"
      router
    >
      <el-menu-item index="/home">Home</el-menu-item>
      <el-menu-item index="/dashboard">Dashboard</el-menu-item>
      <el-menu-item index="/map">Map</el-menu-item>
      <el-menu-item index="/about">About Us</el-menu-item>
 
    </el-menu>
  </div>
</template>

<script>
export default {
  name: "NavBar",

  data() {
    return {
      activeIndex: "1",
      activeIndex2: "1",
    };
  },

  computed: {
    activeMenu() {
      const route = this.$route
      const { path } = route
      if (path === '/dashboard/distribution' || path === '/dashboard/ranking') {
        return '/dashboard'
      }
      return path
    }
  },

  mounted() {},

  methods: {
  },
};
</script>

<style lang="scss" scoped>
.header-container {
  display: flex;
  height: 78px;
  border-bottom: none !important;
  align-items: center;
  a {
    text-decoration: none;
  }
}
.navbar-container {
  height: 78px;
  width: 100%;
  background: #333;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
</style>
