<template>
  <div
    id="app"
    style="height: 120vh"
    v-loading="loading"
    element-loading-text="loading..."
    element-loading-spinner="el-icon-loading"
    element-loading-background="rgba(0, 0, 0, 0.8)"
  >
    <el-col :span="24" class="chart">
      <el-row class="figurerow1">
        <!-- figure1 -->
        <el-col class="figureitem1" :span="20">
          <div class="tablelabel3" style="margin-left: 10px">
            Census Data Trends on Tweets Data
          </div>
          <div class="ch">
            <img
              :src="img_src"
              style="
                max-width: 100%;
                max-height: 100%;
                height: auto;
                width: auto;
              "
            />
          </div>
        </el-col>
        <el-col class="filter" :span="4">
          <el-row>
            <div class="filter1">
              <div class="filter1label">Cencus Data:</div>
              <el-select v-model="cencus">
                <el-option
                  v-for="item in options1"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                >
                </el-option>
              </el-select>
            </div>
          </el-row>
          <el-row>
            <div class="filter1">
              <div class="filter1label">Election:</div>
              <el-select v-model="election">
                <el-option
                  v-for="item in options2"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                >
                </el-option>
              </el-select>
            </div>
          </el-row>
        </el-col>
      </el-row>
      <el-row class="tablerow3">
        <!-- table1 -->
        <el-col class="tablebody3" :span="20">
          <div class="tablelabel3">Tweets vs Toots</div>
          <table>
            <tr>
              <th style="width: 44%; height: 25%"></th>
              <th style="width: 28%; height: 25%">Tweet</th>
              <th style="width: 28%; height: 25%">Toots</th>
            </tr>
            <tr>
              <td>Total number of political posts/partial matched posts</td>
              <td>{{ tweets_political }}</td>
              <td>{{ toots_political }}</td>
            </tr>
            <tr>
              <td>Total number of posts</td>
              <td>{{ tweets_total }}</td>
              <td>{{ toots_total }}</td>
            </tr>
            <tr>
              <td>Percentage of political posts/partiao matched posts</td>
              <td>{{ tweets_rate.toFixed(4) }}</td>
              <td>{{ toots_rate.toFixed(4) }}</td>
            </tr>
          </table>
        </el-col>
        <el-col class="filter" :span="4"> </el-col>
      </el-row>
    </el-col>
  </div>
</template>
<script>
export default {
  name: "comparison",
  data() {
    return {
      loading: true,
      img_src: "",
      //table1 filter1
      options1: [
        {
          value: "migration",
          label: "Migration",
        },
        {
          value: "age",
          label: "Age of Voters",
        },
        {
          value: "income",
          label: "Weekly Income",
        },
        {
          value: "education",
          label: "Education Level",
        },
      ],
      cencus: "migration",
      options2: [
        {
          value: "2019percentage",
          label: "Percentage of Support in 2019",
        },
        {
          value: "2022percentage",
          label: "Percentage of Support in 2022",
        },
        {
          value: "sentiment",
          label: "Sentiment",
        },
        {
          value: "status",
          label: "Change Status",
        },
      ],
      election: "2019percentage",
      tweets_political: 0,
      tweets_total: 0,
      tweets_rate: 0,
      toots_political: 0,
      toots_total: 0,
      toots_rate: 0,
    };
  },
  created() {
    this.updateFigure();
    this.getData();
  },
  mounted() {
    let timer = setInterval(() => {
      this.getData(timer);
    }, 10000);
  },
  watch: {
    cencus: {
      handler(value) {
        this.updateFigure();
      },
      deep: true,
    },
    election: {
      handler(value) {
        this.updateFigure();
      },
      deep: true,
    },
  },

  methods: {
    updateFigure() {
      this.img_src = require("../../assets/images/" +
        this.cencus +
        "_" +
        this.election +
        ".png");
    },
    getData() {
      setTimeout(() => {
        this.loading = true;
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
            this.loading = false;
          });
      }, 0);
    },
  },
};
</script>
<style>
.el-menu-vertical-demo {
  height: 100vh;
}
.figurerow1 {
  height: 85vh;
  display: flex;
  background-color: #5f4848;
  justify-content: center;
  align-items: center;
  border-bottom: 0.1em solid #fff;
}
.figureitem1 {
  height: 80%;
  width: 65%;
  border: 0.5em solid #cb7f67;
  background-color: #fff;
  padding: 10px;
}
.ch {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: calc(100% - 40px);
  overflow: hidden;
}
.filter1 {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.filter1label {
  color: #cb7f67;
  font-weight: 600;
  font-size: 20px;
  margin-bottom: 10px;
}
.scatter {
  height: 95%;
  width: 98%;
}

.tablerow3 {
  height: 35vh;
  display: flex;
  background-color: #444a5b;
  justify-content: center;
  align-items: center;
  border-bottom: 0.1em solid #fff;
}
.tablebody3 {
  height: 80%;
  width: 65%;
  border: 0.5em solid #cb7f67;
  background-color: #fff;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  padding: 10px;
}
.tablelabel3 {
  font-size: 24px;
  font-weight: 500;
  margin-left: 10px;
  color: #666;
  margin-bottom: 15px;
}

.filter {
  margin-left: 100px;
}
.filter1 {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin: 20px;
}

.filter1label {
  color: #cb7f67;
  font-weight: 600;
  font-size: 20px;
  margin-bottom: 10px;
}

td,
th {
  border: 1px solid #dddddd;
  padding: 8px;
  text-align: center;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
