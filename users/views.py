from django.urls import reverse_lazy 
from .forms import CustomUserCreationForm
from django.views import generic


class SignUp(generic.CreateView):

	form_class = CustomUserCreationForm 

	success_url = reverse_lazy('login')

	template_name = 'signup.html'
	