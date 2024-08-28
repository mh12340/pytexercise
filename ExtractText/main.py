user_input = input("Bitte geben Sie eine Zeichenfolge(derArtikel[Artikel]wurdebestelltvon[Bestellername] ein: ")
article_name = None
name = None

#find position of square brackets
start_pos1 = user_input.find("[")
end_pos1 = user_input.find("]", start_pos1)

#find position of square brackets
start_pos2 = user_input.find("[", end_pos1)
end_pos2 = user_input.find("]", start_pos2)

#checks if all positions are valid
if start_pos1 != -1 and end_pos1 != -1 and start_pos2 != -1 and end_pos2 != -1:
    article_name = user_input[start_pos1 +1: end_pos1]
    name = user_input[start_pos2 + 1:end_pos2]
    print("Artikelbezeichnung:", article_name)
    print("Besteller/in:", name)
else:
    print("Ungültige Eingabe.")
