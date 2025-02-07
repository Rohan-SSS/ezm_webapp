from flask import Flask, render_template
from data.get_data import *
from news.get_news import *

app = Flask(__name__, template_folder='./templates')

@app.route('/')
@app.route('/dashboard')
def index():
    custom_data = generate_custom_data()
    macd_data = generate_macd()
    srsi_data = get_stochastic_rsi()
    return render_template('index.html', custom_data=custom_data, macd_data=macd_data, srsi_data=srsi_data)

@app.route('/model_specification')
def model_preformance():
    custom_data = generate_custom_data()
    macd_data = generate_macd()
    srsi_data = get_stochastic_rsi()
    return render_template('model_specification.html', custom_data=custom_data, macd_data=macd_data, srsi_data=srsi_data)

@app.route('/news_sentiment')
def news_sentiment():
    news_data = get_news()
    return render_template('news_sentiment.html', news_data=news_data)

@app.route('/model_specification/eurusd')
def eurusd():

    return render_template('model_perf/eurusd.html')