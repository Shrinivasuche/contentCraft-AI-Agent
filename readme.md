# ✨ ContentCraft – AI Social Media Agent

An AI-powered agent that generates platform-specific social media captions, carousel ideas, reel ideas, and content plans using the Google Gemini API.

## 🔗 Live Demo
Try the live app here:  
👉 https://contentcraft-ai-agent-dmkpvbgvefjyg5vrtv8bcd.streamlit.app


## 🚀 Project Overview

ContentCraft is a Streamlit-based AI agent that helps brands and creators instantly generate high-quality, platform-optimized social media content.

This agent uses Google Gemini models to produce:

* Captions
* Multi-post ideas
* Weekly content plans
* Hashtag groups
* Platform-tailored writing styles
* All generated using your custom brand details, tone, niche, and goals.


## 🎯 Features
✔ Multi-Platform Content
* Instagram
* LinkedIn
* Twitter/X
* YouTube
* Facebook

✔ Multiple Content Types
* Single post captions
* Carousel ideas
* Reels/Short video ideas
* Long-form LinkedIn style posts
* Weekly content plans

✔ AI Model Used
* models/gemini-flash-latest (Fastest, free, text-capable model)

## 🧠 Tech Stack

| Component            | Technology                                     |
|----------------------|-------------------------------------------------|
| Programming Language | Python                                          |
| AI Model             | Gemini Flash (`models/gemini-flash-latest`)     |
| Frontend             | Streamlit                                       |
| Backend Workflow     | Python functions + Google Generative AI         |
| Deployment           | Streamlit Cloud                                 |
| Environment          | virtualenv / Python 3.12                        |


🏗 Architecture:

<p align="center">
  <img src="docs/Architecture-diagram.png" width="700" />
</p>


## 🔧 Installation & Local Setup

### **1. Clone the repository**

git clone https://github.com/Shrinivasuche/contentCraft-AI-Agent.git

cd contentcraft-ai-agent

### **2. Create & activate virtual environment**

python -m venv venv

* Windows:
venv\Scripts\activate

* Mac/Linux:
source venv/bin/activate

### **3. Install dependencies**

pip install -r requirements.txt

### **4. Add your Gemini API key**

* Set in the terminal:
export GEMINI_API_KEY="your_key_here"

* On Windows PowerShell:
setx GEMINI_API_KEY "your_key_here"

### **5. Run the app**

streamlit run app.py


## 🌐 Deployment (Streamlit Cloud)

* Go to: https://share.streamlit.io
* Connect your GitHub account
* Select this repo
* Set file path = app.py

### **Add Secrets:**
GEMINI_API_KEY = "your_key_here"

Deploy → Get your public link.
