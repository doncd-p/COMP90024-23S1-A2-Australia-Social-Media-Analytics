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
            <div class="c scatter" id="scatterchart" ref="scatterchart" ></div>
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
// import echarts from 'echarts';
import * as echarts from 'echarts'

export default {
  name: "distribution",
  data() {
      return {
        loading:true,
       //chart1 data
        dailyChartData:null,
        weekChartData:null,
        monthChartData:null,
        scatterchart:{},
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
        description1: 'This graph denotes the aggregated National Political Sentiment on Twitter over the period of analysis. You can select levels of time granularity for aggregation. ',
        description2: 'This graph denotes the sentiment distribution for electorates that changed vs didn’t change governing parties in the recent election. You can select time periods of aggregation relative to the election date.' }
    },
  created(){
    this.initEcharts();
    setTimeout(() => {
      this.storeData1();
      this.getChart2Data();
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
      
      //chart2:
      let chartData2 =  await this.getChart2Data();
      let changed = []
      let not_changed = []
      for(let i = 0 ; i< chartData2.length ; i++){
        if (chartData2[i][0]==1){
          changed.push(chartData2[i][1])
        }else{
          not_changed.push(chartData2[i][1])
        }
      }
       const options2 = {
      title: [
        {
          text: 'Comparison of the sentiment according to whether changed governing party',
          left: 'center'
        },
        {
        
          left: '10%',
          top: '90%'
        }
      ],
      dataset: [
        {
          source: [
            not_changed, changed
          ]
        },
      
        {
          transform: {
            type: 'boxplot',
            config: { itemNameFormatter: function (params) {
              if (params.value == 1) {
                return "changed"
              }
              return "non-changed"
            }}
          }
        },
        {
          fromDatasetIndex: 1,
          fromTransformResult: 1
        }
      ],
      tooltip: {
        trigger: 'item',
        axisPointer: {
          type: 'shadow'
        }
      },
      grid: {
        left: '10%',
        right: '10%',
        bottom: '15%'
      },
      xAxis: {
        type: 'value',
        name: 'Sentiment',
        min: -1,
        max:1
      },
      yAxis: {
        type: 'category',
        boundaryGap: true,
        nameGap: 15,
        splitArea: {
          show: false
        },
        splitLine: {
          show: true
        }
      },
      color:[
        "#ee6666",
      ],
      series: [
        {
          name: 'non-changed',
          type: 'boxplot',
          datasetIndex: 1,
          tooltip: {formatter: function(params){
            return [
              'Type:' + params.name,
              'min:'+params.data[1], 
              'Q1: ' + params.data[2],
              'median:'+params.data[3],
              'Q3:'+params.data[4],
              'max:'+params.data[5],
            ].join('<br/>')
          }},
          itemStyle: {color: '#ffd04b'},
        },
        {
          name: 'changed',
          type: 'scatter',
          datasetIndex: 2,
          tooltip: {formatter: function(params){
            return [
              'Type:' + params.name,
              'min:'+params.data[1], 
              'Q1: ' + params.data[2],
              'median:'+params.data[3],
              'Q3:'+params.data[4],
              'max:'+params.data[5],
            ].join('<br/>')
          }},
          itemStyle: {color: '#dd0000'},
        },
      
      ]
    };

      let scatterchart = echarts.init(this.$refs.scatterchart)
      scatterchart.setOption(options2)
      this.loading = false
      
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
      this.loading = false
      
    },
    
    async loadEcharts2() {
      this.loading = true;
      let chartData2 =  await this.getChart2Data();
      let changed = []
      let not_changed = []
      for(let i = 0 ; i< chartData2.length ; i++){
        if (chartData2[i][0]==1){
          changed.push(chartData2[i][1])
        }else{
          not_changed.push(chartData2[i][1])
        }
      }

    
    const options2 = {
      title: [
        {
          text: 'Comparison of the sentiment according to whether changed governing party',
          left: 'center'
        },
        {
        
          left: '10%',
          top: '90%'
        }
      ],
      dataset: [
        {
          source: [
            not_changed, changed
          ]
        },
      
        {
          transform: {
            type: 'boxplot',
            config: { itemNameFormatter: function (params) {
              if (params.value == 1) {
                return "changed"
              }
              return "non-changed"
            }}
          }
        },
        {
          fromDatasetIndex: 1,
          fromTransformResult: 1
        }
      ],
      tooltip: {
        trigger: 'item',
        axisPointer: {
          type: 'shadow'
        }
      },
      grid: {
        left: '10%',
        right: '10%',
        bottom: '15%'
      },
      xAxis: {
        type: 'value',
        name: 'Sentiment',
        min: -1,
        max:1
      },
      yAxis: {
        type: 'category',
        boundaryGap: true,
        nameGap: 15,
        splitArea: {
          show: false
        },
        splitLine: {
          show: true
        }
      },
      color:[
        "#ee6666",
      ],
      series: [
        {
          name: 'boxplot',
          type: 'boxplot',
          datasetIndex: 1,
          tooltip: {formatter: function(params){
            return [
              'Type:' + params.name,
              'min:'+params.data[1], 
              'Q1: ' + params.data[2],
              'median:'+params.data[3],
              'Q3:'+params.data[4],
              'max:'+params.data[5],
            ].join('<br/>')
          }},
          itemStyle: {color: '#ffd04b'},
          lineStyle: { weight:3},
        },
        {
          name: 'outlier',
          type: 'scatter',
          datasetIndex: 2,
          tooltip: {formatter: function(params){
            return [
              'Type:' + params.name,
              'min:'+params.data[1], 
              'Q1: ' + params.data[2],
              'median:'+params.data[3],
              'Q3:'+params.data[4],
              'max:'+params.data[5],
            ].join('<br/>')
          }},
          itemStyle: {color: '#dd0000'},
        },
      
      ]
    };

    
      let scatterchart = echarts.init(this.$refs.scatterchart)
      scatterchart.setOption(options2)
      this.loading = false;
      
    },
    getData() {
      if (this.interval == "day"){
        return this.$axios
        .get("http://"+process.env.VUE_APP_BASE_URL + ":8080/board/political/sentiments/daily?startdate=2022-02-09&enddate=2023-06-30")
        .then((result) => {
          this.dayChartData = result.data.data;
          return result.data.data;
      });
      }else if( this.interval == "week"){
        return this.$axios
        .get("http://"+process.env.VUE_APP_BASE_URL + ":8080/board/political/sentiments/weekly?startweek=-15&endweek=15")
        .then((result) => {
          this.weekChartData = result.data.data;
          return result.data.data;
      });
      }else{
        return this.$axios
        .get("http://"+process.env.VUE_APP_BASE_URL + ":8080/board/political/sentiments/monthly?startdate=2022-02-09&enddate=2023-06-30")
        .then((result) => {
          this.monthChartData = result.data.data;
          return result.data.data;
      });
      }
   
    },
    storeData1(){
       this.$axios
        .get("http://"+process.env.VUE_APP_BASE_URL + ":8080/board/political/sentiments/daily?startdate=2022-02-09&enddate=2023-06-30")
        .then((result) => {
          this.dailyChartData = result.data.data;
      });
      this.$axios
        .get("http://"+process.env.VUE_APP_BASE_URL + ":8080/board/political/sentiments/weekly?startweek=-15&endweek=15")
        .then((result) => {
          this.weekChartData = result.data.data;
      });
      this.$axios
        .get("http://"+process.env.VUE_APP_BASE_URL + ":8080/board/political/sentiments/month?startdate=2022-02-09&enddate=2023-06-30")
        .then((result) => {
          this.monthChartData = result.data.data;
      });
    },
    getChart2Data(){
      let src = ""
      if(this.after == "1w"){
        src = "http://"+process.env.VUE_APP_BASE_URL + ":8080/board/political/sentiments/winningchange?type=week&after=1"
      }else if(this.after == "2w"){
        src = "http://"+process.env.VUE_APP_BASE_URL + ":8080/board/political/sentiments/winningchange?type=week&after=2"
      }else if(this.after == "1m"){
        src = "http://"+process.env.VUE_APP_BASE_URL + ":8080/board/political/sentiments/winningchange?type=month&after=1"
      }else if (this.after == "2m"){
        src = "http://"+process.env.VUE_APP_BASE_URL + ":8080/board/political/sentiments/winningchange?type=month&after=2"
      }else {
        src = "http://"+process.env.VUE_APP_BASE_URL + ":8080/board/political/sentiments/winningchange?type=month&after=3"
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
    height:240px;
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

