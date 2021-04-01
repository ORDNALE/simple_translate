""" pip install translate

importando a biblioteca translate """
from translate import Translator

# define o idioma do texto e qual idioma a ser traduzido
idioma = Translator(from_lang='pt-br', to_lang='en')


texto = input(str('Digite o Texto: '))
traducao = idioma.translate(texto)

print(traducao)
