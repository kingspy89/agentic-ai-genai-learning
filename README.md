# 🤖 Agentic AI & Generative AI Learning Hub

Welcome to the **Agentic AI & Generative AI Learning Hub**! This repository is dedicated to learning the fundamentals and advanced concepts of building LLM-powered autonomous agents, custom tools, and multi-agent workflows.

The primary goal of this repository is to learn Agentic AI through hands-on, project-based implementation using **LangChain**, **LangGraph**, and state-of-the-art model providers.

---

## 📁 Repository Structure

Below is the directory layout and description of the learning materials in this project:

```text
agentic-ai-genai-learning/
│
├── langchain-1/                     # Basic & Intermediate LangChain concepts
│   ├── langchain.ipynb              # Basics of invoking, streaming, and batching
│   └── MULTI_AGENT_TOOL.ipynb       # Integrating external tools (Tavily, Calculator) into Agents
│
├── tools.ipynb                      # Deep-dive into defining custom tools with decorators
├── main.py                          # Basic Python setup and sanity check script
│
├── requirement.txt                  # Python dependencies
├── .env.example                     # Environment template for API keys
└── .gitignore                       # Ensures local configuration and caches are ignored
```

### 📓 Notebook Descriptions

1. **`langchain-1/langchain.ipynb`**:
   * **Topics Covered**: LangChain basics, Model initialization (Gemini via Google GenAI), Streaming responses token-by-token, Batch invocations with concurrency limits (`max_concurrency`).
2. **`langchain-1/MULTI_AGENT_TOOL.ipynb`**:
   * **Topics Covered**: Constructing intelligent agents with multiple capabilities. Uses `TavilySearch` for real-time web search and a custom calculator tool. Demonstrates streaming step-by-step execution.
3. **`tools.ipynb`**:
   * **Topics Covered**: Utilizing the `@tool` decorator to define reusable tools (e.g., weather fetching), binding tools to model definitions, and building conversational agents capable of execution-loops.

---

## 🛠️ Getting Started

Follow these steps to set up the environment and run the code locally:

### 1. Prerequisites
Ensure you have **Python 3.10+** installed on your system.

### 2. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/agentic-ai-genai-learning.git
cd agentic-ai-genai-learning
```

### 3. Create a Virtual Environment
It is highly recommended to use a virtual environment to manage dependencies.

**Using python's built-in `venv`:**
```bash
python -m venv .venv
# On Windows (Command Prompt)
.venv\Scripts\activate
# On Windows (PowerShell)
.venv\Scripts\Activate.ps1
# On macOS/Linux
source .venv/bin/activate
```

**Or using `uv` (recommended for faster package installation):**
```bash
uv venv
.venv\Scripts\activate  # Adjust activation script for your OS/Shell
```

### 4. Install Dependencies
```bash
pip install -r requirement.txt
```

### 5. Setup Environment Variables
Create a local `.env` file by copying the template file:
```bash
cp .env.example .env
```
Open the `.env` file and insert your API keys:
* **`GOOGLE_API_KEY`**: Obtain from Google AI Studio.
* **`groq_api_key`**: Obtain from Groq Console.
* **`TAVILY_API_KEY`**: Obtain from Tavily Search.

> [!CAUTION]
> Never commit your `.env` file to public version control! The `.gitignore` in this repository is already configured to ignore `.env` files to prevent accidental leakage.

---

## 🚀 Key Libraries Used

* **[LangChain](https://github.com/langchain-ai/langchain)**: Framework for developing applications powered by large language models.
* **[LangGraph](https://github.com/langchain-ai/langgraph)**: Building stateful, multi-actor applications with LLMs.
* **[langchain-google-genai](https://pypi.org/project/langchain-google-genai/)**: LangChain integration with Google Gemini models.
* **[langchain-groq](https://pypi.org/project/langchain-groq/)**: LangChain integration with Groq for ultra-fast open-source LLMs.
* **[langchain-tavily](https://pypi.org/project/langchain-tavily/)**: Search tool API optimized for LLMs.

---

## 📈 Roadmap & Learning Checklist

Here is a checklist of ideas to expand your knowledge of Agentic AI:
- [x] Basic prompt invocation, streaming, and batching.
- [x] Custom tool definitions with `@tool` decorators.
- [x] Simple tool-calling agents.
- [ ] Stateful agent patterns using LangGraph.
- [ ] Memory-enabled agents (storing chat history in SQLite/PostgreSQL).
- [ ] Human-in-the-loop validation (allowing review before an agent executes a tool).
- [ ] Multi-agent collaboration architectures (e.g., supervisor pattern).

---

## 🤝 Contributing & Feedback

Feel free to fork this repository, add your own experiments, or submit PRs if you find bugs or want to add new learning paths!
