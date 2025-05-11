from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)
# Use Flask app.route decorador para mapear la ruta URL
@app.route("/censo")

def home():
    return render_template('/censo')

if __name__ == '__main__':

    app.run(debug=True)

@app.route('/')
def censo_estudiantes():
    df = pd.read_csv('static/censo_estudiantes_2020.csv')

    destino = df['Destino académico'].value_counts()
    sexo = df['Sexo'].value_counts()

    # Gráfico estático
    plt.figure(figsize=(6, 4))
    destino.plot(kind='bar', color='green')
    plt.title('Destino Académico')
    plt.ylabel('Cantidad')
    plt.xticks(rotation=45)

    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png')
    buf.seek(0)
    imagen = base64.b64encode(buf.getvalue()).decode('utf8')

    return render_template('index.html', imagen=imagen, labels=sexo.index.tolist(), valores=sexo.values.tolist())

if __name__ == '__main__':
    app.run(debug=True)
