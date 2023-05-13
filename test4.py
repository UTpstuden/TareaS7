def f_cuenta_vocal(txt):
	contador_voc = 0
	for letra in txt:
		if letra.lower() in "aeiou":
			contador_voc += 1
		if  letra.upper() in "aeiou":
			contador_voc += 1
		if letra.lower() in "áéíóú":
			contador_voc += 1
		if letra.upper() in "áéíóú":
			contador_voc += 1
	return contador_voc
x = f_cuenta_vocal('Australia perdió ante Argentina')
print('El número de vocales es', x)