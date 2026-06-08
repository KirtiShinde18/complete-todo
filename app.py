"""
This is a Flask application.
It starts a web server and

returns a JSON response on the home route.
"""

from flask import Flask, render_template

# ------------------ 
#  Create Flask app
# ------------------
app = Flask(__name__) 


# -------------
# ROUTE ⏩
# -------------
@app.route("/") 
def home():    
    # return {"message": "Flask Server Running Successfully 🚀 "}
    return render_template("index.html")

# -------------
# SERVER 🌍 
# -------------
if __name__ == "__main__": 
    app.run(debug=True)