class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, new_name):
        self._nome = new_name.title()

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.duracao} minutos - {self.ano} - {self._likes} Likes'

class Serie(Programa):
    def __init__(self, nome, ano, seasons):
        super().__init__(nome, ano)
        self.seasons = seasons

    def __str__(self):
        return f'{self._nome} - {self.seasons} Seasons - {self.ano} - {self._likes} Likes'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


justice_league = Filme('zack snyder - liga da justiça', 2021, 240)
homem_aranha = Filme('homem aranha: sem volta para casa', 2021, 190)
o_bruxo = Serie('the witcher', 2020, 2)
got = Serie('Game of Thrones', 2011, 8)
hotd = Serie('house of the dragon', 2022, 1)

justice_league.dar_likes()
homem_aranha.dar_likes()
homem_aranha.dar_likes()
o_bruxo.dar_likes()
o_bruxo.dar_likes()
o_bruxo.dar_likes()
got.dar_likes()
got.dar_likes()
got.dar_likes()
got.dar_likes()
got.dar_likes()
hotd.dar_likes()
hotd.dar_likes()
hotd.dar_likes()
hotd.dar_likes()
hotd.dar_likes()
hotd.dar_likes()
hotd.dar_likes()

filmes_e_series = [justice_league, homem_aranha, o_bruxo, got, hotd]
maratona = Playlist('Maratonar', filmes_e_series)

for programa in maratona:
    print(programa)

print(f'Tamanho da playlist: {len(maratona)}')