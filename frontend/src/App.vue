<template>
    <v-app id="inspire">
        <v-navigation-drawer
        v-model="drawer"
        app
        >
        <sidebar />
    </v-navigation-drawer>
    
    
    <v-app-bar app>
        <v-app-bar-nav-icon v-on:click="drawer = !drawer"></v-app-bar-nav-icon>
        <v-toolbar-title>
           <a href="/" style="text-decoration: none; color: rgba(0, 0, 0, 0.87);">Lifelog</a>
        </v-toolbar-title>
    </v-app-bar>
    
    <v-main>
        <router-view />
    </v-main>
</v-app>
</template>

<script>
import sidebar from './components/sidebar';

export default {
    name: 'App',
    
    components: {
        sidebar,
    },
    data: () => ({
        drawer: '',
    }),
    mounted:() =>{
        
    }
};
</script>
