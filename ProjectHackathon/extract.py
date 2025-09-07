from newspaper import Article

def extract_content(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return {
            "title": article.title,
            "text": article.text,
            "publish_date": article.publish_date
        }
    except Exception as e:
        return {
            "title": "Error",
            "text": f"Could not extract content from {url}",
            "publish_date": None
        }