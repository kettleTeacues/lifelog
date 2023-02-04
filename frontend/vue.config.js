const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  outputDir: process.env.VUE_OUTPUT_DIR,
  indexPath: process.env.VUE_INDEX_PATH,
  publicPath: process.env.NODE_ENV === 'production'
      ? '/static/'
      : '/static/',
  transpileDependencies: [
    'vuetify'
  ]
})
