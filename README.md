 Email Classification System with PII Masking

This project is an **Email Classification System** that detects and classifies emails into categories while masking sensitive **Personally Identifiable Information (PII)** such as names, emails, phone numbers, and more.

## 🚀 Features

- 🛡️ **PII Masking**: Automatically detects and masks sensitive information in email bodies.
- 📂 **Email Classification**: Uses a trained machine learning model to classify emails into categories like spam, business, personal, etc.
- 🔗 **FastAPI API**: A simple API interface for sending email data and receiving structured JSON responses.
- ⚙️ **No spaCy used**: This project is implemented **without using spaCy** and works **without virtual environments**.

## 📁 Project Structure
email_classifier/ ├── app.py # Main FastAPI app script ├── api.py # Defines the API routes and request/response models ├── models.py # Model loading and utility functions ├── utils.py # PII masking and text preprocessing functions ├── requirements.txt # List of dependencies ├── dataset/ │ └── combined_emails_with_natural_pii.csv ├── model/ │ └── classifier.pkl # Trained ML model └── README.md # This file


## 🧪 How to Use

1. **Clone the repository**:
   git clone https://github.com/yourusername/email-classification-pii-masking.git
   cd email-classification-pii-masking
   
2. Install dependencies:
  pip install -r requirements.txt

3. Run the API locally:
  uvicorn app:app --reload

4. Test the API:
  Open your browser and visit: http://127.0.0.1:8000/docs
  Use the Swagger UI to test POST requests by sending email bodies.

📥 Example API Request

POST /classify/
{
  "email_body": "Hi John, please contact me at john.doe@gmail.com or +1-123-456-7890."
}

✅ Example Response:
{
  "original_email": "Hi John, please contact me at john.doe@gmail.com or +1-123-456-7890.",
  "masked_email": "Hi [NAME], please contact me at [EMAIL] or [PHONE].",
  "category": "personal"
}


🛠 Technologies Used
Python
FastAPI
Scikit-learn
Regular Expressions
Pickle (for model)
VS Code



