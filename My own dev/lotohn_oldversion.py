from os import remove
import re
import requests
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime

def run():
    webloto = requests.get ('https://www.loto.hn/loto/diaria')
    soup = BeautifulSoup(webloto.text, 'lxml')
    
    today = date.today()   
    now = datetime.now()

   # print(str(today) + " " + str(now.hour) + ":" + str(now.minute))
    
    #f = open ("Resultado Diaria " + str(today) + " " + str(now.hour) + ":" + str(now.minute) + '.html','w')
    #f.write(str(soup))
    #f.close()

    f = open ("results.txt",'w')
    f.write(str(soup.tr))
    f.close()

    g = []
    with open("results.txt") as fname:
	    lineas = fname.readlines()
	    for linea in lineas:
	    	g.append(linea.strip('\n')) 

    results = str(g[16])
    datenow = str(g[8])
    datenow = datenow.replace("<","").replace("p","").replace(">","").replace("/","").replace("td","")

    
    characters = "<>p/td"
    
    
    for x in range(len(characters)):
        results = results.replace(characters[x],"")

    remove("results.txt")

    print("El Resultado de la Diaria el día " + datenow)
    print(results)

    print ("")
    print("Consulta realizada el " + str(today) + " " + str(now.hour) + ":" + str(now.minute))
    
if __name__ =='__main__':
    run()
