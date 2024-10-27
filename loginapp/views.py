from django.shortcuts import render
from django.views import View
from .forms import RegisterForm
from django.contrib import messages
from . models import Person


class Register(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', locals())

    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            email = request.POST['email']
            username = request.POST['username']

            try:
                person = Person.objects.create(
                    email=email,
                    username=username,
                )
                person.save()
                messages.success(request, 'Login Successfully')
            except Exception as e:
                print(e)
                messages.warning(request, 'Failed to Login')

        return render(request, 'register.html', locals())

