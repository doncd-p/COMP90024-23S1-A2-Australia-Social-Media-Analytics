<template>
  <div class="body-container">
    <app-main></app-main>
  </div>
</template>

<script>
import AppMain from "./AppMain.vue";
import SideBar from "./SideBar"

export default {
  name: "Layout",
  components: {
    AppMain,
    SideBar
  },
  data() {
    return {};
  },

  mounted() {},

  methods: {},
};
</script>

<style lang="scss" scoped>
.body-container {
  width: 100%;
  // overflow: hidden;
  padding-top: 78px;
  height: calc;
}
</style>
