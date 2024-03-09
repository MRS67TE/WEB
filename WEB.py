import webbrowser

url = "https://web.telegram.org"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.95 Safari/537.36'
}

user_agent_string = headers['User-Agent']
webbrowser.open(url, new=2, autoraise=True, app="chrome", url=url, userAgent=user_agent_string)