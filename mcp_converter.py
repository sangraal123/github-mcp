def convert_to_mcp_format(issue, owner, repo):
    return {
        "@context": "https://modelcontext.org/context",
        "@type": "GitHubIssueContext",
        "repository": f"{owner}/{repo}",
        "issueNumber": issue["number"],
        "title": issue["title"],
        "body": issue.get("body", ""),
        "labels": [label["name"] for label in issue.get("labels", [])]
    }
