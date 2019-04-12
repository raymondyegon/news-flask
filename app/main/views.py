from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_news


@main.route("/")
def index():
    '''
    View root page function that returns the index page and its data
    '''
    top_headlines = get_news("top-headlines")

    title = "News headlines"

    return render_template("index.html", title = title, top=top_headlines)
