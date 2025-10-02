# Harvard Systems Blog

A clean, minimalist blog for systems research articles featuring modern design and excellent typography.

## Project Structure

```
harvardSys_blog/
├── index.html              # Main landing page (8 most recent articles)
├── articles.html          # All articles page (auto-generated)
├── topics.html            # Topics/tags page (auto-generated)
├── styles.css             # Main stylesheet for the blog
├── article.css            # Article-specific styles
├── pyproject.toml         # Python dependencies
├── README.md              # This file
├── .gitignore             # Git ignore patterns
├── articles/              # Article content directory
│   └── example/           # Individual article folder
│       ├── meta.toml      # Article metadata
│       ├── segcache.md    # Markdown source
│       ├── segcache.html  # Generated HTML
│       └── figure/        # Article images/figures (PDF and SVG)
└── scripts/
    ├── convert_md.py      # Markdown to HTML converter
    └── build_index.py     # Page generator (index, articles, topics)
```



## Installation

### Install Dependencies

This project uses `pyproject.toml` to manage dependencies. Install them using:

```bash
# Using pip
pip install -e .

# Or install just the runtime dependencies
pip install markdown tomli
```



## Contributing

When adding new articles:
1. Follow the existing markdown structure
2. Test the converted HTML in a browser
3. Ensure images are properly linked
4. Verify responsive design on mobile devices
5. Check that all navigation links work correctly


## Adding New Articles

### Method 1: Write in Markdown (Recommended)

1. Create a new directory under `articles/` for your article:
   ```bash
   mkdir -p articles/YYYY_article-name
   ```

2. Create a `meta.toml` file for article metadata:
   ```bash
   touch articles/YYYY_article-name/meta.toml
   ```

   Add metadata in TOML format:
   ```toml
   [article]
   title = "Your Article Title"
   author = "Author Name"
   date = "Month Day, Year"
   tags = ["tag1", "tag2", "tag3"]
   abstract = "A brief summary of your article that will appear on the main page and at the beginning of the article."
   ```

3. Create your article as a markdown file:
   ```bash
   touch articles/YYYY_article-name/article-name.md
   ```

4. Write your article in markdown format. Start with an H1 for the title:
   ```markdown
   # Your Article Title
   
   Your article content goes here...
   
   ## Section Heading
   
   More content...
   ```

5. Add any images to a `figure/` subdirectory:
   ```bash
   mkdir -p articles/YYYY_article-name/figure
   ```

6. Convert markdown to HTML:
   ```bash
   python scripts/convert_md.py
   ```

   The converter will automatically:
   - Generate a complete HTML page with proper styling
   - Extract the first H1 as the article title
   - Add navigation, header, and footer
   - Link to the correct CSS files
   - Include the Inter font family

### Method 2: Write HTML Directly

Copy a generated HTML from an existing article and modify it, then create a `meta.toml` file for the article metadata.

## Generating Index Pages

After adding or modifying articles (via either Method 1 or Method 2), rebuild the index pages:

```bash
python scripts/build_index.py
```

The index builder will:
- Scan all articles with `meta.toml` files
- Generate the main index page (index.html) with 8 most recent articles
- Generate an all articles page (articles.html) with complete chronological list
- Generate a topics page (topics.html) with tag filtering
- Add interactive tag-based filtering on the topics page 


