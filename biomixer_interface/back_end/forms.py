from django import forms

class Ingredient:
    name = ""
    quantity = 0
    unity = ""
    Id = ""

class Mix:
    id = ""
    name = ""
    label = ""
    ingredients<Ingredient> = []

class MixForm (forms.Form):
