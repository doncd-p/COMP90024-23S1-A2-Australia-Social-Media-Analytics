<template>
    <div id="app">  
      <el-col :span="24" class="table">
        <el-row class="table1">
          <!-- figure1 -->
          <el-col class="tablebody" :span="20">
            <div class="tablelabel"> Sentiment Ranking</div>
            <el-table class="tablecontent" :data="tableData1" stripe height="250" border style="width: 100%"  :default-sort = "{prop: 'sentiment', order: 'descending'}" >
                <el-table-column prop="electorate" label="Electorate" width="180"> </el-table-column>
                <el-table-column prop="party1" label="2019 Party" width="180"> </el-table-column>
                <el-table-column prop="party2" label="2022 Party" width="180"> </el-table-column>
                <el-table-column prop="vote" label="2022 Vote" width="180"> </el-table-column>
                <el-table-column prop="sentiment" label="Sentiment" sortable width="180"> </el-table-column>
            </el-table>
          </el-col>
          <el-col class="filter" :span="4">
            <el-row>
                <div class="filter1"> 
                  <div class="filter1label"> State:</div>
                  <el-select v-model="state1" :change="handleClick()" >
                    <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value"> </el-option>
                  </el-select>
                </div>
            </el-row>
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
            <el-table class="tablecontent" :data="tableData2" stripe height="250" border style="width: 100%"  :default-sort = "{prop: 'tweets', order: 'descending'}" >
                <el-table-column prop="electorate" label="Electorate" width="180"> </el-table-column>
                <el-table-column prop="party1" label="2019 Party" width="180"> </el-table-column>
                <el-table-column prop="party2" label="2022 Party" width="180"> </el-table-column>
                <el-table-column prop="vote" label="2022 Vote" width="180"> </el-table-column>
                <el-table-column prop="tweets" label="Tweets Number" sortable width="180"> </el-table-column>
            </el-table>
          </el-col>
          <el-col class="filter" :span="4">
            <el-row>
                <div class="filter1"> 
                  <div class="filter1label"> State:</div>
                  <el-select v-model="state2" :change="handleClick()" >
                    <el-option v-for="item in options2" :key="item.value" :label="item.label" :value="item.value"> </el-option>
                  </el-select>
                </div>
            </el-row>
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
import { getNoParam, getParam, postParam } from '../../api/test'

export default {
  name: "distribution",
  data() {
      return {
       //table1 data
       tableData1: [{
          electorate: 'Eleborate1',
          party1: 'LP',
          party2: 'ALP',
          vote:'56%',
          sentiment: 76,
          state: 'vic'
        }, {
          electorate: 'Eleborate2',
          party1: 'LP',
          party2: 'GRN',
          vote:'76%',
          sentiment: 34,
          state: 'vic'
        }, {
          electorate: 'Eleborate3',
          party1: 'IND',
          party2: 'ALP',
          vote:'45%',
          sentiment: -34,
          state: 'nsw'
        }, {
          electorate: 'Eleborate4',
          party1: 'XEN',
          party2: 'NP',
          vote:'78%',
          sentiment: 5,
          state: 'nsw'
        },{
          electorate: 'Eleborate5',
          party1: 'KAP',
          party2: 'LNP',
          vote:'67%',
          sentiment: -89,
          state: 'vic'
        }],
        //table1 filter1
        options: [{
          value: 'all',
          label: 'ALL'
        }, {
          value: 'vic',
          label: 'VIC'
        }, {
          value: 'nsw',
          label: 'NSW'
        }],
        state1: 'all',
        //table1 filter2
        pickerOptions1: {
          shortcuts: [{
            text: 'last a week',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
              picker.$emit('pick', [start, end]);
            }
          }, {
            text: 'last a month',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
              picker.$emit('pick', [start, end]);
            }
          }, {
            text: 'last three months',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 90);
              picker.$emit('pick', [start, end]);
            }
          }]
        },
        timeline1: [],
        //table2 data
        tableData2: [{
          electorate: 'Eleborate1',
          party1: 'LP',
          party2: 'ALP',
          vote:'56%',
          tweets: 2003
        }, {
          electorate: 'Eleborate2',
          party1: 'LP',
          party2: 'GRN',
          vote:'76%',
          tweets: 3432
        }, {
          electorate: 'Eleborate3',
          party1: 'IND',
          party2: 'ALP',
          vote:'45%',
          tweets: 3430
        }, {
          electorate: 'Eleborate4',
          party1: 'XEN',
          party2: 'NP',
          vote:'78%',
          tweets: 50000
        },{
          electorate: 'Eleborate5',
          party1: 'KAP',
          party2: 'LNP',
          vote:'67%',
          tweets: 34356
        }],
      //table2 filter1
        options2: [{
          value: 'all',
          label: 'ALL'
        }, {
          value: 'vic',
          label: 'VIC'
        }, {
          value: 'nsw',
          label: 'NSW'
        }],
        state2: 'all',
        //table2 filter2
        pickerOptions2: {
          shortcuts: [{
            text: 'a week before eleboration',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
              picker.$emit('pick', [start, end]);
            }
          }, {
            text: 'a month before eleboration',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
              picker.$emit('pick', [start, end]);
            }
          }, {
            text: 'a month after eleboration',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 90);
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
    start.setFullYear(2019,0,14);
    end.setFullYear(2022,11,24);
    this.timeline1 = [start, end];
    this.timeline2 = [start, end];
    
  },

  methods: {

    handleClick() {
      this.updateData();

    },
    updateData(){
       //tabledata
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

