from flask import Flask
import random

app = Flask(__name__)

QUOTES = [
    "The grass is greener where you water it 🐄",
    "Moo-ve on and stay positive! 🌿",
    "Don’t cry over spilled milk, learn from it 🥛",
    "Keep calm and love cows 🐮",
    "Patience is the udder key to success 🐾"
]

@app.route('/')
def home():
    quote = random.choice(QUOTES)
    return f"""
    <html>
        <head><title>Wisecow 🐮</title></head>
        <body style='font-family: Arial; text-align: center; padding: 50px;'>
            <h1>🐮 Welcome to Wisecow!</h1>
            <h2>{quote}</h2>
            <p>Served with ❤️ using Flask</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4499)


