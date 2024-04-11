from django.shortcuts import render, redirect


# Create your views here.
def index(request, path=""):
    return render(request, template_name="index.html", )


# def draw_menu(request, path):
#     splitted_path = path.split('/')
#     return redirect("/" + splitted_path[-1] + "/")
