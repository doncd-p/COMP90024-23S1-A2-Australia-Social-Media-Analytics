<template>
  <div class="banner">
    <section class="slider">
      <div style="height: calc(100vh - 78px)">
        <ul class="rslides" id="slider">
          <li>
            <div class="w3layouts-banner-top w3layouts-banner-top1">
              <div class="banner-dott" style="height: calc(100vh - 78px)"></div>
            </div>
          </li>
        </ul>
        <div class="callbacks_container" style="padding-top: 78px;">
          <div class="slider-info">
            <div>
              <div class="border-top h2" id="info1" v-html="typingtext1"></div>
              <div class="border-top h4" id="info2" v-html="typingtext2"></div>
              <div>
                <router-link to="/dashboard/ranking">
                  <div class="downbutton"></div>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: "Home",

  data() {
    return {
      typingtext1: "<h1>Everyone has the right to fight for it</h1>",
      typingtext2: "WELCOME TO ELECTION ANALYSIS",
    };
  },

  mounted() {
  },

  methods: {
  },
};
</script>

<style lang="scss" scoped>
.banner {
  height: calc(100vh - 78px);
  background: url('../../assets/images/bg7.jpg')  center center / cover no-repeat;
}
</style>
