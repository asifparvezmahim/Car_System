from typing import Any
from django.shortcuts import render, redirect, get_list_or_404
from . import forms
from . import models
from cars.models import Car
from django.contrib.auth.models import User

# Create your views here.
from django.views.generic import DetailView


class DetailClassView(DetailView):
    model = models.Car
    pk_url_kwarg = "id"
    template_name = "car_details.html"

    def post(self, request, *arg, **kwarg):
        comment_form = forms.CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *arg, **kwarg)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        comment_form = forms.CommentForm()

        context["comments"] = comments
        context["comment_form"] = comment_form
        return context
