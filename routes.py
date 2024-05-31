from flask import render_template, request
from app import app
# from app import db
# from models import User, Device, Analysis, Spectrum, Chemical, Intensity, Shift
from models_static import user_s, device_s, analysis_s_1, analysis_s_2, chemical_s_1, chemical_s_2

@app.route("/", methods=["GET", "POST"])
def dashboard():
    return render_template(
        "dashboard.html",
        user=user_s,
        device=device_s,
        analysis_1=analysis_s_1,
        analysis_2=analysis_s_2
    )
        

@app.route("/analysis/<int:id>")
def get_analysis(id):
    analysis = None

    if id == 1:
        analysis = analysis_s_1
    elif id == 2:
        analysis = analysis_s_2

    return render_template("analysis.html", analysis=analysis)

@app.route("/profile")
def profile():
    return render_template("profile.html", user=user_s)