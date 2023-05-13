texto = '''Según el sitio timeanddate21.com, con mas de 500000 visitas por día, una web sobre recursos para medir el tiempo y las zonas horarias, la tierra duró 1,59 milisegundos menos en girar sobre su propio eje el pasado 29 junio.

O mejor, el 29 junio duró 1,59 milisegundos menos que 24 horas.

Para que te hagas una idea, el parpadeo de un ojo dura 300 milisegundos. Es decir, el tiempo que perdió ese día es el equivalente a poco más de una 300 partes de un parpadeo, solo se puede percibir con instrumentos muy precisos.'''
texto=texto.replace('.',' ')
lst_pal=texto.split(' ')
print('------------------------------------')
print('Los valores y sus unidades son: ')
for i in range(len(lst_pal)):
    if lst_pal[i].isnumeric():
        print(lst_pal[i],lst_pal[i+1])
    if ',' in lst_pal[i]:
        n=lst_pal[i].split(',')
        if n[0] in '1234567890':
          print(lst_pal[i],lst_pal[i+1])








