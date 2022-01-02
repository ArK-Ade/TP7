#!/usr/bin/python3
import cgi

form = cgi.FieldStorage()

# Identifiant enregistrés
password = "password"
login = "etudiant"

print("Content-type: text/html; charset=utf-8\n")


def footer():
    print("""
        </BODY>
        </HTML>
    """)


""""
Cette fonction retourne les données envoyées en GET
"""


def affichage_donnees():
    donnees = ""
    if form.keys().__contains__("name"):
        donnees += "Voici le contenu de la clé name : "
        donnees += form["name"].value + " "

    if form["login"].value == login and form["password"].value == password:
        donnees += "<center><hr><H3>Bienvenue, " + form["login"].value + "</H3><hr></center>"

    else:
        donnees += "<H1>Erreur de connexion</H1>"
        donnees += "Veuillez corriger votre nom d'utilisateur et votre mot de passe"

    return donnees


html = """
<HTML>
<HEAD><TITLE>Page de connexion</TITLE></HEAD>
<BODY>
<CENTER>
<FORM method="POST" action="index.py">
<paragraph> Entrez votre nom d'utilisateur : <input type="text" name="login">
<paragraph> Entrez votre mot de passe : <input type="password" name="password">
<paragraph> <input type="submit" value="Connexion">
</FORM>
</CENTER>
<HR>

</BODY>
</HTML>
"""

print(html)
print(affichage_donnees())
