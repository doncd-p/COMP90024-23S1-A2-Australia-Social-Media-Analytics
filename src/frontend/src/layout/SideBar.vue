<template>
  <el-menu 
    :default-active="activeMenu"
    class="el-menu-vertical-demo"
    background-color="#333"
    text-color="#fff"
    router
    active-text-color="#ffd04b">
    <el-menu-item index="/dashboard/ranking">
      <span slot="title">Ranking</span>
    </el-menu-item>
    <el-menu-item index="/dashboard/distribution">
      <span slot="title">Distribution</span>
    </el-menu-item>
    <el-menu-item index="/dashboard/comparison">
      <span slot="title">Comparison</span>
    </el-menu-item>
    
  </el-menu>
</template>

<script>
export default {
    name: 'SideBar',
    computed:{
      activeMenu(){
        const {path} = this.$route;
        return path;
      }
    }
      
    
}
</script>

<style>

</style>