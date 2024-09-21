from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def register(request):
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        name1=request.COOKIES['name'] 
        contact1=request.COOKIES['contact']
        email1=request.COOKIES['email'] 
        password1=request.COOKIES['password'] 
        print(name1,contact1,email,password1)
        if email==email1:
            if password1==password:
                data={
                    'name':name1,
                    'email':email1,
                    'contact':contact1,
                    'pass':password1
                    }
                return render(request,'dashboard.html',data)
                # return render(request,'first.html',data)
            else:
                msg="email & password not matched "
                return render(request,'login.html',{'msg':msg})
        else:
                msg="email not register "
                return render(request,'login.html',{'msg':msg})
 
    else:
       msg="Welcome to login page"
       return render(request,'login.html',{'msg':msg})

# def rdata(request):
#     print(request.method)
#     print(request.POST)
#     cstoken = request.POST.get('csrfmiddlewaretoken')
#     name = request.POST.get('nm')
#     contact = request.POST.get('con')
#     email = request.POST.get('em')
#     password = request.POST.get('pass')
#     # print(cstoken)
#     # print(name)
#     # print(contact)
#     # print(email)
#     # print(password)
#     response = render(request,'login.html')
#     response.set_cookie('name',name)
#     response.set_cookie('contact',contact)
#     response.set_cookie('email',email)
#     response.set_cookie('password',password)
#     return response
# def userlogin(request):
#     if request.method=='POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         print(email,password)


    


