"""
🌟 Python API Mastery Lesson: GitHub Repository Dashboard 🌟
Teacher: Let's build a professional API client together!

Lesson Goals:
1. Understand REST API fundamentals
2. Learn Python's requests library
3. Handle API responses and errors
4. Create a web dashboard from API data
5. Follow best practices (Kaizen + KISS)
"""

import requests
import webbrowser
from datetime import datetime
import json

# Configuration - Let's make these easy to change
BASE_URL = "https://api.github.com/users/"
USERNAME = "KhanRiyazi"  # Student: Try your own GitHub username here!
DASHBOARD_FILE = "github_dashboard.html"

class GitHubAPIStudent:
    """
    Student, this class will help you:
    1. Fetch data from GitHub's API
    2. Handle potential errors
    3. Generate a beautiful dashboard
    """
    
    def __init__(self, username):
        self.username = username
        self.repos = []
        self.error = None
    
    def get_repos(self):
        """Teacher: This method shows proper API request handling"""
        try:
            url = f"{BASE_URL}{self.username}/repos"
            print(f"\n🔍 Teacher: Making API request to: {url}")
            
            # Student: Notice how we set headers for proper API etiquette
            headers = {
                "Accept": "application/vnd.github.v3+json",
                "User-Agent": "PythonAPIStudent/1.0"
            }
            
            response = requests.get(url, headers=headers)
            
            # Teacher: Always check the status code!
            if response.status_code == 200:
                data = response.json()
                self.repos = [(repo['name'], repo['html_url'], repo['description'] or "No description") 
                             for repo in data]
                print(f"✅ Teacher: Success! Found {len(self.repos)} repositories")
                return True
            elif response.status_code == 404:
                self.error = f"User '{self.username}' not found on GitHub"
            else:
                self.error = f"API returned status code: {response.status_code}"
            return False
            
        except requests.exceptions.RequestException as e:
            self.error = f"Network error: {str(e)}"
            return False
    
    def generate_dashboard(self):
        """Teacher: Let's make a professional dashboard with the data"""
        if not self.repos:
            print("⚠️ Teacher: No repositories to display. Did the API call fail?")
            return
        
        print("\n🎨 Teacher: Generating beautiful dashboard...")
        
        # Current date for the dashboard footer
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Student: Here's a more professional HTML template
        html = f"""<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>{self.username}'s GitHub Repositories</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500&display=swap" rel="stylesheet">
    <style>
        body {{
            font-family: 'Roboto', sans-serif;
            background: #f8f9fa;
            color: #333;
            line-height: 1.6;
            padding: 2rem;
            max-width: 1000px;
            margin: 0 auto;
        }}
        header {{
            background: #24292e;
            color: white;
            padding: 2rem;
            border-radius: 8px 8px 0 0;
            margin-bottom: 0;
        }}
        h1 {{
            margin: 0;
            font-weight: 500;
        }}
        .subtitle {{
            opacity: 0.8;
            font-weight: 300;
        }}
        .repo-container {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
            margin-top: 0;
        }}
        .repo-card {{
            background: white;
            border-radius: 8px;
            padding: 1.5rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            transition: transform 0.2s;
        }}
        .repo-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }}
        .repo-name {{
            color: #0366d6;
            font-weight: 500;
            text-decoration: none;
            font-size: 1.1rem;
        }}
        .repo-desc {{
            color: #586069;
            margin: 0.5rem 0;
        }}
        footer {{
            text-align: center;
            margin-top: 2rem;
            color: #6a737d;
            font-size: 0.9rem;
        }}
        .error {{
            color: #d73a49;
            background: #ffebee;
            padding: 1rem;
            border-radius: 4px;
        }}
    </style>
</head>
<body>
    <header>
        <h1>{self.username}'s GitHub Repositories</h1>
        <p class="subtitle">Generated with Python API Mastery Lesson</p>
    </header>
    
    <div class="repo-container">
"""
        # Add each repository as a card
        for name, url, desc in self.repos:
            html += f"""
        <div class="repo-card">
            <a href="{url}" target="_blank" class="repo-name">📦 {name}</a>
            <p class="repo-desc">{desc}</p>
            <a href="{url}" target="_blank">View on GitHub →</a>
        </div>
"""
        
        # Close the HTML
        html += f"""
    </div>
    
    <footer>
        <p>Dashboard generated on {current_date}</p>
        <p>Lesson: Python API Mastery - Teacher-Student Edition</p>
    </footer>
</body>
</html>
"""
        
        # Write to file
        with open(DASHBOARD_FILE, "w", encoding="utf-8") as f:
            f.write(html)
        
        print(f"📊 Teacher: Dashboard saved as '{DASHBOARD_FILE}'")
        return True
    
    def open_dashboard(self):
        """Teacher: Let's view our creation!"""
        try:
            webbrowser.open(DASHBOARD_FILE)
            return True
        except Exception as e:
            print(f"⚠️ Teacher: Couldn't open dashboard: {str(e)}")
            return False

def main():
    print("""
🌟 Python API Mastery Lesson 🌟
    
Teacher: Today we'll build a GitHub repository dashboard!
Student: I'm ready to learn!

We'll:
1. Connect to GitHub's API
2. Fetch repository data
3. Handle any errors
4. Create a beautiful dashboard
""")
    
    # Initialize our student project
    student_project = GitHubAPIStudent(USERNAME)
    
    # Step 1: Fetch data from GitHub API
    print("\n💻 Teacher: First, let's fetch data from GitHub's API...")
    if not student_project.get_repos():
        print(f"\n❌ Teacher: Oh no! We encountered an error: {student_project.error}")
        print("Let's troubleshoot:")
        print("1. Check if the username is correct")
        print("2. Make sure you have internet connection")
        print("3. GitHub might be temporarily unavailable")
        return
    
    # Step 2: Generate the dashboard
    print("\n🎨 Teacher: Now let's visualize this data beautifully...")
    if not student_project.generate_dashboard():
        return
    
    # Step 3: Open the dashboard
    print("\n👀 Teacher: Let's view our dashboard in the browser...")
    student_project.open_dashboard()
    
    print("""
🎉 Teacher: Congratulations on completing this lesson!

Homework:
1. Try with your own GitHub username
2. Add more repository details (stars, forks)
3. Implement error handling for rate limits
4. Style the dashboard differently

Remember the principles:
- Kaizen (continuous improvement)
- KISS (Keep It Simple, Student!)
""")

if __name__ == "__main__":
    main()