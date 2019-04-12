from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_news, search_news


@main.route("/")
def index():
    '''
    View root page function that returns the index page and its data
    '''
    top_headlines = get_news("top-headlines")

    title = "News headlines"
    
    search_news = request.args.get("news_query")
    
    if search_news:
        return redirect(url_for(".search", news_name = search_news))

    return render_template("index.html", title = title, top=top_headlines)


@main.route("/search/<news_name>")
def search(news_name):
    '''
    View function to display the search results
    '''
    news_name_list = news_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f" Search results for {news_name}"
    
    return render_template("search.html", news = searched_news)