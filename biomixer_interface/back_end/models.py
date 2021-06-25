from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


# Create your models here.
class Doc(models.Model):
    upload = models.FileField(upload_to='recipes/')

    def __str__(self):
        return str(self.pk)


class Recipe(models.Model):
    """
        An additive recipe of biomaterials
    """
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    img_link = models.URLField()
    creation_date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.name


class Step(models.Model):
    """
        List of materials and its Quantities
        used in a recipe
    """
    recipe_id = models.ForeignKey(Recipe, on_delete=models.RESTRICT)
    text = models.CharField(max_length=100)


class Material(models.Model):
    """
        Material used in a step recipe.
    """
    class Types(models.TextChoices):
        CARBOHIDRATES = 'CH', _('Carbohidrates')
        PROTEINS = 'PR', _('Proteins')
        MINERALS = 'MN', _('Minerals')
        LIPIDS = 'LP', _('Lipids')
        RESINS = 'RS', _('Resins')
        PHENOLICS = 'PH', _('Phenolics')
        NATURAL_COMPOSITES = 'NC'

    type = models.CharField(
        max_length=2,
        choices=Types.choices
    )
    name = models.CharField(max_length=200)
    chemical_formula = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Supply(models.Model):
    """
        Material and it's order in a recipe \n
        @:attribute recipe: Recipe to which it belongs the current supply \n
        @:param material: Material used in this supply \n
        @:param position: Order in which materials are placed
    """
    class Types(models.TextChoices):
        GRAMS = 'g', _('Grams')
        MILILITERS = 'ml', _('Milliliters')

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    position = models.IntegerField()
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    value = models.IntegerField()
    type = models.CharField(
        max_length=20,
        choices=Types.choices)
