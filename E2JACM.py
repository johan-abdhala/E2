try:
    import requests
    import os
    import sys
    from bs4 import BeautifulSoup as bs
    import webbrowser
    ##Elaborado por Johan Abdhala Caldera Melendez
    ##Este script se encarga de buscar noticias
    ##relacionas a la facultad que seleccionamos y llevarnos a la noticia mas reciente de la falcultad
    print("Este script navega en las páginas de noticas de la UANL")
    while True:
        try:
            inicioRango = int(input("Pagina inicial para buscar: "))
            finRango = int(input("Pagina final para buscar: "))
            dependencia = input("Ingrese las siglas de la Facultad a buscar: ")
            if inicioRango > finRango:
                inicioRango,finRango = finRango,inicioRango
            for i in range (inicioRango,finRango,1):
                url = "https://www.uanl.mx/noticias/page/"+str(i)
                pagina = requests.get (url)
                if pagina.status_code != 200:
                    raise TypeError("Pagina no encontrada")
                else:
                    soup = bs(pagina.content,"html.parser")
                    info = soup.select("h3 a")
                    for etiqueta in info:
                        url2 = etiqueta.get("href")
                        pagina2 = requests.get(url2)
                        if pagina2.status_code == 200:
                            soup2 = bs(pagina2.content,"html.parser")
                            parrafos = soup2.select("p")    
                            for elemento in parrafos:
                                if dependencia in elemento.getText():
                                    print ("Abriendo",url2)
                                    webbrowser.open(url2)
                                    break
            break
        except ValueError:
            print("Valor introducido no valido vuelvalo a intentar")
            continue

except ImportError as e:
    
    os.system('pip install'+str(e)) 

    print('Installing'+str(e)+'...') 

    print('Ejecuta de nuevo tu script...') 

    exit() 

    

