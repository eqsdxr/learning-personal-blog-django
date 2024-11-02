from django.shortcuts import render
from note.models import Note
# Create your views here.

def homepage_view(request):
    return render(request=request, template_name="homepage/homepage.html", context={'notes': Note.objects.all()})