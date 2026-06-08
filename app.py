"""
This is a Flask application.
It starts a web server and
returns a JSON response on the route.
"""

from flask import Flask, render_template, request
import json

# ------------------ 
#  Create Flask app
# ------------------
app = Flask(__name__) 

# -------------
# FUNCTIONS
# -------------
# read  👀
def read_todo():
    with open("db.json", "r") as file:
        return json.load(file)

# create  ✍️
def create_todo(data):
    with open("db.json", "w") as file:
        json.dump(data, file)

# -------------
# ROUTE ⏩
# -------------
@app.route("/") 
def home():    
    # return {"message": "Flask Server Running Successfully 🚀 "}
    return render_template("index.html")

@app.route("/todos", methods=["GET"])
def get_todos():
    return read_todo()["notes"]

@app.route("/todos", methods=["POST"])
def create_new_todo():

    body = request.json
    all_notes = read_todo()

    # 1️⃣ read db,json and notes list
    id = len(all_notes["notes"]) + 1
    latest_note = {**body, "id" : id}
    all_notes = read_todo()

    # 2️⃣ append to notes list 
    all_notes["notes"].append(latest_note)

    # 3️⃣ write to db.json
    create_todo(all_notes)
    return {"message": "Todo created successfully ✅"}

@app.route("/todo/<int:tid>", methods=["DELETE"])
def remove_todo(tid):
    # 1️⃣ read todos
    all_notes = read_todo()

    # 2️⃣ remove todo from notes
    result = []
    for item in all_notes["notes"]:
        if item["id"] != tid:
            result.append(item)
    all_notes["notes"] = result

    # 3️⃣ write to db.json
    create_todo(all_notes)
    return {"message": "Todo deleted successfully ✅"}

# -------------
# SERVER 🌍 
# -------------
if __name__ == "__main__": 
    app.run(debug=True)