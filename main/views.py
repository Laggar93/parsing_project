import os
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .models import GoodsModel
from .forms import CsvFileForm
import csv


def list_view(request):
    goods = GoodsModel.objects.all()
    context = {
        'goods': goods
    }
    return render(request, 'list.html', context=context)


class IndexView(FormView):
    template_name = 'index.html'
    form_class = CsvFileForm
    success_url = '/'

    def form_valid(self, form):
        form.save()

        messages.add_message(self.request, messages.SUCCESS, message='CSV data has been uploaded successfully')

        return super(IndexView, self).form_valid(form)

