<template>
  <div class="body-container">
    <app-main></app-main>
  </div>
</template>

<script>
import AppMain from "./AppMain.vue";

export default {
  name: "Layout",
  components: {
    AppMain,
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
  top: 0;
  width: 100%;
  z-index: 9999;
}
.body-container {
  // overflow: hidden;
  margin-top: 78px;
}
</style>
