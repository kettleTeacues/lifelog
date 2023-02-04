const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  outputDir: process.env.VUE_OUTPUT_DIR,
  transpileDependencies: [
    'vuetify'
  ]
})
