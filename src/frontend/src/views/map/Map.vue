<template>
    <div class="container">
        <!-- option -->
        <el-row class="option" :gutter="2">
            <el-col :span="10">
                <div class="label-text">Senario:</div>
                <el-radio-group v-model="senario" class="radio-container">
                    <el-radio-button label="vote" >Percentage of votes</el-radio-button>
                    <el-radio-button label="sentiment">&nbsp;&nbsp;&nbsp;Sentiment&nbsp;&nbsp;&nbsp;</el-radio-button><br/> 
                    <el-radio-button label="tweets">Number of Tweets</el-radio-button>
                    <el-radio-button label="status">Changed Status</el-radio-button>
                </el-radio-group>
            </el-col>
            <el-col :span="6">
                <div class="party">
                    <div class="label-text" >Govering Party:</div>
                    <div class="party-text">{{party}}</div>
                </div>
            </el-col>
            <el-col :span="8"><div class="label-text">Time:</div>
                <div class="time">
                 <el-radio-group v-model="time" :change="handleClick()">
                    <el-radio label="pre" border >&nbsp;&nbsp;&nbsp;&nbsp;pre-election&nbsp;&nbsp;&nbsp;&nbsp;</el-radio>
                    <el-radio label="post" border>&nbsp;&nbsp;&nbsp;post-election&nbsp;&nbsp;&nbsp;</el-radio>
                </el-radio-group>
                   
                </div>
            </el-col>
        </el-row>

        <!-- map -->
        <el-row class="map">nihao</el-row>
    </div>
</template>

<script>

export default {
    name: 'Map',
    props: {
        msg: String
    },
    data() {
        return {
            senario: 'vote',
            time:'pre',
            data: [],
            map: null,
            mapData: null,
            party: 'Libera'
        };
    },
    methods: {
        handleClick() {
            if (this.time === 'pre' ){
                this.party = 'LP'
            }else{
                this.party = 'ALP'
            }
        }
    },
    mounted() {
        
    }
}
</script>

<style scoped>
    .container{
        height: 100%;
        width:100%;
        background-color: #232838;
        opacity: 0.9;
    }
    .option{
        width:100%;
        height:10em;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .map{
        height:50em;
        background-color: green;
    }
    .radio-container{
        width: 100%;
        height: 100%;
        display: flex;
        justify-content: center;
    }
    .label-text{
        font-weight: 800;
        font-size: 24px;
        margin-bottom: 15px;
        margin-left:30px;
        color: #ffd04b;
    }
    .time{
        display: flex;
        justify-content: center;
    }
    .party{
        height: 100px;
        width:100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        border:0.2em solid #ffd04b;
        border-radius: 2em;
    }
    .party-text{
        display: flex;
        justify-content: center;
        font-weight: 400;
        font-size: 20px;
        color: #fff;
    }
</style>
