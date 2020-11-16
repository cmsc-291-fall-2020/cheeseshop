from django.shortcuts import render, get_object_or_404

from .forms import RateCheeseForm
from .models import Cheese, Rating


def cheese_list(request):
    cheeses = Cheese.objects.all()
    return render(request, "cheese_list.html", {"cheeses": cheeses})


def cheese_detail(request, cheese_id):
    cheese = get_object_or_404(Cheese, slug=cheese_id)
    if request.method == "POST":
        form = RateCheeseForm(request.POST)
        if form.is_valid():
            rating = Rating(cheese=cheese, rating=form.cleaned_data["rating"])
            rating.save()
    else:
        form = RateCheeseForm()
    return render(request, "cheese_detail.html", {"cheese": cheese, "form": form})
