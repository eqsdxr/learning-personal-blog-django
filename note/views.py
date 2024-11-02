from django.shortcuts import render, get_object_or_404

from . import models

# Create your views here.

def view_note(request, id: int):
    note = get_object_or_404(models.Note, id=id)
    return render(request=request, template_name='note/note.html', context={'note': note})