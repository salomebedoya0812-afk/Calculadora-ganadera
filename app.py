from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def formulario():

    return """
    <h1>Calculadora de Producción de Leche</h1>

    <form action="/resultado" method="post">
        <label>¿Cuántas vacas hay?</label><br>
        <input type="number" name="vacas"><br><br>

        <label>¿Cuánta leche produce cada vaca?</label><br>
        <input type="number" name="leche"><br><br>

        <label>¿Cuánto vale un litro de leche?</label><br>
        <input type="number" name="precio"><br><br>

        <label>¿Cuáles son los gastos diarios por vaca?</label><br>
        <input type="number" name="gasto"><br><br>

        <button type="submit">Calcular</button>
    </form>
    """

@app.route('/resultado', methods=['POST'])
def resultado():

    vacas = int(request.form['vacas'])
    leche = float(request.form['leche'])
    precio = float(request.form['precio'])
    gasto = float(request.form['gasto'])

    produccion = vacas * leche
    ingreso = produccion * precio
    gastos = vacas * gasto
    ganancia = ingreso - gastos

    return f"""
    <h1>Resultados</h1>

    Producción total: {produccion} litros <br>
    Ingreso total: ${ingreso} <br>
    Gastos totales: ${gastos} <br>
    <h3>Ganancia diaria: ${ganancia}</h3>

    <br><br>
    <a href="/">Volver</a>
    """

if __name__ == '__main__':
    app.run(debug=True)