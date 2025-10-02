import os
from pathlib import Path
from collections import defaultdict
from datetime import datetime

try:
    import tomllib  # Python 3.11+
except ImportError:
    try:
        import tomli as tomllib  # Fallback for older Python
    except ImportError:
        tomllib = None


# HTML Components
HTML_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>"""

HTML_NAV = """    <nav class="navbar">
        <div class="nav-container">
            <div class="nav-logo"><a href="index.html">Harvard Systems Research Blog</a></div>
            <div class="nav-links">
                <a href="index.html">Home</a>
                <a href="articles.html">Articles</a>
                <a href="topics.html">Topics</a>
                <a href="index.html#about">About</a>
            </div>
        </div>
    </nav>"""

HTML_FOOTER = """    <footer class="footer">
        <div class="container">
            <p>Harvard John A. Paulson School of Engineering and Applied Sciences © 2025 · Terms of Service · Privacy Notice</p>
        </div>
    </footer>
</body>
</html>"""


def generate_hero(title):
    """Generate hero section with title"""
    return f"""    <header class="hero">
        <div class="container">
            <h1 class="hero-title">{title}</h1>
        </div>
    </header>"""


def generate_page(title, hero_title, content):
    """Generate a complete HTML page with common structure"""
    return f"""{HTML_HEAD.format(title=title)}
{HTML_NAV}
{generate_hero(hero_title)}

    <main class="container">
{content}
    </main>

{HTML_FOOTER}
"""


def load_article_metadata(article_dir):
    """Load metadata from an article directory"""
    meta_path = os.path.join(article_dir, "meta.toml")

    if not os.path.exists(meta_path) or tomllib is None:
        return None

    try:
        with open(meta_path, "rb") as f:
            meta = tomllib.load(f)
            article_meta = meta.get("article", {})

            # Find the HTML file
            html_files = [f for f in os.listdir(article_dir) if f.endswith(".html")]
            if html_files:
                article_meta["html_file"] = html_files[0]
                article_meta["relative_path"] = os.path.join(
                    os.path.basename(article_dir), html_files[0]
                )

            return article_meta
    except Exception as e:
        print(f"Warning: Could not parse {meta_path}: {e}")
        return None


def parse_date(date_str):
    """Parse date string to datetime for sorting"""
    try:
        return datetime.strptime(date_str, "%B %d, %Y")
    except:
        try:
            return datetime.strptime(date_str, "%b %d, %Y")
        except:
            return datetime.min


def collect_all_articles():
    """Collect all articles from the articles directory"""
    articles_dir = "articles"
    articles = []

    if not os.path.exists(articles_dir):
        print(f"Directory '{articles_dir}' not found!")
        return articles

    for directory in os.listdir(articles_dir):
        dir_path = os.path.join(articles_dir, directory)
        if os.path.isdir(dir_path):
            meta = load_article_metadata(dir_path)
            if meta and "relative_path" in meta:
                articles.append(meta)

    # Sort articles by date (newest first)
    articles.sort(key=lambda x: parse_date(x.get("date", "")), reverse=True)

    return articles


def organize_by_tags(articles):
    """Organize articles by tags"""
    tags_dict = defaultdict(list)

    for article in articles:
        tags = article.get("tags", [])
        for tag in tags:
            tags_dict[tag].append(article)

    return dict(sorted(tags_dict.items()))


def generate_article_card(article):
    """Generate HTML for a single article card"""
    title = article.get("title", "Untitled")
    date = article.get("date", "")
    abstract = article.get("abstract", "")
    path = article.get("relative_path", "#")
    tags = article.get("tags", [])

    # Truncate abstract if too long
    if abstract and len(abstract) > 200:
        abstract = abstract[:197] + "..."

    tags_html = ""
    if tags:
        tags_items = " ".join([f'<span class="card-tag">{tag}</span>' for tag in tags[:3]])
        tags_html = f'\n                        <div class="card-tags">{tags_items}</div>'

    return f"""                <a href="articles/{path}" class="article-card-link">
                    <article class="article-card">
                        <h3>{title}</h3>
                        <p class="article-date">{date}</p>
                        <p class="article-excerpt">
                            {abstract}
                        </p>{tags_html}
                        <span class="read-more">Read more →</span>
                    </article>
                </a>
"""


def generate_articles_page(articles):
    """Generate a complete articles.html page listing all articles"""

    # Generate article cards
    article_cards = "\n".join([generate_article_card(article) for article in articles])

    content = f"""        <section id="articles" class="articles-section">
            <div class="articles-grid">
{article_cards}
            </div>
        </section>"""

    return generate_page("All Articles - Harvard Systems Research Blog", "All Articles", content)


def generate_topics_page(articles, tags_dict):
    """Generate a complete topics.html page"""
    if not tags_dict:
        return None

    tag_buttons = []
    for tag, articles_with_tag in tags_dict.items():
        count = len(articles_with_tag)
        tag_buttons.append(
            f'                <button class="tag-filter" data-tag="{tag}">{tag} ({count})</button>'
        )

    # Generate article cards with tags
    article_cards_with_tags = []
    for article in articles:
        tags = article.get("tags", [])
        tags_str = " ".join(tags)
        card_html = generate_article_card(article)
        card_html = card_html.replace(
            '<article class="article-card">',
            f'<article class="article-card" data-tags="{tags_str}">',
        )
        article_cards_with_tags.append(card_html)

    article_cards = "\n".join(article_cards_with_tags)

    filter_script = """    <script>
        // Tag filtering functionality
        const tagFilters = document.querySelectorAll('.tag-filter');
        const articleCards = document.querySelectorAll('.article-card');
        
        tagFilters.forEach(filter => {
            filter.addEventListener('click', () => {
                // Update active state
                tagFilters.forEach(f => f.classList.remove('active'));
                filter.classList.add('active');
                
                const selectedTag = filter.dataset.tag;
                
                // Filter articles
                articleCards.forEach(card => {
                    const cardTags = card.dataset.tags || '';
                    if (selectedTag === 'all' || cardTags.includes(selectedTag)) {
                        card.style.display = '';
                    } else {
                        card.style.display = 'none';
                    }
                });
            });
        });
    </script>"""

    content = f"""        <section class="tags-section">
            <div class="tags-container">
                <button class="tag-filter active" data-tag="all">All Articles ({len(articles)})</button>
{chr(10).join(tag_buttons)}
            </div>
        </section>

        <section id="articles" class="articles-section">
            <h2>Articles</h2>
            <div class="articles-grid">
{article_cards}
            </div>
        </section>"""

    # Generate page with script inserted before closing body tag
    page = generate_page("Topics - Harvard Systems Research Blog", "Browse by Topic", content)
    return page.replace("</body>", f"{filter_script}\n</body>")


def generate_index_html(articles, tags_dict):
    """Generate the complete index.html"""

    # Show only the 8 most recent articles on homepage
    recent_articles = articles[:8]

    # Generate article cards
    article_cards = "\n".join([generate_article_card(article) for article in recent_articles])

    content = f"""        <section id="articles" class="articles-section">
            <div class="articles-grid">
{article_cards}
            </div>
            <div class="view-all-container">
                <a href="articles.html" class="view-all-link">View all articles →</a>
            </div>
        </section>

        <section id="about" class="join-section">
            <h2>About</h2>
            <p class="join-text">
                This is the blog for systems research at Harvard John A. Paulson School of Engineering and Applied Sciences. 
                We explore systems, networking, databases, and computer architecture that power 
                modern computing.
            </p>
            <p class="join-text">
                We're building a community of systems researchers and practitioners who are passionate 
                about understanding and improving the infrastructure that powers modern computing.
            </p>
            <p class="join-text">
                Follow us on X at @HarvardSystems for updates or reach out to contribute your own insights.
            </p>
        </section>"""

    return generate_page("Harvard Systems Research Blog", "Harvard Systems Research Blog", content)


def main():
    """Main function to build the index and topics pages"""
    print("Collecting articles...")
    articles = collect_all_articles()
    print(f"Found {len(articles)} articles")

    if not articles:
        print("No articles found with meta.toml files")
        return

    print("Organizing by tags...")
    tags_dict = organize_by_tags(articles)
    print(f"Found {len(tags_dict)} unique tags")

    print("Generating index.html...")
    html = generate_index_html(articles, tags_dict)

    with open("index.html", "w") as f:
        f.write(html)

    print("✓ index.html has been generated successfully!")

    print("Generating articles.html...")
    articles_html = generate_articles_page(articles)

    with open("articles.html", "w") as f:
        f.write(articles_html)
    print("✓ articles.html has been generated successfully!")

    print("Generating topics.html...")
    topics_html = generate_topics_page(articles, tags_dict)

    if topics_html:
        with open("topics.html", "w") as f:
            f.write(topics_html)
        print("✓ topics.html has been generated successfully!")

    print(f"\nSummary:")
    print(f"  - {len(articles)} articles")
    print(f"  - {len(tags_dict)} tags")


if __name__ == "__main__":
    main()
