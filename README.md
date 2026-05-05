**🛡️ Influencer Guard Pro AI-Based Suspicious Comment Detection & Moderation System**


**🚀 Overview**

Influencer Guard Pro is a smart web-based system that automatically detects suspicious, unsafe, or harmful comments using a custom NLP-based approach.

It helps in real-time moderation by analyzing user comments and taking intelligent actions such as blocking, flagging, or approving content.

**🎯 Key Features**

🔍 Real-time Comment Analysis
⚠️ Detects Safe, Suspicious, and Unsafe Content
🧠 Custom NLP-based Keyword & Context Analysis
🚫 Auto-Blocking Users after repeated violations
🏷️ Manual Actions:
       Block
       Flag
       Approve
📊 History & Analytics Dashboard
👤 User Behavior Tracking (Strike System)

**🧠 How It Works**
1. User enters a comment
2. System analyzes text using keyword matching
3. Assigns a risk score
4. Applies threshold logic
5. Classifies comment:
     ✅ Safe
     ⚠️ Suspicious
    🚨 Unsafe
6. Stores result in database
7. Tracks user violations for auto-blocking

   
**⚙️ Algorithm Logic**
Strong keywords (kill, attack, explode) → High risk
Medium keywords (bomb) → Moderate risk
Context words (hotel, airport, etc.) → Increase severity
Positive words → Reduce risk

**📌 Classification:**
Score ≥ 1 → Unsafe
Score ≥ 0.5 → Suspicious
Else → Safe


**🏗️ Tech Stack**
🐍 Python (Flask)
🗄️ SQLite Database
🌐 HTML, CSS, JavaScript
⚡ REST API (Flask routes)

**📂 Project Structure**

InfluencerGuard/ 


├── app.py

├── history.db


├── templates/

     └── index.html



**▶️ How to Run**

# Install dependencies
pip install flask

# Run the app
python app.py

  Open browser:

  http://127.0.0.1:5000

  
📸 Screenshots of Webpage Created

Home Dashboard
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/242a94b5-3bba-41fc-aa19-2c07cec00cb8" />

Comment Analysis
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/820dcada-52d1-48e0-a4fb-df9f7bb21532" />

History & Analytics
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/7ea050cd-5a99-4879-9be1-8f3585de2ea2" />

Auto-Block Feature
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/3232bd53-f959-43f9-a93b-7cd0a73c3e62" />


📊 Example Use Case

Input:

"There is a bomb in the hotel"

Output:

⚠️ Suspicious / 🚨 Unsafe


**🔐 Auto-Block Feature**
Tracks repeated unsafe behavior
Automatically blocks users after threshold
Prevents further commenting

**📈 Advantages**
Fast and real-time moderation
Reduces manual effort
Improves platform safety
Simple and efficient implementation

**⚠️ Limitations**
Rule-based (not deep learning)
Limited vocabulary detection
May require updates for new patterns


**🔮 Future Scope**
Integrate Machine Learning / Deep Learning
Add sentiment analysis
Deploy as browser extension
Real-time API integration with social media
