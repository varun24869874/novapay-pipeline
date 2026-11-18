from flask import Flask, jsonify
app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.get("/balance/<acct>")
def balance(acct):
    return jsonify(account=acct, balance=1000.0)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
