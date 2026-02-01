import json

from flask import Flask, redirect, render_template, request

app = Flask(__name__)

tareas = []

siguiente_id = 1


def agregar_tarea(texto):
    global siguiente_id

    tareas.append({"id": siguiente_id, "texto": texto, "hecho": False})

    siguiente_id += 1


def completar_tarea(id):
    for tarea in tareas:
        if tarea["id"] == id:
            tarea["hecho"] = True

            break


@app.route("/")
def index():
    # Ordenar tareas: incompletas primero, luego completadas

    tareas_ordenadas = sorted(tareas, key=lambda t: t["hecho"])

    return render_template("index.html", tareas=tareas_ordenadas)


@app.route("/agregar", methods=["POST"])
def agregar():
    texto_tarea = request.form.get("texto_tarea")

    if texto_tarea:
        agregar_tarea(texto_tarea)

    return redirect("/")


@app.route("/completar/<int:id>")
def completar(id):
    completar_tarea(id)

    return redirect("/")


def guardar_datos():
    with open("tareas.json", "w") as f:
        json.dump({"siguiente_id": siguiente_id, "tareas": tareas}, f)


def cargar_datos():
    global siguiente_id, tareas

    try:
        with open("tareas.json", "r") as f:
            data = json.load(f)

            tareas = data["tareas"]

            siguiente_id = data["siguiente_id"]

    except FileNotFoundError:
        pass


if __name__ == "__main__":
    app.run(debug=True)
