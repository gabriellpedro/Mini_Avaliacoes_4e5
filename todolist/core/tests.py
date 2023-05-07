from django.test import TestCase
from core.forms import TaskForm
from core.models import TaskModel

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

class TaskFormTest(TestCase):
    def test_form_has_fields(self):
        form = TaskForm()
        expected =  ['nome_atividade','data_atividade']
        self.assertSequenceEqual(expected, list(form.fields))

class coreGetCadastro(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:cadastro'))
