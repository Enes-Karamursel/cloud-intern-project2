// const { defineConfig } = require('@vue/cli-service');
//
// module.exports = defineConfig({
//   transpileDependencies: true,
//   lintOnSave: false,
// });

const { defineConfig } = require('@vue/cli-service');

module.exports = defineConfig({
  devServer: {
    proxy: 'http://127.0.0.1:5000',
    host: 'localhost',
  },
  transpileDependencies: [
    'quasar',
  ],
  filenameHashing: true,

  pluginOptions: {
    quasar: {
      importStrategy: 'kebab',
      rtlSupport: false,
    },
  },
});
