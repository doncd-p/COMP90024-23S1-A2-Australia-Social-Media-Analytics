<template>
  <div class="proCharts" ref="charts" style="height: 330px"></div>
</template>

<script>
import echarts from "echarts";

export default {
  name: "LineData",
  props: {
    lineData: {
      type: Array,
      require: true,
    },
  },
  data() {
    return {
      myChart: {},
      myChartStyle: { width: "100%", height: "330px" },
    };
  },

  mounted() {
    this.mycharts()
  },
  watch: {
     lineData: {
      handler(value) {
       this.mycharts();
      },
      deep: true,
    },
  },

  methods: {
    mycharts() {
      const dateList = this.lineData.map(function (item) {
          return item[0];
        });
      const valueList = this.lineData.map(function (item) {
          return item[1];
        });
      const options = {
           // Make gradient line here
        visualMap: [
          {
            show: false,
            type: 'continuous',
            seriesIndex: 0,
            min: -1,
            max: 1
          }
        ],
        title: [
          {
            left: 'center',
            text: "Daily Sentiment"
          }
        ],
        tooltip: {
          trigger: 'axis'
        },
        xAxis: [
          {
            data: dateList
          }
        ],
        yAxis: [
          {
            min:-1,
            max:1
          }
        ],
        grid: [
          {
          }
        ],
        series: [
          {
            type: 'line',
            showSymbol: true,
            data: valueList
          }
        ]
      };
      let myChart = echarts.init(this.$refs.charts);
      myChart.setOption(options);
      window.addEventListener("resize", function () {
        myChart.resize(); 
      });
    },
  
  },
};
</script>

<style lang="scss" scoped></style>
