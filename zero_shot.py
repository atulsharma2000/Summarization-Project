import base64
from io import BytesIO
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask, render_template, Response
from transformers import pipeline
import torch  # Added import

app = Flask(__name__)

model_name = "facebook/bart-large-mnli"
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

def load_model(device):
    return pipeline("zero-shot-classification", model=model_name, device=device)

news_sentiment_analysis = load_model(device)
sentiment_list = ["positive", "negative", "neutral", "joy", "sadness", "anger", "fear", "trust"]

def generate_plot(article_str):
    try:
        analysis_output = news_sentiment_analysis(article_str, candidate_labels=sentiment_list, multi_label=True)
        sentiments = {emotion: score for emotion, score in zip(analysis_output['labels'], analysis_output['scores'])}
        
        df_sentiments = pd.DataFrame(sentiments.items(), columns=['Emotion', 'Score'])
        
        plt.figure(figsize=(10, 6))
        sns.set_theme(style="whitegrid")
        sns.set_palette("husl")
        
        bar_plot = sns.barplot(x='Emotion', y='Score', data=df_sentiments)
        
        plt.title('Sentiment Analysis', fontsize=16, fontweight='bold')
        plt.xlabel('Emotion', fontsize=14)
        plt.ylabel('Score', fontsize=14)
        
        for index, row in df_sentiments.iterrows():
            plt.text(index, row['Score'], round(row['Score'], 2), color='black', ha="center")
        
        plt.xticks(rotation=45)
        sns.despine()

        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close()
        
        return base64.b64encode(buf.getvalue()).decode('ascii')
    except Exception as e:
        print(f"Error during plotting: {e}")
        return None

@app.route("/")
def index():
    article_str = "The incident took place when Kejriwal, with Greater Kailash MLA and Delhi minister Saurabh Bharadwaj, was walking in a narrow lane, greeting people. Police personnel had controlled the crowd by placing a rope on both sides of the two leaders."  # Consider dynamic input here
    plot_data = generate_plot(article_str)
    return render_template("index.html", plot_data=plot_data)

if __name__ == "__main__":
    app.run(debug=True)