from flask import Flask 

#app = Flask(__name__)
app = Flask(__name__)

#give a root to access the page 
@app.route("/") #this will take your to the homepage 
# return what is displayed on the page 
def home():
    return "Hello! this is the main page <h1>Hello<h1>"

if __name__ == "__main__":
    app.run()