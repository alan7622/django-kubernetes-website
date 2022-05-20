from django.urls import path


from . import views  # from local directory import views


app_name = "public"  # set the route to public:index, public:about
urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
]
