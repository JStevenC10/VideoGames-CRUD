from django.db import models

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    plataforms = models.CharField(max_length=100, verbose_name='plataforms')
    category = models.CharField(max_length=100, verbose_name='category')
    image = models.ImageField(upload_to='image/', null=True, verbose_name='image')

    def __str__(self):
        presentation = f'{self.name} - {self.plataforms} - {self.category}'
        return presentation  

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()