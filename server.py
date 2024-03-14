# debug run:        flask --app filename run --debug
# Free HTML templates:  https://html5up.net/

from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():  ## url_for work with name of def
    return render_template("index.html")

@app.route("/project")
def project():
    return render_template("work.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

def write_to_file(data):
    """
    This function can add data to .txt database
    """
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f"\n{email},{subject},{message}")
    return file

def write_to_csv(data):
    """
    This function can add data to .txt database
    """
    with open('database.csv', mode='a', newline="") as csv_database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writter = csv.writer(csv_database, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        csv_writter.writerow([email,subject,message])

# Keep in mind: all inputs in form in html must have a `name=`` tage
# The 'name=' is the way we interact with a form --> you can check form data in developer tool
@app.route("/submit_form", methods=['POST','GET']) # This /submit_form will be active with action in form
def email_form(): # After activation of route ---> def will be active
    if request.method == 'POST':
        try:
            # data is our forms input
            data = request.form.to_dict()
            # Add to .txt database & .csv database
            # write_to_file(data)
            write_to_csv(data)
            print(f"form new information in dict status: {data}")
            return render_template("/thankyou.html", email_name=data['email'])
        except:
            return "Your data is not saved! try again!"
    return f"Something is wrong. Try again!"
