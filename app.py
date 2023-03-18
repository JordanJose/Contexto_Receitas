from pywebio import start_server
from pywebio.output import put_table, put_text, clear
from pywebio.input import input
import os

from receitas import pesquisar_receita

def main():
    user_name = input('Qual seu nome de usuário?').lower()
    put_text(user_name)
    while True:
        question = input('Qual receita você quer hoje?')
        clear()
        put_table([
            ['Q:', question],
            ['A:', pesquisar_receita(question)]
        ])

if __name__ == '__main__':
    start_server(main, port=8080, debug=True)