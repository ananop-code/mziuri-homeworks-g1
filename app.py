from flask import Flask, render_template

app = Flask(__name__)

years = [
    {"id": 1, "GEO_history": "Vakhtang I Gorgasali", "name": "449_502-", "img": "Vakhtang I Gorgasali.jpg",
     "link": "https://en.wikipedia.org/wiki/Vakhtang_I"},
    {"id": 2, "GEO_history": "Tamar Mefe", "name": "1184_1213-", "img": "Tamar Mefe.jpg",
     "link": "https://ka.wikipedia.org/wiki/%E1%83%97%E1%83%90%E1%83%9B%E1%83%90%E1%83%A0_%E1%83%9B%E1%83%94%E1%83%A4%E1%83%94"},
    {"id": 3, "GEO_history": "Heraclius II", "name": "1744_1762-", "img": "Heraclius II.jpg",
     "link": "https://en.wikipedia.org/wiki/Heraclius_II_of_Georgia"},
    {"id": 4, "GEO_history": "Dmanisi hominins", "name": "million years ago", "img": "Dmanisi hominins.jpg",
     "link": "https://en.wikipedia.org/wiki/Dmanisi_hominins"},
    {"id": 5, "GEO_history": "Giorgi II", "name": "1072_1089", "img": "George II.jpg",
     "link": "https://en.wikipedia.org/wiki/George_II_of_Georgia"}
]


@app.route("/")
def home():
    return render_template("index.html", years=years)  # HTML-ისთვის ცვლადის გადაცემა


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/years/<int:history_id>")
def view_movie_details(history_id):
    for year in years:
        if year["id"] == history_id:
            return render_template("history_details.html", year=year)
    return "information Not Found"


app.run(
    debug=True)
