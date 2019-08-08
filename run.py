import os

#We are importing the Flask class
from flask import Flask

"""
We are creating instance of this and storing it in a variable called app
The first argument of the Flask class is the name of the applications module - our package
Since we are using a single module , we can use __name__ which is a built-in Python variable
"""
app = Flask(__name__)

"""
We're then using the app.route decorator. In Python, a decorator starts with the @ sign, which is
also called pie notation.
"""
@app.route("/")
def index():
    return "Hello, World"

"""
We can import "os" from the standard Python library, and
then we're going to reference this built-in variable and say that
if __name__ == "__main__":
then we're going to run our app with the following
arguments: the host is going to be set to os.environ.get("IP"). This is an
internal environment variable that Cloud9 has set, and we're using the os
module from the standard library to get that environment variable for us.
It's the same with PORT, but this time we're casting it as an int, because it
needs to be an integer. We're also then putting debug=true
because that will allow us to debug our code easier. 
"""
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)