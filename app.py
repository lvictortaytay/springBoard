# Put your app in here.
from flask import Flask , request
from operations import add,sub,mult,div

app = Flask(__name__)

@app.route("/welcome")
def welcome_page():
    """creating a route that returns welcome on this page"""
    return f"{1 + 1}"



@app.route("/welcome/home")
def home_page():
    """creating a route that returns welcome home on this page
    >>> home_page()
    welcome home
    
    
    """
    return "welcome home"



@app.route("/welcome/back")
def back_page():
    """creating a route that returns welcome on this page"""
    return "welcome back"



#calc , build a simple calculator with flask that uses URL query parameter to get the numbers 
# to calculate with
@app.route("/addi")
def addi():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return f"calculation {a} + {b} = {add(a,b)}"

@app.route("/subi")
def subi():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return f"calculation {a} - {b} = {sub(a,b)}"

@app.route("/multi")
def multi():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return f"calculation {a} x {b} = {mult(a,b)}"

@app.route("/divi")
def divi():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return f"calculation {a} ÷ {b} = {div(a,b)}"


#combine these all in one function and try not to use a lot of if/else statements
data_base = {
    "route":"math",
    "add":add,
    "sub":sub,
    "mult":mult,
    "div":div
}
@app.route('/<route>/<function>')
def dynamic_calc(route,function):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    if route == "math":
        return f"calculation {a} {function} {b} = {data_base[function](a,b)}"


