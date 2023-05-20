<template>
    <div id="app" v-loading="loading" style="height: 100vh"
      element-loading-text="loading..."
      element-loading-spinner="el-icon-loading"
      element-loading-background="rgba(0, 0, 0, 0.8)">  
      <el-col :span="24" class="table">
        <el-row class="table1">
          <!-- figure1 -->
          <el-col class="tablebody" :span="20">
            <div class="tablelabel"> Sentiment Ranking</div>
            <el-table class="tablecontent" :data="tableData1" stripe height="250" style="width: 100%"  :default-sort = "{prop: 'sentiment', order: 'descending'}" >
                <el-table-column type="index" :index="indexMethod" width="width:10%" align="center"> </el-table-column>
                <el-table-column prop="electorate" label="Electorate" width="width:18%" align="center"> </el-table-column>
                <el-table-column prop="party1" label="2019 Party" width="width:18%" align="center"> </el-table-column>
                <el-table-column prop="party2" label="2022 Party" width="width:18%" align="center"> </el-table-column>
                <el-table-column prop="vote" label="2022 Vote" width="width:18%" sortable align="center"> </el-table-column>
                <el-table-column prop="sentiment" label="Sentiment" sortable width="width:18%" align="center"> </el-table-column>
            </el-table>
          </el-col>
          <el-col class="filter" :span="4">
            
            <el-row>
                <div class="filter1"> 
                  <div class="filter1label"> Timeline:</div>
                   <el-date-picker v-model="timeline1" type="daterange" align="right" unlink-panels range-separator="to" start-placeholder="start date"
                    end-placeholder="end date" :picker-options="pickerOptions1"></el-date-picker>
                </div>
            </el-row>
          </el-col>
        </el-row>
        <el-row class="table2">
          <!-- figure1 -->
          <el-col class="tablebody" :span="20">
            <div class="tablelabel"> #Tweets Ranking</div>
            <el-table class="tablecontent" :data="tableData2" stripe height="250" style="width: 100%"  :default-sort = "{prop: 'tweets', order: 'descending'}" >
                <el-table-column type="index" :index="indexMethod" width="width:10%" align="center"> </el-table-column>
                <el-table-column prop="electorate" label="Electorate" width="width:18%" align="center"> </el-table-column>
                <el-table-column prop="party1" label="2019 Party" width="width:18%" align="center"> </el-table-column>
                <el-table-column prop="party2" label="2022 Party" width="width:18%" align="center"> </el-table-column>
                <el-table-column prop="vote" label="2022 Vote" width="width:18%" sortable align="center"> </el-table-column>
                <el-table-column prop="tweets" label="Tweets Number" sortable width="width:18%" align="center"> </el-table-column>
                
            </el-table>
          </el-col>
          <el-col class="filter" :span="4">
            
            <el-row>
                <div class="filter1"> 
                  <div class="filter1label"> Timeline:</div>
                  <el-date-picker v-model="timeline2" type="daterange" align="right" unlink-panels range-separator="to" start-placeholder="start date"
                    end-placeholder="end date" :picker-options="pickerOptions2"></el-date-picker>
                </div>
            </el-row>
          </el-col>
        </el-row>
      </el-col>
       
    </div>
   
    
</template>
<script>

export default {
  name: "distribution",
  data() {
      return {
      loading:true,
      index:[],
       //table1 data
      tableData1: [],
      //table1 filter2
      pickerOptions1: {
        shortcuts: [ {
          text: 'a month before election',
          onClick(picker) {
            const end = new Date();
            const start = new Date();
            start.setFullYear(2022,3,21);
            end.setFullYear(2022,4,21);
            this.timeline1 = [start, end];
            picker.$emit('pick', [start, end]);
          }
        }, {
          text: 'a month after election ',
          onClick(picker) {
            const end = new Date();
            const start = new Date();
            start.setFullYear(2022,4,22);
            end.setFullYear(2022,5,22);
            this.timeline1 = [start, end];
            picker.$emit('pick', [start, end]);
          }
        }]
      },
      timeline1: [],
      //table2 data
      tableData2: [],
    
      //table2 filter2
      pickerOptions2: {
        shortcuts: [{
          text: 'a month before election',
          onClick(picker) {
            const end = new Date();
            const start = new Date();
            start.setFullYear(2022,3,21);
            end.setFullYear(2022,4,21);
            this.timeline2 = [start, end];
            picker.$emit('pick', [start, end]);
          }
        }, {
          text: 'a month after election ',
          onClick(picker) {
            const end = new Date();
            const start = new Date();
            start.setFullYear(2022,4,22);
            end.setFullYear(2022,5,22);
            this.timeline2 = [start, end];
            picker.$emit('pick', [start, end]);
          }
        }]
      },
      timeline2: [],
      }
    },

  mounted() {
    const end = new Date();
    const start = new Date();
    start.setFullYear(2022,1,9);
    end.setFullYear(2023,5,30);
    this.timeline1 = [start, end];
    this.timeline2 = [start, end];
    
    this.initData();
  },
  watch:{
     timeline1: {
      handler(value) {
      
        if(value){
           this.updateData1();
        }
      },
      deep: true,
    },
     timeline2: {
      handler(value) {
      
        if(value){
          this.updateData2();
        }
      },
      deep: true,
    },
  },
methods: {

    
  getDate(date){
    let year = date.getFullYear(); 
    let month = (date.getMonth()+1)< 10?'0'+ (date.getMonth()+1) : (date.getMonth()+1);
    let day   = date.getDate() < 10?'0'+ date.getDate(): date.getDate();
    return ""+year+"-"+month+"-"+day
  },
  async updateData1(){
  
    this.loading = true
    const senSrc = "http://"+process.env.VUE_APP_BASE_URL + ":8080/political/sentiments/daily?startdate="+this.getDate(this.timeline1[0])+"&enddate="+this.getDate(this.timeline1[1])
    const senTweets = await this.$axios.get(senSrc).then((result) => {return result.data.data;});

    let tableData = []
    for(let i=0; i<this.tableData1.length; i++){
        // Get the name and value of the old object
        let name = this.tableData1[i]["electorate"];
        let party1 = this.tableData1[i]["party1"];
        let party2 = this.tableData1[i]["party2"];
        let vote = this.tableData1[i]["vote"];
        let sentiment;
        if(senTweets[name]){
          sentiment = senTweets[name]["avg_sentiment"];
          // Create the new object
          let newObj = {
            electorate: name,
            party1: party1,
            party2: party2,
            vote: vote,
            sentiment: sentiment.toFixed(3)
          }
          // Push the new object into the array of objects
          tableData.push(newObj);
        }
        
      }
      this.tableData1 = tableData;
      this.loading = false
    },
    async updateData2(){
      this.loading = true
      const senSrc = "http://"+process.env.VUE_APP_BASE_URL + ":8080/political/sentiments/daily?startdate="+this.getDate(this.timeline2[0])+"&enddate="+this.getDate(this.timeline2[1])
      const senTweets = await this.$axios.get(senSrc).then((result) => {return result.data.data;});

      let tableData = []
      for(let i=0; i<this.tableData1.length; i++){
          // Get the name and value of the old object
          let name = this.tableData1[i]["electorate"];
          let party1 = this.tableData1[i]["party1"];
          let party2 = this.tableData1[i]["party2"];
          let vote = this.tableData1[i]["vote"];
           if(senTweets[name]){
              let tweets = senTweets[name]["num_tweets"];
              // Create the new object
              let newObj = {
                electorate: name,
                party1: party1,
                party2: party2,
                vote: vote,
                tweets: tweets
              }
              // Push the new object into the array of objects
              tableData.push(newObj);
           }
        }
        this.tableData2 = tableData;
        this.loading = false
    },
    async initData(){
       //tabledata
      const src = "http://"+process.env.VUE_APP_BASE_URL + ":8080/electorate/sudo_data/all"
      const senSrc = "http://"+process.env.VUE_APP_BASE_URL + ":8080/political/sentiments/daily?startdate="+this.getDate(this.timeline1[0])+"&enddate="+this.getDate(this.timeline1[1])
     
      const senTweets = await this.$axios.get(senSrc).then((result) => {return result.data.data;});
      let tableData1 = [];
      let tableData2 = [];
      this.$axios.get(src).then((result) => {
        const obj = result.data.data;
        for(let i=0; i<Object.keys(obj).length; i++){
          // Get the name and value of the old object
          let name = Object.keys(obj)[i];
          let values = obj[name];
          let sentiment = senTweets[name]["avg_sentiment"];
          let tweet_num = senTweets[name]["num_tweets"];
          // Create the new object
          let newObj1 = {
            electorate: name,
            party1: values.winningParty2019,
            party2: values.winningParty2022,
            vote: values.winningPercentage2022.toFixed(3),
            sentiment: sentiment.toFixed(3)
          }
          let newObj2 = {
            electorate: name,
            party1: values.winningParty2019,
            party2: values.winningParty2022,
            vote: values.winningPercentage2022.toFixed(3),
            tweets: tweet_num
          }
          // Push the new object into the array of objects
          tableData1.push(newObj1);
          tableData2.push(newObj2);
        }
      });
      this.tableData1 = tableData1;
      this.tableData2 = tableData2;

      this.loading = false
    },
   
    
  },
};
</script>
<style>
  .el-menu-vertical-demo{
    height:100vh;
  }
  .table{
    height: 100px;
  }
  .table1{
    height: 30em;
    display: flex;
    background-color: #5f4848;
    justify-content:center;
    align-items: center;
    border-bottom:0.1em solid #fff;
  }
  .table2{
    height: 30em;
    background-color: #444a5b;
    display: flex;
    justify-content:center;
    align-items: center;
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
</style>

