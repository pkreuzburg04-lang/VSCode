from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('Captcha text.html')

@app.route('/fail', methods=['POST'])
def fail():
    data = request.json
    print("From frontend:", data)
    return {"status": "received"}

if __name__ == '__main__':
    app.run(debug=True)