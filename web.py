from flask import Flask, render_template

app = Flask(__name__)
#创建了网址/show/info 和 函数index的对应关系
#以后用户在浏览器上访问 /show/info，网站自动执行

@app.route("/show/info")
def index():
    return render_template("index.html")


@app.route("/get/news")
def get_news():
    return render_template("get_news.html")

@app.route("/goods/list")
def goods_list():
    return render_template("goods_list.html")

@app.route("/register")
def register():
    return render_template("register.html")


if __name__ == '__main__':
    app.run()