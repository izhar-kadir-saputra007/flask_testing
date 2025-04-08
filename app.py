import os
from flask import Flask
app = Flask(__name__)  # Nama variabel HARUS 'app'

@app.route('/')
def home():
    return "Hello Railway"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))