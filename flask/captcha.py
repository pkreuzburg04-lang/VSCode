from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('next')
        return f"Hello {name}, POST request received"
    return render_template('Captcha text.html')

# --- NEW: endpoint to receive fail messages ---
@app.route('/captcha text', methods=['POST'])
def fail():
    data = request.json
    print("From frontend:", data)  # printed in terminal
    return {"status": "received"}

if __name__ == '__main__':
    app.run(debug=True)