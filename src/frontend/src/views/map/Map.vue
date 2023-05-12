<template>
  <div class="container">
    <!-- option -->
    <el-row class="option" :gutter="2">
      <el-col :span="10">
        <div class="label-text">Senario:</div>
        <el-radio-group v-model="senario" class="radio-container">
          <el-radio-button label="vote">Percentage of votes</el-radio-button>
          <el-radio-button label="sentiment"
            >&nbsp;&nbsp;&nbsp;Sentiment&nbsp;&nbsp;&nbsp;</el-radio-button
          ><br />
          <el-radio-button label="tweets">Number of Tweets</el-radio-button>
          <el-radio-button label="status">Changed Status</el-radio-button>
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
          <el-radio-group v-model="time" :change="handleClick()">
            <el-radio label="pre" border
              >&nbsp;&nbsp;&nbsp;&nbsp;pre-election&nbsp;&nbsp;&nbsp;&nbsp;</el-radio
            >
            <el-radio label="post" border
              >&nbsp;&nbsp;&nbsp;post-election&nbsp;&nbsp;&nbsp;</el-radio
            >
          </el-radio-group>
        </div>
      </el-col>
    </el-row>

    <div style="width: 100%; text-align: center; color: #fff; margin: 10px 0;">
        <div style="height: 20px; width: 30%; background: linear-gradient(to right, yellow, red);"></div>
    </div>

    <!-- map -->
    <div class="map" id="map"></div>

    <el-dialog
      :title="mapItem.divisionName"
      :visible.sync="dialogVisible"
      :append-to-body="true"
      width="50%"
      :before-close="handleClose"
    >
        <el-form label-width="150px" label-position="left">
            <el-form-item label="avgAge: ">
                {{ mapItem.avgAge }}
            </el-form-item>
            <el-form-item label="avgEducYears: ">
                {{ mapItem.avgEducYears }}
            </el-form-item>
            <el-form-item label="avgWeeklyIncome: ">
                {{ mapItem.avgWeeklyIncome }}
            </el-form-item>
            <el-form-item label="erp: ">
                {{ mapItem.erp }}
            </el-form-item>
            <el-form-item label="netMigration: ">
                {{ mapItem.netMigration }}
            </el-form-item>
        </el-form>
        <el-divider>tweets</el-divider>
        <p v-for="(item, index) in mapItem.tweets" :key="item.url">
            <a :href="item.url" target="__blank"  >
                {{ index + 1 }}.&nbsp;{{ item.title }}
            </a>
        </p>
        
    </el-dialog>
  </div>
</template>

<script>
import { Loader } from "@googlemaps/js-api-loader";

export default {
  name: "Map",

  props: {
    msg: String,
  },
  data() {
    return {
      senario: "vote",
      time: "pre",
      data: [],
      map: null,
      mapData: null,
      party: "Libera",
      map: {},
      dialogVisible: false,
      mapItem: {
        divisionName: undefined,
        avgAge: undefined,
        avgEducYears: undefined,
        avgWeeklyIncome: undefined,
        erp: undefined,
        netMigration: undefined,
        tweets: []
      },
    };
  },
  methods: {
    handleClick() {
      if (this.time === "pre") {
        this.party = "LP";
      } else {
        this.party = "ALP";
      }
    },
    handleClose() {
      this.dialogVisible = false;
    },
    initMap() {
      const loader = new Loader({
        apiKey: "AIzaSyA7qMWed4cLNiIl922Yy3nrZVVSASlDQJw",
        version: "weekly",
        language: 'en'
      });

      const mapData = [
        // displayed data
        {
          divisionName: "Banks",
          avgAge: 44.34516963142491,
          avgEducYears: 10.395970873626483,
          avgWeeklyIncome: 1724.3859379956157,
          erp: 246738.93,
          netMigration: -3036.45,
          tweets: [
            {
                url: "https://www.baidu.com",
                title: "Jamie Dimon’s Surprising New Move: Bailing Out First Republic Bank"
            },
            {
                url: "https://www.baidu.com",
                title: "His immediate concern is that the internet will be flooded with false photos, videos and text, and the average person will ‘not be able to know what is true anymore"
            },
            {
                url: "https://www.baidu.com",
                title: "A little bit of this and a little bit of that.No affiliation with Twitter the company.",
            },
            {
                url: "https://www.baidu.com",
                title: "ESG Investing: A Beginner’s Guide to #Investing in a Sustainable Future",
            },
            {
                url: "https://www.baidu.com",
                title: "Well I guess that's how to fell alive!"
            },
          ],
          
          color: "#67C23A",
          // lat and lng of polygon
          polygon: [
            { lat: 25.774, lng: -80.19 },
            { lat: 18.466, lng: -66.118 },
            { lat: 32.321, lng: -64.757 },
            { lat: 29.774, lng: -80.19 },
            { lat: 25.774, lng: -80.19 },
          ],
        },
        {
          divisionName: "Revers",
          avgAge: 44.34516963142491,
          avgEducYears: 10.395970873626483,
          avgWeeklyIncome: 1724.3859379956157,
          erp: 246738.93,
          netMigration: -3036.45,
          tweets: [
            {
                url: "https://www.baidu.com",
                title: "Jamie Dimon’s Surprising New Move: Bailing Out First Republic Bank"
            },
            {
                url: "https://www.baidu.com",
                title: "His immediate concern is that the internet will be flooded with false photos, videos and text, and the average person will ‘not be able to know what is true anymore"
            },
            {
                url: "https://www.baidu.com",
                title: "A little bit of this and a little bit of that.No affiliation with Twitter the company.",
            },
            {
                url: "https://www.baidu.com",
                title: "ESG Investing: A Beginner’s Guide to #Investing in a Sustainable Future",
            },
            {
                url: "https://www.baidu.com",
                title: "Well I guess that's how to fell alive!"
            },
          ],
          color: "#FF0000",
          polygon: [
            { lat: 27.774, lng: -83.19 },
            { lat: 20.466, lng: -69.118 },
            { lat: 34.321, lng: -67.757 },
            { lat: 31.774, lng: -83.19 },
            { lat: 27.774, lng: -83.19 },
          ],
        },
      ];

      loader.load().then(() => {
        const map = new google.maps.Map(document.getElementById("map"), {
          center: { lat: 24.886, lng: -70.268 },
          zoom: 5,
        });

        mapData.forEach((item, i) => {
          // define the parameters of polygon
          const itemPolygon = new google.maps.Polygon({
            paths: item.polygon,
            strokeColor: item.color,
            strokeOpacity: 0.8,
            strokeWeight: 2,
            fillColor: item.color,
            fillOpacity: 0.35,
          });

          itemPolygon.addListener("click", () => {
            this.mapItem.divisionName = item.divisionName;
            this.mapItem.avgAge = item.avgAge;
            this.mapItem.avgEducYears = item.avgEducYears;
            this.mapItem.avgWeeklyIncome = item.avgWeeklyIncome;
            this.mapItem.erp = item.erp;
            this.mapItem.netMigration = item.netMigration;
            this.mapItem.tweets = item.tweets;
            this.dialogVisible = true;
          });
          const infowindow = new google.maps.InfoWindow({
            content: item.divisionName,
          });
            
          itemPolygon.addListener("mouseover",  (event) => {
            infowindow.setPosition(event.latLng);
            infowindow.open(map, itemPolygon);
          });
          itemPolygon.addListener('mouseout', () => {
            map.data.revertStyle();
            infowindow.close();
          });
          // draw polygons in the map
          itemPolygon.setMap(map);
        });
      });
    },
  },
  mounted() {
    this.initMap();
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
