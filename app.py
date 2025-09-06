from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route("/")
def home():
    user = "Kevin"
    return render_template("index.html", user=user)


photos = ["goodmorning.png", "sparky.jpg", "starwars1.jpg" ]

@app.route("/gallery")
def gallery():
    image_folder = os.path.join("static", "images")
    photos = []

    # loop through all files in static/images
    for filename in os.listdir(image_folder):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
            photos.append(filename)

    return render_template("gallery.html", photos=photos)


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files.get("photo")  # safer than request.files["photo"]
        if file and file.filename != "":
            filepath = os.path.join("static/images", file.filename)
            file.save(filepath)
            return redirect(url_for("gallery"))  # go back to gallery
        else:
            return "No file selected", 400

    # This part always runs for GET requests
    return render_template("upload.html")


if __name__ == "__main__":
    app.run(debug=True)
