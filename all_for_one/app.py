from flask import Flask, render_template, request, jsonify, url_for
import mysql.connector
from transformers import pipeline
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

app = Flask(__name__)

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost", user="root", password="manager", database="news_db"
)

# Initialize Hugging Face summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Include your scraping logic here or import from indianExpress.py


@app.route("/")
def index():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM news ORDER BY id DESC LIMIT 25")
    results = mycursor.fetchall()
    return render_template("index.html", news=results)


# Other routes...

if __name__ == "__main__":
    app.run(debug=True)
