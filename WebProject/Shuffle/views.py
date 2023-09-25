from django.shortcuts import render
from django.views import View


class AppPages(View):
    def home_page(self, requests):
        return render(requests, 'Shuffle/home.html')

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


