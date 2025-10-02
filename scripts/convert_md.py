import markdown
import os
import re
from datetime import datetime
try:
    import tomllib  # Python 3.11+
except ImportError:
    try:
        import tomli as tomllib  # Fallback for older Python
    except ImportError:
        tomllib = None

def load_metadata(directory_path):
    """Load metadata from meta.toml file if it exists"""
    meta_path = os.path.join(directory_path, 'meta.toml')
    if os.path.exists(meta_path) and tomllib is not None:
        try:
            with open(meta_path, 'rb') as f:
                meta = tomllib.load(f)
                return meta.get('article', {})
        except Exception as e:
            print(f"Warning: Could not parse {meta_path}: {e}")
    return {}

def extract_title_and_content(html_content):
    """Extract the first h1 as title and return remaining content"""
    match = re.match(r'<h1>(.*?)</h1>(.*)', html_content, re.DOTALL)
    if match:
        title = match.group(1)
        content = match.group(2).strip()
        return title, content
    return "Untitled Article", html_content

def generate_article_html(title, content, metadata=None):
    """Generate a complete HTML document with blog styling"""
    if metadata is None:
        metadata = {}
    
    # Extract metadata with defaults
    date = metadata.get('date', 'October 2, 2025')
    author = metadata.get('author', 'Research Team')
    tags = metadata.get('tags', [])
    abstract = metadata.get('abstract', '')
    
    # Generate tags HTML if tags exist
    tags_html = ''
    if tags:
        tags_items = ' '.join([f'<span class="article-tag">{tag}</span>' for tag in tags])
        tags_html = f'\n                    <div class="article-tags">{tags_items}</div>'
    
    # Generate abstract HTML if abstract exists
    abstract_html = ''
    if abstract:
        abstract_html = f'\n                <p class="lead">{abstract}</p>'
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Harvard Systems Blog</title>
    <link rel="stylesheet" href="../../styles.css">
    <link rel="stylesheet" href="../../article.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <div class="nav-logo"><a href="../../index.html">HARVARD SYSTEMS BLOG</a></div>
            <div class="nav-links">
                <a href="../../index.html">Home</a>
                <a href="../../articles.html">Articles</a>
                <a href="../../topics.html">Topics</a>
                <a href="../../index.html#about">About</a>
            </div>
        </div>
    </nav>

    <main class="container article-container">
        <article class="article">
            <header class="article-header">
                <h1>{title}</h1>
                <div class="article-meta">
                    <span class="article-date">{date}</span>
                    <span class="article-author">by {author}</span>
                </div>{tags_html}
            </header>

            <div class="article-content">{abstract_html}
{content}
            </div>

            <footer class="article-footer">
                <a href="../../index.html" class="back-link">← Back to articles</a>
            </footer>
        </article>
    </main>

    <footer class="footer">
        <div class="container">
            <p>Harvard Systems Blog © 2025 · Terms of Service · Privacy Notice</p>
        </div>
    </footer>
</body>
</html>
"""

def convert_md_to_html(md_file_path, directory_path):
    with open(md_file_path, 'r') as file:
        md_content = file.read()
    
    # Load metadata from meta.toml
    metadata = load_metadata(directory_path)
    
    # Convert markdown to HTML
    html_content = markdown.markdown(md_content, extensions=['extra', 'codehilite'])
    
    # Extract title and content
    title, content = extract_title_and_content(html_content)
    
    # Override title from metadata if provided
    if 'title' in metadata:
        title = metadata['title']
    
    # Add proper indentation to content
    content_lines = content.split('\n')
    indented_content = '\n'.join(['                ' + line if line.strip() else '' for line in content_lines])
    
    # Generate complete HTML document
    full_html = generate_article_html(title, indented_content, metadata)
    
    return full_html

def convert_md_to_html_in_directory(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith('.md'):
            md_file_path = os.path.join(directory_path, filename)
            html_content = convert_md_to_html(md_file_path, directory_path)
            output_path = os.path.join(directory_path, filename.replace('.md', '.html'))
            with open(output_path, 'w') as file:
                file.write(html_content)
            print(f"Converted {md_file_path} to {output_path}")

if __name__ == "__main__":
    articles_dir = "articles"
    if os.path.exists(articles_dir):
        for directory in os.listdir(articles_dir):
            dir_path = os.path.join(articles_dir, directory)
            if os.path.isdir(dir_path):
                convert_md_to_html_in_directory(dir_path)
    else:
        print(f"Directory '{articles_dir}' not found!")


