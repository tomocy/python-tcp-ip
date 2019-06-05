import webbrowser

DEFAULT_URL = "http://localhost:9000"

url = input("> ")
if url == "":
    url = DEFAULT_URL

webbrowser.open(url)
