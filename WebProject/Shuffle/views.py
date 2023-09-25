from django.shortcuts import render
from django.views import View


class AppPages(View):
    def home_page(self, requests):
        soma1 = 1 + 1
        soma2 = 2+2

        return render(requests, 'Shuffle/home.html', context={'soma1': soma1, 'soma2':soma2})

    def cadastro_page(self, requests):
        return render(requests, 'Shuffle/cadastro.html')

    def adm_home_page(self, requests):
        return render(requests, 'Shuffle/adm.html')

    def login_page(self, requests):
        return render(requests, 'Shuffle/login.html')

    def manter_page(self, requests):
        return render(requests, 'Shuffle/manter.html')

    def resultado_pagina(self, requests):
        return render(requests, 'Shuffle/resultado.html')


