const path = require("path");

module.exports = {
    mode: "development",
    entry: "./renderer.js", // Your entry file
    output: {
        path: path.resolve(__dirname, "dist"),
        filename: "renderer.bundle.js",
    },
    watch: true,
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader",
                    options: {
                        presets: ["@babel/preset-env", "@babel/preset-react"],
                    },
                },
            },
            {
                test: /\.css$/, // ✅ Add CSS loader
                use: ["style-loader", "css-loader"],
            },
        ],
    },
    resolve: {
        extensions: [".js", ".jsx"],
    },
};
