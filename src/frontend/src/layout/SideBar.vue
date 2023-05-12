<template>
  <el-menu 
    default-active="/dashboard/ranking"
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
    
  </el-menu>
</template>

<script>
export default {
    name: 'SideBar'
}
</script>

<style>

</style>