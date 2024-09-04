#funktion um user eingabe in liste zu splitten und mit list comprehension in integer liste umzuwandeln
def eingabe_liste():
    user_eingabe = input("Bitte geben Sie eine Liste von Bilanzergebnissen ein.")
    bilanz_erg = user_eingabe.split()
    bilanz_erg = [int(x) for x in bilanz_erg]
    return bilanz_erg

#funktion um mindestwert aus der liste auszulesen
def minimum(eingabe_liste):
    min_wert = min(eingabe_liste)
    return min_wert

#funktion um maximum aus der liste auszulesen
def maximum(eingabe_liste):
    max_wert = max(eingabe_liste)
    return max_wert

#funktion um die summe der bilanzergebnisse der liste zu berechnen
def gesamtsumme(eingabe_liste):
    summe = sum(eingabe_liste)
    return summe

#funktion um den durchschnitt der beträge in der liste zu berechnen
def durchschnitt(eingabe_liste):
    durchschn_wert = sum(eingabe_liste) / len(eingabe_liste)
    return durchschn_wert

#verwendet die funktion
bilanzen = eingabe_liste()

#gibt die ergebnisse in der konsole aus
print("Minimum:", minimum(bilanzen))
print("Maximum:", maximum(bilanzen))
print("Gesamtsumme:", gesamtsumme(bilanzen))
print("Durchschnitt:", durchschnitt(bilanzen))