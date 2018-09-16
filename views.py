from django.shortcuts import render
from django.template import Context,loader
from .models import user

# Create your views here.
def index(request):
	if request.method=='POST':
		myemailid=request.POST.get('emailid')
		mypassword=request.POST.get('password')
		dbrecord=user.objects.filter(emailid=myemailid);
		for r in dbrecord:
			if r.emailid==myemailid and r.password==mypassword:
				context={'userid':r.emailid,'role':r.role};
				return render(request,'landingpage.html',context)
			else :
				msg='Ooops !  Wrong Credentials : '
				context={'message':msg};
				return render(request,'index.html',context)
				
		
	
	return render(request,'index.html')

def nxtpage(request):
	if request.method=='POST':
		return render(request,'nxtpage.html')
