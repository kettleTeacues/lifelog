
<template>
    <v-card
    class="mx-auto"
    max-width="400"
    tile
    >
    <v-list-item>
        <v-list-item-content>
            <v-list-item-title>
                <router-link to="/month">month</router-link>
            </v-list-item-title>
        </v-list-item-content>
    </v-list-item>
    <v-list-item>
        <v-list-item-content>
            <v-list-item-title>
                <router-link to="/week">week</router-link>
            </v-list-item-title>
        </v-list-item-content>
    </v-list-item>
    <v-list-item>
        <v-list-item-content>
            <v-list-item-title>
                <router-link to="/list">list</router-link>
            </v-list-item-title>
        </v-list-item-content>
    </v-list-item>
    <v-list-item>
        <v-list-item-content>
            <v-list-item-title>
                <router-link to="/about">about</router-link>
            </v-list-item-title>
        </v-list-item-content>
    </v-list-item>
</v-card>
</template>


<script>
export default {
    name: 'list',
    data: () => ({
    }),
}
</script>