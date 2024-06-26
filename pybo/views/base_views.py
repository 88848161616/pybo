from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question

def index(request):
    """
    pybo 목록 출력

    """
    # 입력 인자
    page = request.GET.get('page', '1') # 페이지

    # 조회
    question_list = Question.objects.order_by('-create_date')

    # 페이징 처리
    paginator = Paginator(question_list, 10) # 페이지 당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id): # , 뒤는 매개변수로 url에 입력받은 수가 자동으로 이곳으로 전달됨.
    """
    pybo 내용 출력

    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)