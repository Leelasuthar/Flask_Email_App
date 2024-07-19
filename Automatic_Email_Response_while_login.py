from flask import Flask, request, render_template, redirect, url_for
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

app = Flask(__name__)

def send_welcome_email(sender_email, app_password, recipient_email, username, registration_date):
    subject = "Welcome to Affirmation App"
    message = f"""
    <html>
    <body>
        <p>Dear {username},</p>
        <p>Welcome to Affirmation App! We are excited to have you on board.</p>
        <p>Here are your account details:</p>
        <ul>
            <li>Username: {username}</li>
            <li>Registration date: {registration_date}</li>
        </ul>
        <p>Feel free to explore our features and let us know if you have any questions.</p>
        <p>Best regards,<br>The Affirmation App Team</p>
    </body>
    </html>
    """

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'html'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            print("Logging in to SMTP server...")
            server.login(sender_email, app_password)
            print("Logged in, sending email...")
            server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['name']
        email = request.form['email']
        registration_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sender_email = " " #enter the sender's email
        app_password = " " #enter the app password obtained after 2-step verfication 

        send_welcome_email(sender_email, app_password, email, username, registration_date)
        return redirect(url_for('success'))
    return render_template('register.html')

@app.route('/success')
def success():
    return "Registration successful! A welcome email has been sent."

if __name__ == '__main__':
    app.run(debug=True)
