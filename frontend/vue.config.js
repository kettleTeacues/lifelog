const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
    outputDir: process.env.VUE_OUTPUT_DIR,
    indexPath: process.env.VUE_INDEX_PATH,
    publicPath: '/static/',
    transpileDependencies: [
        'vuetify'
    ],
    pages: {
        index: {
            entry: "src/main.js",
            title: "lifelog",
        }
    }
})
