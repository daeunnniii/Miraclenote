from django.shortcuts import get_object_or_404, render
from addnote.models import Note
from addnote.models import NoteCnt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from django.utils.dateformat import DateFormat
from datetime import datetime

@login_required(login_url='common:login')
def index(request):
    note_list = Note.objects.select_related('user').filter(user_id=request.user.id).order_by('-reg_date')
    user = request.user
    
    today = DateFormat(datetime.now()).format('Ymd')
    noteCnt = NoteCnt.objects.get(input_date = today)
    noteCntPer = noteCnt.save_cnt/1000*100
    print(noteCntPer)
    
    context = {'note_list':note_list, 'user':user, 'noteCntPer':noteCntPer, 'noteCnt':noteCnt.save_cnt}
    return render(request, 'mynote/fullnote.html', context)
