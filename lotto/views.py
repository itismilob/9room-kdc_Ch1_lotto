from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm

# Create your views here.
def index(request):
    lottos = GuessNumbers.objects.all()
    return render(request, 'lotto/default.html', {'lottos':lottos}) # context-dict


def post(request):

    if request.method == "POST" :
        form = PostForm(request.POST) # 채워진 양식

        if form.is_valid(): # 데이터 유효성 검사
            lotto = form.save(commit=False) # 받아온 데이터 중간 저장 (실제 DB에는 반영하지 않음)
            # lotto.text = lotto.text.upper() 데이터를 수정할 수 있다.
            lotto.generate()
            # lotto.save() 수정이 끝나면 저장한다 (generate 함수에서 저장함)

            return redirect("index")

    else:
        form = PostForm() # 비워진 양식
        return render(request, 'lotto/form.html', {'form':form})



def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk=lottokey) # id == pk
    
    return render(request, 'lotto/detail.html', {'lotto':lotto})







def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello</h1>")