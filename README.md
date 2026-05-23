# 🚀 AI Multi-Agent Research System

An AI-powered multi-agent research platform built using LangChain, OpenRouter, and Streamlit that automates the complete research workflow from information discovery to report generation and evaluation.

Instead of relying on a single LLM prompt, this project uses multiple specialized AI agents working together:

🔎 Search Agent → 📄 Reader Agent → ✍ Writer Agent → 🎯 Critic Agent

---

## 📌 Features

✅ Multi-agent architecture  
✅ Automated web research  
✅ URL scraping and information extraction  
✅ Detailed report generation  
✅ AI-based report quality evaluation  
✅ Interactive Streamlit dashboard  
✅ Download generated reports  
✅ Modular architecture for scalability

---

## 🧠 System Architecture

```text
                    User Topic
                         │
                         ▼
                🔎 Search Agent
        (Finds relevant information)
                         │
                         ▼
                📄 Reader Agent
      (Scrapes and extracts web content)
                         │
                         ▼
                 ✍ Writer Agent
      (Generates structured report)
                         │
                         ▼
                 🎯 Critic Agent
      (Reviews and scores report)
                         │
                         ▼
                  Final Output
```

---

## ⚙ Tech Stack

| Component | Technology |
|------------|------------|
| LLM Framework | LangChain |
| Model Provider | OpenRouter |
| LLM | GPT-4o Mini |
| Frontend | Streamlit |
| Web Search | Custom Search Tool |
| Web Scraping | BeautifulSoup |
| Environment Variables | Python Dotenv |
| Language | Python |

---

## 📂 Project Structure

```text
Langchain-Multi-Agent-Research-System/
│
├── app.py
├── main.py
├── requirements.txt
├── .env
├── README.md
│
├── src/
│
│   ├── agents/
│   │      └── agents.py
│   │
│   ├── pipeline/
│   │      └── pipeline.py
│   │
│   └── tools/
│          └── tools.py
```

---

## 🔧 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Langchain-Multi-Agent-Research-System.git
```

Move into project directory:

```bash
cd Langchain-Multi-Agent-Research-System
```

Create virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key_here
```

Get API key from:

https://openrouter.ai/

---

## ▶ Run Application

### Streamlit UI

```bash
streamlit run app.py
```

### Terminal Mode

```bash
python main.py
```

---

## 🖥 User Interface

The dashboard includes:

- Interactive research topic input
- Agent workflow visualization
- Progress tracking
- Search results display
- Scraped content display
- Final report generation
- Critic feedback section
- Report download functionality

---

## 📝 Example Workflow

Input:

```text
Future of Generative AI in Healthcare
```

Process:

```text
Search Agent
↓
Reader Agent
↓
Writer Agent
↓
Critic Agent
```

Output:

```text
✔ Research Findings
✔ Structured Report
✔ Quality Evaluation
✔ Downloadable Report
```

---

## 🎯 Future Enhancements

- PDF report generation
- LangGraph workflow integration
- Memory-enabled agents
- Vector database support
- Advanced RAG pipeline
- Multi-model selection
- Research history storage
- Real-time agent logs
- Authentication system
- Deployment on cloud platforms

---

## 📈 Use Cases

### Research Automation
Automate lengthy online research tasks.

### Academic Assistance
Generate structured study material and reports.

### Market Research
Collect and summarize market trends.

### Business Intelligence
Extract insights from multiple sources.

### Competitive Analysis
Compare technologies, products, and companies.

---

## 🤝 Contributing

Contributions are welcome.

Steps:

1. Fork repository
2. Create feature branch

```bash
git checkout -b feature/new-feature
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push changes

```bash
git push origin feature/new-feature
```

5. Open Pull Request

---

## 📜 License

This project is licensed under the MIT License.



