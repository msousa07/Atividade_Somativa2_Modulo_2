from flask import Flask, request, render_template

app = Flask(__name__)

# Página inicial explicando como usar
@app.route("/")
def index():
    return render_template("index.html")

#Primeira Rota é soma


# Segunda é subtrair 


# Terceira é multiplicar



# Terceira é dividir 


# 🚨🚨🚨🚨🚨🚨🚨🚨🚨 Não mexa aqui, pois isso que executa o arquivo 🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨
if __name__ == "__main__":
    app.run(debug=True)


