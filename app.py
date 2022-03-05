from flask import Flask, flash, render_template, redirect, request
from flask_session import Session
import sqlite3

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["TEMPLATES_AUTO_RELOAD"] = True
Session(app)

@app.route("/")
def index():
    return(redirect("/home"))

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/posts")
def posts():
    with sqlite3.connect("example.db") as con:
            cur = con.cursor()
            cur.execute("select * from posts")
            posts = cur.fetchall()
            lengthOfPosts = len(posts)
            return render_template("posts.html", lengthOfPosts = lengthOfPosts, posts=posts)

@app.route("/create", methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        with sqlite3.connect("example.db") as con:
            cur = con.cursor()
            name = request.form.get("name").strip()
            contact = request.form.get("contact").strip()
            title = request.form.get("title").strip()
            description = request.form.get("description").strip()
            cur.execute("insert into posts (name, contact, title, description) values(?, ?, ?, ?)", (name, contact, title, description))
            con.commit()
        flash("Posted!")
        return redirect("/posts")
    return render_template("create.html")

if __name__ == "__main__":
    app.run()