from search import search_web

query = "AI tools for research"
results = search_web(query)

print("Search Results:")
for r in results:
    print("-", r)