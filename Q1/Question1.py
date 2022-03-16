from flask import Flask

app = Flask(__name__)

""" 
Home route
"""
@app.route('/')
def root():
    return '<h1>Welcome to my CSCB20 website!</h1>'



""" 
Helper for user()
"""
def removeNonAlpha(str):
    newStr = ""
    for char in str:
        if char.isalpha():
            newStr += char
    return newStr

"""
User input route
"""
@app.route('/<name>')
def user(name: str):

    if not name.isalpha():
        ## 'D1A2V3E123' case
        name = removeNonAlpha(name)
    elif name.islower():
        ## 'dave' case
        name = name.upper()
    elif name.isupper():
        ## 'DAVE' case
        name = name.lower()
    else:
        ## 'dAve' case
        name = name.capitalize()

    return '<h1>Welcome, ' + name + ', to my CSCB20 website!</h1>'


if __name__ == '__main__': 
    app.run(debug=True)