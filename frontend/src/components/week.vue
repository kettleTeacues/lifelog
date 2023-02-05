<template>
    <v-row>
        <v-col>
            <v-sheet height="800">
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
    mounted: async function(){
        this.$refs.calendar.scrollToTime('08:00')

        // APIクライアント
        const api = axios.create({
            baseURL: "http://localhost:8000/",
            timeout: 5000, 
            headers: {
                "Content-Type": "application/json",
                'Authorization': process.env.VUE_APP_AUTH_TOKEN,
            }
        });

        // 取得api
        let response = await api.request({
            method: 'get',
            url: `week/?date=${this.today}`,
        }).then(function(res){
            return res
        }).catch(function(error){
            return false;
        });
        console.log(response);
        if(response.status == 200){
            response.data.forEach(record => {
                let sta = new Date(record.start_datetime)
                let end = new Date(record.end_datetime)
                this.events.push({
                    name: record.event,
                    start: record.start,
                    end: record.end,
                })
            });
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
</style>