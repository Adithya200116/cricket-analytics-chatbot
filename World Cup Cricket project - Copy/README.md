
Cricket Analytics Chatbot  

Project Overview
This project is a Cricket Analytics Chatbot built using Flask and Machine Learning. It provides users with detailed cricket insights by processing structured data and answering natural language queries. The chatbot is capable of answering questions related to batting, bowling, match details, and player performances by leveraging pre-trained models and datasets.  

Key Features:  
- Fetches statistics like runs, wickets, strike rates, economy, and match winners.  
- Handles detailed queries such as "How many sixes did Player X hit?" or "Who won Match Y?"  
- Integrates structured datasets (batting, bowling, match schedules) for dynamic responses.  
- Employs a machine learning model for query intent classification using TfidfVectorizer and Logistic Regression.  

---

How to Use the Project

1. Prerequisites
- Install Python (3.8 or higher).  
- Install required libraries using the command:  
  ```bash
  pip install flask pandas joblib scikit-learn
  ```  
- Ensure the datasets (e.g., `batting.csv`, `bowling.csv`, etc.) and the pre-trained ML model (`trained_model.pkl`) are in the appropriate folders.  

2. Running the Application
1. Open a terminal and navigate to the project directory.  
2. Run the Flask app:  
   ```bash
   python app.py
   ```  
3. Access the application in your browser at: `http://127.0.0.1:5000`.  

3. Using the Chatbot
- Enter cricket-related questions into the chatbot interface, such as:  
  - "How many runs did Virat Kohli score?"  
  - "Who won Match 5?"  
  - "What is Jasprit Bumrah's economy rate?"  
- The chatbot will process the query and return the requested information.  

