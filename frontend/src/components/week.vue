<template>
    <v-row>
        <v-col>
            <v-sheet height="700">
                <v-btn
                    outlined
                    class="mr-4"
                    color="grey darken-2"
                    @click="setToday"
                >
                    Today
                </v-btn>
                <v-btn
                    fab
                    text
                    small
                    color="grey darken-2"
                    @click="prev"
                >
                    <v-icon small>
                    mdi-chevron-left
                    </v-icon>
                </v-btn>
                <v-btn
                    fab
                    text
                    small
                    color="grey darken-2"
                    @click="next"
                >
                    <v-icon small>
                    mdi-chevron-right
                    </v-icon>
                </v-btn>
                <v-calendar
                    ref="calendar"
                    :now="today" 
                    :value="today"
                    :events="events"
                    color="primary"
                    type="week"
                ></v-calendar>
            </v-sheet>
        </v-col>
    </v-row>
</template>

<script>
import axios from 'axios'
export default {
    name: 'calendar',
    data: () => ({
        today: '2022-12-05',
        events: [
        ],
    }),
    methods: {
        async getRecords(date){
            // APIクライアント
            let api = axios.create({
                baseURL: "http://localhost:8000/",
                timeout: 5000, 
                headers: {
                    "Content-Type": "application/json",
                    'Authorization': process.env.VUE_APP_AUTH_TOKEN,
                }
            });

            // 取得api
            let response = await axios.get(
                `week/?date=${this.today}`,
                Credential=true
            ).then(function(res){
                return res
            }).catch(function(error){
                return false;
            });
            console.log(response);
            if(response.status == 200){
                this.today = date;
                this.events = response.data;
                window.history.replaceState('','',`?date=${date}`);
            } else {
                window.alert('サーバーエラーが発生しました。');
            }
        },
        setToday(){
            let today = new Date();
            this.getRecords(`${today.getFullYear()}-${today.getMonth()+1}-${today.getDate()}`);
        },
        prev(){
            let prev = new Date(this.today);
            prev.setDate(prev.getDate()-7);
            let prevStr = `${prev.getFullYear()}-${prev.getMonth()+1}-${prev.getDate()}`;
            this.getRecords(prevStr);
        },
        next(){
            let next = new Date(this.today);
            next.setDate(next.getDate()+7);
            let nextStr = `${next.getFullYear()}-${next.getMonth()+1}-${next.getDate()}`;
            this.getRecords(nextStr);
        },
    },
    mounted: async function(){
        this.$refs.calendar.scrollToTime('08:00')

        // todayを取得
        // urlパラメータを整形
        let params = window.location.search;
        params = params.replace('?','');
        params = params.split('&');

        // urlパラメータをobjに変換
        let paramsObj = {};
        params.forEach(param => {
            let arr =param.split('=');
            paramsObj[arr[0]] = arr[1];
        });
        
        // urlパラメータのdateをtodayに代入
        if(paramsObj.date){
            this.today = paramsObj.date;
        } else {
            let today = new Date();
            this.today = `${today.getFullYear()}-${today.getMonth()+1}-${today.getDate()}`;
        }

        // 取得api
        let response = await axios.get(
            `week/?date=${this.today}`,
            Credential=true
        ).then(function(res){
            return res
        }).catch(function(error){
            return false;
        });
        console.log(response);
        if(response.status == 200){
            this.events = response.data
        } else {
            window.alert('サーバーエラーが発生しました。');
        }
    },
}
</script>

<style scoped>
.my-event {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    border-radius: 2px;
    background-color: #1867c0;
    color: #ffffff;
    border: 1px solid #1867c0;
    font-size: 12px;
    padding: 3px;
    cursor: pointer;
    margin-bottom: 1px;
    left: 4px;
    margin-right: 8px;
    position: relative;
}

.my-event.with-time {
    position: absolute;
    right: 4px;
    margin-right: 0px;
}
body::-webkit-scrollbar {
  display: none;
}
</style>