import webbrowser as web

def workSetup():
    chromPath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    URLs = (
        'https://youtube.com',
        'https://instagram.com',
        'https://github.com',
        'https://facebook.com',
    )
    for url in URLs:
        web.get(chromPath).open(url)

workSetup()