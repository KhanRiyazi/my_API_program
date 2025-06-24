# Kaizen + KISS: Simple Python API Client with Dashboard Template
# Goal: Query GitHub API and render repos to HTML dashboard (beginner-friendly)

import requests
import webbrowser

BASE_URL = "https://api.github.com/users/"
USERNAME = "KhanRiyazi"  # Replace with any GitHub username

def get_repos(username):
    """Fetch public repositories for a given GitHub username"""
    try:
        url = f"{BASE_URL}{username}/repos"
        print(f"🔍 Fetching repos from: {url}")
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad responses

        data = response.json()
        print(f"✅ {len(data)} repositories found for user: {username}\n")

        repos = [(repo['name'], repo['html_url']) for repo in data]
        return repos

    except requests.exceptions.HTTPError as err:
        print(f"❌ HTTP Error: {err}")
        return []
    except Exception as e:
        print(f"❌ Error: {e}")
        return []

def generate_html_dashboard(username, repos):
    """Generate an HTML file showing the list of repositories"""
    html = f"""
    <!DOCTYPE html>
    <html lang='en'>
    <head>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
        <title>{username}'s GitHub Repositories</title>
        <style>
            body {{ font-family: 'Segoe UI', sans-serif; background: #f4f4f4; padding: 2em; }}
            h1 {{ color: #4a148c; }}
            ul {{ background: #fff; padding: 1em; border-radius: 10px; box-shadow: 0 2px 6px rgba(0,0,0,0.1); }}
            li {{ margin-bottom: 0.5em; }}
            a {{ color: #333; text-decoration: none; }}
            a:hover {{ text-decoration: underline; }}
        </style>
    </head>
    <body>
        <h1>{username}'s GitHub Repositories</h1>
        <ul>
    """
    for name, url in repos:
        html += f"<li>📁 <a href='{url}' target='_blank'>{name}</a></li>"

    html += """
        </ul>
    </body>
    </html>
    """
    with open("dashboard.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("📄 dashboard.html created.")
    webbrowser.open("dashboard.html")

if __name__ == "__main__":
    repositories = get_repos(USERNAME)
    generate_html_dashboard(USERNAME, repositories)
