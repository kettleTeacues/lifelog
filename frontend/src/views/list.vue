<template>
    <v-data-table
        :headers="headers"
        :items="events"
        :items-per-page="5"
        class="elevation-1"
    ></v-data-table>
</template>

<script>
export default {
    data () {
        return {
            headers: [
                { text: 'index', value: 'index' },
                { text: 'start_date', value: 'start_date' },
                { text: 'end_date', value: 'end_date' },
                { text: 'event', value: 'event' },
            ],
            events: [
            ],
        }
    },
}
</script>