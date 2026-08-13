# Classe Mãe
class Midia:
    def __init__(self, titulo, duracao):
        self._titulo = titulo
        self._duracao = duracao
        self.favoritados = 0

        def favoritar(self):
            self.favoritados += 1

        def __str__(self):
            return f"Titulo: {self._titulo} | Duração: {self._duracao} | Favoritados: {self.favoritados}"
        
# Classes filhas
class Musica(Midia):
    def __init__(self, titulo, duracao, genero, artista):
        super().__init__(duracao, titulo)
        self._genero = genero
        self._artista = artista
        self.favoritados = 0

        def __str__(self):
            return f"Titulo: {self._titulo} | Artista: {self._artista} | Genero: {self._genero} | Duração: {self._duracao} secs| Favoritados: {self.favoritados}"
        
class Podcast(Midia):
    def __init__(self, titulo, duracao, autor, convidado):
        super().__init__(duracao, titulo)
        self._autor = autor
        self._convidado = convidado
        self.favoritados = 0

        def __str__(self):
            return f"Titulo: {self._titulo} | Autor: {self._autor} | Duração: {self._duracao} mins | Favoritados: {self.favoritados}"

class Audiobook(Midia):
    def __init__(self, titulo, duracao, genero, autor, canal):
        super().__init__(titulo, duracao, genero)
        self._autor = autor
        self._canal = canal
        self.favoritados = 0
        
        def __str__(self):
            return f"Titulo: {self._titulo} | Autor: {self.autor} | Genero: {self._genero} | Duração: {self._duracao} mins | Canal: {self._canal} | Favoritados: {self.favoritados}"
        
#Musicas
gummybear = Musica("Eu sou o Gummy Bear", 150, "Infantil", "Gummy Bear")
minadocondominio = Musica("Mina do Condomínio", 400, "Samba e Pagode", "Seu Jorge")
billiejean = Musica("Bellie Jean", 296, "Pop", "Michael Jackson")

# Podcasts
balela = Podcast("COPA SINUCA DO BALELA #122", 40, "Balela", "Sem convidados")
flow = Podcast("SACANI RESPONDE [VIDA NO UNIVERSO]", 133, "Flow Podcast", "Sérgio Sacani")

podpah = Podcast()"OVNIS, ATENTADO E O SUMIÇO DE CIENTISTAS: DANIEL LOPEZ - Inteligência Ltda. Podcast #1829"

# Audiobooks
