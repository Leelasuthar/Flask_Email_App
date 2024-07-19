# Flask-Email-App

## Setup Instructions

## 1. Clone the Repository
```
git clone https://github.com/your-username/flask_email_app.git
cd flask_email_app
```

## 2. Install Dependencies
Make sure you have a requirements.txt file with the necessary packages listed. Install them using:
```
pip install -r requirements.txt
```

## 3. Generate a Gmail App Password
Follow these steps to generate an app password:
### Go to Your Google Account Settings:
Visit [Google Account Security](https://myaccount.google.com)
### Enable 2-Step Verification (if not already enabled):
1. Scroll down to the "Signing in to Google" section and click on "2-Step Verification."
2. Follow the instructions to set up 2-Step Verification if it’s not already enabled.
### Generate an App Password:
1. After enabling 2-Step Verification, return to the "Security" section.
2. Scroll down to "App passwords" and click on it.
3. You may need to sign in again for security verification.
4. Under "Select app," choose "Other (Custom name)" and enter a name like "Flask App."
5. Click "Generate."
6. Copy the generated password (it will look like abcd efgh ijkl mnop).

## 4. Update Your Configuration
In Automatic_email_response_while_login.py, replace the placeholders with your actual email and the generated app password:
```
sender_email = " " #enter the sender's email
app_password = " " #enter the app password obtained after 2-step verfication
```

## 5. Run the Flask Application
Start your Flask application:
```
python Automatic_email_response_while_login.py
```
By default, the app will be available at http://127.0.0.1:5000/.


