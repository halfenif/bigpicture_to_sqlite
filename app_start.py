from flask import Flask, render_template, request
import db_article_list
import db_item_list
import db_item_image

app = Flask(__name__)

@app.route("/")
def article_list():
    return render_template('article_list.html', articles=db_article_list.selectArticle())

@app.route("/item_list")
def item_image_list():
    return render_template('item_list.html', items=db_item_list.selectItem(request.args.get("seq")))

@app.route("/item_image")
def item_image():
    pseq = request.args.get("pseq")
    seq = request.args.get("seq")
    return render_template('item_image.html', item=db_item_image.selectItem(pseq, seq))

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
