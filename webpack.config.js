// const path = require("path");

// module.exports = {
//     mode: "development",
//     entry: "./renderer.js", // Your entry file
//     output: {
//         path: path.resolve(__dirname, "dist"),
//         filename: "renderer.bundle.js",
//     },
//     module: {
//         rules: [
//             {
//                 test: /\.(js|jsx)$/,
//                 exclude: /node_modules/,
//                 use: {
//                     loader: "babel-loader",
//                     options: {
//                         presets: ["@babel/preset-env", "@babel/preset-react"],
//                     },
//                 },
//             },
//             {
//                 test: /\.css$/, // ✅ Add CSS loader
//                 use: ["style-loader", "css-loader"],
//             },
//         ],
//     },
//     resolve: {
//         extensions: [".js", ".jsx"],
//     },
// };

const path = require('path');
const { Generator } = require('webpack');

module.exports = {
  // Look for your actual main JS file
  entry: './welcome.js', // Adjust this to match your actual main JS file location
  output: {
    path: path.resolve(__dirname, 'build'),
    filename: 'bundle.js',
    publicPath: '/'
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env', '@babel/preset-react']
          }
        }
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader']
      },
      // Add support for image files
      {
        test: /\.(png|jpe?g|gif)$/i,
        type: 'asset/resource',
        generator : {
            filename : 'images/[hash][ext][query]'
        }
      }
    ]
  },
  resolve: {
    extensions: ['.js', '.jsx']
  },
  target: 'electron-renderer'
};