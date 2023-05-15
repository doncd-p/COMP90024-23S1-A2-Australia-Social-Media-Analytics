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
    <div class="map" id="map"></div>

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
      </el-form>
      <el-divider>Top Tweets</el-divider>
      <p v-for="(item, index) in mapItem.tweets" :key="item.url">
        <a :href="item.url" target="__blank">
          {{ index + 1 }}.&nbsp;{{ item.title }}
        </a>
      </p>
    </el-dialog>
  </div>
</template>

<script>
import { Loader } from "@googlemaps/js-api-loader";
import axios from "axios";

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
        divisionName: "",
        avgAge: null,
        avgEducYears: null,
        avgWeeklyIncome: null,
        erp: null,
        netMigration: null,
        tweets: [],
      },
      output: null,
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

    _func() {
      return axios
        .get(
          "http://localhost:8080/political/sentiments/avg/daterange?startdate=2022-02-09&enddate=2022-05-22&type=daily"
        )
        .then((res) => {
          return res.data;
        });
    },

    async initMap() {
      const loader = new Loader({
        apiKey: "AIzaSyA7qMWed4cLNiIl922Yy3nrZVVSASlDQJw",
        version: "weekly",
        language: "en",
      });

      const response = await this._func();
      this.output = response.data;
      console.log(this.output);

      loader.load().then(() => {
        const map = new google.maps.Map(document.getElementById("map"), {
          center: { lat: -26.2744, lng: 133.7751 },
          zoom: 4.5,
        });

        map.data.loadGeoJson(
          "http://localhost:8080/electorate/geo_data",
          null,
          () => {
            // Style the polygons
            // let that = this;
            console.log(this.output);
            map.data.setStyle((feature) => {
              console.log(feature.getProperty("divisionName")); //banks
              console.log(this.output[feature.getProperty("divisionName")]);
              const winningParty2019 = feature.getProperty("winningParty2019");
              // const sentiment =
              //   this.output[feature.getProperty("divisionName")][
              //     "avg_sentiment"
              //   ];
              // console.log(sentiment);
              let color;
              if (winningParty2019 === "LP") {
                color = "green";
              } else if (winningParty2019 === "ALP") {
                color = "red";
              } else {
                color = "grey";
              }

              return {
                fillColor: color,
                strokeWeight: 2,
              };
            });

            // Add click and mouseover listeners
            map.data.addListener("click", (event) => {
              console.log("Clicked feature: ", event.feature);
              that.mapItem.divisionName =
                event.feature.getProperty("divisionName");
              that.mapItem.avgAge = event.feature
                .getProperty("averageAge")
                .toFixed(2);
              that.mapItem.avgEducYears = event.feature
                .getProperty("averageEducationYears")
                .toFixed(2);
              that.mapItem.avgWeeklyIncome = event.feature
                .getProperty("averageWeeklyIncome")
                .toFixed(2);
              that.mapItem.erp = event.feature
                .getProperty("estimatedResidentPopulation")
                .toFixed(2);
              that.mapItem.netMigration = event.feature
                .getProperty("netMigration")
                .toFixed(2);
              // that.mapItem.tweets = event.feature.getProperty("tweets");
              that.dialogVisible = true;
            });

            // Define infowindow outside the listeners
            const infowindow = new google.maps.InfoWindow();

            map.data.addListener("mouseover", (event) => {
              infowindow.setContent(event.feature.getProperty("divisionName"));
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
