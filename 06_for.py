Nombres = ["Thiago", "Pedro","Felipe","Pau","Ariane","Giovana","Luci","Jose"]
print("\n Nombres en la lista: " + str(Nombres))

Selected = []
for nombre in Nombres:
    if "a" in nombre:
        Selected.append(nombre)

print("\n Los nombres que contienen una 'a' son: " + str(Selected) + "\n")