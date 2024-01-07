from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [
    {"id": 1, "title": "Data Analyst", "location": "Bei Jing, China", "salary": "10 000$"},
    {"id": 2, "title": "Web Developer", "location": "Shanghai, China", "salary": "12 000$"},
    {"id": 3, "title": "Software Engineer", "location": "Hangzhou, China", "salary": "15 000$"},
    {"id": 4, "title": "UX Designer", "location": "Guangzhou, China", "salary": "13 000$"},
    {"id": 5, "title": "Network Administrator", "location": "Chengdu, China", "salary": "5 400$"}
]

@app.route("/")

def index():
    return render_template("index.html", jobs=jobs)

@app.route("/api/jobs")

def list_jobs():
    return jsonify(jobs)

if __name__ == "__main__":
    app.run()