from flask import Flask, render_template_string
import redis
import random
import os

app = Flask(__name__)

 
redis_host = os.environ.get('REDIS_HOST', 'localhost')
cache = redis.Redis(host=redis_host, port=6379)  

quotes = [
    "Работает? Не трогай.",
    "В мире есть 10 типов людей: те, кто понимают двоичную систему, и те, кто нет.",
    "Код пишется для людей, а не для машин.",
    "Лучшая документация — это чистый код.",
    "Удаление кода лучше, чем его написание."
]

@app.route('/')
def hello():
    try:
        count = cache.incr('hits')
    except redis.exceptions.ConnectionError:
        count = "База данных Redis недоступна :("

    quote = random.choice(quotes)
    
    html = f"""
    <div style="text-align: center; margin-top: 50px; font-family: sans-serif;">
        <h1>💡 Техническая мудрость дня</h1>
        <h2 style="color: #4CAF50;">"{quote}"</h2>
        <br>
        <p>Эту страницу посмотрели {count} раз(а).</p>
        <p><small>Обнови страницу для новой мудрости.</small></p>
    </div>
    """
    return html

if __name__ == "__main__":
   
 app.run(host="0.0.0.0", port=5000)