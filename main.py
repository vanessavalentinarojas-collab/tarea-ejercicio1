from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    res1 = ""
    res2 = ""
    if request.method == "POST":
        n1 = request.form.get("nom1", "")
        n2 = request.form.get("nom2", "")
        n3 = request.form.get("nom3", "")
        l1 = len(n1)
        l2 = len(n2)
        l3 = len(n3)
        mayor = max(l1, l2, l3)
        if mayor == l1:
            res1 = "El nombre con mayor cantidad de caracteres es: " + n1
            res2 = "El nombre tiene : " + str(l1) + " caracteres"
        elif mayor == l2:
            res1 = "El nombre con mayor cantidad de caracteres es: " + n2
            res2 = "El nombre tiene : " + str(l2) + " caracteres"
        else:
            res1 = "El nombre con mayor cantidad de caracteres es: " + n3
            res2 = "El nombre tiene : " + str(l3) + " caracteres"
    return render_template("ejercicio1.html", res1=res1, res2=res2)