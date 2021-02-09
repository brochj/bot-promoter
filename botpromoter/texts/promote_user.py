# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 17:25:20 2021

@author: broch
"""

import random


class PromoteUser:
    URL = 'https://cursosinteressantes.com.br/'

    def __init__(self):
        pass

    def getTextMethod(self):
        texts = [
            self.text1,
            self.text2,
            self.text3,
            self.text4,
            self.text5,
            self.text6,
        ]
        return random.choice(texts)

    def text1(self, user='', url=URL):
        return (
            f"Olá, @{user} tudo bem?\n"
            f"Se estiver afim de fazer algum curso online , que seja para se profissionalizar 🎓 ou tirar uma Renda Extra 🤑\n"
            f"Dê uma olhada em nosso site.\n\n"
            f"Tenha um ótimo dia 😊❤️\n"
            f"#cursoonline #cursosinteressantes\n"
            f"⬇️ Clique aqui: {url}"
        )

    def text2(self, user='', url=URL):
        return (
            f"Olá, @{user} tudo bom?\n"
            f"Se estiver afim de fazer algum curso online , que seja para se profissionalizar 🎓 ou tirar uma Renda Extra 🤑\n"
            f"Dê uma olhada em nosso site.\n\n"
            f"Tenha um ótimo dia 😊❤️\n"
            f"⬇️ Saiba Mais aqui: {url}"
        )

    def text3(self, user='', url=URL):
        return (
            f"Olá @{user}, vamos dar início ao seu próprio negócio?\n"
            f"Temos cursos que podem mudar sua vida🤑\n"
            f"Dê uma olhada em nosso site.\n\n"
            f"Tenha um ótimo dia 😊❤️\n"
            f"⬇️ {url}"
        )

    def text4(self, user='', url=URL):
        return (
            f"Olá @{user}, se não estiver conseguindo emprego, dê uma olhada no nosso site\n"
            f"Temos cursos online para se profissionalizar 🎓, tirar uma Renda Extra 🤑\n"
            f"criar seu Próprio Negócio.🙏\n\n"
            f"⬇️ {url}"
        )

    def text5(self, user='', url=URL):
        return (
            f"Olá @{user}, Quer criar seu próprio negócio?\n"
            f"Entre no nosso site e veja nossas opções de cursos.🙏\n\n"
            f"Tenha um ótimo dia 😊❤️\n"
            f"#cursosinteressantes\n"
            f"⬇️ Veja mais: {url}"
        )

    def text6(self, user='', url=URL):
        return (
            f"Olá @{user}, Vamos fazer começar uma carreira?\n"
            f"Cursos de Beleza, Culinária, Administração, e muito mais 😊\n\n"
            f"Veja todas as opções de cursos.🙏\n\n"
            f"⬇️ Entre aqui: {url}"
        )


if __name__ == '__main__':
    print('Just Testing' + __name__)
    tweet = PromoteUser().getTextMethod()
    a = tweet('teste')
