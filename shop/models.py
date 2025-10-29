from django.db import models 

# Create your models here.
class Remera(models.Model):
    
    TALLE_CHOICES = [
        (1, 'XS'),
        (2, 'S'),
        (3, 'M'),
        (4, 'L'),
        (5, 'XL'),
        (6, 'XXL'),
    ]
    
    GENERO_CHOICES = [
        (1, 'Hombre'),
        (2, 'Mujer'),
        (3, 'Unisex'),
    ]
    
    marca = models.CharField(max_length=100)
    talle = models.PositiveSmallIntegerField(choices=TALLE_CHOICES)
    color = models.CharField(max_length=50)
    lisa = models.BooleanField()
    genero = models.PositiveSmallIntegerField(choices=GENERO_CHOICES)
    
    def __str__(self):
        return f"{self.marca} - {self.get_talle_display()} - {self.color} - {'Lisa' if self.lisa else 'Estampada'} - {self.get_genero_display()}"
