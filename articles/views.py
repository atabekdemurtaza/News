from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin # new 


class ArticleListView(ListView):

    model = models.Article

    template_name = 'article_list.html'

    login_url = 'login'

class ArticleDetailView(DetailView):

    model = models.Article

    template_name = 'article_detail.html'

    login_url = 'login'

class ArticleUpdateView(UpdateView):

    model = models.Article

    fields = ['title', 'body']

    template_name = 'article_edit.html'

    login_url = 'login'

class ArticleDeleteView(DeleteView):

    model = models.Article

    template_name = 'article_delete.html'

    success_url = reverse_lazy('article_list')

    login_url = 'login'

class ArticleCreateView(LoginRequiredMixin, CreateView):

    model = models.Article

    template_name = 'article_new.html'

    fields = ['title', 'body', ]

    login_url = 'login'

    def form_valid(self, form):  # Этот функция дает нам что ? Если пользователь зарегистрирован то он
                                 # может добавить новости , если нет не может !

        form.instance.author = self.request.user

        return super().form_valid(form)

