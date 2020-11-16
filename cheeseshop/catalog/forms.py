from django import forms


class RateCheeseForm(forms.Form):
    rating = forms.TypedChoiceField(choices=(("5", "⭐⭐⭐⭐⭐"),
                                             ("4", "⭐⭐⭐⭐"),
                                             ("3", "⭐⭐⭐"),
                                             ("2", "⭐⭐"),
                                             ("1", "⭐")),
                                    coerce=int,
                                    required=True)
