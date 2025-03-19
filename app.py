
from flask import Flask,render_template,request
import sqlite3
import requests
import praw
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

conn=sqlite3.connect('C:/Users/Steve Aaron Dmello/.vscode/myprojects/.venv/ideas/history.db',check_same_thread=False)
db=conn.cursor()
db.execute("CREATE TABLE IF NOT EXISTS stocks (id INTEGER PRIMARY KEY AUTOINCREMENT,company TEXT,sentiment TEXT,date DATETIME  DEFAULT CURRENT_DATE,time DATETIME DEFAULT CURRENT_TIME)")
conn.commit()
APIKEY="6b4d833dbf43489c9686bace8ddbfea9"

reddit = praw.Reddit(
    client_id="DlLfFGngV38Rq-QnnasKxw",
    client_secret="hCS5gsMsOFXZg93Yp3x1P2hS_d1ICQ",
    user_agent="Finler/1.0"
)

app = Flask(__name__)

@app.route('/')
def home():
    infos=db.execute("SELECT * FROM stocks").fetchall()
    print(infos)

    return render_template('home.html',infos=infos)

@app.route('/search', methods=['GET', 'POST'])    
def search():

    try:
        stock=request.form.get('search') 
        if not stock:
            stock=request.args.get('search')
        
    except AttributeError or not stock:
        return render_template('Apology.html',apology='Please enter a valid Company name')
    stock=stock.lower()
    url = f"https://newsapi.org/v2/everything?q={stock}&language=en&sortBy=publishedAt&apiKey={APIKEY}"
    sia=SentimentIntensityAnalyzer()

    subreddit = reddit.subreddit("StockMarket")
    redtitles = []
    redurls=[]
    i=0
    for post in subreddit.hot(limit=100):
        if stock in post.title.lower() and i<4:
            redtitles.append(post.title)
            redurls.append(post.url)
            i+=1

    red_score=sia.polarity_scores(str(redtitles))
    red_score=red_score['compound']  

    news=requests.get(url).json()
    newsscores=[]
    newstitles=[]
    for article in news['articles'][:5]:
        newstitles.append(article['title'])
    newsscores=sia.polarity_scores(str(newstitles))
    newsscores=newsscores['compound']
    if (newsscores+red_score)/2>0:
        sentiment="Positive"
    elif (newsscores+red_score)/2<0:
        sentiment="Negative"
    else:
        sentiment="Neutral"
    print(sentiment,stock)

    db.execute("INSERT INTO stocks (company,sentiment) VALUES (?,?)",(stock.upper(),sentiment)) 
    conn.commit()             
    return render_template('search.html',redurls=redurls,redtitles=redtitles,stock=stock,redscore=red_score,news=news['articles'][:5],newsscore=newsscores,i=i)
