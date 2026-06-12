from scholarly import scholarly
from feedgen.feed import FeedGenerator

SCHOLAR_ID = "TKbYqt0AAAAJ"

author = scholarly.search_author_id(SCHOLAR_ID)
author = scholarly.fill(author, sections=['publications'])

fg = FeedGenerator()

fg.title(f"Google Scholar Publications - {author['name']}")
fg.link(href=author['url_picture'] if 'url_picture' in author else '')
fg.description("Latest publications from Google Scholar")

publications = author['publications']

for pub in publications[:20]:

    try:
        pub = scholarly.fill(pub)

        title = pub['bib'].get('title', 'Untitled')
        year = str(pub['bib'].get('pub_year', ''))

        entry = fg.add_entry()

        entry.title(title)

        entry.description(
            f"{title} ({year})"
        )

        entry.guid(title)

    except Exception as e:
        print(e)

fg.rss_file('feed.xml')
print("RSS feed generated")
