from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from wiki.models import Page
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from wiki.forms import PageForm


class PageListView(ListView):
    """ Renders a list of all Pages. """
    model = Page

    def get(self, request):
        """ GET a list of Pages. """
        pages = self.get_queryset().all()
        return render(request, 'list.html', {
          'pages': pages
        })


class PageDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Page

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {
          'page': page
        })


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class CreatePage(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': PageForm()}
        return render(request, 'createPage.html', context)

    def post(self, request, *args, **kwargs):
        form = PageForm(request.POST)
        if form.is_valid():
            new_Page = form.save()
            new_Page.save()
            return HttpResponseRedirect(reverse_lazy('wiki-list-page'))
        return render(request, 'createPage.html', {'form': form})
