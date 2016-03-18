from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect,render_to_response
from django.template import RequestContext
from models import *
from forms import *
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger

# Create your views here.

def index(request):
	posts=Post.objects.filter(published_time__isnull=False)
	paginator = Paginator(posts,4)
	try:
		page = int(request.GET.get('page',1))
		posts=paginator.page(page)
	except (InvalidPage,EmptyPage,PageNotAnInteger):
		pass
	return render(request,'base.html',locals())

#def post_list(request):
#	posts=Post.objects.filter(published_time__isnull=False)
#	return render(request,'post_list.html',locals())

def post_detial(request,id):
	post=Post.objects.get(id=id)
	return render(request,'post_detial.html',locals())


def post_new(request):
	if request.method == 'POST':
		user=User.objects.get(username='zhao')
		form = PostForm(request.POST) 
		if form.is_valid:
			title=request.POST['title']
			content=request.POST['content']
			post=Post.objects.create(title=title,
						content=content,
						user=user)
			id=post.id
			return HttpResponseRedirect('/post/%s'%id)
	else :
		form = PostForm()
		return render(request,'post_new.html',locals())	

def post_draft(request):
	posts=Post.objects.filter(published_time__isnull=True)
	paginator = Paginator(posts,4)
	try :
		page = int(request.GET.get('page',1))
		posts = paginator.page(page)
	except (InvalidPage,EmptyPage,PageNotAnInteger):
		pass
	return render(request,'post_draft.html',locals())



def post_publish(request,id):
	id=id
	post=Post.objects.get(id=id)
	post.publish()
	return HttpResponseRedirect('/')
	
def post_register(request):
	user=request.user
	if request.method == 'POST':
		form = RegisterForm(request.POST,instance=user)
		if form.is_valid():
			if request.POST.get('password') == request.POST.get('repassword'):
				form.save()
				return HttpResponseRedirect('/post/login/')
	else:
		form = RegisterForm()			
		return render_to_response('register.html',RequestContext(request,locals()))


def post_login(request):
	username=request.POST.get('username','')
	password = request.POST.get('password','')
	user=auth.authenticate(username=username,password=password)
	if user is not None and user.is_active:
		auth.login(request,user)
		return HttpResponseRedirect('/')
	else:
		form = LoginForm()
		return render(request,'login.html',locals())
