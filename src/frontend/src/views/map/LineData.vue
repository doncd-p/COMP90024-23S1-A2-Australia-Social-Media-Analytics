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
    console.log(this.lineData)
  },

  methods: {
    mycharts() {
      const options = {
           // Make gradient line here
        visualMap: [
          {
            show: false,
            type: 'continuous',
            seriesIndex: 0,
            min: -0.4,
            max: 0.4
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
            min:-0.4,
            max:0.4
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
      myChart.setOption(option);
      window.addEventListener("resize", function () {
        myChart.resize(); 
      });
    },
  
  },
};
</script>

<style lang="scss" scoped></style>
