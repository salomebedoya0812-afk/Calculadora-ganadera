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
                width:350px;
            }
            input, select{
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
        </style>
        <script>
            function mostrarFormulario(){
                var animal = document.getElementById("animal").value;
                document.getElementById("form_vaca").style.display = (animal=="vaca") ? "block" : "none";
                document.getElementById("form_cerdo").style.display = (animal=="cerdo") ? "block" : "none";
                document.getElementById("form_gallina").style.display = (animal=="gallina") ? "block" : "none";
            }
        </script>
    </head>
    <body>
        <div class="contenedor">
            <h1>Calculadora de Producción 🐄🐖🐔</h1>
            <label>Seleccione el animal:</label>
            <select id="animal" onchange="mostrarFormulario()">
                <option value="">-- Elegir --</option>
                <option value="vaca">Vaca</option>
                <option value="cerdo">Cerdo</option>
                <option value="gallina">Gallina</option>
            </select>

            <!-- Formulario Vaca -->
            <form id="form_vaca" action="/resultado" method="post" style="display:none;">
                <input type="hidden" name="tipo" value="vaca">
                <label>¿Cuántas vacas hay?</label>
                <input type="number" name="cantidad">
                <label>¿Cuánta leche produce cada vaca?</label>
                <input type="number" name="produccion">
                <label>¿Cuánto vale un litro de leche?</label>
                <input type="number" name="precio">
                <label>¿Cuáles son los gastos diarios por vaca?</label>
                <input type="number" name="gasto">
                <button type="submit">Calcular</button>
            </form>

            <!-- Formulario Cerdo -->
            <form id="form_cerdo" action="/resultado" method="post" style="display:none;">
                <input type="hidden" name="tipo" value="cerdo">
                <label>¿Cuántos cerdos hay?</label>
                <input type="number" name="cantidad">
                <label>¿Cuántos lechones produce al año?</label>
                <input type="number" name="produccion">
                <label>¿Cuánto vale un lechón?</label>
                <input type="number" name="precio">
                <label>¿Cuáles son los gastos diarios por cerdo?</label>
                <input type="number" name="gasto">
                <button type="submit">Calcular</button>
            </form>

            <!-- Formulario Gallina -->
            <form id="form_gallina" action="/resultado" method="post" style="display:none;">
                <input type="hidden" name="tipo" value="gallina">
                <label>¿Cuántas gallinas hay?</label>
                <input type="number" name="cantidad">
                <label>¿Cuántos huevos produce cada gallina?</label>
                <input type="number" name="produccion">
                <label>¿Cuánto vale un huevo?</label>
                <input type="number" name="precio">
                <label>¿Cuáles son los gastos diarios por gallina?</label>
                <input type="number" name="gasto">
                <button type="submit">Calcular</button>
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

    # Cálculo genérico: cantidad * producción * precio
    total_produccion = cantidad * produccion
    ingreso = total_produccion * precio
    gastos = cantidad * gasto
    ganancia = ingreso - gastos

    return f"""
    <h1>Resultados ({tipo.capitalize()})</h1>
    Producción total: {total_produccion} unidades <br>
    Ingreso total: ${ingreso} <br>
    Gastos totales: ${gastos} <br>
    <h3>Ganancia: ${ganancia}</h3>
    <br><br>
    <a href="/">Volver</a>
    """

if __name__ == '__main__':
    app.run(debug=True)
