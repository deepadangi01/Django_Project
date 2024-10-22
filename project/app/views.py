from django.shortcuts import render
from.models import Students
from.models import myQuery

# Create your views here.
def home(request):
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('con')
        password=request.POST.get('pass')
        cpassword=request.POST.get('cpass')
        if password==cpassword:
            user=Students.objects.filter(stu_email=email)
            if user:
               
                return render(request,'login.html')
            else:
                Students.objects.create(
                    stu_name=name,
                    stu_email=email,
                    stu_contact=contact,
                    stu_password=password
                    )
                msg="Registration sccessfull"
                return render (request,'index.html',{'msg':msg})
        else:
            msg="Password is not matching"
            return render(request,'register.html',{'msg':msg})
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('pass')
        user=Students.objects.filter(stu_email=email)
        if user:
            userdata=Students.objects.get(stu_email=email)
            print(userdata)
            email1=userdata.stu_email
            password1=userdata.stu_password
            name1=userdata.stu_name
            contact1=userdata.stu_contact
            if password==password1:
                data={
                    'name':name1,
                    'email':email1,
                    'password':password1,
                    'contact':contact1,
                }
                query_data = myQuery.objects.filter(stu_email=email)
                return render(request,'dashboard.html',{'data':data,'query_data':query_data})
            else:
                msg="email and password not matched"
                return render(request,'login.html',{'msg':msg})
        else:
            msg="email not registed"
            return render(request,'register.html',{'msg':msg})
    else:
        return render(request,'login.html')
def query(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        query=request.POST.get('query')

        myQuery.objects.create(
        stu_email=email,
        stu_name=name,
        stu_contact=contact,
        stu_query=query)
        data=Students.objects.get(stu_email=email)
        data={
        'name':data.stu_name,
        'email':data.stu_email,
        'contact':data.stu_contact,
        'password':data.stu_password
        }
        
        query_data=myQuery.objects.filter(stu_email=email)
        print(data,query_data)
        return render(request,'dashboard.html',{'data':data,'query_data':query_data})
    msg="succusfull....."
    return render(request,'dashboard.html',{'msg':msg})

def edit(request,x):
    data1=myQuery.objects.get(id=x)
    id1=data1.id
    email=data1.stu_email
    name=data1.stu_name
    contact=data1.stu_contact
    query=data1.stu_query
    data=Students.objects.get(stu_email=email)
    data={
        'name':data.stu_name,
        'email':data.stu_email,
        'contact':data.stu_contact,
        'password':data.stu_password
        }
    query_data=myQuery.objects.filter(stu_email=email)
    edit_data={
        'id':id1,
        'email':email,
        'name':name,
        'contact':contact,
        'query':query,
    }
    return render(request,'dashboard.html',{'key2':edit_data, 'data':data, 'query_data':query_data})
def update(request,x):
    if request.method=="POST":
        name1=request.POST.get('name')
        email1=request.POST.get('email')
        contact1=request.POST.get('contact')
        query1=request.POST.get('query')
        print(name1,email1,query1)
        oldData=myQuery.objects.get(id=x)

        oldData.stu_name=name1
        oldData.stu_email=email1
        oldData.stu_contact=contact1
        oldData.stu_query=query1
        oldData.save()
    
        data=Students.objects.get(stu_email=email1)
        
        data={
           'name':data.stu_name,
           'email':data.stu_email,
           'contact':data.stu_contact,
           'password':data.stu_password
        }  
        query_data=myQuery.objects.filter(stu_email=email1)
    return render(request,'dashboard.html',{'data':data, 'query_data':query_data}) 

def delete(request,x,y):
    queryData=myQuery.objects.filter(id=x)
    if queryData:
        queryData=myQuery.objects.get(id=x)
        name1=queryData.stu_name
        email1=queryData.stu_email
        contact1=queryData.stu_contact
        query1=queryData.stu_query

        queryData.delete()
        data=Students.objects.get(stu_email=email1)
        
        data={
           'name':data.stu_name,
           'email':data.stu_email,
           'contact':data.stu_contact,
           'password':data.stu_password
        } 
        query_data=myQuery.objects.filter(stu_email=email1)
        return render(request,'dashboard.html',{'data':data,'query_data':query_data})
    else:
        data=Students.objects.get(stu_email=y)
        data={
           'name':data.stu_name,
           'email':data.stu_email,
           'contact':data.stu_contact,
           'password':data.stu_password
        }  
        query_data=myQuery.objects.filter(stu_email=y)
        return render(request,'dashboard.html',{'query_data':query_data,'data':data})
def logout(request):
    return render(request,'index.html')        
       
    
    

# def rdata(request):
#     print(request.method)
#     print(request.POST)
#     cstoken = request.POST.get('csrfmiddlewaretoken')
#     name = request.POST.get('nm')
#     contact = request.POST.get('con')
#     date = request.POST.get('dt')
#     email = request.POST.get('em')
#     password=request.POST.get('pass')
#     course=request.POST.get('course')
    
#     # print(cstoken)
#     # print(name)
#     # print(contact)
#     # print(email)
#     # print(password)
#     response = render(request,'login.html')
#     response.set_cookie('name',name)
#     response.set_cookie('contact',contact)
#     response.set_cookie('date',date)
#     response.set_cookie('email',email)
#     response.set_cookie('pass',password)
#     response.set_cookie('course',course)
#     return response
# def userlogin(request):
#     if request.method=='POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         print(email,password)


    


