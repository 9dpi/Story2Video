import main
html = main.FRONTEND_HTML
html = html.replace("{{VERSION}}", "1.0.0")
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
