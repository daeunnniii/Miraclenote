from django.shortcuts import render
from .forms import CustomPasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='common:login')
def index(request):
    return render(request, 'mypage/mypage.html')

@login_required(login_url='common:login')
def password_edit_view(request):
    if request.method == 'POST':
        password_change_form = CustomPasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "비밀번호를 성공적으로 변경하였습니다.")
            #return redirect('index')
    else:
        password_change_form = CustomPasswordChangeForm(request.user)

    return render(request, 'mypage/mypage.html', {'password_change_form':password_change_form})
