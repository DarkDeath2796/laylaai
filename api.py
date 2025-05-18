#! ./.venv/Scripts/python.exe


import flask, main


app = flask.Flask(__name__)
layla: main.LaylaAI = main.LaylaAI()


@app.route("/api/message", methods=["POST", "GET"])
def message():
    # Default page if accessed from a web browser
    if flask.request.method == "GET":
        return "Welcome to the API"
    data = flask.request.json
    message = data.get("message")
    name = data.get("name")
    response: str | None = layla.process_message(message, name)
    return f"Response: {response}"



if __name__ == "__main__":
    app.run(debug=True)