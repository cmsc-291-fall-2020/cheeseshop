from django.db import models
from django.db.models import Avg


class Cheese(models.Model):
    slug = models.SlugField(primary_key=True, max_length=200)
    name = models.CharField(unique=True, max_length=200)
    description = models.TextField(blank=True)
    country_of_origin = models.CharField(max_length=200)
    fat_content = models.FloatField(blank=True, null=True)
    last_updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ["name"]
        get_latest_by = "last_updated"

    def __str__(self):
        return self.name

    def is_high_fat(self):
        if self.fat_content is None:
            return False
        return self.fat_content >= 0.5

    def avg_rating(self):
        avg_rating = self.rating_set.all().aggregate(Avg('rating'))["rating__avg"]
        if not avg_rating:
            return "not rated"
        else:
            return round(avg_rating, 2)


class Rating(models.Model):

    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE)
    rating = models.IntegerField()
