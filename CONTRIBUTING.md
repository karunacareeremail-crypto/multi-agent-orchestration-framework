# Contributing to Multi-Agent Orchestration Framework

Thank you for your interest in contributing to this project! This document provides guidelines for contributing.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/yourusername/multi-agent-orchestration-framework.git
   cd multi-agent-orchestration-framework
   ```
3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

## Development Workflow

### 1. Create a Branch

Create a new branch for your feature or bug fix:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### 2. Make Your Changes

- Write clean, readable code
- Follow the existing code style
- Add type hints to all functions
- Include docstrings for all public methods and classes
- Update documentation as needed

### 3. Test Your Changes

Run the test suite to ensure your changes don't break existing functionality:

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest --cov=src tests/
```

### 4. Format Your Code

Format your code using black:

```bash
black src/ examples/ tests/
```

### 5. Commit Your Changes

Write clear, descriptive commit messages:

```bash
git add .
git commit -m "Add: Brief description of your changes"
```

Commit message prefixes:
- `Add:` - New feature
- `Fix:` - Bug fix
- `Update:` - Update existing feature
- `Docs:` - Documentation changes
- `Test:` - Add or update tests
- `Refactor:` - Code refactoring

### 6. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub with:
- Clear description of changes
- Reference to any related issues
- Screenshots (if applicable)

## Code Style Guidelines

### Python Code Style

- Follow PEP 8 guidelines
- Use type hints for function parameters and return values
- Maximum line length: 88 characters (black default)
- Use descriptive variable and function names

### Docstring Format

Use Google-style docstrings:

```python
def example_function(param1: str, param2: int) -> dict:
    """
    Brief description of function.
    
    Longer description if needed, explaining the function's
    purpose and behavior.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        dict: Description of return value
        
    Raises:
        ValueError: When invalid input is provided
    """
    pass
```

## Adding New Features

### Adding a New Agent

1. Create agent file in `src/agents/`
2. Define agent configuration and tools
3. Add factory function (e.g., `create_your_agent()`)
4. Update `src/agents/__init__.py`
5. Add tests in `tests/test_agents.py`
6. Update documentation

### Adding a New Tool

1. Create tool in appropriate `src/tools/` module
2. Decorate with `@function_tool`
3. Add comprehensive docstring
4. Add to agent's tool list
5. Write tests for the tool
6. Update documentation

### Adding New APIs

1. Update `src/api/config.py` with endpoints
2. Create tool functions in `src/tools/`
3. Add error handling
4. Write integration tests
5. Update API documentation

## Testing Guidelines

### Writing Tests

- Write tests for all new features
- Aim for >80% code coverage
- Use descriptive test names
- Group related tests in classes
- Mock external API calls

### Test Structure

```python
class TestFeatureName:
    """Test suite for feature name."""
    
    def test_specific_behavior(self):
        """Test that specific behavior works correctly."""
        # Arrange
        # Act
        # Assert
```

## Documentation

### Updating Documentation

When adding features, update:
- `README.md` - If it affects usage or installation
- `docs/architecture.md` - If it changes architecture
- Inline code comments - For complex logic
- Docstrings - For all public APIs

### Documentation Style

- Use clear, concise language
- Include code examples where helpful
- Keep documentation up-to-date with code
- Use Markdown formatting consistently

## Pull Request Guidelines

### Before Submitting

- [ ] Code follows project style guidelines
- [ ] All tests pass
- [ ] Code is formatted with black
- [ ] Documentation is updated
- [ ] Commit messages are clear
- [ ] No unnecessary files are included

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Refactoring

## Testing
Describe testing performed

## Related Issues
Closes #issue_number
```

## Questions or Problems?

- Open an issue for bugs or feature requests
- Check existing issues before creating new ones
- Be respectful and constructive in discussions

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to the Multi-Agent Orchestration Framework!
