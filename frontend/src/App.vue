<template>
  <v-app id="inspire">
      <v-navigation-drawer
          v-model="drawer"
          app
      >
      <list />
      </v-navigation-drawer>


      <v-app-bar app>
          <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
          <v-toolbar-title>
              Lifelog
          </v-toolbar-title>
      </v-app-bar>


      <v-main>
          <week />
      </v-main>
  </v-app>
</template>

<script>
import list from './components/list';
import week from './components/week';
import month from './components/month';

export default {
  name: 'App',
  
  components: {
      list,
      week,
      month,
  },
  data: () => ({
      drawer: '',
   }),
};
</script>
