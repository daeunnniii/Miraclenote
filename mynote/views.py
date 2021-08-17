from django.shortcuts import render
from addnote.models import Note
from . import textrank_word2vec
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='common:login')
def index(request):
    note_list = Note.objects.order_by('-reg_date')
    context = {'note_list':note_list}
    return render(request, 'mynote/fullnote.html', context)

@login_required(login_url='common:login')
def result(request):
    return render(request, 'mynote/result_test.html')

@login_required(login_url='common:login')
def view_network(request):    #def view_network(request, text)
    text='''딥러닝은 사람에게는 자연스러운 일, 즉 예시를 통해 학습하는 것을 컴퓨터가 수행할 수 있도록 가르치는 머신러닝 기법입니다. 딥러닝은 무인 자동차에서 활용되는 핵심 기술로, 자동차가 정지 신호를 인식하고 보행자와 가로등을 구별할 수 있도록 합니다. 딥러닝은 전화, 태블릿, TV 및 핸즈프리 스피커와 같은 가전의 음성 제어를 위한 핵심 요소입니다. 최근 딥러닝이 많은 관심을 받고 있습니다. 딥러닝을 통해 이전에는 불가능했던 결과를 도출합니다. 딥러닝에서는 컴퓨터 모델이 직접 이미지, 텍스트 또는 사운드로부터 분류 작업 방법을 학습합니다. 딥러닝 모델은 종종 사람의 능력을 넘어서는 최고 수준의 정확도에 도달하고 있습니다. 여러 레이어를 포함하는 신경망 아키텍처와 함께 레이블링된 대단위 데이터를 활용하여 모델이 학습됩니다. 딥러닝은 어떻게 이처럼 뛰어난 결과를 얻을 수 있을까요? 다시 말하면 정확성입니다. 딥러닝은 그 어느 때보다 높은 수준의 인식 정확도를 달성합니다. 이러한 정확성은 가전제품에서 사용자의 기대치를 충족할 수 있으며, 무인 자동차처럼 안전이 중요한 응용 분야에서는 중대한 요소로 작용합니다. 최근 딥러닝의 발전은 딥러닝을 통해 이미지의 객체를 분류하는 것과 같은 일부 작업에서 사람을 능가하는 수준까지 향상되었습니다. 1980년대에 처음 이론화된 딥러닝이 최근에 유용하게 된 두 가지 주된 이유가 있습니다. 딥러닝에는 방대한 양의 레이블 지정 데이터가 필요합니다. 예를 들어 무인 자동차를 개발하려면 수백만 장의 이미지 및 수천 시간 분량의 비디오가 필요합니다. 딥러닝에는 강력한 컴퓨팅 성능이 요구됩니다. 고성능의 GPU는 딥러닝에 효과적인 병렬 아키텍쳐를 갖고 있습니다. 개발 팀이 이를 클러스터 또는 클라우드 컴퓨팅과 함께 사용할 경우 몇 주씩 걸리던 딥러닝 네트워크의 학습 시간을 몇 시간 이내로 단축할 수 있습니다.'''
    nodes_request, edges_request = textrank_word2vec.textrank_w2v_to_vis(text)
    context = {'result': 'success', 'nodes':nodes_request, 'edges':edges_request}
    print(nodes_request)
    print(edges_request)
    return JsonResponse(context)