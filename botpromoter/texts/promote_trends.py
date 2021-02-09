# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 21:58:51 2021

@author: broch
"""
import random


class PromoteTrends:
    URL = 'https://cursosinteressantes.com.br/'

    def getTweetMethod(self):
        texts = [
            self.text1,
            self.text2,
            self.text3,
            self.text4,
            self.text5,
            self.text6,
        ]
        return random.choice(texts)

    def text1(self, trends='', url=URL):
        return (
            f"Olá, tudo bem?\n"
            f"Se estiver afim de fazer algum curso online , que seja para se profissionalizar 🎓 ou tirar uma Renda Extra 🤑\n"
            f"Dê uma olhada em nosso site.\n\n"
            f"Tenha um ótimo dia 😊❤️\n"
            f"{trends}\n"
            f"⬇️ Abra aqui: {url}"
        )

    def text2(self, trends='', url=URL):
        return (
            f"Fala galera!😃\n"
            f"Alguém está procurando algum curso para fazer uma Renda Extra 🤑\n"
            f"Dê uma passada em nosso site.\n\n"
            f"{trends}\n"
            f"⬇️ Clique aqui: {url}"
        )

    def text3(self, trends='', url=URL):
        return (
            f"Olá, vamos dar início ao seu próprio negócio?\n"
            f"Temos curso que podem mudar sua vida🤑\n"
            f"Dê uma olhada em nosso site.\n\n"
            f"Tenha um ótimo dia 😊❤️\n"
            f"{trends}\n"
            f"⬇️ {url}"
        )

    def text4(self, trends='', url=URL):
        return (
            f"Não está conseguindo emprego?\n"
            f"Temos cursos online para se profissionalizar 🎓, tirar uma Renda Extra 🤑\n"
            f"ou melhor ainda, criar seu Próprio Negócio.🙏\n\n"
            f"{trends}\n"
            f"⬇️ Leia mais: {url}"
        )

    def text5(self, trends='', url=URL):
        return (
            f"Quer criar seu próprio negócio?\n"
            f"Entre no nosso site e veja nossas opções de cursos.🙏\n\n"
            f"{trends}\n"
            f"⬇️ Veja mais: {url}"
        )

    def text6(self, trends='', url=URL):
        return (
            f"Vamos fazer começar uma carreira?\n"
            f"Manicure, Alongamento de Unhas, Design de Sobrancelhas e muito mais\n\n"
            f"Entre no nosso site e veja todas as opções de cursos.🙏\n\n"
            f"{trends}\n"
            f"⬇️ Entre aqui: {url}"
        )


if __name__ == '__main__':
    print('Just Testing')
    tweet = PromoteTrends().getTweetMethod()
    a = tweet('teste')
