# Advanced Developer Tools Research Agent 🔍

An intelligent AI-powered research agent that helps developers discover, analyze, and compare developer tools and technologies. Built with LangGraph, OpenAI GPT-4, and Firecrawl for comprehensive web research and analysis.

## ✨ Features

- **Smart Tool Discovery**: Automatically extracts relevant developer tools from web articles and documentation
- **Comprehensive Analysis**: Analyzes pricing models, tech stacks, API availability, and integration capabilities
- **Developer-Focused**: Tailored specifically for programmers and software engineers
- **Interactive CLI**: Easy-to-use command-line interface for quick research
- **Structured Output**: Clean, organized results with key information at a glance

## 🛠️ Tech Stack

- **Python 3.12+**
- **LangGraph** - Workflow orchestration
- **LangChain + OpenAI GPT-4** - AI-powered analysis
- **Firecrawl** - Web scraping and search
- **Pydantic** - Data validation and modeling
- **UV** - Fast Python package manager

## 🚀 Quick Start

### Prerequisites

- Python 3.12 or higher
- OpenAI API key
- Firecrawl API key

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/asheint/advanced-research-agent.git
   cd advanced-research-agent
   ```

2. **Install dependencies with UV**

   ```bash
   uv sync
   ```

3. **Set up environment variables**

   Create a `.env` file in the root directory:

   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   FIRECRAWL_API_KEY=your_firecrawl_api_key_here
   ```

4. **Run the application**
   ```bash
   uv run python main.py
   ```

## 💡 Usage

Once running, simply enter your developer tools query:

```
🔍 Developer Tools Query: best database for python web apps

📊 Results for: best database for python web apps
============================================================

1. 🏢 PostgreSQL
   🌐 Website: https://postgresql.org
   💰 Pricing: Free
   📖 Open Source: True
   🛠️  Tech Stack: SQL, ACID, JSON, XML
   💻 Language Support: Python, JavaScript, Java, Go, Rust
   🔌 API: ✅ Available
   🔗 Integrations: Django, SQLAlchemy, Prisma, Supabase
   📝 Description: Advanced open-source relational database system

Developer Recommendations:
----------------------------------------
PostgreSQL is the best choice for Python web apps due to excellent SQLAlchemy integration and Django ORM support. It's completely free with enterprise-grade features. Main advantage is robust ACID compliance and JSON support for hybrid workloads.
```

### Example Queries

- "best CI/CD tools for small teams"
- "python web frameworks comparison"
- "database hosting solutions"
- "API documentation tools"
- "monitoring tools for microservices"

## 🏗️ Architecture

The agent follows a structured workflow:

1. **Tool Extraction** - Searches for articles and extracts relevant tool names
2. **Research** - Gathers detailed information about each discovered tool
3. **Analysis** - Uses structured AI analysis to extract key developer-relevant information
4. **Recommendations** - Provides concise, actionable recommendations

## 📁 Project Structure

```
advanced-research-agent/
├── src/
│   ├── __init__.py
│   ├── workflow.py      # Main workflow orchestration
│   ├── models.py        # Pydantic data models
│   ├── prompts.py       # AI prompts and templates
│   └── firecrawl.py     # Web scraping service
├── main.py              # CLI application entry point
├── pyproject.toml       # UV configuration
├── .env                 # Environment variables (create this)
├── .python-version      # Python version specification
└── README.md           # This file
```

## 🔧 Configuration

### Environment Variables

- `OPENAI_API_KEY` - Your OpenAI API key for GPT-4 access
- `FIRECRAWL_API_KEY` - Your Firecrawl API key for web scraping

### Model Configuration

The agent uses GPT-4o-mini by default for cost efficiency. You can modify the model in [`src/workflow.py`](src/workflow.py):

```python
self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.1)
```

## 🤝 Contributing

Contributions are welcome! This is an open-source project. Please feel free to:

- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

This project is open source and available under the MIT License.

## ☕ Support

If you find this project helpful, consider supporting its development:

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Support-orange?style=flat-square&logo=buy-me-a-coffee)](https://buymeacoffee.com/asheint)

## 🔗 Links

- **Repository**: [https://github.com/asheint/advanced-research-agent](https://github.com/asheint/advanced-research-agent)
- **Support**: [https://buymeacoffee.com/asheint](https://buymeacoffee.com/asheint)

---

⭐ **Star this repository if you find it helpful!**
