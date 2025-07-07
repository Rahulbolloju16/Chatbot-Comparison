
# 🤖 Chatbot Comparison: Traditional vs Generative AI Models

This project compares the performance and capabilities of **traditional chatbot frameworks** with **modern Generative AI-powered agents** using a unified dataset and evaluation framework.

---

## 📌 Objectives

- Benchmark multiple chatbot architectures under consistent input
- Evaluate generative vs rule-based chatbot accuracy, relevance, and speed
- Enable extensibility for future models and datasets

---

## 📁 Project Structure

```
Chatbot-Comparison/
├── bots/                     # All chatbot implementations
│   ├── base_bot.py           # Interface all bots inherit from
│   ├── openai_bot.py         # OpenAI GPT-based bot
│   ├── langchain_bot.py      # LangChain agent bot
│   ├── llamaindex_bot.py     # LlamaIndex retrieval-based bot
│   ├── haystack_bot.py       # Haystack pipeline bot
│   ├── fastchat_bot.py       # FastChat / Vicuna-style LLM bot
│   ├── dialogflow_bot.py     # Traditional NLP bot: Dialogflow
│   ├── rasa_bot.py           # Traditional NLP bot: Rasa
│   ├── botpress_bot.py       # Traditional NLP bot: Botpress
│   ├── witai_bot.py          # Traditional NLP bot: Wit.ai
├── data/
│   └── Knowledge_base/       # Source documents for question answering
├── datasets/
│   └── test_questions.json   # List of test questions to benchmark all bots
├── evaluate.py               # Main script to compare bots
├── requirements.txt          # Required Python packages
```

---

## 🧠 Models Compared

### 🔹 Generative AI Bots

- **OpenAI GPT (via API)**
- **LangChain Agent**
- **LlamaIndex (RAG)**
- **Haystack Pipeline**
- **FastChat (e.g., Vicuna)**

### 🔸 Traditional Bots

- **Dialogflow**
- **Rasa**
- **Botpress**
- **Wit.ai**

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Rahulbolloju16/Chatbot-Comparison.git
cd Chatbot-Comparison
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your-api-key
```

> Use `python-dotenv` or similar to load these in your code.

### 4. Run Evaluation

```bash
python evaluate.py
```

---

## 📊 Evaluation Metrics

Each bot is evaluated based on:

- ✅ **Accuracy** (Correctness of answer)
- 🧠 **Relevance** (To the source documents)
- ⏱️ **Response Time**
- 💬 **Language Coherence** (for LLMs)

---

## 📉 Sample Results Table

| Bot              | Accuracy | Response Time | Notes                      |
|------------------|----------|----------------|-----------------------------|
| OpenAI GPT-4     | 95%      | 1.2s           | High-quality generation     |
| LangChain Agent  | 90%      | 2.3s           | Strong and grounded         |
| Rasa             | 60%      | 0.8s           | Fast, rule-based            |
| Dialogflow       | 65%      | 1.0s           | Good for structured flows   |

---

## 📦 Use Cases

- Enterprise Q&A systems
- Helpdesk automation
- GenAI prototype benchmarking
- Research/academic comparisons

---

## 🙋 Author

**Rahul Bolloju**  
AI/ML & GenAI Engineer  
🔗 [GitHub Profile](https://github.com/Rahulbolloju16)

---

## 📄 License

This project is licensed under the **MIT License**.  
Use, modify, and contribute freely.

---

## 🔧 Future Enhancements

- [ ] Save evaluation metrics to CSV
- [ ] Add support for vector DBs like FAISS or Pinecone
- [ ] Create a Streamlit UI for interactive testing
- [ ] Include plots and visual comparison charts
