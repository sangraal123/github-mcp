import os
import requests
from mcp_converter import convert_to_mcp_format
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
OWNER = "octocat"
REPO = "Hello-World"
ISSUE_NUMBER = 348

def get_issue(owner, repo, issue_number):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    issue_data = get_issue(OWNER, REPO, ISSUE_NUMBER)
    mcp_context = convert_to_mcp_format(issue_data, OWNER, REPO)
    print(mcp_context)
