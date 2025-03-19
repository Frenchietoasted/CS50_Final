# FINLER
#### [FINLER-URL]()
#### DESCRIPTION:
For my final project I have decided to make a webapp **Finler**. Finler is an app that conducts an analysis on the current market sentiments and trends of any stock in the world. It scours the internet through a news 
api to analyse professional opinion, and Reddit to get the people's opinion as well.

It is somewhat of a spiritual successor to week 9's finance problem. But since this is simply a tracker with no personal information involved, I decided to do away with the login and user id processes. The website 
is extremely simple to use with a navigation bar on top to search for a given company and it will display the top related news articles as well as the top reddit posts regarding that comapany and it will automatically 
evaluate the current market sentiment or outlook regarding that company which can help prospective investors make decisions regarding investing or staying away from that particular stock.The home page contains the 
history of all the previously viewed companies.

## TECHNICAL ASPECTS:
The webapp was made using html, python(flask), sqlite3 and bootstrap's css and it's icon was drawn by me using MS paint.
### HTML File List:
1. layout.html
2. home.html
3. search.html
4. apology.html

#### 1.layout.html
It contains all of the basic layout for the whole website. Using bootstrap I was able to implement dark mode(for aesthetic reasons) and also the navbar with an inbuilt search bar.
#### 2.home.html
It is used to display the home page of **Finler**.The home page contains a welcome message and a table displaying the recent searches. It is integrated with an **sqlite3** db and hence will store data even after the 
site is closed and reopened
#### 3.search.html
Searches / Queries for the company entered in the home search box and displays the top results, 5 top news articles and 5 top reddit posts. It makes use of the card component from bootstrap to display the news snippets
. In the end it displays the sentiment analyses of the given stock based on the internet's opinions.
#### 4.apology.html
Displays error messages in case of any invalid cases.  
### Database:
The database **history.db** stores data in the table stocks regarding company name, market sentiment(positive,negative or neutral) and the date and time of the last check.
### app.py
The main application for the backend of the site. The header files used and their purpose:
* flask - For the basic flask functionality
* sqlite3 - For hooking up the sql database and querying
* requests - To use the newsapi
* praw - To use the reddit api
* ntlk,ntlk.sentiment - To use vader sentiment analyser
app.py first begins with a couple of initializations for vader, sqlite, newsapi and for the reddit api.  
### The two routes implemented in app.py are:
* / - where home is rendered
* /search - where search is rendered
## Features
* Fetches stock-related news articles using NewsAPI.
* Extracts relevant Reddit discussions from r/StockMarket.
* Analyzes sentiment using VADER SentimentIntensityAnalyzer.
* Stores analyzed stock sentiment in an SQLite database.
## Code Explanation
1. Home Route (/)
  - Retrieves all stock sentiment records from the database.
  - Displays them on the home page.
2. Search Route (/search)
    1. Get Search Query:
        * Reads user input from an HTML form (request.form.get('search')).
        * If missing, it tries to get it from the query string (request.args.get('search')) (This happens when you click on the embedded links in home).
        * If no valid stock name is provided, an apology page is rendered.
    2. Fetch News using url & Reddit Data using praw functionality:
        * Calls NewsAPI to fetch stock-related articles (limits 5).
        * Searches the r/StockMarket subreddit for relevant discussions (limits 5).
    3. Perform Sentiment Analysis:
        * Uses VADER to analyze sentiment of news and Reddit titles.
        * Determines whether the sentiment is Positive, Negative, or Neutral.
    4. Store in Database:
        * Saves the company name and sentiment in an SQLite database.
        * Commits the transaction to save data.
## About VADER

VADER (Valence Aware Dictionary and sEntiment Reasoner) is a sentiment analysis tool that specializes in analyzing text from social media and short sentences. It assigns scores for positive, negative, and neutral
sentiments, along with a compound score that represents the overall sentiment. VADER uses a lexicon-based approach and is particularly effective at handling slang, emojis, and punctuation emphasis. It is widely 
used in applications that require fast and accurate sentiment classification, such as stock market analysis and social media monitoring. Since VADER is rule-based and does not require training data, it is efficient
and easy to integrate into various projects.

This project provides insights into public sentiment regarding stocks, helping users gauge market trends.


