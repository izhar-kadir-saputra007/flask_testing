from flask import Flask

# 1. Inisialisasi Flask
app = Flask(__name__)

# 2. Definisi Route
@app.route('/')
def home():
    return "Hello World!"

# 3. Jalankan Aplikasi
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)