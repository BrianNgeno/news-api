from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_new,get_from_new,get_articles


@main.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    #getting sports news
    sports_news = get_from_new('sports')
    general_news = get_from_new('general')
    business_news = get_from_new('business')
    entertainment_news = get_from_new('entertainment')
    technology_news = get_from_new('technology')
    science_news = get_from_new('science')

    title = 'Welcome to the best Online News Highlight application'
    return render_template('index.html',title=title,sports=sports_news,general=general_news,business=business_news,entertainment=entertainment_news,technology=technology_news,science=science_news)


@main.route('/news/<string:id>')
def news(id):
    '''
    Shows
    '''

    news = get_articles(id)

    title = "Top Headlines"
    return render_template('news.html', title = title, news = news)
