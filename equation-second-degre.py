from sympy import symbols, sqrt, latex
import os

################## ÉQUATION ########################
# Coefficients
a = 3
b = 6
c = 2

# Vérifier que a != 0
if a == 0:
    print("Cette équation n'est pas du second degré car a = 0. a a été remplacé par 1")
    a = 1

# Variable
x = symbols('x')

# Chemin du fichier HTML
chemin_sortie = "C:/Users/Kéo/Desktop/mon_fichier.html"
os.makedirs(os.path.dirname(chemin_sortie), exist_ok=True)

etapes = []
solutions_x = []

# Étape 0 : afficher l'équation
equation = a*x**2 + b*x + c
etapes.append(f"On considère l'équation :")
etapes.append(f"\\[{latex(equation)} = 0\\]")

# Étape 1 : discriminant
delta = b**2 - 4*a*c
etapes.append("On calcule le discriminant :")
etapes.append(f"\\[\\Delta = b^2 - 4ac = {b}^2 - 4 \\cdot {a} \\cdot {c} = {b**2} - {4*a*c} = {delta}\\]")

# Étape 2 : résolution
if delta < 0:
    etapes.append("Comme \\(\\Delta < 0\\), l'équation n'a pas de solution réelle.")
elif delta == 0:
    x_sol = -b / (2*a)
    solutions_x.append(x_sol)
    etapes.append("Comme \\(\\Delta = 0\\), l'équation a une solution réelle double :")
    etapes.append(f"\\[x = -\\frac{{b}}{{2a}} = -\\frac{{{b}}}{{2 \\cdot {a}}} = {latex(x_sol)}\\]")
else:
    x1 = (-b + sqrt(delta)) / (2*a)
    x2 = (-b - sqrt(delta)) / (2*a)
    solutions_x.extend([x1, x2])
    etapes.append("Comme \\(\\Delta > 0\\), l'équation a deux solutions réelles :")
    etapes.append(f"\\[x_1 = \\frac{{-b + \\sqrt{{\\Delta}}}}{{2a}} = \\frac{{{-b} + \\sqrt{{{delta}}}}}{{{2*a}}} = {latex(x1)}\\]")
    etapes.append(f"\\[x_2 = \\frac{{-b - \\sqrt{{\\Delta}}}}{{2a}} = \\frac{{{-b} - \\sqrt{{{delta}}}}}{{{2*a}}} = {latex(x2)}\\]")

# Étape 3 : ensemble des solutions
if solutions_x:
    solutions_latex = ";\\;".join([latex(s) for s in solutions_x])
    etapes.append("L'ensemble des solutions est :")
    etapes.append(f"\\[S = \\{{ {solutions_latex} \\}}\\]")
else:
    etapes.append("L'ensemble des solutions est :")
    etapes.append("\\[S = \\varnothing\\]")

############# Génération du fichier HTML #############
def ecrire_fichier(texte):   
    with open(chemin_sortie, "w", encoding="utf-8") as fichier:
        fichier.write(texte)

html = """
<!DOCTYPE html>
<html lang="fr" translate="no">
<head>
<meta charset="UTF-8">
<title>Résolution Équation Second Degré</title>
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>
<style>
    body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #fff; color: #333; margin: 0; padding: 0; display: flex; justify-content: center; margin-bottom: 20px; }
    h2 { color: #1a73e8; margin-bottom: 20px; }
    p { font-size: 1.1rem; line-height: 1.6; margin-bottom: 16px; }
    p:last-child { margin-bottom: 0; }
    .equation { background-color: #f0f4ff; padding: 10px 15px; border-left: 4px solid #1a73e8; border-radius: 6px; margin: 10px 0; display: flex; justify-content: center; }
</style>
</head>
<body>
<div class="container">
<h2>Résolution de l'équation du second degré</h2>
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

