# AI_Career_Mentor
AI Career Mentor Chatbot is a conversational, agentic AI application designed to help students and early-career professionals assess their career readiness through natural language interaction. The system allows users to upload resumes, input skills manually, select target domains and roles, and engage in an ongoing conversation with an AI mentor that analyzes strengths, identifies skill gaps, and provides personalized guidance along with structured 30–60–90 day learning roadmaps. Built using Python, ipywidgets, resume parsing tools, and a Large Language Model (Perplexity API), the project demonstrates practical application of AI for social impact and aligns with UN SDG 8: Decent Work and Economic Growth by promoting skill development, employability, and equitable access to career guidance.

# Key Features
- 💬 Free-form conversational chatbot (ChatGPT-style interaction)
- 📄 Resume upload support (PDF parsing)
- ✍️ Manual skill input for flexibility
- 🎯 Domain & role-based guidance using a structured knowledge base
- 🧠 Context-aware AI reasoning with conversation memory
- 📊 Skill gap analysis & readiness scoring
- 📅 Personalized 30–60–90 day learning roadmap
- 🛡️ Graceful fallback mechanism when LLM API is unavailable
- ⚖️ Ethical & responsible AI design (no data storage, no bias amplification)

# How to Run the Project
**1. Clone the Repository**
git clone https://github.com/0xheaptrace/AI_Career_Mentor.git
cd AI_Career_Mentor

**2. Install Dependencies**
pip install -r requirements.txt

**3. Set API Key (Perplexity)**
export PERPLEXITY_API_KEY="your_api_key_here"
(Use setx on Windows)

**4. Launch the Notebook**
jupyter notebook notebooks/ai_agent.ipynb

**5. Use the Chatbot**
- Upload a resume (optional)
- Enter skills manually (optional)
- Select domain and role
- Start chatting with the AI career mentor


# - By Dhruv
