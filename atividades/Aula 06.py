class Musica:
    nome = ""
    artista = ""
    duracao = int

musica01 = Musica()
musica01.nome = "E.T."
musica01.artista = "Katy Perry"
musica01.duracao = 501

musica02 = Musica()
musica02.nome = "Take It Off"
musica02.artista = "Kesha"
musica02.duracao = 342

musica03 = Musica()
musica03.nome = "Blow"
musica03.artista = "Kesha"
musica03.duracao = 414

print(f"  {'Musica:'.ljust(20)} | {'Artista:'.ljust(20)} | Duração:")
print(f"> {musica01.nome.ljust(20)} | {musica01.artista.ljust(20)} | {musica01.duracao} segundos")
print(f"> {musica02.nome.ljust(20)} | {musica02.artista.ljust(20)} | {musica02.duracao} segundos")
print(f"> {musica03.nome.ljust(20)} | {musica03.artista.ljust(20)} | {musica03.duracao} segundos")