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
