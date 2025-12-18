from flask import Flask, render_template, request
from datetime import datetime

from services.fortune import get_fortune
from services.curated_legends import get_curated_legends
from services.moon import get_moon_phase
from services.stars import generate_stars

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        dob_str = request.form.get("dob")
        name = request.form.get("name", "Best Human Being")

        try:
            dob = datetime.strptime(dob_str, "%Y-%m-%d")
            day = dob.day
            month = dob.month
        except:
            now = datetime.now()
            day = now.day
            month = now.month

        legends = get_curated_legends(day, month)
        fortune = get_fortune(name)
        moon = get_moon_phase(day, month)
        stars = generate_stars(day + month)

        return render_template(
            "experience.html",
            name=name,
            legends=legends,
            fortune=fortune,
            moon=moon,
            stars=stars
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
