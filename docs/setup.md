# Redcase MCP Installation Guide

This guide explains how to install and configure Redcase MCP from scratch.

---

# What is Redcase MCP?

Redcase MCP is a Model Context Protocol (MCP) server that allows AI assistants to create Redcase test cases in Redmine.

Typical workflow:

1. User provides requirements or a feature description
2. AI generates QA test cases
3. User reviews and updates test cases
4. AI creates test cases in Redmine using Redcase

---

# Prerequisites

Before starting, ensure you have:

- Python 3.10+
- Access to a Redmine instance
- Redcase plugin installed in Redmine
- Valid Redmine username/password
- Continue extension (optional)

Verify Python:

```bash
python --version
```

Example:

```bash
Python 3.11.8
```

---

# Step 1 - Download Project

Clone repository:

```bash
git clone https://github.com/<your-org>/redcase-mcp.git
```

Enter project:

```bash
cd redcase-mcp
```

---

# Step 2 - Install Python Dependencies

Install required packages:

```bash
pip install -r requirements.txt
```

Expected packages:

- mcp
- requests
- beautifulsoup4
- python-dotenv

---

# Step 3 - Create Environment File

Copy:

```text
.env.example
```

Create:

```text
.env
```

Example:

```env
REDMINE_USERNAME=myuser
REDMINE_PASSWORD=mypassword
```

Replace:

| Value | Replace With |
|---------|---------|
| myuser | Your Redmine username |
| mypassword | Your Redmine password |

Example:

```env
REDMINE_USERNAME=john.doe
REDMINE_PASSWORD=secret123
```

---

# Step 4 - Configure Redmine Settings

Copy:

```text
config/redcase_config.example.json
```

to:

```text
config/redcase_config.json
```

Example:

```bash
cp config/redcase_config.example.json config/redcase_config.json
```

Windows:

```cmd
copy config\redcase_config.example.json config\redcase_config.json
```

---

# Step 5 - Update Configuration

Open:

```text
config/redcase_config.json
```

---

## Update Redmine URL

Find:

```json
"base_url": "https://your-redmine-instance.example.com"
```

Replace with your Redmine URL:

Example:

```json
"base_url": "https://redmine.company.com"
```

---

## Update Project Slug

Find:

```json
"project_slug": "sample_project"
```

Replace with your project identifier.

Example:

If project URL is:

```text
https://redmine.company.com/projects/my_project
```

Then:

```json
"project_slug": "my_project"
```

---

## Update Tracker ID

Find:

```json
"tracker_id": 1
```

Replace with your Redmine testcase tracker ID.

Example:

```json
"tracker_id": 15
```

---

## Update Test Suite ID

Find:

```json
"test_suite_id": 1
```

Replace with your Redcase test suite ID.

Example:

```json
"test_suite_id": 111
```

---

## Update Author ID

Find:

```json
"author_id": 1
```

Replace with your Redmine user ID.

Example:

```json
"author_id": 60
```

---

## Update Watcher IDs

Example:

```json
"watcher_user_ids": [60]
```

or

```json
"watcher_user_ids": []
```

---

# Step 6 - SSL Certificate Configuration

If your Redmine uses a custom SSL certificate:

Create:

```text
certs/
```

Place certificate:

```text
certs/redmine.crt
```

Update:

```json
"ssl_cerificate": "./certs/redmine.crt"
```

---

## If SSL Verification Is Not Required

You may modify the code to disable certificate verification.

Example:

```python
verify=False
```

Only for development environments.

Do not use in production.

---

# Step 7 - Verify Login

Run:

```bash
python src/redcase_client.py
```

Expected output:

```text
Login successful
```

If login fails:

Verify:

- Username
- Password
- Redmine URL
- SSL certificate

---

# Step 8 - Run MCP Server

Start MCP server:

```bash
python src/mcp_server.py
```

Expected:

```text
Redcase MCP running...
```

Keep this terminal open.

---

# Step 9 - Configure Continue

Open:

```text
continue/mcpServers/redcase-mcp.yaml
```

Update path:

Example Windows:

```yaml
args:
  - C:/Users/John/redcase-mcp/src/mcp_server.py
```

Example Linux:

```yaml
args:
  - /home/john/redcase-mcp/src/mcp_server.py
```

---

Copy MCP configuration into your Continue configuration.

Restart Continue.

---

# Step 10 - Install Prompt

Open:

```text
continue/prompts/enterprise-testcase-generator.yaml
```

Import prompt into Continue.

Restart Continue.

---

# Example Usage

User prompt:

```text
Generate test cases for login functionality.

Requirements:

- User enters username
- User enters password
- User clicks Login
- Dashboard opens on success
```

AI generates test cases.

Review them.

Ask AI:

```text
Create these testcases in Redmine
```

The MCP server will create the test cases.

---

# Troubleshooting

## Login Failed

Check:

- Username
- Password
- SSL certificate
- Redmine URL

---

## Project Not Found

Check:

```json
"project_slug"
```

---

## Test Suite Not Found

Check:

```json
"test_suite_id"
```

---

## Tracker Not Found

Check:

```json
"tracker_id"
```

---

## SSL Errors

Verify:

```json
"ssl_cerificate"
```

points to a valid certificate file.

---

# Security Notes

Never commit:

```text
.env
config/redcase_config.json
certs/
```

Only commit:

```text
.env.example
config/redcase_config.example.json
```

These files may contain credentials or organization-specific information.