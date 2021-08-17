from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Note
from django.utils import timezone

import librosa
import soundfile as sf

import urllib3
import json
import base64

from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='common:login')
def index(request):
    return render(request, 'addnote/making_note.html')

@login_required(login_url='common:login')
def saveNote(request):
    user_input_str = request.POST['file_route']
    note = Note()
    note.subject = request.POST['subject']
    note.note_description = request.POST['note_description']
    note.audio = request.FILES['audio']
    note.reg_date=timezone.now()
    note.save()

    openApiURL = "http://aiopen.etri.re.kr:8000/WiseASR/Recognition"
    accessKey = "b1a210f3-f6fd-4fab-8819-0e47149b2a92"
    languageCode = "korean"
    
    sr = 16000
    sec = 30
    y, sr = librosa.load('./media/audio/'+user_input_str, sr=sr)
    test = round(len(y)/sr)
    strResult = ""
    
    for i in range(0, test, 10):
        file_name = str(datetime.now().microsecond)
        ny = y[sr*i:sr*(i+10)]
        sf.write('./media/result/'+file_name+'.wav', ny, sr, format='WAV', endian='LITTLE', subtype='PCM_16') # 깨지지 않음

        audioFilePath = './media/result/'+file_name+'.wav'
        file = open(audioFilePath, "rb")
        audioContents = base64.b64encode(file.read()).decode("utf8")
        file.close()

        requestJson = {
            "access_key": accessKey,
            "argument": {
                "language_code": languageCode,
                "audio": audioContents
            }
        }

        http = urllib3.PoolManager()
        response = http.request(
            "POST",
            openApiURL,
            headers={"Content-Type": "application/json; charset=UTF-8"},
            body=json.dumps(requestJson)
        )
        
        jsonObject = json.loads(str(response.data,"utf-8"))
        strResult = strResult + str(jsonObject.get("return_object").get("recognized"))

    n = Note.objects.get(id=note.id)
    n.sttText = strResult
    n.user = request.user
    n.save()
    
    return redirect('/mynote/')   
