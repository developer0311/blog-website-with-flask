from flask import Flask, render_template
import requests
import datetime




app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", year=datetime.datetime.now().year)


@app.route("/blog")
def post():
    
    response = requests.get("https://api.npoint.io/14bcfea5121bec82ac6c")
    response.raise_for_status()
    data = response.json()

    return render_template("index.html", all_blogs=data, year=datetime.datetime.now().year)

@app.route("/post/<int:index>")
def show_post(index):
    
    response = requests.get("https://api.npoint.io/14bcfea5121bec82ac6c")
    response.raise_for_status()
    data = response.json()
    post_data = (data[index-1])

    return render_template("post.html", post_data= post_data, year=datetime.datetime.now().year)






if __name__ == "__main__":
    app.run(debug=True)