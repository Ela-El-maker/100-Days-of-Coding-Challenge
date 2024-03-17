import smtplib


toSendee = input("Enter the email address to receiver: ")

message = input("Please enter the message:- ")

def sendEmail(toSendee,message):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('xft95591@zslsz.com', '#One.')
        server.sendmail('xft95591@zslsz.com', ['xfthd093js@zslsz.com'], 'Hello World!')
        server.close()
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError as e:
        print("SMTP Authentication Error:", e)
    except Exception as e:
        print("An error occurred:", e)
# sendEmail()


sendEmail(toSendee, message)