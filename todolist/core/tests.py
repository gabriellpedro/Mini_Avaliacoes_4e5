from django.test import TestCase
from core.forms import TaskForm
from core.models import TaskModel

class Home_Test(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_200_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_text(self):
        self.assertContains(self.response, 'To-Do List:')

    def test_template_used(self):
        self.assertTemplateUsed(self.response, 'index.html')

class TaskModelTest(TestCase):
    def setUp(self):
        self.nome_atividade = 'Feriado do dia 3/05'
        self.data_atividade = "2023-05-03"
        self.atividade = TaskModel(
            nome_atividade=self.nome_atividade,
            data_atividade=self.data_atividade,
        )
        self.atividade.save()

    def test_created(self):
        self.assertTrue(TaskModel.objects.exists())

    def test_str_do_objeto(self):
        objeto = TaskModel.objects.all()[0]
        self.assertEqual(str(objeto), self.nome_atividade)

    def test_nome_atividade(self):
        nome = self.atividade.__dict__.get('nome_atividade', '')
        self.assertEqual(nome, self.nome_atividade)

    def test_data_atividade(self):
        data = self.atividade.__dict__.get('data_atividade', '')
        self.assertEqual(data, self.data_atividade)

class TaskFormTest(TestCase):
    def test_form_has_fields(self):
        form = TaskForm()
        expected =  ['nome_atividade','data_atividade']
        self.assertSequenceEqual(expected, list(form.fields))

    def make_validated_form(self, **kwargs):
        valid = dict(
            nome_atividade = 'Dia da mentira',
            data_atividade = "01/04/2023"
        )
        data = dict(valid, **kwargs)
        form = TaskForm(data)
        form.is_valid()
        return form
