### 📄 `README.md`

````markdown
# GitHub Issue to MCP Converter

This is a minimal Python application that demonstrates integration with the GitHub API by fetching issue data from a repository and converting it into a [Model Context Protocol (MCP)](https://modelcontextprotocol.io) format.

This example can be used as a simple starting point for registering with the [GitHub Developer Program](https://developer.github.com/).

---

## ✨ Features

- Uses GitHub REST API to fetch issue data
- Converts GitHub Issue to structured MCP-compatible JSON
- Easily adaptable to your own repositories
- Simple to run locally with minimal dependencies

---

## 📦 Requirements

- Python 3.7+
- A GitHub personal access token (classic)
- The following Python packages (see `requirements.txt`):
  - `requests`
  - `python-dotenv`

---

## 🔧 Setup

1. **Clone this repository** (or copy the files locally):

   ```bash
   git clone https://github.com/sangraal123/github-mcp.git
   cd github-mcp-demo
````

2. **Create a `.env` file** and add your GitHub token:

   ```env
   GITHUB_TOKEN=your_personal_access_token_here
   ```

   > You can generate a token at [https://github.com/settings/tokens](https://github.com/settings/tokens).
   > Only `public_repo` scope is needed.

3. **Create a virtual environment (optional but recommended)**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

4. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ How to Run

Run the script with:

```bash
python main.py
```

It will output MCP-formatted JSON like this:

```json
{
  "@context": "https://modelcontext.org/context",
  "@type": "GitHubIssueContext",
  "repository": "octocat/Hello-World",
  "issueNumber": 348,
  "title": "Testing comments",
  "body": "Let's add some, shall we?",
  "labels": []
}
```

---

## 🔁 Customize

To use your own repository and issue, edit these lines in `main.py`:

```python
OWNER = "your-username"
REPO = "your-repository"
ISSUE_NUMBER = 1  # Your issue number
```

---

## 📄 Project Structure

```
github-mcp-demo/
├── main.py             # Main script that fetches and converts GitHub Issue
├── mcp_converter.py    # Converter from GitHub JSON to MCP format
├── .env                # Stores your GitHub token (not committed)
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

---

## 🧠 About MCP

Model Context Protocol (MCP) is a structured data format for sharing AI-relevant context.
It allows large language models to better understand the surrounding environment of tasks or data sources, such as GitHub issues.

Learn more: [https://modelcontextprotocol.io](https://modelcontextprotocol.io)

---

## 📫 Support

This project is intended for demonstration and developer onboarding purposes.
If you plan to publish or integrate this into production, be sure to handle API errors and rate limits properly.

---

## 📜 License

MIT License.
You are free to use, modify, and distribute this example.
