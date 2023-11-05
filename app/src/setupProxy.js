const { createProxyMiddleware } = require("http-proxy-middleware")

var target = "http://127.0.0.1:8080"

console.log("PROXY TARGET", target)

module.exports = function (app) {
    app.use(
        "/api",
        createProxyMiddleware({ target: target, changeOrigin: true })
    )
}
