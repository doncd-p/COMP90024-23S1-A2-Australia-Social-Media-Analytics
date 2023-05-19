<template>
  <div class="pie-container">
    <div ref="charts" id="mychart" :style="myChartStyle"></div>
  </div>
</template>

<script>
import echarts from "echarts";

export default {
  name: "PieData",
  props: {
    pieData: {
      type: Object,
      require: true,
    },
  },
  data() {
    return {
      myChart: {},
      pieName: [],
      myChartStyle: { width: "100%", height: "330px" }, 
    };
  },

  mounted() {
    this.initData();
    this.initEcharts();
  },
  watch: {
    pieData: {
      handler(value) {
       this.initData();
       this.initEcharts()
      },
      deep: true,
    },

  },
  methods: {
    initData() {
      this.pieName = ["Negative Tweets", "Netural Tweets", "Positive Tweets"]
    },
    initEcharts() {
      // 饼图
      const option = {
        color: [
          "rgb(102, 177, 255)",
          "#fac858",
          "#ee6666",
          // "#91cc75",
        ],
        legend: {
          data: this.pieName,
          bottom: "bottom",
        },
        title: {
          text: "Sentiment Analysis",
          top: "0%",
          left: "left",
        },
        tooltip: {
          trigger: "item",
        },
        series: [
          {
            type: "pie",
            label: {
              show: true,
              formatter(param) {
                // correct the percentage
                return param.name + ' (' + param.percent + '%)';
              }
            },
            radius: "60%", 
            data: [
              {
                name: "Negative Tweets",
                value: this.pieData.num_neg_tweets
              },
              {
                name: "Netural Tweets",
                value: this.pieData.num_neu_tweets
              },
              {
                name: "Positive Tweets",
                value: this.pieData.num_pos_tweets
              }
            ],

          },
        ],
      };
      this.myChart = echarts.init(this.$refs.charts);
      this.myChart.setOption(option);
      window.addEventListener("resize", () => {
        this.myChart.resize();
      });
    },
  },
};
</script>
<style lang="scss" scoped>
.pie-container {
  width: 100%;
  height: 100%;
}
</style>