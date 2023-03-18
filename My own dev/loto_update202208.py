urlWeb = "https://loto.hn/"

def getData(url):
    import requests
    from bs4 import BeautifulSoup
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def separateData(data):
    dataList = []
    for i in data:
        dataList.append(i.text)
    return dataList

def deleteSpace(data):
    dataList = []
    for i in data:
        dataList.append(i.replace(" ", ""))
    return dataList

def getTime():
    import datetime
    now = datetime.datetime.now()
    if now.hour >= 11:
        return "Sorteo de la mañana 11:00 AM"
    elif now.hour >= 3:
        return "Sorteo de la tarde 3:00 PM"
    else:
        return "Sorteo de la noche 9:00PM"


websiteDownload = getData(urlWeb)


selector = websiteDownload.find_all('div', class_='esferas esfera-verde')
diariaResult = "".join(deleteSpace(separateData(selector)))
selector = websiteDownload.find_all('div', class_='esferas esfera-verde-light')
diariaResultPlus = " ".join(deleteSpace(separateData(selector)))
selector = websiteDownload.find_all('div', class_='esferas esfera-marron')
multiSelect = "".join(deleteSpace(separateData(selector)))
selector = websiteDownload.find_all('div', class_='esferas esfera-azul esferas-texto-blanco')
pega3Result = "".join(deleteSpace(separateData(selector)))
selector = websiteDownload.find_all('div', class_='esferas esfera-amarillo')
premia2Result = "".join(deleteSpace(separateData(selector)))
selector = websiteDownload.find_all('div', class_='esferas esfera-morado')
premia2Result2 = "".join(deleteSpace(separateData(selector)))

superPremioResult = premia2Result[2:9] 


time = getTime()
print(time)
print("La Diaria: " + diariaResult + " +" + diariaResultPlus + "  " + multiSelect)
# print("Pega3 es: " + pega3Result[0:2] + " " + pega3Result[2:4])
# print("Premia2 es: " + premia2Result[0:2] + " " + premia2Result2 )
# print("Superpremio: " + superPremioResult[0:2] + " " + superPremioResult[2:4] + " " + superPremioResult[4:6] + " " + superPremioResult[6:8] + " " + superPremioResult[8:10] + " " + superPremioResult[10:12])
# print("¡Advertencia! Los resultados de pega3 y superpremio si estan incompleto, son resultados erroneos.")


