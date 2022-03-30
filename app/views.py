from django.shortcuts import render, redirect
from django.db import connection
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def index(request):
    """Shows the main page"""

    ## Show recommendation list
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM house_info ORDER BY expected_price LIMIT(5)")
        houses = cursor.fetchall()

    result_dict = {'records': houses}

    return render(request,'app/index.html',result_dict)



def rent(request):

    ## Rent the house
    if request.POST:
        if request.POST['action'] == 'rent':
            with connection.cursor() as cursor:
                cursor.execute("UPDATE house_info SET house_status = 'RENTED' WHERE house_title = %s",[request.POST['id']])
                # Update the record in rent_history
            
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM house_info ORDER BY expected_price")
        houses = cursor.fetchall()
    result_dict = {'records': houses}

    return render(request,'app/rent.html',result_dict)




def register(request):
    context={}
    status=''

    ## Add the user
    if request.POST:
        with connection.cursor() as cursor:
            user_name = request.POST['user_name']
            real_name = request.POST['real_name']
            password = request.POST['password']
            phone_no = request.POST['phone_number']
            email = request.POST['email']

            cursor.execute("INSERT INTO user_info VALUES (%s,%s,%s,%s,%s)",
            [user_name,real_name,password,phone_no,email])

            user = User.objects.create_user(user_name, email, password)
            user.save()

            status='You have registed successfully!'

    context["status"] = status

    return render(request, "app/register.html", context)


def view(request, title):

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM house_info WHERE house_title = %s", [title])
        house = cursor.fetchone()

        result_dict = {'house': house}
        
    ## Rent the house
    if request.POST:
        if request.POST['action'] == 'rent':
            with connection.cursor() as cursor:
                cursor.execute("UPDATE house_info SET house_status = 'RENTED' WHERE house_title = %s",[request.POST['title']])
                # Update the record in rent_history

    return render(request,'app/view.html',result_dict)

def login(request):
    context={}
    status = ''

    if request.POST:
        user_name = request.POST['user_name']
        pw = request.POST['password']
        user = authenticate(request, username=user_name, password=pw)

        if user is not None:
            status='You have log in successfully!'
            context["status"] = status
        
        else:
            status='Emmm... Seems username/password is wrong! Please check again!'
            context["status"] = status
    
    return render(request, "app/login.html", context)
