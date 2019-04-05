
strList=["str1", "str2", "str3", "str4", "str5"]
intrList=[10, 20, 30, 40, 50]
dblList=[1.5, 2.5, 3.5, 4.5, 5.5]

mixList = [str(strList[3]) + ", " + str(intrList[4]) + (", ") + str(dblList[2])]


print("\n Lista de strings: " + str(strList) + "\n Lista de integer: " + str(intrList) + "\n Lista de floats: " + str(dblList))
print("\n Lista de string, integer y float: " + str(mixList))

ultStr = strList[4]
ultInt = intrList[4]
ultDbl = dblList[4]

print("\n Ultima posicion en lista strList: " + str (ultDbl) + "\n" +  " Ultima posicion en lista intrList: " + str(ultInt) +"\n" + " Ultima posicion en lista strList: " + str(ultStr))

dicObras = {"9ª Sinfonia":"Betowen", "5ª Sifonia" : "Betowen" , "The Lord Of God":"Stive vay"}

print("\n Valores en el diccionario: " + str(dicObras))

print("\n Clave en el diccionario: " + str(dicObras.keys()))
