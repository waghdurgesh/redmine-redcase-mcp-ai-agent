# Redmine+Redcase MCP Server & AI Agent

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![MCP](https://img.shields.io/badge/MCP-Compatible-orange)
<p align="left">
  <img src="https://komarev.com/ghpvc/?username=waghdurgesh&label=Repository%20Views&color=0e75b6&style=flat" alt="Repository Views" />
</p>

### AI-Powered Redcase Testcase Automation using Continue + MCP + Python Agent

Create Redcase test cases in Redmine directly from AI-generated test scenarios using the Model Context Protocol (MCP).

Redcase MCP bridges the gap between requirement analysis and test management by allowing AI assistants to generate high-quality QA test cases and automatically create them inside Redmine + Redcase.

<img width="1536" height="1024" alt="Redcase Ai TestCase Gen Title Image" src="https://github.com/user-attachments/assets/98d4fe95-a3ea-42c2-a650-fd8232f86cff" />


## Overview

Devlopers & QA teams often spend significant time manually:

- Reading requirements
- Analyzing bug reports
- Reviewing feature discussions
- Writing test cases
- Creating Redcase entries in Redmine

Redcase MCP automates this workflow.

Using MCP-enabled AI assistants (such as Continue), users can:

1. Provide code, requirements, user stories, bugs, or specifications
2. Generate structured QA test cases
3. Review and refine them
4. Create Redcase test cases directly in Redmine

---

## Problem Statement

Traditional testcase creation typically involves:

```text
Requirement
    ↓
Manual Analysis
    ↓
Manual Testcase Writing
    ↓
Manual Redmine Entry
    ↓
Execution
```

This process is:

- Time-consuming
- Repetitive
- Error-prone
- Difficult to scale

Redcase MCP streamlines the process:

```text
Requirement
    ↓
AI Analysis
    ↓
AI Testcase Generation
    ↓
User Review
    ↓
Automatic Redcase Creation
```

---

## What This Project Does

This MCP server:

- Authenticates with Redmine
- Creates Redcase test cases
- Supports bulk testcase creation
- Converts AI-generated test scenarios into Redcase-compatible payloads
- Integrates with Continue and other MCP clients

<img width="1536" height="1024" alt="redmine-redcase-mcp-ai-agent" src="https://github.com/user-attachments/assets/e98ae7bc-ba3f-4940-bee4-df82c29d8819" />

---

## Key Features

### AI-Powered Test Case Generation

Generate test cases from:

- User stories
- Requirements
- Bug reports
- Feature requests
- Technical specifications
- Workflow descriptions
- API documentation

---

### Redmine + Redcase Integration

Automatically creates:

- Test case issues
- Preconditions
- Test steps
- Expected results
- Priorities

---

### Bulk Creation

Create multiple test cases in a single request.

---

### MCP Compatible

Built using:

- Model Context Protocol (MCP)

Compatible with:

- Continue
- MCP-enabled AI clients
- Custom MCP integrations

---

### Enterprise QA Focus

Generates scenarios covering:

- Business workflows
- Security
- Permissions
- Integrations
- Data validation
- Regression testing
- Workflow transitions
- Error handling

---

## Architecture

```text
+---------------------+
|     User Prompt     |
+----------+----------+
           |
           v
+---------------------+
| AI Test Generation  |
+----------+----------+
           |
           v
+---------------------+
| Continue Prompt     |
+----------+----------+
           |
           v
+---------------------+
|    MCP Tool Call    |
+----------+----------+
           |
           v
+---------------------+
|   Redcase MCP       |
+----------+----------+
           |
           v
+---------------------+
| Redmine + Redcase   |
+---------------------+
```

---

## Technology Stack

### Backend

- Python 3.10+
- Requests
- BeautifulSoup4
- python-dotenv

### MCP

- FastMCP
- Model Context Protocol

### Test Management

- Redmine
- Redcase

### AI Integration

- Continue
- MCP-compatible AI clients

---

## Repository Structure

```text
redcase-mcp/
│
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── .env.example
│
├── src/
│   ├── mcp_server.py
│   └── redcase_client.py
│
├── config/
│   └── redcase_config.example.json
│
├── examples/
│   └── testcase_payload.json
│
├── continue/
│   ├── mcpServers/
│   │   └── redcase-mcp.yaml
│   └── prompts/
│       └── enterprise-testcase-generator.yaml
│
├── docs/
│   └── setup.md
│
└── certs/
    └── README.md
```

---

## Workflow

### Step 1

Provide a requirement:

```text
Implement user login functionality.

Users should:
- Enter username
- Enter password
- Click Login
- Access dashboard on success
```

### Step 2

AI generates test cases:

```text
Testcase 1 - Successful Login

Testcase 2 - Invalid Password

Testcase 3 - Empty Username

Testcase 4 - Session Timeout
```

### Step 3

Review and update generated test cases.

### Step 4

Confirm creation.

### Step 5

MCP server creates Redcase test cases automatically.

---

## Example MCP Payload

```json
{
  "testcases": [
    {
      "title": "Successful Login",
      "description": "Verify successful login",

      "priority_id": 3,

      "preconditions": [
        "User account exists"
      ],

      "steps": [
        "Open login page",
        "Enter valid username",
        "Enter valid password",
        "Click Login"
      ],

      "expected_results": [
        "User is authenticated",
        "Dashboard is displayed"
      ]
    }
  ]
}
```

---

## Benefits

### Faster QA Documentation

Reduce manual testcase creation effort.

---

### Improved Coverage

AI can identify:

- Happy paths
- Negative scenarios
- Permission checks
- Integration risks
- Regression scenarios

---

### Standardized Test Cases

Enforces consistent structure for:

- Preconditions
- Steps
- Expected Results

---

### Reduced Human Error

Avoid manual copy/paste and testcase entry mistakes.

---

### Better Traceability

Requirements can be quickly converted into executable test cases.

---

## Typical Use Cases

### QA Engineers

Generate test cases from requirements.

---

### Test Leads

Improve regression coverage.

---

### Business Analysts

Convert business requirements into QA scenarios.

---

### Product Owners

Validate acceptance criteria.

---

### Development Teams

Generate validation scenarios during implementation.

---

## Security

Credentials are stored using environment variables.

Example:

```env
REDMINE_USERNAME=myuser
REDMINE_PASSWORD=mypassword
```

Never commit:

```text
.env
config/redcase_config.json
certs/
```

---

## Installation

See:

```text
docs/setup.md
```

for a complete step-by-step installation guide.

---

## Limitations

Current version:

- Supports username/password authentication
- Requires Redcase plugin
- Requires Redmine access
- Focused on testcase creation

Future enhancements may include:

- API token authentication
- Docker deployment
- Automated test suite mapping
- Advanced validation
- CI/CD integration

---

## Contributing

Contributions are welcome.

Potential areas:

- Additional authentication methods
- Better configuration management
- Automated testing
- Docker support
- Additional MCP tools

---

## License

MIT License

---

## Acknowledgements

Built using:

- Redmine
- Redcase
- FastMCP
- Continue
- Python

Special thanks to the open-source communities behind these projects.
