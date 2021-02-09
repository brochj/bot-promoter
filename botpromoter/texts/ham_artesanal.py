# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 09:20:34 2021

@author: broch
"""

import random


class HamArtesanalUser:
    URL = 'https://cursosinteressantes.com.br/posts/curso-de-hamburger-artesanal'

    def __init__(self):
        pass

    def getTweetMethod(self):
        texts = [
            self.text1,
            self.text2,
            self.text3,
            self.text4,
            self.text5,
            self.text6,
            self.text7,
            self.text8,
            self.text9,
            self.text10,
            self.text11,
            self.text12,
            self.text13,
            self.text14,
        ]
        return random.choice(texts)

    def text1(self, user='', url=URL):
        return (
            f"Olá @{user}😃\n"
            f"Está procurando algum curso para fazer uma Renda Extra 🤑\n"
            f"🍔Curso de Hamburguer Artesanal.🍔 \n"
            f"Dê uma passada em nosso site.\n"
            f"\n\n"
            f"⬇️ {url}"
        )

    def text2(self, user='', url=URL):
        return (
            f"Olá @{user}😃\n"
            f"🤑 Gostaria de Faturar até 10 mil reais por mês trabalhando no seu próprio negócio?\n"
            f"🍔 O Curso de Hambúrguer Artesanal é a sua garantia para você mudar de vida.\n"
            f"\n"
            f"👀 Conheça todo Conteúdo do Curso clicando abaixo:\n\n"
            f"⬇️ {url}"
        )

    def text3(self, user='', url=URL):
        return (
            f"Olá @{user}😃\n"
            f"🍔 Em Média, os alunos do Curso de Hambúrguer Artesanal conseguem faturar até 7 mil reais de lucro 🤑 em até três meses.\n"
            f"Não perca essa chance!\n\n"
            f"⬇️ {url}"
        )

    def text4(self, user='', url=URL):
        return (
            f"Olá @{user}😃\n"
            f"Escolha mudar de vida e crescer financeiramente, conquiste seus sonhos, seja seu próprio chefe. \n"
            f"Aposto que não irá se arrepender como as diversas pessoas que já adquiriram o Curso de Hambúrguer Artesanal \n"
            f"e hoje já alcançaram tudo isso.\n\n"
            f"⬇️ {url}"
        )

    def text5(self, user='', url=URL):
        return (
            f"Olá @{user}😃\n"
            f"Está buscando um curso para aprender a fazer hamburgueres de forma profissional?\n"
            f"selecionamos um curso que poderá lhe ajudar muito a se capacitar:\n"
            f"\n"
            f"Qualquer Pessoa pode fazer, mesmo começando do Zero.\n\n"
            f"⬇️ {url}"
        )

    def text6(self, user='', url=URL):
        return (
            f"Olá @{user}😃\n"
            f"Você irá aprender no curso de 🍔Hamburguer Artesanal,\n"
            f"todos os processos para fazer um hambúrguer de qualidade,\n"
            f"mesmo que você não saiba nada.👨🏼‍🍳\n"
            f"Se você deseja mudar de vida clique no link abaixo 🤩:\n\n"
            f"⬇️ {url}"
        )

    def text7(self, user='', url=URL):
        return (
            f"Olá @{user}😃\n"
            f"🍔O Curso de Hambúrguer Artesanal foi criado para você aprender a preparar\n"
            f"👨🏼‍🍳 OS VERDADEIROS HAMBÚRGUERES ARTESANAIS MAIS DELICIOSOS.\n"
            f"\n"
            f"Não perca tempo e faça sua inscrição\n"
            f"⬇️ {url}"
        )

    def text8(self, user='', url=URL):
        return (
            f"Olá @{user}😃\n"
            f"Quer começar um negócio de hambúrguer totalmente rentável do absoluto zero?\n"
            f"Então confira 🍔 Curso de Hambúrguer Artesanal!\n"
            f"É o que você precisava para começar a realizar os seus sonhos 😊❤️.\n"
            f"Aproveite 👌!\n\n"
            f"⬇️ {url}"
        )

    def text9(self, user='', url=URL):
        return (
            f"Olá @{user}😃\n"
            f"No 🍔 Curso de Hambúrguer Artesanal você aprenderá a fazer o melhor e mais suculento hambúrguer artesanal.\n"
            f"O único curso que te ensina todos os bastidores passo a passo para você iniciar sua produção ainda essa semana. \n\n"
            f"⬇️ {url}"
        )

    def text10(self, user='', url=URL):
        return (
            f"Olá @{user}😃\n"
            f"Saia na frente dos seus concorrentes e aprenda com o 🍔 Curso de Hambúrguer Artesanal,\n"
            f"o passo a passo para produzir e vender os melhores hamburgueres da sua cidade.🤑\n"
            f"Se você deseja mudar de Vida clique no link abaixo: 👀\n\n"
            f"⬇️ {url}"
        )

    def text11(self, user='', url=URL):
        return (
            f"Olá @{user}😃\n"
            f"🍔 O Curso de Hambúrguer Artesanal é para quem tem plena certeza de que quer mudar a vida.🤑\n"
            f"No Curso você irá aprender tudo para criar o hamburguer ideal para todos os tipos de público.\n\n"
            f"⬇️ {url}"
        )

    def text12(self, user='', url=URL):
        return (
            f"Olá @{user}😃\n"
            f"🍔 Aprenda a fazer hambúrgueres de sabores variados, suculentos e saborosos com o Curso de Hambúrguer Artesanal e, \n"
            f"ao mesmo tempo, tenha sua própria renda sem sair de casa e sem precisar investir muito dinheiro.🤑\n\n"
            f"⬇️ {url}"
        )

    def text13(self, user='', url=URL):
        return (
            f"Olá @{user}😃\n"
            f"🍔 No curso de Hambúrguer Artesanal você vai ter acesso ao treinamento que vai ensinar você a preparar as melhores combinações [ Blends ] de hambúrgueres.\n\n"
            f"E Claro! Molhos. Pois são eles que dão um toque especial a todas as receitas.\n"
            f"⬇️ {url}"
        )

    def text14(self, user='', url=URL):
        return (
            f"Olá @{user}😃\n"
            f"Você está disposto a investir em algo que lhe dê retorno rápido? 🤑\n"
            f"Se a sua resposta é Sim, então precisa conhecer o Curso de Hambúrguer Artesanal.🍔\n"
            f"Com ele você pode iniciar sua Produção ainda essa semana.\n"
            f"⬇️ {url}"
        )


class HamArtesanalTrends:
    URL = 'https://cursosinteressantes.com.br/posts/curso-de-hamburger-artesanal'

    def getTweetMethod(self):
        texts = [
            self.text1,
            self.text2,
            self.text3,
            self.text4,
            self.text5,
            self.text6,
            self.text7,
            self.text8,
            self.text9,
            self.text10,
            self.text11,
            self.text12,
            self.text13,
            self.text14,
        ]
        return random.choice(texts)
    
    def text1(self, trends='', url=URL):
        return (
            f"Fala galera!😃\n"
            f"Alguém está procurando algum curso para fazer uma Renda Extra 🤑\n"
            f"🍔Curso de Hamburguer Artesanal.🍔 \n"
            f"Dê uma passada em nosso site.\n"
            f"\n\n"
            f"{trends}\n"
            f"⬇️ {url}"
        )

    def text2(self, trends='', url=URL):
        return (
            f"🤑 Gostaria de Faturar até 10 mil reais por mês trabalhando no seu próprio negócio?\n"
            f"🍔 O Curso de Hambúrguer Artesanal é a sua garantia para você mudar de vida.\n"
            f"\n"
            f"👀 Conheça todo Conteúdo do Curso clicando abaixo:\n\n"
            f"{trends}\n"
            f"⬇️ {url}"
        )

    def text3(self, trends='', url=URL):
        return (
            f"🍔 Em Média, os alunos do Curso de Hambúrguer Artesanal conseguem faturar até 7 mil reais de lucro 🤑 em até três meses.\n"
            f"Aposto que isso é bem mais que você anda tirando mensalmente, correto? \n"
            f"Não perca essa chance!\n\n"
            f"{trends}\n"
            f"⬇️ {url}"
        )

    def text4(self, trends='', url=URL):
        return (
            f"Escolha mudar de vida e crescer financeiramente, conquiste seus sonhos, viaje, seja seu próprio chefe. \n"
            f"Aposto que não irá se arrepender como as diversas pessoas que já adquiriram o Curso de Hambúrguer Artesanal \n"
            f"e hoje já alcançaram tudo isso.\n\n"
            f"{trends}\n"
            f"⬇️ {url}"
        )

    def text5(self, trends='', url=URL):
        return (
            f"Para você que está buscando um curso para aprender a fazer hamburgueres de forma profissional,\n"
            f"selecionamos um curso que poderá lhe ajudar muito a se capacitar:\n"
            f"\n"
            f"Qualquer Pessoa pode fazer, mesmo começando do Zero.\n\n"
            f"{trends}\n"
            f"⬇️ {url}"
        )

    def text6(self, trends='', url=URL):
        return (
            f"Você irá aprender no curso de 🍔Hamburguer Artesanal em Vídeo Aulas,\n"
            f"todos os processos para fazer um hambúrguer de qualidade,\n"
            f"mesmo que você não saiba nada.👨🏼‍🍳\n"
            f"Se você deseja mudar de vida clique no link abaixo 🤩:\n\n"
            f"{trends}\n"
            f"⬇️ {url}"
        )

    def text7(self, trends='', url=URL):
        return (
            f"🍔O Curso de Hambúrguer Artesanal foi criado para você aprender a preparar\n"
            f"👨🏼‍🍳 OS VERDADEIROS HAMBÚRGUERES ARTESANAIS MAIS DELICIOSOS.\n"
            f"\n"
            f"Não perca tempo e faça sua inscrição clicando no link abaixo\n\n"
            f"{trends}\n"
            f"⬇️ {url}"
        )

    def text8(self, trends='', url=URL):
        return (
            f"Quer começar um negócio de hambúrguer totalmente rentável do absoluto zero?\n"
            f"Então confira 🍔 Curso de Hambúrguer Artesanal completo em vídeo aulas!\n"
            f"É o que você precisava para começar a realizar os seus sonhos 😊❤️.\n"
            f"Aproveite 👌!\n\n"
            f"{trends}\n"
            f"⬇️ {url}"
        )

    def text9(self, trends='', url=URL):
        return (
            f"No 🍔 Curso de Hambúrguer Artesanal você aprenderá a fazer o melhor e mais suculento hambúrguer artesanal.\n"
            f"O único curso que te ensina todos os bastidores passo a passo para você iniciar sua produção ainda essa semana. \n\n"
            f"{trends}\n"
            f"⬇️ {url}"
        )

    def text10(self, trends='', url=URL):
        return (
            f"Saia na frente dos seus concorrentes e aprenda com o 🍔 Curso de Hambúrguer Artesanal,\n"
            f"o passo a passo para produzir e vender os melhores hamburgueres da sua cidade.🤑\n"
            f"Se você deseja mudar de Vida clique no link abaixo: 👀\n\n"
            f"{trends}\n"
            f"⬇️ {url}"
        )

    def text11(self, trends='', url=URL):
        return (
            f"🍔 O Curso de Hambúrguer Artesanal é para quem tem plena certeza de que quer mudar a vida.🤑\n"
            f"O Curso conta com vídeo aulas onde você irá aprender tudo para criar o hamburguer ideal para todos os tipos de público.\n\n"
            f"{trends}\n"
            f"⬇️ {url}"
        )

    def text12(self, trends='', url=URL):
        return (
            f"🍔 Aprenda a fazer hambúrgueres de sabores variados, suculentos e saborosos com o Curso de Hambúrguer Artesanal e, \n"
            f"ao mesmo tempo, tenha sua própria renda sem sair de casa e sem precisar investir muito dinheiro.🤑\n\n"
            f"{trends}\n"
            f"⬇️ {url}"
        )

    def text13(self, trends='', url=URL):
        return (
            f"🍔 No curso de Hambúrguer Artesanal você vai ter acesso ao treinamento que vai ensinar você a preparar as melhores combinações [ Blends ] de hambúrgueres.\n"
            f"Também vai ter acesso a receitas maravilhosas.\n"
            f"E Claro! Molhos. Pois são eles que dão um toque especial a todas as receitas.\n"
            f"{trends}\n"
            f"⬇️ {url}"
        )

    def text14(self, trends='', url=URL):
        return (
            f"Você está disposto a investir em algo que lhe dê retorno rápido? 🤑\n"
            f"Se a sua resposta é Sim, então precisa conhecer o Curso de Hambúrguer Artesanal.🍔\n"
            f"Com ele você pode iniciar sua Produção ainda essa semana.\n"
            f"{trends}\n"
            f"⬇️ {url}"
        )


if __name__ == '__main__':
    print('Just Testing' + __name__)
    tweet = PromoteUser().getTextMethod()
    a = tweet('teste')
