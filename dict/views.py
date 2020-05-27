from django.shortcuts import render,get_object_or_404
from .models import Dictionary
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.forms.models import model_to_dict

# Create your views here.
