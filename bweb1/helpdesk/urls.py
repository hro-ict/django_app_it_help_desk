from django.urls import path
from . import views

urlpatterns = [
    path("", views.home ),
    path("login_user", views.login_user),
    path("login_admin", views.login_admin, name="login_admin"),
    path("register", views.register),
    path("mfa", views.otp),
    path("logout", views.logout),
    path("dashboard", views.dashboard),
    # path("tickets", views.tickets ),
    path("dashboard/all_tickets", views.all_tickets, name="all_tickets"),
    path("dashboard/open_tickets", views.open_tickets, name="open_tickets" ),
    path("dashboard/open_tickets/<area>/<search>", views.open_tickets, name="search_open_tickets" ),
    path("dashboard/closed_tickets", views.closed_tickets, name="closed_tickets" ),
    path("dashboard/closed_tickets/<area>/<search>", views.closed_tickets, name="search_closed_tickets" ),
    path("dashboard/grafiek", views.trends, name="grafiek"),
    path("dashboard/user_tickets", views.user_tickets, name="user_tickets"),
    path("dashboard/new_ticket", views.new_ticket, name="new_ticket"),
    path("dashboard/users", views.users, name="users"),
    path("add_solution", views.add_solution, name="add_solution"),
    path("dashboard/all_tickets/<area>/<search>", views.all_tickets, name="search_all_tickets"),
    path("dashboard/user_tickets/delete", views.delete_ticket),
    path("dashboard/users/delete", views.delete_user),
    path("dashboard/users/update", views.update_user),
    path("database", views.database )

]
