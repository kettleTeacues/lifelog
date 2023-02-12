<template>
    <v-row class="fill-height">
        <v-col>
            <v-sheet height="64">
                <v-toolbar flat>
                    <v-btn outlined class="mr-4" color="grey darken-2" @click="setToday">
                        Today
                    </v-btn>
                    <v-btn fab text small color="grey darken-2" @click="prev">
                        <v-icon small>
                            mdi-chevron-left
                        </v-icon>
                    </v-btn>
                    <v-btn fab text small color="grey darken-2" @click="next">
                        <v-icon small>
                            mdi-chevron-right
                        </v-icon>
                    </v-btn>
                    <v-toolbar-title v-if="$refs.calendar">
                        {{ $refs.calendar.title }}
                    </v-toolbar-title>
                    <v-spacer></v-spacer>
                    <v-menu bottom right>
                        <template v-slot:activator="{ on, attrs }">
                            <v-btn outlined color="grey darken-2" v-bind="attrs" v-on="on">
                                <span>{{ typeToLabel[type] }}</span>
                                <v-icon right>
                                    mdi-menu-down
                                </v-icon>
                            </v-btn>
                        </template>
                        <v-list>
                            <v-list-item @click="type = 'day'">
                                <v-list-item-title>Day</v-list-item-title>
                            </v-list-item>
                            <v-list-item @click="type = 'week'">
                                <v-list-item-title>Week</v-list-item-title>
                            </v-list-item>
                            <v-list-item @click="type = 'month'">
                                <v-list-item-title>Month</v-list-item-title>
                            </v-list-item>
                        </v-list>
                    </v-menu>
                </v-toolbar>
            </v-sheet>
            <v-sheet height="600">
                <v-calendar ref="calendar" v-model="focus" color="primary" :events="events" :event-color="getEventColor" :type="type"
                    @click:event="showEvent"
                    @click:more="viewDay"
                    @click:date="viewDay"
                    @change="updateRange">
                    <!-- 
                    <template v-slot:event="{ event, timed, eventSummary }">
                        <div class="v-event-draggable">
                        <component :is="{ render: eventSummary }"></component>
                        </div>
                        <div
                        v-if="timed"
                        class="v-event-drag-bottom"
                        @mousedown.stop="extendBottom(event)"
                        ></div>
                    </template>
                     -->
                </v-calendar>
                <v-menu v-model="selectedOpen" :close-on-content-click="false" :activator="selectedElement" offset-x min-width="350px" max-width="350px">
                    <v-card color="grey lighten-4" flat>
                        <v-toolbar :color="selectedEvent.color" dark>
                            <!--
                            <v-btn icon>
                                <v-icon>mdi-pencil</v-icon>
                            </v-btn>
                            -->
                            <v-toolbar-title v-html="selectedEvent.name"></v-toolbar-title>
                            <!--
                            <v-spacer></v-spacer>
                            <v-btn icon>
                                <v-icon>mdi-dots-vertical</v-icon>
                            </v-btn>
                            -->
                        </v-toolbar>
                        <v-card-subtitle>
                            <span v-html="selectedEvent.startStr"></span> - 
                            <span v-html="selectedEvent.endStr"></span>
                        </v-card-subtitle>
                        <v-card-text>
                            <div>detail</div>
                            <span v-html="selectedEvent.detail"></span>
                        </v-card-text>
                        <v-card-actions>
                            <v-btn text color="secondary" @click="selectedOpen = false">
                                Cancel
                            </v-btn>
                        </v-card-actions>
                    </v-card>
                </v-menu>
                <v-alert
                    v-show="debug"
                    border="right"
                    color="blue-grey"
                    dark
                >
                    {{ debugDate }}
                </v-alert>
                <v-alert
                    v-show="debug"
                    border="right"
                    color="blue-grey"
                    dark
                >
                    {{ debugConsole }}
                </v-alert>
            </v-sheet>
        </v-col>
    </v-row>
</template>

<style scoped lang="scss">
    .v-event-draggable {
    padding-left: 6px;
    }

    .v-event-drag-bottom {
    position: absolute;
    left: 0;
    right: 0;
    bottom: 4px;
    height: 4px;
    cursor: ns-resize;

    &::after {
        display: none;
        position: absolute;
        left: 50%;
        height: 4px;
        border-top: 1px solid white;
        border-bottom: 1px solid white;
        width: 16px;
        margin-left: -8px;
        opacity: 0.8;
        content: '';
    }

    &:hover::after {
        display: block;
    }
}
</style>

<script>
import axios from 'axios'
export default {
    data: () => ({
        focus: '1970-01-01',
        type: 'week',
        typeToLabel: {
            month: 'Month',
            week: 'Week',
            day: 'Day',
        },
        selectedEvent: {},
        selectedElement: null,
        selectedOpen: false,
        events: [],
        debug: false,
        debugDate:'',
        debugConsole: ''
    }),
    mounted() {
        this.$refs.calendar.checkChange()
    },
    methods: {
        viewDay({ date }) {
            this.focus = date
            this.type = 'day'
        },
        getEventColor(event) {
            return event.color
        },
        setToday() {
            this.focus = this.formatDate(new Date());
        },
        prev() {
            this.$refs.calendar.prev()
        },
        next() {
            this.$refs.calendar.next()
        },
        showEvent({ nativeEvent, event }) {
            const open = () => {
                this.selectedEvent = event;
                this.selectedElement = nativeEvent.target
                this.selectedEvent.startStr = this.formatDate(event.start, true);
                this.selectedEvent.endStr = this.formatDate(event.end, true);
                requestAnimationFrame(() => requestAnimationFrame(() => this.selectedOpen = true))
            }

            if (this.selectedOpen) {
                this.selectedOpen = false
                requestAnimationFrame(() => requestAnimationFrame(() => open()))
            } else {
                open()
            }

            nativeEvent.stopPropagation()
        },
        startDrag ({ event, timed }) {
            if (event && timed) {
                this.dragEvent = event
                this.dragTime = null
                this.extendOriginal = null
            }
        },
        startTime (tms) {
            const mouse = this.toTime(tms)

            if (this.dragEvent && this.dragTime === null) {
                const start = this.dragEvent.start

                this.dragTime = mouse - start
            }
        },
        extendBottom (event) {
            this.createEvent = event
            this.createStart = event.start
            this.extendOriginal = event.end
        },
        mouseMove (tms) {
            const mouse = this.toTime(tms)

            if (this.dragEvent && this.dragTime !== null) {
                const start = this.dragEvent.start
                const end = this.dragEvent.end
                const duration = end - start
                const newStartTime = mouse - this.dragTime
                const newStart = this.roundTime(newStartTime)
                const newEnd = newStart + duration

                this.dragEvent.start = newStart
                this.dragEvent.end = newEnd
                } else if (this.createEvent && this.createStart !== null) {
                const mouseRounded = this.roundTime(mouse, false)
                const min = Math.min(mouseRounded, this.createStart)
                const max = Math.max(mouseRounded, this.createStart)

                this.createEvent.start = min
                this.createEvent.end = max
            }
        },
        endDrag () {
            this.dragTime = null
            this.dragEvent = null
            this.createEvent = null
            this.createStart = null
            this.extendOriginal = null
        },
        cancelDrag () {
            if (this.createEvent) {
                if (this.extendOriginal) {
                    this.createEvent.end = this.extendOriginal
                } else {
                    const i = this.events.indexOf(this.createEvent)
                    if (i !== -1) {
                        this.events.splice(i, 1)
                    }
                }
            }

            this.createEvent = null
            this.createStart = null
            this.dragTime = null
            this.dragEvent = null
        },
        roundTime (time, down = true) {
            const roundTo = 15 // minutes
            const roundDownTime = roundTo * 60 * 1000

            return down
            ? time - time % roundDownTime
            : time + (roundDownTime - (time % roundDownTime))
        },
        toTime (tms) {
            return new Date(tms.year, tms.month - 1, tms.day, tms.hour, tms.minute).getTime()
        },
        rndElement (arr) {
            return arr[this.rnd(0, arr.length - 1)]
        },
        async updateRange() {
            try{
                let date = this.focus
                this.debugDate = date;

                // 取得api
                let response = await axios.get(`spanApi/?date=${date}&span=${this.type}`,{
                    'withCredentials':true
                }).then(function(res){
                    return res
                }).catch(function(error){
                    return false;
                });
                if(response.status == 200){
                    this.events = response.data.map(d=>{
                        d.start = new Date(d.start);
                        d.end = new Date(d.end);
                        d.color = 'blue';
                        d.timed = true;
                        return d;
                    });
                    this.debugConsole = response;
                    window.history.replaceState('','',`?date=${date}`);
                }
            } catch(err){
                this.debugConsole = err;
            }
        },
        rnd(a, b) {
            return Math.floor((b - a + 1) * Math.random()) + a
        },
        formatDate(date, includeTime){
            let dateStr = `${date.getFullYear()}-${('00'+(date.getMonth()+1)).slice(-2)}-${('00'+date.getDate()).slice(-2)}`
            let timeStr = `${('00'+date.getHours()).slice(-2)}:${('00'+date.getMinutes()).slice(-2)}`
            if(includeTime){
                return `${dateStr} ${timeStr}`;
            } else {
                return dateStr;
            }
        }
    },
    mounted: async function(){
        try{
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

            // debug用の制御
            if(paramsObj.debug){
                this.debug = true;
            }
            
            // urlパラメータのdateをfocusに代入
            if(paramsObj.date){
                this.focus = paramsObj.date;
                this.debugDate = paramsObj.date;
            } else {
                this.focus = this.formatDate(new Date);
                this.debugDate = this.formatDate(new Date);
            }

            // urlパラメータのspanをtypeに代入
            if(paramsObj.span){
                this.type = paramsObj.span;
            }

            // 取得api
            let response = await axios.get(`spanApi/?date=${this.focus}&span=${this.type}`,{
                'withCredentials':true
            }).then(function(res){
                return res
            }).catch(function(error){
                return false;
            });
            if(response.status == 200){
                this.events = response.data.map(d=>{
                    d.start = new Date(d.start);
                    d.end = new Date(d.end);
                    d.color = 'blue';
                    d.timed = true;
                    return d;
                });
                this.debugConsole = response;
            }
        } catch(err) {
            this.debugConsole = err;
        }
    },
}
</script>