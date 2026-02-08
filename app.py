from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

FILE_NAME = "daily_status.csv"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        name = request.form.get("name")
        date = request.form.get("date")
        status = request.form.get("status")

        lines = status.splitlines()

        work = lines[0] if len(lines) > 0 else ""
        block = lines[1] if len(lines) > 1 else ""
        plan = lines[2] if len(lines) > 2 else ""

        result = {
            "name": name,
            "date": date,
            "work": work,
            "block": block,
            "plan": plan
        }

        # ✅ Save to Excel (CSV)
        file_exists = os.path.isfile(FILE_NAME)

        with open(FILE_NAME, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(["Name", "Date", "Work Done", "Blockers", "Plan"])

            writer.writerow([name, date, work, block, plan])

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
