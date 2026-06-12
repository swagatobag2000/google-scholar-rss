from scholarly import scholarly
from feedgen.feed import FeedGenerator

# Google Scholar ID
SCHOLAR_ID = "TKbYqt0AAAAJ"

print("Fetching author profile...")

author = scholarly.search_author_id(SCHOLAR_ID)

author = scholarly.fill(
    author,
    sections=["publications"]
)

print(f"Author: {author['name']}")
print(f"Publications found: {len(author['publications'])}")

fg = FeedGenerator()

fg.title(
    f"Google Scholar Publications - {author['name']}"
)

fg.link(
    href=f"https://scholar.google.com/citations?user={SCHOLAR_ID}"
)

fg.description(
    "Latest publications from Google Scholar"
)

for pub in author["publications"][:20]:

    try:

        pub = scholarly.fill(pub)

        bib = pub.get("bib", {})

        title = bib.get(
            "title",
            "Untitled"
        )

        year = bib.get(
            "pub_year",
            ""
        )

        entry = fg.add_entry()

        entry.title(title)

        entry.link(
            href=f"https://scholar.google.com/citations?user={SCHOLAR_ID}"
        )

        entry.description(
            f"{title} ({year})"
        )

        entry.guid(title)

        print(title)

    except Exception as e:

        print(
            f"Failed: {e}"
        )

fg.rss_file("feed.xml")

print("RSS generated successfully")
