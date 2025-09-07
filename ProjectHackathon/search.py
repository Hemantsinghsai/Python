from serpapi import GoogleSearch

def search_web(query):
    print(f"Searching for: {query}")
    params = {
        "engine": "google",
        "q": query,
        "api_key": "Your API Key",
        "num": 5
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    links = []
    for result in results.get("organic_results", []):
        link = result.get("link")
        if link:
            links.append(link)

    return links if links else ["No results found."]
