from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError

from .models import Cheese


class CheeseAdminForm(forms.ModelForm):

    def clean_fat_content(self):
        # do something that validates your data
        fat_content = self.cleaned_data["fat_content"]
        if fat_content and fat_content > 1.0:
            raise ValidationError("Fat content is a percentage and cannot be more than 1.0")
        return fat_content


@admin.register(Cheese)
class CheeseAdmin(admin.ModelAdmin):

    date_hierarchy = "last_updated"
    list_display = ("name", "country_of_origin", "last_updated")
    list_filter = ("country_of_origin",)
    fields = ("name", "slug", "description", "country_of_origin", "fat_content")
    form = CheeseAdminForm
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name", "description"]


