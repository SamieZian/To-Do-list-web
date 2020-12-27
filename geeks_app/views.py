from django.shortcuts import render, HttpResponse , redirect
from .models import GeeksModel,contactModel
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from django.contrib import messages



# Bloging View is here

def geeksView(request):
    #a = GeeksModel.objects.all()
    a = GeeksModel.objects.order_by('-date_T')
    return render(request,'index.html',{'result':a})

def addingBlog(request):
    return render(request,'add.html')

def BlogBackend(request):
    if request.method == 'POST':
        b = GeeksModel(title=request.POST['title'],description=request.POST['Description'])
        b.save()
        return redirect('/')
    
def contact_us(request):
    if request.method == 'POST':
        name = request.POST['name']
        number = request.POST['number']
        address = request.POST['address']
        address2 = request.POST['address2']
        city = request.POST['city']
        state = request.POST['state']
        postal_c = request.POST['postal_c']
        if (name=='' or number=='' or address=='' or address2=='' or city=='' or state=='' or postal_c==''):
            messages.warning(request,'Invalid field ,plz Fill All content !!')
            return redirect('/contact_us')
        else:
            con = contactModel(name = request.POST['name'],number = request.POST['number'],address = request.POST['address'],address2 = request.POST['address2'],city = request.POST['city'],state = request.POST['state'],postal_c = request.POST['postal_c'])
            con.save()
            messages.success(request,'Your Contact Detaile was Submitted   !!')
            return redirect('/')
    else:
        return render(request,'contact.html')
    

# Login & Sign up Authentications is here 

def  login_handle(request):
    if request.method == 'POST':
        LOGIN_username = request.POST['username']
        LOGIN_password = request.POST['password1']
        user = authenticate(username=LOGIN_username,password=LOGIN_password)
        if user is not None:
            login( request , user )
            messages.success(request,'You Are Successfully Log In !!')
            return redirect('/')
        else:
            messages.warning(request,'Invalid Username Or Password , Plz Try Again !!')
            return redirect('/')

def  register_handle(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 != password2:
            messages.warning(request,'Your Password & Re-Password Not Match , Plz Try Again !!')
            return redirect('/')
        else:
            myuser = User.objects.create_user(username,email,password2)
            myuser.save()
            messages.success(request, f'Hey "{username}" You Are Successfully Sign In !!')
            return redirect('/')

def logout_handle(request):
    logout(request)
    messages.warning(request, "Log Out Successfully !!")
    return redirect('/')
    
def admin_panel(request):
    a = User.objects.all()
    b = contactModel.objects.all()
    return render(request,'admin_panel.html',{'admin_data':a,'contact_data':b})


def Update_admin_value(request):
    if request.method == 'POST':
        User_id = request.POST['user_admin_id']
        abc = User.objects.get(pk=User_id)
        return render(request,'update_admin_value.html', {'data':abc})
    

def Edit_admin_data(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password2 = request.POST['password2']
        User_id = request.method['get_id']
        # instance=User_id
        myuser = User.objects.create_user(User_id,username,email,password2,instance=User_id)
        myuser.save()
        return redirect('/admin_panel')
     

def Delete_admin_data(request):
    if request.method == 'POST':
        User_id = request.POST['user_admin_id']
        update_sec = User.objects.get(pk=User_id)
        update_sec.delete()
        return redirect('/admin_panel')

    
  