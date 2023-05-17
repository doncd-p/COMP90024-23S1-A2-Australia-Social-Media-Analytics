<template>
  <div class="container">
    <!-- option -->
    <el-row class="option" :gutter="2">
      <el-col :span="10">
        <div class="label-text">Senario:</div>
        <el-radio-group v-model="senario" class="radio-container">
          <el-radio-button label="vote" >Percentage of votes</el-radio-button>
          <el-radio-button label="sentiment"
            >&nbsp;&nbsp;&nbsp;Sentiment&nbsp;&nbsp;&nbsp;</el-radio-button
          ><br />
          <el-radio-button label="tweets" >Number of Tweets</el-radio-button>
          <el-radio-button label="status" >Changed Status</el-radio-button>
        </el-radio-group>
      </el-col>
      <el-col :span="6">
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

    <div style="width: 100%; text-align: center; color: #fff; margin: 10px 0">
      <div
        style="
          height: 20px;
          width: 30%;
          background: linear-gradient(to right, yellow, red);
        "
      ></div>
    </div>

    <!-- map -->
    <div class="map" id="map" v-loading="loading" style="height: 100vh"
      element-loading-text="loading..."
      element-loading-spinner="el-icon-loading"
      element-loading-background="rgba(0, 0, 0, 0.8)"></div>

    <el-dialog
      :title="mapItem.divisionName"
      :visible.sync="dialogVisible"
      :append-to-body="true"
      width="50%"
      :before-close="handleClose"
    >
      <el-form label-position="left">
        <el-form-item label="Average Age: ">
          {{ mapItem.avgAge }}
        </el-form-item>
        <el-form-item label="Average Education Years: ">
          {{ mapItem.avgEducYears }}
        </el-form-item>
        <el-form-item label="Average Weekly Income: ">
          {{ mapItem.avgWeeklyIncome }}
        </el-form-item>
        <el-form-item label="Estimated Resident Population: ">
          {{ mapItem.erp }}
        </el-form-item>
        <el-form-item label="Net Migration Rate: ">
          {{ mapItem.netMigration }}
        </el-form-item>
          <div >
           <pie-data
            :pieData="mapItem.sentiment">
          </pie-data>
        </div>
       
      </el-form>
    
      <el-divider>Top Tweets</el-divider>
      <div>Positive:</div>
      <p v-for="item in mapItem.posTweets" :key="item.tweet_id">
          &nbsp;{{ item.text }}
      </p>
      <br>
      <div>Negative:</div>
      <p v-for="item in mapItem.negTweets" :key="item.tweet_id">
          &nbsp;{{ item.text }}
      </p>
    </el-dialog>
  </div>
</template>

<script>
import { Loader } from "@googlemaps/js-api-loader";
import axios from "axios";
import { faLandmarkFlag } from "@fortawesome/free-solid-svg-icons";
import PieData from "./PieData.vue";
export default {
  name: "Map",
  components:{
    PieData
  },
  props: {
    msg: String,
  },
  data() {
    return {
      loading: true,
      senario: "tweets",
      time: "pre",
      data: [],
      map: null,
      mapData: null,
      party: "Libera",
      map: {},
      dialogVisible: false,
      mapItem: {
        divisionName: "",
        avgAge: null,
        avgEducYears: null,
        avgWeeklyIncome: null,
        erp: null,
        netMigration: null,
        posTweets: [],
        negTweets: [],
        sentiment: []
      },
      colorList:[],
      output: null,

 
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
        this.party = "LP";
      } else {
        this.party = "ALP";
      }
      this.initMap(this.senario);
    },
    //////////////////
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
    ///////////////////
    getCloudData() {
      let url;
      if(this.time == "pre"){
        url = "http://172.26.128.247:8080//political/sentiments/daily?startdate=2022-02-09&enddate=2022-05-21"
      }else{
        url = "http://172.26.128.247:8080//political/sentiments/daily?startdate=2022-05-22&enddate=2023-06-30"
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
      
      const posSrc = "http://172.26.128.247:8080/tweet/top_positive?num=5&electorate="+eName;
      const negSrc = "http://172.26.128.247:8080/tweet/top_negative?num=5&electorate="+eName;
      let sentimentSrc;
      if (this.time == "pre"){
        sentimentSrc = "http://172.26.128.247:8080//political/sentiments/number?startdate=2022-02-09&enddate=2022-05-21&electorate="+eName;
      }else{
        sentimentSrc = "http://172.26.128.247:8080//political/sentiments/number?startdate=2022-05-22&enddate=2023-06-30&electorate="+eName;
      }
      
      const [posResponse, negResponse, senResponse] = await Promise.all([
        axios.get(posSrc),
        axios.get(negSrc),
        axios.get(sentimentSrc),
      ]);
      this.mapItem.posTweets = posResponse.data.data;
      this.mapItem.negTweets = negResponse.data.data;
      this.mapItem.sentiment = senResponse.data.data[eName];
      

      console.log(senResponse.data.data[eName])
      console.log(this.mapItem.sentiment)
      
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
          zoom: 4.5,
        });
        this.loading = false;
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
          "http://172.26.128.247:8080/electorate/geo_data",
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
                console.log(sentiment,color);
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
              this.mapItem.erp = event.feature
                .getProperty("estimatedResidentPopulation")
                .toFixed(2);
              this.mapItem.netMigration = event.feature
                .getProperty("netMigration")
                .toFixed(2);
              await that.getDetail(event.feature.getProperty("divisionName"));
          
              this.dialogVisible = true;
              this.loaidng = false;
            });

            // Define infowindow outside the listeners
            const infowindow = new google.maps.InfoWindow();

            map.data.addListener("mouseover", async (event) => {
              let value;
              if (label == 'sentiment'){
                value = await this.output[event.feature.getProperty("divisionName")]["avg_sentiment"];
              }else if (label == 'vote'){
                if(this.time == "pre"){
                  value = event.feature.getProperty("winningPercentage2019");
                }else{
                  value = event.feature.getProperty("winningPercentage2022");
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
  created(){
    
    
  },

  mounted() {
    this.initMap(this.senario);
    
  },
  
  watch: {
    senario: {
      handler(value) {
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
  height: 10em;
  display: flex;
  align-items: center;
  justify-content: center;
}
.map {
  height: 700px;
  margin-bottom: 30px;
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
</style>
