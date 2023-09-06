from django.shortcuts import render
from .models import Lessons
from django.views.generic import ListView

# Create your views here.
class ThemeLessonsView(ListView):
    def get(self, request, **kwargs):
        context = {}
        theme = Lessons.objects.all()
        context['lesson'] = theme
        return render(request, 'mavzular.html', context)
