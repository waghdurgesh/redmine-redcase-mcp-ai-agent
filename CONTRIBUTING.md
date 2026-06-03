# Contributing to Redcase MCP

First off, thank you for considering contributing to Redcase MCP.

Whether you're fixing bugs, improving documentation, adding features, or sharing ideas, your contributions are appreciated.

---

## Code of Conduct

Please be respectful and constructive when interacting with other contributors.

We aim to maintain a welcoming and collaborative environment for everyone.

---

## Ways to Contribute

You can contribute in many ways:

### Report Bugs

Open an issue if you encounter:

- Unexpected behavior
- Installation problems
- Configuration issues
- Redmine integration issues
- MCP-related issues

When reporting a bug, please include:

- Python version
- Operating system
- Error messages
- Steps to reproduce

---

### Suggest Enhancements

Feature requests are welcome.

Examples:

- Docker support
- API token authentication
- Additional MCP tools
- Better configuration management
- Automated test coverage
- CI/CD integrations

Please describe:

- The problem you're solving
- Proposed solution
- Expected benefits

---

### Improve Documentation

Documentation improvements are highly valuable.

Examples:

- Installation guides
- Troubleshooting guides
- Usage examples
- Configuration examples
- Architecture documentation

---

### Submit Code Changes

Bug fixes and improvements are welcome.

Please keep changes focused and well documented.

---

## Development Setup

Clone the repository:

```bash
git clone <repository-url>
cd redcase-mcp
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create environment variables:

```bash
cp .env.example .env
```

Update:

```env
REDMINE_USERNAME=your_username
REDMINE_PASSWORD=your_password
```

Create configuration:

```bash
cp config/redcase_config.example.json config/redcase_config.json
```

Update configuration values for your environment.

For detailed setup instructions see:

```text
docs/setup.md
```

---

## Pull Request Process

### 1. Create a Branch

Example:

```bash
git checkout -b feature/improve-login-validation
```

or

```bash
git checkout -b fix/redmine-login-error
```

---

### 2. Make Changes

Keep commits focused and descriptive.

Examples:

```text
Add support for custom SSL certificate paths

Fix issue ID extraction logic

Improve Redmine authentication validation
```

---

### 3. Update Documentation

If your change affects:

- Installation
- Configuration
- Usage
- Behavior

please update the relevant documentation.

---

### 4. Submit Pull Request

Include:

- What changed
- Why it changed
- Any limitations
- Screenshots if applicable

---

## Coding Guidelines

### General

Prefer:

- Readable code
- Clear naming
- Small focused functions
- Consistent formatting

---

### Python

Follow PEP 8 where practical.

Examples:

```python
def create_testcase(payload):
    pass
```

Prefer descriptive names over abbreviations.

---

### Error Handling

Handle failures gracefully.

Example:

```python
try:
    response = session.post(...)
except Exception as e:
    return {
        "success": False,
        "error": str(e)
    }
```

---

### Configuration

Do not hardcode:

- Credentials
- URLs
- Environment-specific values
- User-specific paths

Use:

- Environment variables
- Configuration files

instead.

---

## Security Guidelines

Never commit:

```text
.env
config/redcase_config.json
certs/
```

Never commit:

- Passwords
- API keys
- Access tokens
- Internal URLs
- Organization-specific confidential data

Always use placeholders in examples.

Example:

```env
REDMINE_USERNAME=your_username
REDMINE_PASSWORD=your_password
```

---

## Project Scope

Current focus:

- Redmine integration
- Redcase testcase creation
- MCP integration
- AI-assisted testcase workflows

Contributions aligned with this scope are most likely to be accepted.

---

## Future Areas of Interest

Potential future enhancements include:

- Docker support
- Automated testing
- GitHub Actions
- API token authentication
- Improved configuration management
- Additional MCP tools
- Better logging and diagnostics

---

## Questions

If you have questions, open a GitHub issue and provide as much detail as possible.

---

## Thank You

Thank you for helping improve Redcase MCP and making enterprise QA automation more accessible to the community.