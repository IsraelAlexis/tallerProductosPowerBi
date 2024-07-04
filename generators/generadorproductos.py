import random

def generarProductos():
    productos=["Musica","TV","Aplicaciones","PC","Celulares",'Tablets','Accesorios']
    datos=[]
    for producto in productos:
        responsable={}
        categoria=random.choice(["Plus",'Mega','Basico'])
        responsable=[categoria,producto]
        datos.append(responsable)
    return datos
print(generarProductos())