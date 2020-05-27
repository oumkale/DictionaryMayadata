from django.shortcuts import render,get_object_or_404
from .models import Dictionary
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.forms.models import model_to_dict

# Create your views here.

def word_search(request):
    context = {}
    url_parameter = request.GET.get("q")
    if url_parameter:
        words = Dictionary.objects.filter(word__icontains=url_parameter)[:10]
        if request.is_ajax():
            html = render_to_string(template_name="word_search.html",context={"words": words})
            data_dict = {"html_from_view": html}
            return JsonResponse(data=data_dict, safe=False)
    return render(request, "home.html")

def get_word_meaning(request,pk):
    instance = get_object_or_404(Dictionary,pk=pk)
    word = model_to_dict(instance)
    return JsonResponse(word,safe=False)