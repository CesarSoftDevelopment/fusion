from django.test import TestCase
from django.test import Client    # metodos http
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.dados = {
            'nome': 'Cesar Developer',
            'email': 'cesardeveloper@gmail.com',
            'assunto': 'Meu assunto',
            'mensagem': 'Minha mensagem'
        }
        self.cliente = Client()

    # nos estamos aplicando um post pra essa rota aplicando estes dados
    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302)

    def test_form_invalid(self):
        dados = {
            'nome': 'Cesar Developer',
            'assunto': 'Meu assunto'
        }
        request = self.cliente.post(reverse_lazy('index'), data=dados)
        self.assertEquals(request.status_code, 200)
