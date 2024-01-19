from flask import Flask 
import random 

app = Flask(__name__)
fact_list=['Законодательство США допускало отправку детей по почте до 1913 года.','В современной истории есть промежуток времени, когда на счетах компании «Apple», было больше средств, чем у американского правительства.','Среднее облако весит порядка 500 тонн, столько же весят 80 слонов.']

@app.route("/") 
def index(): 
    return f'<h1>Привет! Здесь ты можешь узнать пару интересных фактов</h1><a href="/random_fact">Посмотреть случайный факт!</a><p><h1>А Здесь ты можешь посмотреть погоду</h1><a href="/weather">Погода</a></p>'

@app.route("/random_fact") 
def facts(): 
    return f'<p>{random.choice(fact_list)}</p>' 

@app.route("/weather") 
def weath(): 
    return f'<p><iframe src="https://www.meteoblue.com/en/weather/widget/daily/ip_romania_675514?geoloc=fixed&days=7&tempunit=FAHRENHEIT&windunit=METER_PER_SECOND&precipunit=MILLIMETER&coloured=coloured&pictoicon=0&pictoicon=1&maxtemperature=0&maxtemperature=1&mintemperature=0&mintemperature=1&windspeed=0&windspeed=1&windgust=0&windgust=1&winddirection=0&winddirection=1&uv=0&uv=1&humidity=0&humidity=1&precipitation=0&precipitation=1&precipitationprobability=0&precipitationprobability=1&spot=0&spot=1&pressure=0&pressure=1&layout=light"  frameborder="0" scrolling="NO" allowtransparency="true" sandbox="allow-same-origin allow-scripts allow-popups allow-popups-to-escape-sandbox" style="width: 378px; height: 467px"></iframe><div><!-- DO NOT REMOVE THIS LINK --><a href="https://www.meteoblue.com/en/weather/week/ip_romania_675514?utm_source=weather_widget&utm_medium=linkus&utm_content=daily&utm_campaign=Weather%2BWidget" target="_blank" rel="noopener">meteoblue</a></div></p>' 

app.run(debug=True)
