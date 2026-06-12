from scholarly import scholarly
from feedgen.feed import FeedGenerator

SCHOLAR_ID = "TKbYqt0AAAAJ"

print("Fetching author...")

author = scholarly.search_author_id(SCHOLAR_ID)

fg = FeedGenerator()

fg.title(f"Publications - {author.get('name','Scholar Author')}")
fg.link(href=f"https://scholar.google.com/citations?user={SCHOLAR_ID}")
fg.description("Latest Google Scholar Publications")

publications = author.get("publications", [])

for pub in publications[:20]:

    bib = pub.get("bib", {})

    title = bib.get("title", "Untitled")
    year = bib.get("pub_year", "")

    entry = fg.add_entry()

    entry.title(title)
    entry.description(f"{title} ({year})")
    entry.guid(title)

fg.rss_file("feed.xml")

print("RSS feed generated")
