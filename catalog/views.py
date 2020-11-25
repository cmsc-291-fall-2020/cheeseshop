from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .forms import CheeseForm, RateCheeseForm, ReviewForm
from .models import Cheese, Rating


def cheese_list(request):
    if request.method == "POST":
        form = CheeseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("cheese_list"))
        else:
            cheeses = Cheese.objects.all()
    else:
        cheeses = Cheese.objects.all()
        form = CheeseForm()
    return render(request, "cheese_list.html", {"cheeses": cheeses, "form": form})


def cheese_delete(request, cheese_id):
    if request.method == "POST":
        cheese = get_object_or_404(Cheese, slug=cheese_id)
        cheese.delete()
    return HttpResponseRedirect(reverse("cheese_list"))


def cheese_detail(request, cheese_id):
    cheese = get_object_or_404(Cheese, slug=cheese_id)
    if request.method == "POST":
        if "rating" in request.POST:
            rating_form = RateCheeseForm(request.POST)
            if rating_form.is_valid():
                rating = Rating(cheese=cheese, rating=rating_form.cleaned_data["rating"])
                rating.save()
        else:
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review_form.save()
        url = reverse("cheese_detail", kwargs={"cheese_id": cheese.slug})
        return HttpResponseRedirect(url)
    else:
        rating_form = RateCheeseForm()
        review_form = ReviewForm(initial={"cheese": cheese.slug})
    return render(request, "cheese_detail.html", {"cheese": cheese,
                                                  "rating_form": rating_form,
                                                  "review_form": review_form})
