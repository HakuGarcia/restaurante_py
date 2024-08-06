from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self.categoria = categoria
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"> {self._nome.ljust(20)} | {self.categoria.ljust(20)} | {self.ativo}"
    
    def listar():
        print(f"  {'Restaurante:'.ljust(20)} | {'Categoria:'.ljust(20)} | {'Avaliação'.ljust(20)} | Status:")
        for restaurante in Restaurante.restaurantes:
            print(f"> {restaurante._nome.ljust(20)} | {restaurante.categoria.ljust(20)} | {restaurante.media_avaliacao:<20} | {restaurante.ativo}")

    @property
    def ativo(self):
        return "ativo" if self._ativo else "inativo"

    def alternar_estado(self):
        self._ativo = not self._ativo
        
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        
    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return "-"
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quant_notas = len(self._avaliacao)
        media = round(soma_notas / quant_notas, 1)
        return media
    
    def add_no_cardapio(self,item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f"Cardapio - {self._nome}\n")
        for i,item in enumerate(self._cardapio, start=1):
            if hasattr(item,'descricao'):
                mensagem_prato = f"{i}. Nome: {item._nome} | Preço R${item._preco} | {item.descricao}"
                print(mensagem_prato)
            else:
                mensagem_bebida = f"{i}. Nome: {item._nome} | Preço R${item._preco} | Tamanho: {item.tamanho}ml"
                print(mensagem_bebida)