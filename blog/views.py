from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'detail.html', {'detail':blog_detail})

def api(request):
    return render(request, 'api.html')

def new(request):
    return render(request, 'new.html')
    
def create(request): #입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog() #model Blog의 객체 blog생성
    #blog안에 title, body, pub_date변수 생성
    blog.title = request.POST['title'] #'title' = new의 input태그의 이름, 이것을 blog라는 객체의 title변수에 담아줌
    blog.body = request.POST['body']
    blog.pub_date = timezone.datetime.now()#블로그작성순간을 넣어주는 함수 timezone을 import해와야 쓸 수 있음
    blog.save()#쿼리셋 메소드중하나/ 위에서 넣은 것들을 데이터베이스에 저장하라는 메소드 cf)객제.delete() 객체에 해당하는 내용을 지워라
    return redirect('/blog/'+str(blog.id))#redirect import해주어야함, 위에있는거 다하고 괄호안에있는 url로 이동하세요 라는 뜻
    #blog.id는 int형이지만 blog는 항상 문자열이기때문에 str로형변환함

    #render vs redirect
    #render : 함수에서 처리한 내용을 html에 변수이름으로 담아서 볼 수 있도록 함
    #redirect : 다른 사이트의 url끌어올 수 있음


def edit(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    
    if request.method == 'POST':
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.save()

        return redirect('/blog/'+str(blog.id))

    else:
        return render(request, 'edit.html', {'blog':blog})

def delete(request, blog_id):

    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()

    return redirect('/')