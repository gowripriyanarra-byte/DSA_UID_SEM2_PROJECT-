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


Algorithms Used in AI-Based Suspicious Comment Detection System



1. Rule-Based Classification Algorithm

The Rule-Based Classification Algorithm is the foundation of the system. It uses predefined rules to analyze user input and classify it accordingly.

✔️ How it works:
A set of predefined rules is created
Each rule checks for specific patterns or words
If a rule condition is satisfied, a classification is triggered
📌 Example:
If text contains "kill" → mark as suspicious
If text contains "great job" → mark as safe
✅ Advantages:
Simple and fast
Easy to implement and understand


🔹 2. Keyword Matching Algorithm

This algorithm scans the input text for the presence of sensitive or predefined keywords.

✔️ How it works:
Input text is converted to lowercase
Each word is compared against a keyword dictionary
Matches are identified and processed
📌 Example:
Input: "I will attack"
Match found: "attack"
✅ Purpose:
Detect potentially harmful intent quickly
Acts as the first filtering layer



🔹 3. Custom Scoring Algorithm (Risk Scoring Model)

This algorithm assigns a risk score to the input text based on detected keywords.

✔️ How it works:
Each sensitive word has a weight (severity score)
When a word is detected, its score is added to a total
Final score determines risk level
📌 Example:
Word	Score
bomb	1.0
attack	0.8
Input: "bomb attack"
Total Score = 1.0 + 0.8 = 1.8
✅ Purpose:
Provides quantitative analysis
Helps in more flexible decision-making
🔹 4. Context-Based Analysis Algorithm

This algorithm improves accuracy by analyzing the context or intent of the sentence.

✔️ How it works:
Looks for safe/neutral context words
Reduces risk score if the sentence appears harmless
📌 Example:
"You look like a bomb"
"bomb" → dangerous
"look" → safe context

👉 Final interpretation: Compliment, not threat

✅ Purpose:
Reduces false positives
Handles slang and informal language
