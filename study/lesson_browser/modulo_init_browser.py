import webbrowser


def abrir_browser(url):
    chrome_path = webbrowser.get(using='chrome')
    chrome_path.open(url)
    return chrome_path


