from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def formulario():
    return """
    <html>
    <head>
        <title>Calculadora de Producción</title>
        <style>
            body{
                font-family: Arial, sans-serif;
                background-image: url("https://images.unsplash.com/photo-1500382017468-9049fed747ef");
                background-size: cover;
                background-position: center;
                display:flex;
                justify-content:center;
                align-items:center;
                height:100vh;
                margin:0;
            }
            .contenedor{
                background: rgba(255,255,255,0.92);
                padding:40px;
                border-radius:12px;
                box-shadow:0 15px 35px rgba(0,0,0,0.25);
                text-align:center;
                width:400px;
                overflow-y:auto;
                max-height:90vh;
            }
            .bloque{
                margin-top:20px;
                margin-bottom:20px;
                padding:20px;
                border-radius:10px;
                color:#000;
                box-shadow:0 4px 10px rgba(0,0,0,0.15);
            }
            .vaca{
                background: linear-gradient(135deg, #AEC6CF, #B0E0E6);
            }
            .cerdo{
                background: linear-gradient(135deg, #F4C2C2, #FFD1DC);
            }
            .gallina{
                background: linear-gradient(135deg, #FFFACD, #FAFAD2);
            }

            input{
                width:100%;
                padding:8px;
                margin-top:5px;
                margin-bottom:15px;
                border-radius:5px;
                border:1px solid #ccc;
            }
            button{
                background:#4CAF50;
                color:white;
                border:none;
                padding:10px;
                width:100%;
                border-radius:6px;
                cursor:pointer;
                font-weight:bold;
            }
            button:hover{ background:#3e8e41; }
            h2{ margin-top:20px; }
        </style>
    </head>
    <body>
        <div class="contenedor">
            <h1>Calculadora de Producción 🐄🐖🐔</h1>

            <!-- Formulario Vaca -->
            <div class="bloque vaca">
            <h2>Vacas</h2>
            <form action="/resultado" method="post">
                <input type="hidden" name="tipo" value="vaca">
                <label>¿Cuántas vacas hay?</label>
                <input type="number" name="cantidad">
                <label>¿Cuánta leche produce cada vaca?</label>
                <input type="number" name="produccion">
                <label>¿Cuánto vale un litro de leche?</label>
                <input type="number" name="precio">
                <label>¿Cuáles son los gastos diarios por vaca?</label>
                <input type="number" name="gasto">
                <button type="submit">Calcular Vacas</button>
            </form>
        </div>

            <!-- Formulario Cerdo -->
            <div class="bloque cerdo">
            <h2>Cerdos</h2>
            <form action="/resultado" method="post">
                <input type="hidden" name="tipo" value="cerdo">
                <label>¿Cuántos cerdos hay?</label>
                <input type="number" name="cantidad">
                <label>¿Cuántos lechones produce al año?</label>
                <input type="number" name="produccion">
                <label>¿Cuánto vale un lechón?</label>
                <input type="number" name="precio">
                <label>¿Cuáles son los gastos diarios por cerdo?</label>
                <input type="number" name="gasto">
                <button type="submit">Calcular Cerdos</button>
            </form>
        </div>

            <!-- Formulario Gallina -->
            <div class="bloque gallina">
            <h2>Gallinas</h2>
            <form action="/resultado" method="post">
                <input type="hidden" name="tipo" value="gallina">
                <label>¿Cuántas gallinas hay?</label>
                <input type="number" name="cantidad">
                <label>¿Cuántos huevos produce cada gallina?</label>
                <input type="number" name="produccion">
                <label>¿Cuánto vale un huevo?</label>
                <input type="number" name="precio">
                <label>¿Cuáles son los gastos diarios por gallina?</label>
                <input type="number" name="gasto">
                <button type="submit">Calcular Gallinas</button>
            </form>
        </div>
    </body>
    </html>
    """

@app.route('/resultado', methods=['POST'])
def resultado():
    tipo = request.form['tipo']
    cantidad = int(request.form['cantidad'])
    produccion = float(request.form['produccion'])
    precio = float(request.form['precio'])
    gasto = float(request.form['gasto'])

    total_produccion = cantidad * produccion
    ingreso = total_produccion * precio
    gastos = cantidad * gasto
    ganancia = ingreso - gastos

    # Personalizar unidad según animal
    if tipo == "vaca":
        unidad = "litros de leche"
    elif tipo == "cerdo":
        unidad = "lechones"
    else:
        unidad = "huevos"

    return f"""
    <h1>Resultados ({tipo.capitalize()})</h1>
    Producción total: {total_produccion} {unidad} <br>
    Ingreso total: ${ingreso} <br>
    Gastos totales: ${gastos} <br>
    <h3>Ganancia: ${ganancia}</h3>
    <br><br>
    <a href="/">Volver</a>
    """

if __name__ == '__main__':
    app.run(debug=True)
