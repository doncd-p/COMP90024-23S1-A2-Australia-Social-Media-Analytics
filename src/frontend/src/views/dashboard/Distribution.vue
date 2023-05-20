<template>
    <div id="app" v-loading="loading" style="height: 80em"
      element-loading-text="loading..."
      element-loading-spinner="el-icon-loading"
      element-loading-background="rgba(0, 0, 0, 0.8)">  
      <el-col :span="24" class="chart">
        <el-row class="scatter1">
          <!-- figure1 -->
          <el-col class="figure" :span="20">
            <div class="c"  ref="linechart" ></div>
          </el-col>
          <el-col class="filter" :span="4">
            
            <el-row>
              <div class="filter1"> 
                  <div class="filter1label"> Interval:</div>
                  <el-select v-model="interval"  >
                  <el-option
                    v-for="item in options"
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
                  <div style="margin:10px;margin-top:0px;color:#fff;">{{description1}}</div>
              </div>
            </el-row>
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
                  <el-select v-model="after">
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
                  <div style="margin:10px;margin-top:0px;color:#fff;">{{description2}}</div>
              </div>
            </el-row>
          </el-col>
        </el-row>
      </el-col>
       
    </div>
   
    
</template>
<script>
import echarts from 'echarts';

export default {
  name: "distribution",
  data() {
      return {
        loading:true,
       //chart1 data
        dailyChartData:null,
        weekChartData:null,
        monthChartData:null,
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
        options2: [{
          value: '1w',
          label: '1 Week'
        }, {
          value: '2w',
          label: '2 Weeks'
        }, {
          value: '1,',
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
        description1: 'This graph denotes the change in aggregated overall sentiment for whole Australia for the period of analysis; with option of selecting daily interval, weekly interval, or monthly interval for measuring sentiment.',
        description2: 'This graph denotes the sentiment distribution for electorates that changed governing parties in the recent election and those that doesn’t; for aggregations of sentiments are based on 1 week, 2 weeks, 1 months, 2 months and 3 months after the election.'
      }
    },
  created(){
    this.initEcharts();
    this.getChart2Data();
    setTimeout(() => {
      this.storeData1();
   }, 0);
  },
  mounted() {
  },
  watch: {
    interval: {
      handler(value) {
       
        this.loadEcharts1()
      },
      deep: true,
    },
     after: {
      handler(value) {
       
        this.loadEcharts2()
      },
      deep: true,
    },

  },

  methods: {
   
    async initEcharts() {
      let chartData;
      if(this.interval=="day"&&this.dailyChartData){
        chartData = this.dailyChartData;
      }else if (this.interval == "week" &&this.weekChartData){
        chartData = this.weekChartData;
      }else if (this.interval=="month"&&this.monthChartData){
        chartData = this.monthChartData;
      }else{
        chartData = await this.getData();
      }
      
      // chart1:
      this.dateList = chartData.map(function (item) {
          return item[0];
        });
      this.valueList = chartData.map(function (item) {
          return Math.round(item[1] * 1000) / 1000;
        });
      const options = {
           // Make gradient line here
        visualMap: [
          {
            show: false,
            type: 'continuous',
            seriesIndex: 0,
            min: -0.2,
            max: 0.2
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
            data: this.dateList
          }
        ],
        yAxis: [
          {
            min:-0.2,
            max:0.2
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
            data: this.valueList
          }
        ]
      };

      let linechart = echarts.init(this.$refs.linechart)
      linechart.setOption(options)
      
      let chartData2 =  await this.getChart2Data();
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
          min:-1,
          max:1,
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
      chartData2.forEach(function (dataItem) {
        series[dataItem[0]].data.push([dataItem[1]]);
      });
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
      this.loading = false;
      
    },
    async loadEcharts1() {
      this.loading = true;
      let chartData;
      if(this.interval=="day"&&this.dailyChartData){
        chartData = this.dailyChartData;
      }else if (this.interval == "week" &&this.weekChartData){
        chartData = this.weekChartData;
      }else if (this.interval=="month"&&this.monthChartData){
        chartData = this.monthChartData;
      }else{
        chartData = await this.getData();
      }
      
      // chart1:
      const dateList = chartData.map(function (item) {
          return item[0];
        });
      const valueList = chartData.map(function (item) {
          return Math.round(item[1] * 1000) / 1000;
        });
      const options = {
           // Make gradient line here
        visualMap: [
          {
            show: false,
            type: 'continuous',
            seriesIndex: 0,
            min: -0.2,
            max: 0.2
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
            min:-0.2,
            max:0.2
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
      this.loading=false
      
    },
    async loadEcharts2() {
      this.loading = true;
      let chartData2 =  await this.getChart2Data();
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
          min:-1,
          max:1,
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
      chartData2.forEach(function (dataItem) {
        series[dataItem[0]].data.push([dataItem[1]]);
      });
    
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
      this.loading = false;
      
    },
    getData() {
      if (this.interval == "day"){
        return this.$axios
        .get(process.env.VUE_APP_BASE_URL + "/board/political/sentiments/daily?startdate=2022-02-09&enddate=2023-06-30")
        .then((result) => {
          this.dayChartData = result.data.data;
          return result.data.data;
      });
      }else if( this.interval == "week"){
        return this.$axios
        .get(process.env.VUE_APP_BASE_URL + "/board/political/sentiments/weekly?startweek=-15&endweek=15")
        .then((result) => {
          this.weekChartData = result.data.data;
          return result.data.data;
      });
      }else{
        return this.$axios
        .get(process.env.VUE_APP_BASE_URL + "/board/political/sentiments/monthly?startdate=2022-02-09&enddate=2023-06-30")
        .then((result) => {
          this.monthChartData = result.data.data;
          return result.data.data;
      });
      }
   
    },
    storeData1(){
       this.$axios
        .get(process.env.VUE_APP_BASE_URL + "/board/political/sentiments/daily?startdate=2022-02-09&enddate=2023-06-30")
        .then((result) => {
          this.dailyChartData = result.data.data;
      });
      this.$axios
        .get(process.env.VUE_APP_BASE_URL + "/board/political/sentiments/weekly?startweek=-15&endweek=15")
        .then((result) => {
          this.weekChartData = result.data.data;
      });
      this.$axios
        .get(process.env.VUE_APP_BASE_URL + "/board/political/sentiments/month?startdate=2022-02-09&enddate=2023-06-30")
        .then((result) => {
          this.monthChartData = result.data.data;
      });
    },
    getChart2Data(){
      let src = ""
      if(this.after == "1w"){
        src = process.env.VUE_APP_BASE_URL + "/board/political/sentiments/winningchange?type=week&after=1"
      }else if(this.after == "2w"){
        src = process.env.VUE_APP_BASE_URL + "/board/political/sentiments/winningchange?type=week&after=2"
      }else if(this.after == "1m"){
        src = process.env.VUE_APP_BASE_URL + "/board/political/sentiments/winningchange?type=month&after=1"
      }else if (this.after == "2m"){
        src =  process.env.VUE_APP_BASE_URL + "/board/political/sentiments/winningchange?type=month&after=2"
      }else {
        src = process.env.VUE_APP_BASE_URL + "/board/political/sentiments/winningchange?type=month&after=3"
      }
      return this.$axios
        .get(src)
        .then((result) => {
          let chartData = [];
          const obj = result.data.data;
          for (let i = 0;i<Object.values(obj).length; i++){
            const value = Object.values(obj)[i]
            let itemList = []
            itemList.push(value.hasChangedWinningParty)
            itemList.push(Math.round(value.avg_sentiment * 1000) / 1000)
            chartData.push(itemList)
          }
          return chartData
      });

    },


    
  },
};
</script>
<style>
  .el-menu-vertical-demo{
    height:80em;
    
  }
  .scatter1{
    height: 40em;
    display:flex;
    background-color: #5f4848;
    justify-content:center;
    align-items: center;
    border-bottom:0.1em solid #fff;
  }
  .scatter2{
    height: 40em;
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
    overflow: scroll;
    width:91%;
    margin-left: 5%;
    margin-top:2%;
    background-color:#5f4848;
    border:0.5em solid#cb7f67;
    word-wrap: break-word;
    word-break: break-all;
  }
</style>

