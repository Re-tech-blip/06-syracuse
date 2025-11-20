#### Fonctions secondaires

"""Module pour les calculs liés à la suite de Syracuse"""

# Tentative d'import de plotly, gestion d'erreur si non installé
try:
    from plotly.graph_objects import Scatter, Figure
    PLOTLY_OK = True
except ImportError:
    PLOTLY_OK = False

### NE PAS MODIFIER ###

def syr_plot(lsyr):
    """Affiche la suite de Syracuse avec plotly si disponible."""
    if not PLOTLY_OK:
        print("Plotly n'est pas installé. Impossible d'afficher le graphique.")
        return None
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )
    x = list(range(len(lsyr)))
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color="blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
    return None
#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """

    l = [ n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
        l.append(n)
    return l

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol"""
    n = len(l)-1
    return n  # pas d'espace inutile ici

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """
    altitude0 = l[0]

    # Si la suite descend directement → 0
    if l[1] < altitude0:
        return 0

    # Cherche la première descente définitive sous altitude0
    for i in range(2, len(l)):
        if l[i] < altitude0:
            return i - 1

    # Par sécurité, ne devrait jamais arriver
    return len(l) - 1


def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """
    return max(l)


#### Fonction principale



def tests():
    """Tests unitaires simples pour vérifier les fonctions."""
    print("Test altitude_maximale :", altitude_maximale([3, 10, 5, 16, 8, 4, 2, 1]))
    print("Test temps_de_vol_en_altitude :", temps_de_vol_en_altitude([3, 10, 5, 16, 8, 4, 2, 1]))
    print("Test temps_de_vol :", temps_de_vol([3, 10, 5, 16, 8, 4, 2, 1]))
    l7 = syracuse_l(7)
    print("Suite de Syracuse pour 7 :", l7)
    lsyr = syracuse_l(15)
    print("Suite de Syracuse pour 15 :", lsyr)
    print("Altitude max pour 15 :", altitude_maximale(lsyr))
    print("Temps de vol pour 15 :", temps_de_vol(lsyr))
    print("Temps de vol en altitude pour 15 :", temps_de_vol_en_altitude(lsyr))


def main():
    """"Fonction pour  executer le programme de syracuse"""
    print("Bienvenue dans le programme Syracuse !")
    try:
        n = int(input("Entrez la valeur de départ (entier > 0) : "))
        if n <= 0:
            raise ValueError
    except ValueError:
        print("Entrée invalide. Veuillez entrer un entier strictement positif.")
        return
    lsyr = syracuse_l(n)
    print(f"Suite de Syracuse pour {n} : {lsyr}")
    print(f"Altitude maximale : {altitude_maximale(lsyr)}")
    print(f"Temps de vol : {temps_de_vol(lsyr)}")
    print(f"Temps de vol en altitude : {temps_de_vol_en_altitude(lsyr)}")
    syr_plot(lsyr)


if __name__ == "__main__":
    # Décommente la ligne suivante pour lancer les tests
    # tests()
    main()
