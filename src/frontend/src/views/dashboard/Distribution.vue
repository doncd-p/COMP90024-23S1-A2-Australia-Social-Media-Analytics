<template>
    <div id="app">  
      <el-col :span="24" class="chart">
        <el-row class="scatter1">
          <!-- figure1 -->
          <el-col class="figure" :span="20">
            <div class="c" ref="linechart" ></div>
          </el-col>
          <el-col class="filter" :span="4">
            <div class="filter1"> 
                  <div class="filter1label"> Interval:</div>
                  <el-select v-model="interval" :change="handleClick()" >
                  <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                  </el-option>
                </el-select>
                </div>
          </el-col>
        </el-row>
        <el-row class="scatter2">
          <el-col class="figure" :span="20">
            <div class="c scatter" ref="scatterchart" ></div>
          </el-col>
          <el-col class="filter" :span="4">
            <el-row>
              <div class="filter1"> 
                  <div class="filter1label"> Time After Election:</div>
                  <el-select v-model="after" :change="handleClick()" >
                  <el-option
                    v-for="item in options2"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                  </el-option>
                </el-select>
                </div>
            </el-row>
            <el-row>
              <div class="description">
                  <div style="font-size:20px;font-weight:600;margin-top:10px;margin-left:10px;color:#cb7f67;">About Figure:</div> <br/>
                  <div style="margin:10px;margin-top:0px;color:#fff;">{{description}}</div>
              </div>
            </el-row>
          </el-col>
        </el-row>
      </el-col>
       
    </div>
   
    
</template>
<script>
import echarts from 'echarts';
import { getNoParam, getParam, postParam } from '../../api/test'

export default {
  name: "distribution",
  data() {
      return {
       //chart1 data
        chartData: [["2000-06-05", -34], ["2000-06-06", -65], ["2000-06-07", -76], ["2000-06-08", 0], ["2000-06-09", -56], ["2000-06-10", 45], ["2000-06-11", 34], ["2000-06-12", 56], ["2000-06-13", 56], ["2000-06-14", 34], ["2000-06-15", 79], ["2000-06-16", 80]],
        options: [{
          value: 'day',
          label: 'Day'
        }, {
          value: 'week',
          label: 'Week'
        }, {
          value: 'month',
          label: 'Month'
        }],
        interval: 'day',

        //chart2 data
        chartData2 : [[0, 5], [0, -10], [0, -89], [0, 45], [0, 23], [1, 34], [1,46], [1,35], [1,-30]],
        options2: [{
          value: '1w',
          label: '1 Week'
        }, {
          value: '2w',
          label: '2 Weeks'
        }, {
          value: '1m',
          label: '1 Month'
        },{
          value: '2m',
          label: '2 Months'
        },{
          value: '3m',
          label: '3 Months'
        }
        ],
        after: '1w',
        description: 'This is about xxx'
      }
    },

  mounted() {
    this.loadEcharts()
  },
  watch: {
    chartData: function(value) {
      this.loadEcharts()
    }
  },

  methods: {

    loadEcharts() {
      // chart1:
      const dateList = this.chartData.map(function (item) {
          return item[0];
        });
      const valueList = this.chartData.map(function (item) {
          return item[1];
        });
      const options = {
           // Make gradient line here
        visualMap: [
          {
            show: false,
            type: 'continuous',
            seriesIndex: 0,
            min: -100,
            max: 100
          }
        ],
        title: [
          {
            left: 'center',
            text: "The Sentiment of Whole Australia Before and After the Election"
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
            min:-100,
            max:100
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

      let linechart = echarts.init(this.$refs.linechart)
      linechart.setOption(options)
      
      // chart2:
      const status = ['non-changed', 'changed'];
      const title = [];
      const singleAxis = [];
      const series = [];
      status.forEach(function (sta, idx) {
        title.push({
          textBaseline: 'middle',
          top: ((idx + 0.5) * 100) / 2 + '%',
          text: sta
        });
        singleAxis.push({
          left: 150,
          type: 'value',
          min:-100,
          max:100,
          boundaryGap: false,
          top: (idx * 100) / 2 + 5 + '%',
          height: 100 / 2 - 13 + '%',
        });
        series.push({
          singleAxisIndex: idx,
          coordinateSystem: 'singleAxis',
          type: 'scatter',
          data: [],
          markLine: {}
          });
      });
      this.chartData2.forEach(function (dataItem) {
        series[dataItem[0]].data.push([dataItem[1]]);
      });
      console.log(series)
      series.markLine = {
        lineStyle: {
          type: 'solid'
        },
        data: [{ type: 'average', name: 'avg' }]
      };
      
      const options2= {
        emphasis: {
        focus: 'series'
        },
        tooltip: {
          position: 'top'
        },
        title: title,
        singleAxis: singleAxis,
        series: series
      };
      let scatterchart = echarts.init(this.$refs.scatterchart)
      scatterchart.setOption(options2)
    },

    handleClick() {
      this.updateChart();

    },
    
   
    updateChart() {
      if (this.interval === 'day') {
        this.chartData = [["2000-06-05", -34], ["2000-06-06", -65], ["2000-06-07", -76], ["2000-06-08", 0], ["2000-06-09", -56], ["2000-06-10", 45], ["2000-06-11", 34], ["2000-06-12", 56], ["2000-06-13", 56], ["2000-06-14", 34], ["2000-06-15", 79], ["2000-06-16", 80]];
      } else if (this.interval === 'week') {
        this.chartData = [["2000-06-05", -34], ["2000-06-06", -65], ["2000-06-07", -76], ["2000-06-08", 0], ["2000-06-09", -56]];
      } else { 
        this.chartData = [["2000-06-05", -34], ["2000-06-06", -65], ["2000-06-07", -76]];
      }

      if (this.after === '1w'){
        this.chartData2 = [[0, 5], [0, -10], [0, -89], [0, 45], [0, 23], [1, 34], [1,46], [1,35], [1,-30]]
      } else if(this.after === '2w'){
        this.chartData2 = [[0, 5], [0, -90], [0, -34], [0, 54], [0, 3], [1, 4], [1,86], [1,45], [1,-76]]
      } else if (this.after === '1m'){
        this.chartData2 = [[0, 5], [0, -8], [0, -12], [0, 64], [0, 87], [1, 45], [1,6], [1,53], [1,-79]]
      } else if(this.after === '2m'){
        this.chartData2 = [[0, 5], [0, 54], [0, 3], [1, 4], [1,86], [1,-76]]
      } else{
        this.chartData2 = [[0, 5], [0, -90], [0, -34],  [1, 4], [1,86]]
      }
    },
  },
};
</script>
<style>
  .el-menu-vertical-demo{
    height:100vh;
  }
  .scatter1{
    height: 30em;
    display:flex;
    background-color: #5f4848;
    justify-content:center;
    align-items: center;
    border-bottom:0.1em solid #fff;
  }
  .scatter2{
    height: 30em;
    background-color: #444a5b;
    display:flex;
    justify-content:center;
    align-items: center;
  }
  .figure{
    height: 80%;
    width:65%;
    border: 0.5em solid #cb7f67;
    background-color: #fff;
  }
  .c{
    margin: 10px;
    height:100%;
    width:100%;
  }
  .filter1{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  .filter1label{
    color:#cb7f67;
    font-weight: 600;
    font-size: 20px;
    margin-bottom: 10px;
  }
  .scatter{
    height:95%;
    width:98%;
  }
  .description{
    height:220px;
    width:91%;
    margin-left: 5%;
    margin-top:2%;
    background-color:#5f4848;
    border:0.5em solid#cb7f67;
  }
</style>

