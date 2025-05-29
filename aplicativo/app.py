from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)
app.secret_key= "chave_secreta"

led_state = {"on": False}

@app.route("/", methods=["GET"])
def index():
    image_file = "led_aceso.png" if led_state["on"] else "led_desligado.png"
    return render_template("index.html", image=image_file)


@app.route("/toggle", methods=["POST"])
def toggle_led():
    led_state["on"] = not led_state["on"]  # Inverte o estado do LED
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)