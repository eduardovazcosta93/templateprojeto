from django.db import models


# Create your models here.
class Register(models.Model):

    gender_ops = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )

    grade_ops = (('1', 'Ensino básico incompleto'),
                 ('2', 'Ensino básico completo'),
                 ('3', 'Ensino médio incompleto'),
                 ('4', 'Ensino médio completo'),
                 ('5', 'Ensino superior incompleto'),
                 ('6', 'Ensino superior completo')
                )
    name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    cpf = models.CharField(max_length=14)
    address = models.CharField(max_length=30)
    cep = models.CharField(max_length=9)
    gender = models.CharField(max_length=15, choices=gender_ops)
    grade = models.CharField(max_length=1, choices=grade_ops)
