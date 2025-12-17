from flask import Flask, render_template, request
import subprocess
import json
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        uploaded_file = request.files.get("code_file")

        if uploaded_file is None or uploaded_file.filename == "":
            result = {
                "status": "FAIL",
                "errors": ["No file selected"]
            }
        else:
            filepath = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
            uploaded_file.save(filepath)

            checker_output = subprocess.check_output(
                ["python3", "code_checker.py", filepath]
            )

            result = json.loads(checker_output.decode())

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
