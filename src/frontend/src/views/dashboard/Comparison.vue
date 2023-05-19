<template>
    <div id="app">  
      <el-col :span="24" class="chart">
        <el-row class="figurerow">
          <!-- figure1 -->
          <el-col class="figureitem" :span="20">
           <div class="tablelabel">Sudo Data Trends on Tweets Data</div>
            <div class="ch" ><img :src="img_src" width="700" height="480"></div>
          </el-col>
           <el-col class="filter" :span="4">
            <el-row>
                <div class="filter1"> 
                  <div class="filter1label"> Cencus Data:</div>
                  <el-select v-model="cencus"  >
                    <el-option v-for="item in options1" :key="item.value" :label="item.label" :value="item.value"> </el-option>
                  </el-select>
                </div>
            </el-row>
            <el-row>
                <div class="filter1"> 
                  <div class="filter1label"> Election:</div>
                   <el-select v-model="election"  >
                    <el-option v-for="item in options2" :key="item.value" :label="item.label" :value="item.value"> </el-option>
                  </el-select>
                </div>
            </el-row>
          </el-col>
        </el-row>
        <el-row class="tablerow">
            <!-- table1 -->
          <el-col class="tablebody" :span="20">
            <div class="tablelabel">Tweets vs Toots</div>
            <table>
                <tr>
                    <th style="width:400px;"></th>
                    <th style="width:28%; ">Tweet</th>
                    <th style="width:28%;">Toots</th>
                </tr>
                <tr>
                    <td>The Number of Total Non-partial Match Political Items </td>
                    <td>{{tweets_political}}</td>
                    <td>{{toots_political}}</td>
                </tr>
                <tr>
                    <td >Total Items Number</td>
                    <td>{{tweets_total}}</td>
                    <td>{{toots_total}}</td>
                </tr>
                <tr>
                    <td >Percentage of Non-partial Match Political Items</td>
                    <td>{{tweets_rate}}</td>
                    <td>{{toots_rate}}</td>
                </tr>
            </table>
          </el-col>
          <el-col class="filter" :span="4">
            <el-row>
                <!-- button -->
            </el-row>
            <el-row>
            
            </el-row>
          </el-col>
        </el-row>
      </el-col>
       
    </div>
   
    
</template>
<script>

export default {
  name: "comparison",
  data() {
      return {
        img_src:"",
        //table1 filter1
        options1: [{
          value: 'migration',
          label: 'Migration'
        }, {
          value: 'age',
          label: 'Age of Voters'
        }, {
          value: 'income',
          label: 'Weekly Income'
        },{
          value: 'education',
          label: 'Education Level'
        }],
        cencus: 'migration',
        options2: [{
          value: '2019percentage',
          label: 'Percentage of Support in 2019'
        },{
          value: '2022percentage',
          label: 'Percentage of Support in 2022'
        }, {
          value: 'sentiment',
          label: 'Sentiment'
        }, {
          value: 'status',
          label: 'Change Status'
        },
        ],
        election: 'percentage',
        tweets_political: 0,
        tweets_total: 0,
        tweets_rate: 0,
        toots_political: 0,
        toots_total: 0,
        toots_rate: 0
      }
    },
  created(){
    this.updateFigure();
    this.getData();
  },
  mounted() {
      
      let  timer = setInterval(() => {
        this.getData(timer)
         }, 10000)
  },
  watch: {
    cencus: {
      handler(value) {
        this.updateFigure();
      },
      deep: true,
    },
    election:{
      handler(value) {
        this.updateFigure();
      },
      deep: true
    }
  },

  methods: {
    updateFigure(){
      this.img_src = require("../../assets/images/"+this.cencus+"_"+this.election+".png")
    },
    getData() {
      setTimeout(()=>{
        this.$axios
            .get(process.env.VUE_APP_BASE_URL + "/toot/meta")
            .then((result) => {
              const data = result.data.data;
              this.toots_political = data.sum;
              this.toots_total = data.count;
              this.toots_rate = data.mean;
            });
         this.$axios
            .get(process.env.VUE_APP_BASE_URL + "/tweet/meta")
            .then((result) => {
              const data = result.data.data;
              this.tweets_political = data.sum;
              this.tweets_total = data.count;
              this.tweets_rate = data.mean;
              
            });
            }, 0)
    },

  },
};
</script>
<style>
  .el-menu-vertical-demo{
    height:100vh;
  }
  .figurerow{
    height: 50em;
    display:flex;
    background-color: #5f4848;
    justify-content:center;
    align-items: center;
    border-bottom:0.1em solid #fff;
  }
  .figureitem{
    height: 80%;
    width:65%;
    border: 0.5em solid #cb7f67;
    background-color: #fff;
    padding: 10px;
  }
  .ch{
    display:flex;
    justify-content:center;
    align-items: center;
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
  .table{
    height: 100px;
  }
  .tablerow{
    height: 20em;
    display: flex;
     background-color: #444a5b;
    justify-content:center;
    align-items: center;
    border-bottom:0.1em solid #fff;
  }
  .tablebody{
    height: 80%;
    width:65%;
    border: 0.5em solid #cb7f67;
    background-color: #fff;
    display: flex;
    flex-direction: column;
    padding: 10px;
  }
  .tablelabel{
    font-size: 24px;
    font-weight: 500;
    margin-left:10px;
    color: #666;
    margin-bottom: 15px;
  }
  .filter{
    margin-left: 100px;
  }
  .filter1{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin: 20px;
    
  }
  
  .filter1label{
    color:#cb7f67;
    font-weight: 600;
    font-size: 20px;
    margin-bottom: 10px;
  }
  table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
  text-align: center;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>

