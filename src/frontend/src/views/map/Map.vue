<template>
  <div class="container" style="height:95vh;">
    <!-- option -->
    <el-row class="option" :gutter="2" style="height:15vh;">
      <el-col :span="12">
        <div class="label-text">Senario:</div>
        <el-radio-group v-model="senario" class="radio-container">
          <el-radio-button label="vote" >Percentage of votes</el-radio-button>
          <el-radio-button label="sentiment"
            >&nbsp;&nbsp;&nbsp;Sentiment&nbsp;&nbsp;&nbsp;</el-radio-button
          ><br />
          <el-radio-button label="tweets" >Number of Tweets</el-radio-button>
          <el-radio-button label="status" >changed governing party</el-radio-button>
        </el-radio-group>
      </el-col>
      <el-col :span="4">
        <div class="party">
          <div class="label-text">Govering Party:</div>
          <div class="party-text">{{ party }}</div>
        </div>
      </el-col>
      <el-col :span="8"
        ><div class="label-text">Time:</div>
        <div class="time">
          <el-radio-group v-model="time" >
            <el-radio label="pre" border
              >&nbsp;&nbsp;&nbsp;&nbsp;Pre-election&nbsp;&nbsp;&nbsp;&nbsp;</el-radio
            >
            <el-radio label="post" border
              >&nbsp;&nbsp;&nbsp;Post-election&nbsp;&nbsp;&nbsp;</el-radio
            >
          </el-radio-group>
        </div>
      </el-col>
    </el-row>
      <el-row class="colorItem" style="height:5vh;">
       <div class="legend">{{legend.left}}</div>
       <div class="colorRange" :style="cover" v-if="senario != 'status'"></div>
        <div v-else class="colorRange" >
            <div style="height: 100%; margin-right: 2%; width: 48%; background-color: #666666"></div>
            <div style="height: 100%; width:48%;background-color: #FF0000"></div>
        </div>
        <div class="legend">{{legend.right}}</div>
      </el-row>
    <!-- map -->
    <div class="map" id="map" v-loading="loading" style="height: 65vh; margin-bottom:0;"
      element-loading-text="loading..."
      element-loading-spinner="el-icon-loading"
      element-loading-background="rgba(0, 0, 0, 0.8)"></div>
    <div style="color:white; height:5vh; margin-bottom:0" > Note: Percentage of votes won is votes according to Two Candidate Preferences.</div>

    <el-dialog
      :title="mapItem.divisionName"
      :visible.sync="dialogVisible"
      :append-to-body="true"
      width="50%"
      :before-close="handleClose"
    >
      <el-form label-position="left">
        <el-form-item label="Average Voting Age: ">
          {{ mapItem.avgAge }}
        </el-form-item>
        <el-form-item label="Average Education Years: ">
          {{ mapItem.avgEducYears }}
        </el-form-item>
        <el-form-item label="Average Weekly Income: ">
          {{ mapItem.avgWeeklyIncome }}
        </el-form-item>
        <el-form-item label="Net Migration: ">
          {{ mapItem.netMigration }}
        </el-form-item>
        <el-form-item label="Winning Party in 2019: ">
          {{ mapItem.winparty19 }}
        </el-form-item>
        <el-form-item label="Winning Party Vote Rate in 2019: ">
          {{ mapItem.winpartyvote19 }}
        </el-form-item>
        <el-form-item label="Winning Party in 2022: ">
          {{ mapItem.winparty22 }}
        </el-form-item>
        <el-form-item label="Winning Party Vote Rate in 2022: ">
          {{ mapItem.winpartyvote22 }}
        </el-form-item>

        <el-form-item label="Overall Sentiment: ">
          {{ mapItem.overall_sentiment }}
        </el-form-item>
         <el-form-item label="The Number of Tweets: ">
          {{ mapItem.tweets_num }}
        </el-form-item>
          <div >
          <el-divider >Sentiment Analysis</el-divider>
           <pie-data
            :pieData="mapItem.sentiment">
          </pie-data>
        </div>
          <div >
          <el-divider>Weekly Sentiment</el-divider>
           <line-data
            :lineData="mapItem.lineData">
          </line-data>
          <div style="font-size:10px; display:flex; justify-content:center;">Note: "-5" on xAxis refers “the 5th week before the election day", "5" on xAxis refers "the 5th week after the election day".</div>
        </div>
       
      </el-form>
    
      <el-divider>Top Tweets</el-divider>
      <div style="font-weight:bolder;">Positive:</div>
      <div class="tweets" v-for="item in mapItem.posTweets" :key="item.tweet_id">
        <div style="font-weight:bold; margin-bottom:2px;">
          &nbsp;{{ item.author}}:
        </div>
         <p>
          &nbsp;&nbsp;&nbsp;{{ item.text }}
        </p>
      </div>
     
      <br>
      <div style="font-weight:bolder;">Negative:</div>
      <div class="tweets" v-for="item in mapItem.negTweets" :key="item.tweet_id">
        <div style="font-weight:bold; margin-bottom:2px;">
          &nbsp;{{ item.author}}:
        </div>
         <p>
          &nbsp;&nbsp;&nbsp;{{ item.text }}
        </p>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { Loader } from "@googlemaps/js-api-loader";
import axios from "axios";
import { faLandmarkFlag } from "@fortawesome/free-solid-svg-icons";
import PieData from "./PieData.vue";
import LineData from "./LineData";

export default {
  name: "Map",
  components:{
    PieData, LineData
  },
  props: {
    msg: String,
  },
  data() {
    return {
      loading: true,
      senario: "vote",
      time: "pre",
      data: [],
      map: null,
      mapData: null,
      party: "Liberal National Coalition",
      map: {},
      dialogVisible: false,
      mapItem: {
        divisionName: "",
        avgAge: null,
        avgEducYears: null,
        avgWeeklyIncome: null,
        netMigration: null,
        winparty19: null,
        winpartyvote19: null,
        winparty22: null,
        winpartyvote22: null,
        overall_sentiment: null,
        tweets_num: null,
        posTweets: [],
        negTweets: [],
        sentiment: [],
        lineData:[]
      },
      colorList:[],
      output: null,
    legend:{
      left: "50%",
      right:"100%"
    }
 
    };
  },
  methods: {
    handleClose() {
      this.dialogVisible = false;
      this.loading = false;
    },
    handleSenarioChange(value){
      this.initMap(value);
    },
    handleTimeChange(value){
      if (this.time === "pre") {
        this.party = "Liberal National Coalition";
      } else {
        this.party = "Australian Labour Party";
      }
      this.initMap(this.senario);
    },

    rgbToHex(r, g, b) {
      var hex = ((r << 16) | (g << 8) | b).toString(16);
      return "#" + new Array(Math.abs(hex.length - 7)).join("0") + hex;
    },
    hexToRgb(hex) {
      var rgb = [];
      for (var i = 1; i < 7; i += 2) {
        rgb.push(parseInt("0x" + hex.slice(i, i + 2)));
      }
      return rgb;
    },
    gradient(startColor, endColor, step) {
      
      var sColor = this.hexToRgb(startColor),
        eColor = this.hexToRgb(endColor);

      
      var rStep = (eColor[0] - sColor[0]) / step,
        gStep = (eColor[1] - sColor[1]) / step,
        bStep = (eColor[2] - sColor[2]) / step;

      var gradientColorArr = [];
      for (var i = 0; i < step; i++) {
        
        gradientColorArr.push(
          this.rgbToHex(
            parseInt(rStep * i + sColor[0]),
            parseInt(gStep * i + sColor[1]),
            parseInt(bStep * i + sColor[2])
          )
        );
      }
      return gradientColorArr;
    },

    getCloudData() {
      let url;
      if(this.time == "pre"){
        url = process.env.VUE_APP_BASE_URL + "/political/sentiments/daily?startdate=2022-02-09&enddate=2022-05-21"
      }else{
        url = process.env.VUE_APP_BASE_URL + "/political/sentiments/daily?startdate=2022-05-22&enddate=2023-06-30"
      }
      return axios
        .get(
          url
        )
        .then((res) => {
          return res.data;
        });
    },
    async getDetail(eName){
      
      const posSrc = process.env.VUE_APP_BASE_URL + "/tweet/top_positive?num=5&electorate="+eName;
      const negSrc = process.env.VUE_APP_BASE_URL + "/tweet/top_negative?num=5&electorate="+eName;
      let sentimentSrc;
      let lineSrc;
      if (this.time == "pre"){
        sentimentSrc = process.env.VUE_APP_BASE_URL + "/political/sentiments/number?startdate=2022-02-09&enddate=2022-05-21&electorate="+eName;
        lineSrc = process.env.VUE_APP_BASE_URL + "/political/sentiments/weekly?startweek=-5&endweek=-1&electorate="+eName;
      }else{
        sentimentSrc = process.env.VUE_APP_BASE_URL + "/political/sentiments/number?startdate=2022-05-22&enddate=2023-06-30&electorate="+eName;
        lineSrc = process.env.VUE_APP_BASE_URL + "/political/sentiments/weekly?startweek=1&endweek=5&electorate="+eName
      }
      
      const [posResponse, negResponse, senResponse, lineResponse] = await Promise.all([
        axios.get(posSrc),
        axios.get(negSrc),
        axios.get(sentimentSrc),
        axios.get(lineSrc)
      ]);
      this.mapItem.posTweets = posResponse.data.data;
      this.mapItem.negTweets = negResponse.data.data;
      this.mapItem.sentiment = senResponse.data.data[eName];
      let tempLineData = lineResponse.data.data[eName];
      let lineData = [];
      for (let i =0; i<Object.entries(tempLineData).length;i++){
        lineData.push(Object.entries(tempLineData)[i])

      }
      this.mapItem.lineData = lineData;

    },
  
    // ========================== Init Map ==================================================
    async initMap(label) {
      let that = this;
      const loader = new Loader({
        apiKey: "AIzaSyA7qMWed4cLNiIl922Yy3nrZVVSASlDQJw",
        version: "weekly",
        language: "en",
      });
 
    const response = await this.getCloudData();
    this.output = response.data;

      loader.load().then(() => {
        const map = new google.maps.Map(document.getElementById("map"), {
          center: { lat: -26.2744, lng: 133.7751 },
          zoom: 5,
        });
        
      // ========================Icon examples=========================
      const icon=  {
            path: faLandmarkFlag.icon[4],
            fillColor: "#0000ff",
            fillOpacity: 1,
            anchor: new google.maps.Point(
              faLandmarkFlag.icon[0] / 2, // width
              faLandmarkFlag.icon[1] // height
            ),
            strokeWeight: 1,
            strokeColor: "#ffffff",
            scale: 0.035,
          };

      let jsonName;
      if(this.time == "pre"){
        jsonName = require('../../assets/json/centroid19.json')
      }else{
        jsonName = require('../../assets/json/centroid22.json')
      }

      for (let i = 0; i < jsonName.length; i++){
        let pos = {lat: jsonName[i].lng, lng: jsonName[i].lat}
        let name = jsonName[i].name
        const marker = new google.maps.Marker({
            position: pos,
            icon: icon,
            map: map,
            title: `${name}`
        });
      }
        
        map.data.loadGeoJson(
          process.env.VUE_APP_BASE_URL + "/electorate/geo_data",
          null,
          () => {
            
            // Style the polygons
            map.data.setStyle((feature) => {    
              let color;

              if(label == 'vote'){
                let vote;
                if (this.time == "pre"){
                  vote = feature.getProperty("winningPercentage2019");
                }else{
                  vote = feature.getProperty("winningPercentage2022");
                }
                
                color = that.gradient("#FFFF00","#FF0000",31)[parseInt(vote*100-50)];
                

              }else if (label == 'sentiment'){
                const sentiment = that.output[feature.getProperty("divisionName")]["avg_sentiment"];
                if (sentiment < 0){
                  color  = that.gradient("#FFFF00","#0000FF",81)[parseInt(sentiment*(-1)*100)];
                  
                }else{
                  color  = that.gradient("#FFFF00","#FF0000",81)[parseInt(sentiment*100)];
                  if(!color && sentiment > 0.8){
                    color  = "#FF0000";
                  }
                }
              }else if(label == 'tweets'){
                const num_tweets = that.output[feature.getProperty("divisionName")]["num_tweets"];
                color = that.gradient("#FFFFFF","#FF0000",3000)[num_tweets];
                if (num_tweets > 3000){
                  color = "#FF0000";
                }
              
              }else{
                const changed = feature.getProperty("hasChangedWinningParty");
                if (changed == 0){
                  color = "#666666";
                }else{
                  color = "#FF0000";
                }
              }
              this.loading = false;
              return {
                fillColor: color,
                strokeColor: "#000",
                strokeWeight: .2,
                fillOpacity: 1
              };
            });
            
            // Add click and mouseover listeners
            let that = this;
            map.data.addListener("click", async (event) => {
              this.loading = true;
              this.mapItem.divisionName =
                event.feature.getProperty("divisionName");
              this.mapItem.avgAge = event.feature
                .getProperty("averageAge")
                .toFixed(2);
              this.mapItem.avgEducYears = event.feature
                .getProperty("averageEducationYears")
                .toFixed(2);
              this.mapItem.avgWeeklyIncome = event.feature
                .getProperty("averageWeeklyIncome")
                .toFixed(2);
              this.mapItem.netMigration = event.feature
                .getProperty("netMigration")
                .toFixed(2);
              this.mapItem.winparty19 = event.feature
                .getProperty("winningParty2019");
              this.mapItem.winpartyvote19 = event.feature
                .getProperty("winningPercentage2019")
                .toFixed(2);
              this.mapItem.winparty22 = event.feature
                .getProperty("winningParty2022")
              this.mapItem.winpartyvote22 = event.feature
                .getProperty("winningPercentage2022")
                .toFixed(2);
              this.mapItem.overall_sentiment = that.output[event.feature.getProperty("divisionName")]["avg_sentiment"].toFixed(3)
              this.mapItem.tweets_num = that.output[event.feature.getProperty("divisionName")]["num_tweets"]
              await that.getDetail(event.feature.getProperty("divisionName"));
          
              this.dialogVisible = true;
              this.loaidng = false;
            });

            // Define infowindow outside the listeners
            const infowindow = new google.maps.InfoWindow();

            map.data.addListener("mouseover", async (event) => {
              let value;
              if (label == 'sentiment'){
                value = await this.output[event.feature.getProperty("divisionName")]["avg_sentiment"].toFixed(3);
              }else if (label == 'vote'){
                if(this.time == "pre"){
                  value = event.feature.getProperty("winningPercentage2019").toFixed(3);
                }else{
                  value = event.feature.getProperty("winningPercentage2022").toFixed(3);
                }
                
              }else if (label == 'tweets'){
                value = await that.output[event.feature.getProperty("divisionName")]["num_tweets"];
              }else if (label == 'status'){
                value = ''
              }
              const content = event.feature.getProperty("divisionName")+"<br/>"+value;
              infowindow.setContent(content);
              infowindow.setPosition(event.latLng);
              infowindow.open(map);
            });

            map.data.addListener("mouseout", (event) => {
              infowindow.close();
            });

     

          }
        );
      });
    },
  },
  computed: {
    cover() {
      let startColor;
      let endColor;
      switch(this.senario) {
      case 'sentiment': {
        return "background: linear-gradient(to right, #0000FF, #FFFF00, #FF0000);"
      } break;
      case 'tweets': { startColor = '#FFFFFF'; endColor = '#FF0000'; } break;
      case 'vote': { startColor = '#FFFF00'; endColor = '#FF0000'; } break;
      default: return;
      }
      return "background: linear-gradient(to right, " + startColor + "," + endColor + ");"
    }
  },

  mounted() {
    this.initMap(this.senario);
    
  },
  
  watch: {
    senario: {
      handler(value) {
        if(value == "vote"){
          this.legend.left = "50%"
          this.legend.right = "100%"
        }else if (value == "sentiment"){
          this.legend.left = "-1"
          this.legend.right = "1"
        }else if (value == "tweets"){
          this.legend.left = "0"
          this.legend.right = "max"
        }else{
          this.legend.left = "non-changed"
          this.legend.right = "changed"
        }
       
        this.handleSenarioChange(value);
      },
      deep: true,
    },
    time: {
      handler(value) {
        this.handleTimeChange(value);
      },
      deep: true,
    }
  },
};
</script>

<style scoped>
.container {
  height: 100%;
  width: 100%;
  background-color: #232838;
  opacity: 0.9;
}
.option {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.radio-container {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
}
.label-text {
  font-weight: 800;
  font-size: 24px;
  margin-bottom: 15px;
  margin-left: 30px;
  color: #ffd04b;
}
.time {
  display: flex;
  justify-content: center;
}
.party {
  height: 100px;
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  border: 0.2em solid #ffd04b;
  border-radius: 2em;
}
.party-text {
  display: flex;
  justify-content: center;
  font-weight: 400;
  font-size: 20px;
  color: #fff;
}
.colorRange {
  height: 20px;
  width: 70%;
  display: flex;
}
.colorItem{
  display: flex;
  align-items: center;
  margin:1%;
  
}
.legend{
  margin:0 1%;
  color:#fff;
  font-size: 24px;
  margin: auto;
}
.tweets{
  margin: 1em;
  border-style: outset;
}
</style>
