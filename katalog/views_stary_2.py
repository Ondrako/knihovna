from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView

from .models import Kniha
from .forms import KnihaForm

# Create your views here.

class NovaKniha(View):
    def post(self, request):
        form = KnihaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("podekovani")
        contex = { "form" : form }
        return render(request, "knihy/nova_kniha.html", contex)

    def get(self, request):
        form = KnihaForm()
        contex = { "form" : form }
        return render(request, "knihy/nova_kniha.html", contex)

class NovaKniha2(FormView):
    form_class = KnihaForm
    template_name = "knihy/nova_kniha.html"
    succes_url = "dekuji"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class Dekuji(TemplateView):
    template_name = "knihy/dekuji.html"

    def get_context_data(self, **kwargs):
        contex =  super().get_context_data(**kwargs)
        contex["jmeno_slona"] = "Jumbo"
        return contex

#class Seznam(TemplateView):
#    template_name = "knihy/seznam.html"
#    
#    def get_context_data(self, **kwargs):
#        contex = super().get_context_data(**kwargs)
#        knihy = Kniha.objects.all()
#        contex["knihy"] = knihy
#        return contex

class Seznam2(ListView):
    model = Kniha
    template_name = "knihy/seznam.html"
    contex_object_name = "seznam"

#def seznam(request):
#    knihy = Kniha.objects.all()
#    return render(request, "knihy/seznam.html", {"knihy": knihy})

class Detail(DetailView):
    model = Kniha
    template_name = "knihy/detail.html"

#def detail(request, id):
#    kniha = Kniha.objects.get(id=id)
#    return render(request, "knihy/detail.html", {"kniha": kniha})

