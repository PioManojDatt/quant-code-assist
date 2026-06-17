# Quant Code Assist

An AI-powered code assistant specialized for quantitative finance and algorithmic trading.

## Overview

Quant Code Assist is a developer tool that helps quants and algorithmic traders write, debug, and optimize financial code efficiently. It provides intelligent suggestions, explanations, and best practices tailored for quantitative finance workflows using libraries like pandas, NumPy, TA-Lib, Backtrader, Zipline, and QuantConnect.

## Features

- Intelligent code completion for quant libraries
- Trading strategy generation and debugging support
- Financial data analysis and feature engineering assistance
- Code explanation for complex quant logic
- Best practices and performance optimization tips

## Installation

### Prerequisites

- Python 3.11 or higher
- pip package manager

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/PioManojDatt/quant-code-assist.git
   cd quant-code-assist
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate       # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. (Optional) Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

## Usage

### Basic Usage

Run the assistant from the command line:

```bash
python main.py
```

### Using as a Library

You can also import and use it in your Python projects:

```python
from quant_code_assist import CodeAssistant

assistant = CodeAssistant()
response = assistant.suggest_code("Write a moving average crossover strategy using pandas")
print(response)
```

### IDE Integration

Quant Code Assist can be integrated with VS Code or other editors. See the setup guide:

```bash
# Follow instructions in
docs/setup.md
```

### Example Commands

| Command                        | Description                              |
|--------------------------------|------------------------------------------|
| `python main.py --help`        | Show available options                   |
| `python main.py --explain file.py` | Explain the code in a file            |
| `python main.py --strategy "mean reversion"` | Generate a strategy skeleton     |

## Configuration

Create a `.env` file in the root directory to set your preferences:

```env
MODEL_NAME=gpt-4
TEMPERATURE=0.3
MAX_TOKENS=1500
```

## Project Structure

```
quant-code-assist/
├── src/               # Core logic and AI models
├── examples/          # Sample strategies and notebooks
├── docs/              # Documentation and setup guides
├── tests/             # Unit and integration tests
├── requirements.txt
├── main.py
└── README.md
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes
4. Open a Pull Request

For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
