#!/usr/bin/python3
import cgi

form = cgi.FieldStorage()

password = "password"
login = "etudiant"

print("Content-type: text/html; charset=utf-8\n")


def header(title):
    pass


def footer():
    print("""
        </BODY>
        </HTML>
    """)


html = """
<HTML>
<HEAD><TITLE>Page de connexion</TITLE></HEAD>
<BODY>
<CENTER>
<FORM method="POST" action="index.py">
<paragraph> Entrez votre nom d'utilisateur : <input type="text" name="login">
<paragraph> Entrez votre mot de passe : <input type="password" name="password">
<paragraph> <input type="submit" value="Connect">
</FORM>
</CENTER>
<HR>

</BODY>
</HTML>
"""
print(html)

if form["name"].value:
    print(form["name"].value)

if form["login"].value == login and form["password"].value == password:
    print("<center><hr><H3>Welcome back,", form["login"].value, ".</H3><hr></center>")

else:
    print("<H1>Erreur</H1>")
    print("Veuillez rentrer votre nom d'utilisateur et mot de passe svp")
