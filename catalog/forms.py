from django import forms
from django.forms import HiddenInput

from .models import Cheese, Review


class RateCheeseForm(forms.Form):
    rating = forms.TypedChoiceField(choices=(("5", "⭐⭐⭐⭐⭐"),
                                             ("4", "⭐⭐⭐⭐"),
                                             ("3", "⭐⭐⭐"),
                                             ("2", "⭐⭐"),
                                             ("1", "⭐")),
                                    coerce=int,
                                    required=True)


class CheeseForm(forms.ModelForm):

    class Meta:
        fields = ("name", "slug", "description", "country_of_origin", "fat_content")
        model = Cheese


class ReviewForm(forms.ModelForm):

    class Meta:
        fields = ("review", "name", "cheese")
        model = Review
        widgets = {
            "cheese": HiddenInput
        }
