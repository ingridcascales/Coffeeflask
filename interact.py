from flask import Flask, render_template, request
import requests

app = Flask("MyApp")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/menu")
def menu():
    return render_template('menu.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

def send_simple_message(message,email):
    return requests.post("https://api.mailgun.net/v3/sandbox32a8337d071b45849f80c6f363682640.mailgun.org/messages",
        auth=("api", "230870b40f44351bad4f816aa9743e66-8889127d-ee047b69"),
            data={"from": "Coffee Flask <mailgun@sandbox32a8337d071b45849f80c6f363682640.mailgun.org>",
              "to": ["ingridcascales@gmail.com"],
              "subject": "Coffee Flask Newsletter",
              "text": "Hi there! Thank you for your subscription!"})

@app.route("/email", methods = ["POST"])
def email_handler():
   name = request.form["name"]
   email = request.form["email"]
   email = "ingridcascales@gmail.com"
   message = "Hello  %s" % name
   resp = send_simple_message(message,email)
   print (resp.text)
   print (resp.status_code)
   return "Thank you. Your email was sent sucessfully"


   # call your function here to send a email


# user_name = get_userName()
# greet_user = greet_user(user_name)
# user_coffee = get_coffee()
# user_pastry = get_pastry()



# print "Great " + user_name + "! We'll get you a " + user_coffee + " and a " + user_pastry + " right away!"
if __name__ == '__main__':
    app.run(debug=True)
