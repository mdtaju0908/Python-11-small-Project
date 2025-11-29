from flask import Flask
app = Flask(__name__)#run a html code 

@app.route("/hello")
def home():
    return """
    <h1> I am Home Page </h1>
    <h2> I am running in flask</h2>
    """
@app.route("/abouta")
def abouta():
    return"""
    <!DOCTYPE html>
    <html>
    <head>
    <title>My First Page</title>
    </head>
    <body>
    <h1>Welcome to My Website</h1>
    <p>This is a simple HTML page.</p>
    <button onclick="alert('Ram Ram Ji!')">Click Me</button>
    </body>
    </html>
    """
if __name__=='__main__':
    app.run()