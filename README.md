# 📄 Ask Your PDF Anything

A simple Streamlit app that lets you upload a PDF and ask questions based on its content using **Gemini 1.5 Flash (via Google Generative AI API)**.  
It uses **LangChain**, **FAISS**, and **Google Generative AI Embeddings** to create a powerful document-based Question-Answering chatbot.

---

## 🚀 Features

- 📄 Upload any PDF file  
- 🔍 Ask natural language questions  
- 🧠 Uses Gemini 1.5 Flash (Free API model from Google)  
- 📚 Chunk-based document retrieval with FAISS  
- 🖥️ Minimal web UI built using Streamlit  

---

## 🛠️ Technologies Used

- **Python**  
- **Streamlit**  
- **LangChain**  
- **FAISS**  
- **Google Generative AI (Gemini)**  
- **dotenv** (to manage API keys)  

---

## 📂 Folder Structure


```
project/
│
├── app.py              # Main Streamlit application
├── .env                # Contains your API key
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 🔐 Setup: API Key
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey) and generate your API key.  
2. Create a `.env` file in the project directory and add the following line:

```
GOOGLE_API_KEY=your_google_gemini_api_key
```

---

## 💻 How to Run the App

### 1. Clone the Repository  

```
git clone https://github.com/your-username/ask-your-pdf-gemini.git
cd ask-your-pdf-gemini
```

### 2. Install Dependencies  
```
pip install -r requirements.txt
```

_If `requirements.txt` is not available:_

```
pip install streamlit langchain faiss-cpu pypdf python-dotenv langchain-google-genai
```

### 3. Run the App  
```
streamlit run app.py
```

---

## 🌐 Usage

1. Open the app in your browser (usually at [http://localhost:8501](http://localhost:8501))  
2. Upload a PDF document  
3. Ask any question related to the content  
4. Get an instant AI-powered answer from the Gemini model  

---

## 📌 Example

> Upload a PDF about **"Climate Change"**  
> Ask: **"What are the major causes of climate change?"**  
> ✅ Gemini responds with a concise, document-aware answer.

---

## 🧠 How It Works

_Explain the internal flow using bullet points:_

- The uploaded PDF is parsed and split into chunks using **LangChain**  
- Each chunk is embedded using **GoogleGenerativeAIEmbeddings**  
- **FAISS** creates a vector store from those chunks  
- On user input, relevant chunks are retrieved via similarity search  
- **Gemini** generates an answer using the retrieved context  

---

## ✅ Requirements

- Python 3.8 or higher  
- Google API key for Gemini  
- Internet connection to access Gemini API  

---

## 🛡️ License

This project is open-source and free to use under the **MIT License**.

---

## 🙌 Acknowledgements

- LangChain  
- Google AI Studio  
- Streamlit