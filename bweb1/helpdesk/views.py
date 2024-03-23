from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from .models import Tickets, Users
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.core.serializers import serialize
import json
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.utils import timezone
from django.views.decorators.http import require_POST
import re
import pyotp
from django.db.models import Q
from bs4 import BeautifulSoup
import qrcode
import pandas as pd
from django.template.loader import get_template
from django.shortcuts import redirect, get_object_or_404







# counter=0

def database(request):
    # users= Tickets.objects.all().values()
    # for x in users:
    #     print(x["email"])
    for user_data  in database_data:
        user= Users.objects.get(id= user_data["user"])
        ticket = Tickets.objects.create(date=user_data["date"], description= user_data["description"], user= user, solution= user_data["solution"] )
        ticket.save()
        return database_data




def users(request):
    if "search_term" in request.GET:
        search_term= request.GET["search_term"]
        users = Users.objects.filter(
            Q(name__icontains=search_term) |
            Q(email__icontains=search_term)
        )
    else:
        users= Users.objects.all()
    return render(request, "users.html", {"data": users, "search_term":search_term})

def check_password_requirements(password):
    # Reguliere expressie om te controleren op minstens één hoofdletter, één kleine letter en één cijfer
    patroon = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).+$'
    if re.match(patroon, password):
        return True
    else:
        return False


def check_session(request, role=None):
    if "name" in request.session:
        if request.session["role"]==role:
            return True
    else:
        return False




def grafiek(request):
    if request.method=="POST":
        data= []
        counts=[]
        tickets= Tickets.objects.values_list("date", flat=True)
        unieke_list = []
        [unieke_list.append(item) for item in tickets  if item not in unieke_list]
        
        for date in unieke_list[:3]:
            count= Tickets.objects.filter(date=date).count()
            data.append({"x":count, "y": date})


    # data= {
    #     "days": unieke_list[:3],
    #     "counts": counts
    # }
    # print(data)
    # return render(request, "grafiek.html", {"data": data})
        data ={"data": data}
        return JsonResponse(data)



#admin url
def all_tickets(request, area=None, search=None):
    if request.method=="POST":
        queryset = Tickets.objects.all()
        df = pd.DataFrame(list(queryset.values()))
        df['is_open'] = df['is_open'].apply(lambda x: 'open' if x else 'closed')
        excel_file = 'data.xlsx'
        df.to_excel(excel_file, index=False)

        # Excel dosyasını HttpResponse ile kullanıcıya sunun
        with open(excel_file, 'rb') as file:
            response = HttpResponse(file.read(),
                                    content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=' + excel_file
            return response

    if check_session(request,"admin"):
        # tics= Tickets.objects.all()
        # us= Users.objects.all()
        # a= us.all()
        # for x in a:
        #     print(x.email)
        # if search != None and area !=None:
                # if area=="Description":
                #                 tickets= Tickets.objects.filter(description__icontains=search)
                # if area== "user_email":
                #     tickets= Tickets.objects.filter(user__email__icontains=search)
                # if area== "solution":
                #     tickets= Tickets.objects.filter(solution__icontains=search)
        # else:
        #     tickets= Tickets.objects.order_by("-date")
        # for x in tickets:
        #     print(x.user)
        if "search_term" in request.GET and "search_area" in request.GET:
                search= request.GET["search_term"]
                area= request.GET["search_area"]
                if area=="All":
                    tickets = Tickets.objects.filter(
                        Q(description__icontains=search) |
                        Q(solution__icontains=search) |
                        Q(user__email__icontains= search)
                    )
                if area=="Description":
                    tickets= Tickets.objects.filter(description__icontains=search)
                if area== "user_email":
                    tickets= Tickets.objects.filter(user__email__icontains=search)
                if area== "solution":
                    tickets= Tickets.objects.filter(solution__icontains=search)
        else:
                tickets= Tickets.objects.order_by("-date")    
                  
                
        return render(request, "tickets.html", {"data": tickets, "count": tickets.count(), "search_term": search, "title": "Alle Meldingen"})
    else:
        return redirect("/")
    # tickets= list(tickets.values())
    # return JsonResponse(tickets, safe=False)

#admin url
def open_tickets(request, area=None, search=None):
    if request.method=="POST":
        queryset = Tickets.objects.filter(is_open=True)

        # Filtrelenmiş veriyi pandas DataFrame'e dönüştürün
        df = pd.DataFrame(list(queryset.values()))

        # is_open sütununu open/closed olarak değiştir
        df['is_open'] = df['is_open'].apply(lambda x: 'open' if x else 'closed')

        # DataFrame'i Excel dosyasına dönüştürün
        excel_file = 'data.xlsx'
        df.to_excel(excel_file, index=False)

        # Excel dosyasını HttpResponse ile kullanıcıya sunun
        with open(excel_file, 'rb') as file:
            response = HttpResponse(file.read(),
                                    content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=' + excel_file
            return response
    if check_session(request, "admin"):
        if "search_term" in request.GET and "search_area" in request.GET:
                search= request.GET["search_term"].strip()
                area= request.GET["search_area"]
                if area=="All":
                    tickets = Tickets.objects.filter(
                        Q(description__icontains=search) |
                        Q(solution__icontains=search) |
                        Q(user__email__icontains= search), is_open=True
                    )
                if area=="Description":
                    tickets= Tickets.objects.filter(description__icontains=search, is_open=True)
                if area== "user_email":
                    tickets= Tickets.objects.filter(user__email__icontains=search, is_open=True)
                if area== "solution":
                    tickets= Tickets.objects.filter(solution__icontains=search, is_open=True)
        else:
                tickets= Tickets.objects.filter(is_open=True) 
        return render(request, "tickets.html", {"data": tickets, "search_term": search, "title": "Openstaande Meldingen", "count": tickets.count()})
    else:
        return redirect("/")

#admin url
def closed_tickets(request, area=None, search=None):
    if request.method=="POST":
        queryset = Tickets.objects.filter(is_open=True)
        df = pd.DataFrame(list(queryset.values()))
        df['is_open'] = df['is_open'].apply(lambda x: 'open' if x else 'closed')
        excel_file = 'data.xlsx'
        df.to_excel(excel_file, index=False)

        # Excel dosyasını HttpResponse ile kullanıcıya sunun
        with open(excel_file, 'rb') as file:
            response = HttpResponse(file.read(),
                                    content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=' + excel_file
            return response
    if check_session(request, "admin"):
        if "search_term" in request.GET and "search_area" in request.GET:
                search= request.GET["search_term"].strip()
                area= request.GET["search_area"]
                if area=="All":
                    tickets = Tickets.objects.filter(
                        Q(description__icontains=search) |
                        Q(solution__icontains=search) |
                        Q(user__email__icontains= search), is_open=False
                    )

                if area=="Description":
                    tickets= Tickets.objects.filter(description__icontains=search, is_open=False)
                if area== "user_email":
                    tickets= Tickets.objects.filter(user__email__icontains=search, is_open=False)
                if area== "solution":
                    tickets= Tickets.objects.filter(solution__icontains=search, is_open=False)
        else:
                tickets= Tickets.objects.filter(is_open=False) 
        # tickets= Tickets.objects.filter(is_open=False)

        return render(request, "tickets.html", {"data": tickets, "search_term": search, "title": "Afgesloten Meldingen", "count": tickets.count()})
    else:
        return redirect("/")
            

#user url
def new_ticket(request):

    if request.method=="POST":
            print(request.POST)
            email= request.POST["email"]
            problem= request.POST["problem"]
            #current_time= datetime.now()
            current_time= timezone.now()
            #current_time= current_time.strftime("%d-%m-%Y")
           # date= current_time
            current_user_email= request.session["user_email"]
            print(current_user_email)
            user= Users.objects.get(email=current_user_email)
            two_days_before= current_time - timedelta(days=0)
            print(two_days_before)
            ticket= Tickets(user= user, description= problem, date= two_days_before)
            ticket.save()
            return render(request, "new_ticket.html", {"response": "Nieuwe melding  succesvol aangemaakt" })
    else:
        if check_session(request, "user"):
            return render(request, "new_ticket.html")
        else:
            return redirect("/")

def user_tickets(request):
    # if request.method=="POST":
        search_term= ""
        if "name" in request.session:
            if request.session["role"]=="user":
                if "id" in request.GET:
                    print(request.GET["id"])
                    item = get_object_or_404(Tickets, id= int(request.GET["id"]))
                    print(item)
                    item.delete()
                    user_email= request.session["user_email"]
                    user_object= Users.objects.get(email=user_email)
                    tickets= Tickets.objects.filter(user=user_object).values()
                    return render(request, "user_tickets.html", {"data": tickets})
                user_email= request.session["user_email"]
                user_object= Users.objects.get(email=user_email)
                tickets= Tickets.objects.filter(user=user_object).values()
                for x in tickets:
                    print(x["description"])
                if "search_term" in request.GET:
                    search_term= request.GET["search_term"]
                    tickets = Tickets.objects.filter(
                        Q(description__icontains=search_term) |
                        Q(solution__icontains=search_term) |
                        Q(user__email__icontains= search_term), user=user_object
                    )
               
                return render(request, "user_tickets.html", {"data": tickets, "search_term": search_term})
        else:
            return redirect("/")


#admin url
def trends(request):
    #end_date = datetime.now().date()
    if check_session(request, "admin"):
        print(request.GET)
        if "days" in request.GET:
            days= request.GET["days"]
        else:
            days= 7
        if "chart_type" in request.GET:
            chart_type= request.GET["chart_type"]
        else:
            chart_type="column"

        end_date= datum_string = "2024-03-25"
        end_date= datetime.strptime(end_date, "%Y-%m-%d")
        print(end_date)

        start_date = end_date - timedelta(days= int(days))
        print(start_date)
        events_last_week = Tickets.objects.filter(date__range=[start_date, end_date])
        event_count_per_day = {}
        data= []

        for event in events_last_week:
            event_date = event.date.strftime("%d-%m-%Y")
            if event_date in event_count_per_day:
                event_count_per_day[event_date] += 1
            else:
                event_count_per_day[event_date] = 1
        for x in event_count_per_day:
            data.append({
                "label": x,
                "y": event_count_per_day[x]
            })
        open_tickets= Tickets.objects.filter(is_open=True).count()
        closed_tickets= Tickets.objects.filter(is_open=False).count()
        ticket_state= [
            {"label": "Openstaande meldingen", "y": open_tickets},
            {"label": "Gesloten meldingen", "y": closed_tickets},
        ]

        return render(request, 'grafiek.html', { "datapoints" : data, "ticket_state": ticket_state, "days": days, "chart_type": chart_type })
    else:
        return redirect("/")
        #return JsonResponse(event_count_per_day)
        #return render(request, 'event_list.html', {'event_count_per_day': event_count_per_day})

#test



def home(request):
    if "name" in request.session:
        print("session bestaat")
        return redirect("/dashboard")
    else: 
        return render(request, "home.html")
def login_admin(request):
    if request.method=="POST":
        email=request.POST["email"]
        password= request.POST["password"]
        otp_token= request.POST["otp"]
        try:
            user= Users.objects.get(email=email, role="admin")
        except Users.DoesNotExist:
            return render(request, 'login_admin.html', {'error': 'Ongeldig e-mailadres of wachtwoord.'})

        check= check_password(password, user.password)
        if check:
            secret= user.secret
            totp= pyotp.TOTP(secret)
            result= totp.verify(otp_token)
            print(result)
            if result:
                request.session['name'] = user.name
                request.session['role'] = "admin"
                return redirect("/dashboard")
            else:
                return render(request, 'login_admin.html', {'error': 'Ongeldig OTP Token'})                
            #return render(request, "dashboard.html")
        else:
            return render(request, 'login_admin.html', {'error': 'Ongeldig e-mailadres of wachtwoord.'})
    return render(request, "login_admin.html")


def dashboard(request):
    if  "name" in request.session:       
        return render(request, "dashboard.html")
    else: 
        return redirect("/")


def login_user(request):
    if request.method=="POST":
        email=request.POST["email"]
        password= request.POST["password"]
        try:
            user= Users.objects.get(email=email)
        
        except Users.DoesNotExist:
            return render(request, 'login_user.html', {'error': 'Ongeldig e-mailadres of wachtwoord.'})
      
        if user.is_active == False:
            return render(request, 'login_user.html', {'error': 'User is inactive'})
                
        check= check_password(password, user.password)
        if check:
            request.session['name'] = user.name
            request.session["role"]= "user"
            request.session["user_email"]= user.email
            return redirect("/dashboard")
            #return render(request, "dashboard.html")
        else:
            return render(request, 'login_user.html', {'error': 'Ongeldig e-mailadres of wachtwoord.'})
            
                
    return render(request, "login_user.html")

#open url
def register(request):
    error_data=[]
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        password= request.POST["password"]
        re_password= request.POST["re_password"] 
        role= "user"
        check_email= Users.objects.filter(email=email)
        if check_email.exists():
            error_data.append("E-mailadres is al in gebruik")
        if len(name) < 2 or len(name)>50:
            error_data.append("Naam moet minimaal 2 maximaal 50 karakters zijn")
        if len(email) < 2 or len(email)>50:
            error_data.append("Email moet minimaal 2 maximaal 50 karakters zijn")
        if len(password) < 8 or len(password)>10:
            error_data.append("Wachtwoord moet minimaal 8 maximaal 10 karakters zijn")
        if not check_password_requirements(password):
            error_data.append("Wachtwoord moet tenminste 1 hoofdletter, 1 kleine letter, 1 getal bevatten")
        if password != re_password:
            error_data.append("Wachtwoorden komen niet overeen")
        if len(error_data)==0:
            save_user= Users(name=name,email=email, role=role, password= make_password(password))
            save_user.save()
            return redirect("/login_user")
        else:
            return render(request, "register.html", {"error": error_data})

    else:
        return render(request, "register.html")


#admin url
@require_POST
def add_solution(request):
    if check_session(request, "admin"):
        try:
            id= request.POST["ticketnumber"]
            solution= request.POST["solution"]
            tickets= Tickets.objects.get(id=id)
            print(tickets)
            tickets.solution= solution
            tickets.is_open= False
            tickets.save()

            return JsonResponse({"state": "success", "response": "The solution successfully added"})
        except:
            return JsonResponse({"state": "error", "response": "Something went wrong"})
    else:
        return redirect("/")


#user url
@require_POST
def delete_ticket(request):
    if check_session(request,"user"):
        item = get_object_or_404(Tickets, id= int(request.POST["id"]))
        print(item)
        item.delete()
        return JsonResponse({"response": "success"})
    else:
        return redirect("/")
        
@require_POST
def delete_user(request):
    if check_session(request,"admin"):
        item = get_object_or_404(Users, id= int(request.POST["id"]))
        print(item)
        item.delete()
        response= "User {} verwijderd".format(item)
        return JsonResponse({"response": response})
    else:
        return redirect("/")

#admin url
@require_POST
def update_user(request):
    if check_session(request, "admin"):
        id= request.POST["id"]
        state= request.POST["state"]
        user= Users.objects.get(id=id)
        if state=="false":
            user.is_active= False
        else:
            user.is_active= True
        user.save()
        return JsonResponse({"response": "success"})
    else:
        return redirect("/")



def otp(request):
    if request.method == "GET":
            return render(request, "home.html")
    token= request.POST["mfa"]
    data= request.POST
    print("TOKEN ", token)
    key= "O7RQOOY2P6FCUXC3F2JH7HSUWGTWS53Z"
    totp= pyotp.TOTP(key)
    result= totp.verify(token)
    if result:
        return render(request, "home.html", {"name": "yasar abi"})
    else:
        response_data = {'message': 'OTP NOT Succesfull', 'data': data}
        return render(request, "login.html", response_data)
                        


def logout(request):
    request.session.flush()
    return redirect("/")
    #return render(request, "home.html")


#admin
def grafiek(request):
    if check_session(request, "admin"):
        data= []
        counts=[]
        tickets= Tickets.objects.values_list("date", flat=True)
        unieke_list = []
        [unieke_list.append(item) for item in tickets  if item not in unieke_list]

        if len(unieke_list)>7:
            unieke_list= unieke_list[:-7]

        
        for date in unieke_list:
            count= Tickets.objects.filter(date=date).count()
            data.append({"y":count, "label": date})
        print(data)
        open_tickets= Tickets.objects.filter(is_open=True).count()
        closed_tickets= Tickets.objects.filter(is_open=False).count()
        ticket_state= [
            {"label": "Openstaande meldingen", "y": open_tickets},
            {"label": "Gesloten meldingen", "y": closed_tickets},
        ]
        return render(request, 'grafiek.html', { "datapoints" : data, "ticket_state": ticket_state  }) 
    else:
        return redirect("/")


