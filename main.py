import random
from flask import Flask

app = Flask(__name__)

facts_list = [
    "La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos.",
    "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.",
    "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna.",
    "Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo.",
    "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo.",
    "Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos.",
    "Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios.",
    "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas."
]

# Página de inicio
@app.route("/")
def home():
    return """
    <h1>Bienvenido a mi sitio sobre la dependencia tecnológica</h1>
    <p>Haz clic en el siguiente enlace para descubrir un dato interesante:</p>

    <a href="/random_fact">¡Ver un dato aleatorio!</a>
    <br><br>

    <a href="/coin">🪙 Lanzar una moneda</a>
    """

# Página con un dato aleatorio
@app.route("/random_fact")
def random_fact():
    return f"""
    <h2>Dato aleatorio sobre la dependencia tecnológica</h2>
    <p>{random.choice(facts_list)}</p>
    <br>
    <a href="/">⬅ Volver a la página principal</a>
    """

# Tercera página: lanzamiento de moneda
@app.route("/coin")
def coin():
    resultado = random.choice(["Cara", "Cruz"])

    return f"""
    <h2>🪙 Lanzamiento de moneda</h2>
    <p>El resultado es: <strong>{resultado}</strong></p>
    <br>
    <a href="/">⬅ Volver a la página principal</a>
    """

app.run(debug=True)