# Agentic: Research Agent
> An AI-powered research assistant built with phidata for academic paper exploration and analysis.

## Overview
`agent` is a dual-agent system designed to help students and researchers explore academic papers efficiently. It combines ArXiv paper analysis with web search capabilities to provide comprehensive research topic suggestions and implementation insights.

The project uses phidata's Agentic AI capabilities, leveraging the Groq LLM (llama-3.1-70b-versatile) for intelligent paper analysis and research gap identification.

## Features
- **Structured Paper Analysis**: Analyzes ArXiv papers with consistent formatting covering:
  - Topic overview
  - Frequent methodologies
  - Implementation techniques
  - Lesser explored areas
- **Web Search Integration**: Performs targeted Google searches for supplementary research
- **PDF Processing**: Extracts and analyzes PDF content using pypdf
- **Research Gap Identification**: Identifies potential areas for innovative research
- **Trend Analysis**: Tracks popular topics and uncommon implementation techniques

## Prerequisites
- Python 3.12
- Conda environment
- Groq API key [Link]
- Project IDX from Google [Link]

## Installation

1. Clone the repository:
```bash
git clone https://github.com/PhoenixAlpha23/agent.git
cd agent
```

2. Set up the Conda environment using dev.nix:
```bash
conda init
conda config --add channels conda-forge
conda install -y -c conda-forge phidata=2.7.6
conda install -y -c conda-forge groq
```

3. Install required packages:
```bash
conda install phidata python-dotenv packaging fastapi uvicorn groq arxiv pypdf
```

4. Set up your Groq API key:
```bash
export GROQ_API_KEY="your_groq_api_key_here"
```

## Usage

### Research Agent
Run the research agent to analyze ArXiv papers:
```bash
conda run python research.py
```

Example query and output:
```
Message: Search arxiv for 'Optical Character Recognition' and 'LLMs'

Response:
Search Results: Optical Character Recognition and Large Language Models (LLMs) on arXiv

Overview:
The intersection of Optical Character Recognition (OCR) and Large Language Models (LLMs) 
is a rapidly evolving field...

[Full structured output with topics, methodologies, and sources]
```

### Web Search Agent
Run web searches for supplementary research:
```bash
conda run python online_search.py
```

Example query and output:
```
Message: Search for research topics in OCR and LLM combination papers

Response:
Based on the search results, here are some potential research topics in the combination
of Optical Character Recognition (OCR) and Large Language Models (LLM)...
```

## Project Structure
```
agent/
├── research.py        # ArXiv research agent implementation
├── online_search.py   # Web search agent implementation
├── requirements.txt   # Project dependencies
└── dev.nix           # Environment configuration for Project IDX
```

## Future Prospects

### Planned Enhancements
- Integration of research and web search agents
- Development of a user interface
- Implementation of advanced search strategies:
  - Citation network analysis
  - Temporal trend analysis
  - Topic modeling using LDA
  - Cross-domain connection identification

### Search Strategy Improvements
- Keyword co-occurrence mapping
- Research gap analysis
- Trend prediction
- Impact factor analysis

## Contributing

#TODO
1.Figure Out Multiagent workflows  

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](#).

## License
[MIT](#) © [PhoenixAlpha23](#)
