const path = require('path');
const webpack = require('webpack');
const dotenv = require('dotenv');

const envAPIName = "API_ENDPOINT"

const getAPIEndpoint = () => {
    if (process.env[envAPIName]) {
        return process.env[envAPIName]
    } else {
        dotenv.config();
        return process.env[envAPIName]
    }
}

module.exports = {
    entry: {
        vendor: './src/vendor.js',
        admin: './src/admin.js',
        // expression_list: './src/expression_list.js',
        blog: './src/blog.js',

    },
    output: {
        'path': path.resolve(__dirname, 'project', 'staticfiles', 'js'),
        'filename': '[name].js'
    },
    // optimization: {
    //     runtimeChunk: 'single',
    // },
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
                    test: /\.css$/,  // Procesa archivos .css
                    use: [
                    'style-loader',  // Inyecta CSS en el DOM
                    'css-loader'     // Interpreta @import y url()
                    ]
                },
                {
                    test: /\.scss$/,  // Procesa archivos .scss
                    use: [
                    'style-loader',  // Inyecta CSS en el DOM
                    'css-loader',    // Interpreta @import y url()
                    'sass-loader'    // Compila SCSS a CSS
                    ]
                },
            {
                test: /\.(png|svg|jpg|jpeg|gif)$/i,
                type: 'asset/resource',
            },
            {
                test: /\.(woff|woff2|eot|ttf|otf)$/i,
                type: 'asset/resource',
            },
        ]
    },
    plugins: [
        // new webpack.DefinePlugin({
        //   'process.env.API_ENDPOINT': JSON.stringify(getAPIEndpoint),
        // })
      ],
    resolve: {
        extensions: ['.js', '.jsx']
    },
    devServer: {
        contentBase: path.join(__dirname, 'dist'),
        compress: true,
        port: 9000
    }
}
