from django.urls import reverse_lazy, resolve
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import render

from allauth.account.views import SignupView

from .models import UserModel, MatchModel
from .forms import UserModelForm


class ContentView(TemplateView):
    def get_context_data(self, **kwargs):
        return {
            'matchs': MatchModel.objects.all()
        }
    template_name = "blocks/index.html"


class CreateMatchView(TemplateView):
    template_name = "forms/create_match.html"


class CreateUser(CreateView):
    model = UserModel
    form_class = UserModelForm
    template_name = 'forms/create_user.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class RegisterView(SignupView):
    template_name = 'registration/register.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
