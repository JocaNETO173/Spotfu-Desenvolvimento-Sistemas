# Classe Mãe
class Midia:
    def __init__(self, duracao, genero):
        self.duracao = duracao
        self.genero = genero
        self.favoritados = 0


# Classes filhas
class Musica(Midia):
    def __init__(self, duracao, genero, artista):
        super().__init__(duracao, genero)
        self.artista = artista
        

class Podcast(Midia):
    def __init__(self, duracao, genero, autor, convidado):
        super().__init__(duracao, genero)
        self.autor = autor
        self.convidado = convidado
        self.favoritados = 0