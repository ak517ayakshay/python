import webbrowser

url = "https://www.google.com"
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe" 
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open(url)
