# AI-Powered Code Generator (Using Groq API - Mixtral 8x7B)

## 🚀 Overview
This project is an AI-powered code generator that uses the **Groq API (Mixtral 8x7B or another free model)** to generate, optimize, and debug code. The tool is designed to assist developers in writing efficient and well-documented code with AI assistance.

## ✨ Features
- **AI-Powered Code Generation** → Generate code in multiple languages (Python, JavaScript, C++, Java, etc.).
- **Code Optimization & Debugging** → AI analyzes, fixes errors, and suggests improvements.
- **AI-Generated Documentation** → Auto-generate inline comments and README.md files.
- **Multi-Platform Support** → Web UI (Streamlit) and CLI tool.
- **Free & Fast** → Uses Groq API (Mixtral 8x7B) for cost-effective AI-powered coding.

---

## 🛠️ Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/mharoon1578/ai-code-generator.git
cd ai-code-generator
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up Groq API Key
1. Get an API key from [Groq Console](https://console.groq.com/).
2. Create a **.env** file and add your key:
```ini
GROQ_API_KEY=your_api_key_here
```

---

## 🎯 Usage
### CLI Mode
```bash
python generate.py --prompt "Write a Python function for quicksort"
```

To enable debugging & optimization:
```bash
python generate.py --prompt "Write a Python function for quicksort" --debug
```

### Web UI Mode
```bash
streamlit run app.py
```

---

## 📜 Project Structure
```
ai-code-generator/
│── app.py          # Streamlit web UI
│── generate.py     # CLI tool for code generation & debugging
│── api.py          # Handles AI API requests
│── requirements.txt # Dependencies
│── .env.example    # Environment variable template
│── README.md       # Project documentation
│── LICENSE         # License file
```

---

## 📢 Contributing
Contributions are welcome! Feel free to fork the repo, open issues, or submit PRs.

---

## 📜 License
This project is licensed under the MIT License.

