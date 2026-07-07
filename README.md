# 🤖 Agentic AI & Generative AI Learning Hub

Welcome to the **Agentic AI & Generative AI Learning Hub**! This repository is a structured, hands-on learning environment designed to take you from foundational Large Language Model (LLM) prompts to advanced, multi-agent orchestrations and Model Context Protocol (MCP) integrations using **LangChain** and **LangGraph**.

The goal of this repository is to build a robust mental model of LLM architectures, tool-calling capabilities, conversational memory, stateful graphs, and collaborative multi-agent patterns.

---

## 📁 Repository Directory Structure

Here is the complete layout of the learning modules, notebooks, and projects in this repository:

```text
agentic-ai-genai-learning/
│
├── langchain-1/
│   └── langchain_docs_Course/
│       ├── module1/                       # Foundational LangChain & Single-Agent Concepts
│       │   ├── 1.1_foundational_model.ipynb  # Initializing LLMs (Groq, Gemini), Invoking, Streaming, Batching
│       │   ├── 1.1_prompting.ipynb        # Chat prompts, formatting system messages, and templates
│       │   ├── 1.2_tools.ipynb            # Defining custom tools using `@tool` decorator
│       │   ├── 1.2_web_search.ipynb       # Real-time search tools (Tavily search API integration)
│       │   ├── 1.3_memory.ipynb           # Integrating conversational history and memory systems
│       │   ├── 1.4_multimodel_msg.ipynb   # Multimodal interactions (handling images, audio, video)
│       │   ├── 1.5_personal_chef.ipynb    # Interactive notebook for recipe generation
│       │   └── personal_chef.py           # Single-agent assistant utilizing custom web search
│       │
│       ├── module2/                       # Advanced Agent Paradigms & Multi-Agent Workflows
│       │   ├── 2.1_mcp.ipynb              # Model Context Protocol (MCP) integrations & client connections
│       │   ├── 2.1_travel_agent.ipynb     # Building a stateful travel planning agent
│       │   ├── 2.2_runtime_context.ipynb  # Running context dynamically in agent executions
│       │   ├── 2.3_multi_agent.ipynb      # Introductions to multi-agent collaboration & supervisor routing
│       │   ├── 2.4_wedding_planners.ipynb # Collaborative multi-agent workflow for wedding planning
│       │   └── resources/                 # Scripts and configurations for MCP servers and agents
│       │
│       └── module3/                       # Placeholder for advanced projects and future topics
│
├── langgraph/
│   └── basic_chat_bot/
│       └── 1basic_chatbot.ipynb          # LangGraph fundamentals: State, Nodes, Edges, Graphs, and Compilation
│
├── main.py                                # Simple baseline verification script
├── requirement.txt                        # Python dependencies catalog
├── uv.lock                                # Fast package management lockfile (UV)
├── .env.example                           # Template for API credentials and local variables
└── .gitignore                             # Ignored files (virtual environments, keys, logs)
```

---

## 📖 Module Details & Learning Paths

### 🌟 Module 1: Foundational Agentic Concepts
* **[1.1_foundational_model.ipynb](file:///d:/agentic-ai-genai-learning/langchain-1/langchain_docs_Course/module1/1.1_foundational_model.ipynb)**: Introduction to LangChain's `init_chat_model` using providers like Google GenAI (Gemini) and Groq. Covers standard invocation, real-time streaming, and high-concurrency batch execution.
* **[1.1_prompting.ipynb](file:///d:/agentic-ai-genai-learning/langchain-1/langchain_docs_Course/module1/1.1_prompting.ipynb)**: Master structural prompt patterns, system-level guidelines, and parameter optimization.
* **[1.2_tools.ipynb](file:///d:/agentic-ai-genai-learning/langchain-1/langchain_docs_Course/module1/1.2_tools.ipynb)**: Learn how to declare tool signatures using Pydantic validation schemas and bind them directly to LLMs.
* **[1.2_web_search.ipynb](file:///d:/agentic-ai-genai-learning/langchain-1/langchain_docs_Course/module1/1.2_web_search.ipynb)**: Set up and query search indices using the Tavily API to give agents real-time web capabilities.
* **[1.3_memory.ipynb](file:///d:/agentic-ai-genai-learning/langchain-1/langchain_docs_Course/module1/1.3_memory.ipynb)**: Understand how chat history is maintained using message history savers.
* **[1.4_multimodel_msg.ipynb](file:///d:/agentic-ai-genai-learning/langchain-1/langchain_docs_Course/module1/1.4_multimodel_msg.ipynb)**: Work with vision, audio, and documents inside system message payloads.
* **[1.5_personal_chef.ipynb](file:///d:/agentic-ai-genai-learning/langchain-1/langchain_docs_Course/module1/1.5_personal_chef.ipynb)** & **[personal_chef.py](file:///d:/agentic-ai-genai-learning/langchain-1/langchain_docs_Course/module1/personal_chef.py)**: Build an agent that suggests recipes based on leftover ingredients.

### 🚀 Module 2: Stateful & Multi-Agent Architecture
* **[2.1_mcp.ipynb](file:///d:/agentic-ai-genai-learning/langchain-1/langchain_docs_Course/module2/2.1_mcp.ipynb)**: Work with Anthropic's **Model Context Protocol (MCP)**, connecting LLMs directly to external client/server environments to read/write system data.
* **[2.1_travel_agent.ipynb](file:///d:/agentic-ai-genai-learning/langchain-1/langchain_docs_Course/module2/2.1_travel_agent.ipynb)**: Create a conversational travel coordinator containing custom itinerary tools.
* **[2.2_runtime_context.ipynb](file:///d:/agentic-ai-genai-learning/langchain-1/langchain_docs_Course/module2/2.2_runtime_context.ipynb)**: Inspect, query, and inject context during runtime execution loops.
* **[2.3_multi_agent.ipynb](file:///d:/agentic-ai-genai-learning/langchain-1/langchain_docs_Course/module2/2.3_multi_agent.ipynb)**: Orchestrate multiple specialized agents communicating with each other through a supervisor model.
* **[2.4_wedding_planners.ipynb](file:///d:/agentic-ai-genai-learning/langchain-1/langchain_docs_Course/module2/2.4_wedding_planners.ipynb)**: An end-to-end multi-agent pipeline simulating a comprehensive wedding planner system with budget coordinators, venue hunters, and user review loops.

### 🕸️ LangGraph: Chatbots and Workflows
* **[1basic_chatbot.ipynb](file:///d:/agentic-ai-genai-learning/langgraph/basic_chat_bot/1basic_chatbot.ipynb)**: Explores stateful loops using LangGraph, building nodes that modify conversation states, defining transition edges, and compiling complex system graphs.

---

## 🛠️ Getting Started

Follow these instructions to set up your virtual environment, install dependencies, and run the learning notebooks:

### 1. Prerequisites
Ensure you have **Python 3.10+** installed on your system.

### 2. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/agentic-ai-genai-learning.git
cd agentic-ai-genai-learning
```

### 3. Create a Virtual Environment

#### Option A: Using `uv` (Recommended - fast and robust)
This repository includes a `uv.lock` file. Using **uv** is the fastest way to get started:
```bash
# Install uv if you don't have it
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Create a virtual environment and sync dependencies
uv venv
.venv\Scripts\activate      # Windows (CMD/PowerShell)
source .venv/bin/activate   # macOS / Linux

# Sync workspace dependencies from uv.lock
uv sync
```

#### Option B: Using Python's standard `venv`
```bash
# Create the environment
python -m venv .venv

# Activate the environment
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
# Windows (CMD)
.venv\Scripts\activate.bat
# macOS/Linux
source .venv/bin/activate

# Install the packages
pip install -r requirement.txt
```

### 4. Setup Environment Variables
Create a local `.env` file from the template provided:
```bash
cp .env.example .env
```

Open `.env` and fill in your API credentials:
* **`GOOGLE_API_KEY`**: Obtain from [Google AI Studio](https://aistudio.google.com/).
* **`groq_api_key`**: Obtain from [Groq Console](https://console.groq.com/).
* **`TAVILY_API_KEY`**: Obtain from [Tavily Dashboard](https://tavily.com/).

> [!CAUTION]
> Never commit your `.env` file to public version control! The `.gitignore` is pre-configured to block pushing `.env` files.

---

## 🚀 Key Libraries Used

* **[LangChain](https://github.com/langchain-ai/langchain)**: Core developer framework for chaining LLM interactions, prompts, and tools.
* **[LangGraph](https://github.com/langchain-ai/langgraph)**: Stateful orchestration framework for modeling complex, cyclic multi-agent structures.
* **[Model Context Protocol (MCP)](https://modelcontextprotocol.io/)**: Open standard protocol that enables LLMs to interface safely with host systems and applications.
* **[langchain-google-genai](https://pypi.org/project/langchain-google-genai/)**: Dedicated client binding for Google Gemini LLMs.
* **[langchain-groq](https://pypi.org/project/langchain-groq/)**: High-speed connector to inference platforms like Groq (supporting Llama/Qwen models).
* **[Tavily](https://tavily.com/)**: Search service optimized specifically for autonomous agent queries.

---

## 📈 Learning Checklist & Roadmap

- [x] Basic prompt invocation, streaming, and batching.
- [x] Custom tool definitions with `@tool` decorators.
- [x] Simple single-agent loops with tool-calling capabilities.
- [x] Vision and multimodal file processing in messages.
- [x] Model Context Protocol (MCP) client-server tools.
- [x] Stateful single-agent flows (Travel Agent).
- [x] Supervisor and Multi-Agent collaborative routing (Wedding Planners).
- [/] Building stateful graphs using LangGraph.
- [ ] Memory-enabled production agents (SQLite/PostgreSQL checkpoint storage).
- [ ] Human-in-the-loop validation (approval states, interrupts, and editing agent state).
- [ ] Enterprise evaluation metrics and monitoring.
