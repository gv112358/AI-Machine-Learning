from matplotlib import pyplot as plt

def CreaGrafoCartesiano(sTitolo,lListaEtichette,sColor,lX,lY):
    #crea una finestra per un grafico
    fig = plt.figure(sTitolo,figsize = (8,6))

    #crea una griglia 1x1 e metti il piano cartesiano 
    # nella posizione 1 delle griglia
    fig.add_subplot(111)

    plt.title(sTitolo)
    plt.xlabel(lListaEtichette[0])
    plt.ylabel(lListaEtichette[1])
    
    plt.scatter(lX,lY, color = sColor)
    plt.show()



