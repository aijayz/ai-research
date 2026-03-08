# Augment MCP Setup Guide

## Quick Setup for Interactive Workflows

### 1. Easy MCP Setup (Recommended)

#### For GitHub Automation:
1. Open Augment Settings in VS Code (gear icon)
2. Go to "Easy MCP" section
3. Click "+" next to "GitHub"
4. Authenticate with your GitHub account
5. Done! Now you can use natural language for GitHub tasks

#### For Database Queries:
1. Open Augment Settings
2. Go to "Easy MCP" section
3. Click "+" next to your database (PostgreSQL, MySQL, etc.)
4. Enter connection credentials
5. Start querying with natural language!

### 2. Advanced MCP Configuration

If you need custom MCP servers, use the Settings Panel:

#### Example: PostgreSQL Database
```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "POSTGRES_CONNECTION_STRING": "postgresql://user:pass@localhost:5432/mydb"
      }
    }
  }
}
```

#### Example: GitHub (Manual Setup)
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your_token_here"
      }
    }
  }
}
```

### 3. Using Your Workflows

Once configured, you can use natural language:

#### GitHub Examples:
- "Review the latest PR and check for security issues"
- "Create a PR from my current branch to main"
- "Show me all issues assigned to me"
- "What's the status of PR #123?"

#### Database Examples:
- "Show me all users created in the last week"
- "What's the total revenue by product category?"
- "Find all orders with status 'pending' older than 30 days"
- "Create a report of monthly active users"

### 4. Available MCP Integrations

**Development Tools:**
- GitHub - PR reviews, issues, commits
- GitLab - Similar to GitHub
- Linear - Task management
- Jira - Project management

**Databases:**
- PostgreSQL - Relational database
- MySQL - Relational database
- SQLite - Lightweight database
- Redis - Key-value store

**Communication:**
- Slack - Team messaging
- Discord - Community chat

**Cloud Services:**
- AWS - Cloud resources
- Google Cloud - Cloud resources
- Azure - Cloud resources

**And many more!**

### 5. Creating Custom Skills

You can also create custom workflows using Augment's CLI:

```bash
# Create a custom skill for your workflow
auggie skill create my-workflow

# Use it in conversations
auggie "Use my-workflow to process the data"
```

## Next Steps

1. **Start with Easy MCP** - Set up GitHub and your database
2. **Test with simple queries** - Try basic commands
3. **Build complex workflows** - Combine multiple tools
4. **Share with team** - Export your MCP config

## Resources

- [Augment MCP Documentation](https://docs.augmentcode.com/setup-augment/mcp)
- [MCP Server Directory](https://modelcontextprotocol.io/clients)
- [Augment CLI Guide](https://docs.augmentcode.com/cli/overview)

