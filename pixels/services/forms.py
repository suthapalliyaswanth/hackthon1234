# forms.py
from django import forms

class DietCheckForm(forms.Form):
    food_items = forms.CharField(label='Food Items', widget=forms.Textarea)
