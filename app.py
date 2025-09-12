from flask import Flask, render_template, request, redirect, url_for
import os
import time

app = Flask(__name__)

@app.route("/")
def home():
    user = "Kevin"
    return render_template("index.html", user=user)


photos = ["goodmorning.png", "sparky.jpg", "starwars1.jpg" ]

@app.route("/gallery")
def gallery():
    file_folder = os.path.join("static", "images")   # adjust if your folder is named differently
    files = os.listdir(file_folder)                  # list *all* files, no extension filter
    return render_template("gallery.html", files=files)



@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files.get("photo")
        if file and file.filename != "":
            filepath = os.path.join("static/images", file.filename)
            file.save(filepath)
            time.sleep(5) #artificial delay
            return redirect(url_for("gallery"))
        else:
            return "No file selected", 400
    return render_template("upload.html")


if __name__ == "__main__":
    app.run(debug=False)
