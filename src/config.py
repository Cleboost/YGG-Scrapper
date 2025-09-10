import os
from dotenv import load_dotenv

load_dotenv()

CREDENTIALS = {
    "username": os.getenv("USERNAME"),
    "password": os.getenv("PASSWORD")
}

URLS = {
    "login": "https://ygg.re/",
    "search": "https://www.yggtorrent.top/engine/search"
}

SELECTORS = {
    "login_form": "form.login-form",
    "username_field": "input[name='id']",
    "password_field": "input[name='pass']",
    "submit_button": "button[type='submit']",
    "search_form": "form.search",
    "search_input": "input[name='name']",
    "search_button": "form.search button"
}

SEARCH_TERM = "Game"