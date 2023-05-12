<template>
  <div class="page-warpper">
    <side-bar class="sidebar-container"></side-bar>
    <div class="app-warpper">
      <router-view />
    </div>
  </div>
</template>

<script>
import SideBar from '../../layout/SideBar.vue'

export default {
    name: 'Dashboard',
    components: {
      SideBar
    }
}
</script>

<style>
.page-warpper {
    width: 100%;
}

.sidebar-container {
  position: fixed;
  width: 200px;
}

.app-warpper {
  width: calc(100vw - 200px);
  float: right;
}
</style>