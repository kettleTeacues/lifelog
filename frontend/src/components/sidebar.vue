
<template>
    <v-card
    class="mx-auto"
    max-width="400"
    tile
    >
        <v-list-item>
            <v-list-item-content>
                <v-list-item-title>
                    <router-link to="/" style="text-decoration: none;">calendar</router-link>
                </v-list-item-title>
            </v-list-item-content>
        </v-list-item>
        <v-list-item>
            <v-list-item-content>
                <v-list-item-title>
                    <router-link to="/list" style="text-decoration: none;">list</router-link>
                </v-list-item-title>
            </v-list-item-content>
        </v-list-item>
        <v-list-item>
            <v-list-item-content>
                <v-list-item-title>
                    <router-link to="/about" style="text-decoration: none;">about</router-link>
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