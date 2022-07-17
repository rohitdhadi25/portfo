# from urllib import request
from flask import Flask,render_template,request,redirect
import csv
app=Flask(__name__)
print(__name__)
@app.route('/home')
def hello_world():
    return 'Hello, hiii !!!'
@app.route('/index.html')
def home():
    return render_template('index.html')   #in this case we have to make template folder and we need to put our index.html file into it.
# @app.route("/works.html")
# def work():
#     return render_template("works.html")    
# @app.route("/about.html")
# def about():
#     return render_template("about.html")      
# @app.route("/contact.html")
# def contact():
#     return render_template("contact.html")      
# @app.route("/components.html")
# def components():
#     return render_template("components.html")      
# @app.route('/mywebsite')
# def mywebsite():
#     return render_template('my_own_website.html')    


#===============================================================

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)
def write_to_file(data):
    with open('database.txt',mode='a') as data_base_file_obj:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        file=data_base_file_obj.write(f"\n{email},{subject},{message}")

def write_to_csv(data):
    with open('database.csv',mode='a') as data_base_file_obj_csv:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        csv_writer=csv.writer(data_base_file_obj_csv,delimiter=",", quotechar="'", newline='', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method =="POST":
        data=request.form.to_dict()
        write_to_csv(data)
        return redirect("/thankyou.html")
        return 'form_submitted'
    else:
        return 'something went wrong'    