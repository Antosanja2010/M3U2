import random
from flask import Flask

app = Flask(__name__)




@app.route("/")
def hello_world():
    return f'<p>Ссылка на факты</p>'
    
     



@app.route("/random_fact")
def fact():
    spisok = ['Технолоические зависимости становятся проблемой с каждым годом!','Технологическая зависимость распостронена у подростков','при долгом сиденья за гаджиками появляются проблемы со здоровьям']
    return f'<p>{random.choice(spisok)}</p>'



@app.route("/monetki")
def monetka():

    monetki = ["Орел", "Решка"]
    return f'<p>{random.choice(monetki)}</p>'

    



app.run(debug=True)
