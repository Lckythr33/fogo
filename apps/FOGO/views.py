from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your views here.
def index(request):
    return render(request,'index.html')

def logreg(request):
    return render(request,"logreg.html")

def register(request):
    error=False
    #print(request.POST)
    if len(request.POST['company_name'])<1:
        messages.error(request,"Please enter a company name!", extra_tags='name')
        error= True
    if not EMAIL_REGEX.match(request.POST['email']):    # test whether a field matches the pattern
        messages.error(request, "Invalid Email!", extra_tags='invalidemail')
        error = True
    if len(request.POST['password'])<2:
        messages.error(request,"Please enter a better password!", extra_tags='password')
        error = True
    if request.POST['password'] != request.POST['confirm']:
        messages.error(request,"Passwords do not match!" , extra_tags='confirm')
        error = True
    if not any(x.isupper() for x in request.POST['password']):
        messages.error(request,"Password needs upper case!" , extra_tags='upper')
        error = True
    if not any(x.isdigit() for x in request.POST['password']):
        messages.error(request,"Passwords need a digit!" , extra_tags='digit')
        error = True
    if len(request.POST['street'])<1:
        messages.error(request,"Please enter an address!", extra_tags='address')
        error= True
    if not any(x.isdigit() for x in request.POST['zip_code']):
        messages.error(request,"Zip code need a digit!" , extra_tags='zip')
        error = True
    if len(request.POST['city'])<1:
        messages.error(request,"Please enter city!", extra_tags='city')
        error= True
    if len(request.POST['state'])<1:
        messages.error(request,"Please enter state!", extra_tags='state')
        error= True

    matching_users = User.objects.filter(email=request.POST['email'])
    if len(matching_users) > 0:
        messages.error(request, "Sorry, email already taken", extra_tags='email')
        error = True

    if error:
        return redirect('/logreg')
    
    hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())

    user = User.objects.create(
        name=request.POST['company_name'], 
        email=request.POST['email'], 
        street = request.POST['street'],
        city=request.POST['city'],   
        state = request.POST['state'],
        zipcode = request.POST['zip_code'],
        aptnum = request.POST['aptnum'],
        password = hashed)
    
    request.session['user_id'] = user.id
    print(user)
    print(request.session['user_id'])
    return redirect('/userdash')

def login(request):
    print(request.POST)
    matching_users = User.objects.filter(email=request.POST['log_email'])
    if len(matching_users) > 0:
        #email matched now check pw
        user = matching_users[0]
        if bcrypt.checkpw(request.POST['log_password'].encode() , user.password.encode()):
            request.session['user_id'] = user.id
            request.session['admin_flag']= user.admin_flag
            return redirect('/userdash')
        else:
            messages.error(request,"Invalid Credentials!",extra_tags='invalidcred')   
    else:
        messages.error(request,"Invalid Credentials!",extra_tags='invalidcred')  
    return redirect('/logreg')


def logout(request):
    request.session.clear()
    return redirect('/logreg')

def donations(request):
    return render(request, 'donations.html')

def account(request):

    context = {
        "users" : User.objects.filter(id=request.session['user_id']),
    }
    return render(request, 'account.html',context)

def admin(request):
    return render(request, 'admin.html')

def update(request):
    usermatch = User.objects.filter(id=request.session['user_id'])
    user = usermatch[0]
    print(user)
    error=False
    if not 'user_id' in request.session:
        messages.error(request,"No user!", extra_tags='nouser')
        print("no user")
        error= True
    if bcrypt.checkpw(request.POST['old_password'].encode() , user.password.encode()):
        messages.error(request,"Old Password Incorrect!", extra_tags='oldpassword')
        print("wrong pass")
        error= True
    
    # if error:
    #     return redirect('/logreg')

    user.name = request.POST['name']
    user.email = request.POST['email']
    user.password = request.POST['password']
    user.street = request.POST['street']
    user.city = request.POST['city']
    user.state = request.POST['state']
    user.zipcode = request.POST['zipcode']
    user.aptnum = request.POST['aptnum']
    return redirect('/')