from django.shortcuts import get_object_or_404, render
from addnote.models import Note
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from addnote.models import Note

@login_required(login_url='common:login')
def index(request):
    note_list = Note.objects.order_by('-reg_date')
    context = {'note_list':note_list}
    return render(request, 'mynote/fullnote.html', context)