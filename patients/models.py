from django.db import models

class Patient(models.Model):
    STATUS = (
        ('active','Ativo'),
        ('inactive','Inativo'),
        ('screening','Triagem'),
    )


    name = models.CharField(max_length=155, verbose_name='Nome')
    age = models.IntegerField(verbose_name='Idade')
    gender = models.CharField(max_length=155, verbose_name='Genero')
    date_of_birth = models.DateField(verbose_name='Data de nascimento')
    marital_status = models.CharField(max_length=155, verbose_name='Estado Civil')
    education = models.CharField(max_length=155,verbose_name='Escolaridade')
    profession = models.CharField(max_length=155, verbose_name='Profissao')
    status = models.CharField(max_length=155, choices=STATUS, default='inactive')

    class Meta:
        verbose_name = 'Paciente'

    def __str__(self) -> str:
        return self.name