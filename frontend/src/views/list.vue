<template>
    <div>
        <div class="text-center pt-2">
            <v-pagination
                v-model="page"
                :length="pageCount"
                :total-Visible=10
                @input="getList"
            ></v-pagination>
        </div>
        <v-data-table
            :headers="headers"
            :items="events"
            :page.sync="page"
            :items-per-page="itemsPerPage"
            hide-default-footer
            class="elevation-1"
        ></v-data-table>
        <div class="text-center pt-2">
            <v-pagination
                v-model="page"
                :length="pageCount"
                :total-Visible=10
                @input="getList"
            ></v-pagination>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    data:()=>({
        page: 1,
        pageCount: 0,
        itemsPerPage: 100,
        headers: [
            { text: 'index', value: 'id' },
            { text: 'start', value: 'start_datetime' },
            { text: 'end', value: 'end_datetime' },
            { text: 'event', value: 'event' },
        ],
        events: [
        ],
    }),
    methods:{
        getList: async function(){
            // 取得api
            let response = await axios.get(`listApi/?page=${this.page}`,{
                'withCredentials':true
            }).then(function(res){
                return res
            }).catch(function(error){
                return false;
            });
            
            if(response.status == 200){
                this.events = response.data.results;
                return;
            } else {
                this.message = 'error'
                return;
            }
        }
    },
    mounted: async function(){
        // 取得api
        let response = await axios.get(`listApi/`,{
            'withCredentials':true
        }).then(function(res){
            return res
        }).catch(function(error){
            return false;
        });
        
        if(response.status == 200){
            this.events = response.data.results;
            this.pageCount = Math.ceil(response.data.count / this.itemsPerPage);
            return;
        } else {
            this.message = 'error'
            return;
        }
    }
}
</script>