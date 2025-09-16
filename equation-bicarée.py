from sympy import symbols, sqrt, solve, latex
import os

################## ÉQUATION ########################

# Coefficients de l'équation de la forme ax**4 + bx**2 + c = 0
a = 3
b = 6
c = 2

# a doit être différent de 0, sinon, on le remplace par 1
if a == 0:
  print("Cette équation n'est pas du second degré car a = 0. a a été remplacé par 1")
  a = 1

# Déclaration des variables mathématiques
x, X = symbols('x X')

chemin_sortie = "mon_fichier.html"

os.makedirs(os.path.dirname(chemin_sortie), exist_ok=True)

etapes = []
solutions_x = []

# Étape 1 : substitution X = x^2
etapes.append(f"On pose \\(X = x^2\\). On a donc \\({latex(a*X**2 + b*X + c)} = 0\\)")

# Étape 2 : discriminant
delta = b**2 - 4*a*c
etapes.append("On calcule le discriminant :")
etapes.append(f"\\[\\Delta = b^2 - 4ac = {b}^2 - 4 \\cdot {a} \\cdot {c} = {b**2} - {4*a*c} = {delta}\\]")

# Étape 3 : résolution selon le discriminant
if delta < 0:
    etapes.append("Comme \\(\\Delta < 0\\), l'équation en \\(X\\) n'a pas de solution réelle.")
    etapes.append(f"Donc l'équation \\({latex(a*x**4 + b*x**2 + c)}=0\\) n'a pas de solution réelle.")
elif delta == 0:
    X_sol = -b / (2*a)
    etapes.append("Comme \\(\\Delta = 0\\), l'équation a une solution réelle double :")
    etapes.append(f"\\[X = -\\dfrac{{b}}{{2a}} = -\\dfrac{{{b}}}{{2 \\cdot {a}}} = {latex(X_sol)}\\]")

    if X_sol < 0:
        etapes.append("Mais \\(X < 0\\), donc pas de solution réelle pour \\(x\\).")
    else:
        sols_x = [sqrt(X_sol), -sqrt(X_sol)]
        solutions_x.extend(sols_x)
        etapes.append("On en déduit les solutions en \\(x\\) :")
        etapes.append(f"\\[x = {latex(sols_x[0])} \\quad \\text{{ou}} \\quad x = {latex(sols_x[1])}\\]")
else:
    etapes.append("Comme \\(\\Delta > 0\\), l'équation en \\(X\\) a deux solutions réelles :")
    sols_X = solve(a*X**2 + b*X + c, X)

    for i, sol in enumerate(sols_X, 1):
        etapes.append(f"\\[X_{i} = {latex(sol)}\\]")

    for i, sol in enumerate(sols_X, 1):
        if sol.is_real and sol >= 0:
            sols_x = [sqrt(sol), -sqrt(sol)]
            solutions_x.extend(sols_x)
            etapes.append(f"Pour \\(X_{i}\\), les solutions en \\(x\\) sont :")
            etapes.append(f"\\[x = {latex(sols_x[0])} \\quad \\text{{ou}} \\quad x = {latex(sols_x[1])}\\]")
        elif sol.is_real and sol < 0:
            etapes.append(f"Pour \\(X_{i}\\), comme \\(X < 0\\), il n'y a pas de solution réelle en \\(x\\).")

# Étape 4 : ensemble des solutions
if solutions_x:
    solutions_latex = ";\\;".join([latex(s) for s in solutions_x])
    etapes.append(f"L'ensemble des solutions est :")
    etapes.append(f"\\[S = \\{{ {solutions_latex} \\}}\\]")
else:
    etapes.append("L'ensemble des solutions est :")
    etapes.append("\\[S = \\varnothing\\]")

############# Génération du fichier HTML #############
def ecrire_fichier(texte):   
    global chemin_sortie
    with open(chemin_sortie, "w", encoding="utf-8") as fichier:
        fichier.write(texte)

html = """
<!DOCTYPE html>
<html lang="fr" translate="no">
<head>
<meta charset="UTF-8">
<title>Résolution Équation Quartique</title>
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>
<style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: #ffffff;
        color: #333;
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }

    h2 {
        color: #1a73e8;
        margin-bottom: 20px;
    }

    p {
        font-size: 1.1rem;
        line-height: 1.6;
        margin-bottom: 16px;
    }

    p:last-child {
        margin-bottom: 0;
    }

    .equation {
        background-color: #f0f4ff;
        padding: 10px 15px;
        border-left: 4px solid #1a73e8;
        border-radius: 6px;
        /* display: inline-block; */
        margin: 10px 0;
        display: flex;
        justify-content: center;
    }
</style>
</head>
<body>
<div class="container">
<h2>Résolution de l'équation</h2>
"""

for e in etapes:
    if e.startswith("\\[") and e.endswith("\\]"):
        html += f'<p class="equation">{e}</p>\n'
    else:
        html += f"<p>{e}</p>\n"

html += """
</div>
</body>
</html>
"""

ecrire_fichier(html)
print("Fichier généré avec succès !")

