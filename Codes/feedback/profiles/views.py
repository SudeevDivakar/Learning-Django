from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .forms import ProfileForm
from .models import UserProfile

# Create your views here.

'''Class View to save image using the CreateView'''
class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    success_url = "/profiles"
    fields = "__all__"


'''Function to store the image in a directory'''
# def store_file(file):
#     with open("temp/image.jpg", "wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)


'''Class View to save image using a Model'''
# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {
#             "form": form
#         })

#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)

#         if submitted_form.is_valid():
#             profile = UserProfile(image=request.FILES["image"])
#             profile.save()
#             return HttpResponseRedirect("/profiles")
        
#         return render(request, "profiles/create_profile.html", {
#             "form": submitted_form
#         })
    

'''Class View to Store an Image using a Form Class + Above Defined Function'''
# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {
#             "form": form
#         })

#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)

#         if submitted_form.is_valid():
#             store_file(request.FILES["image"])                  #This will print out the file name(but request.FILES["image"] is not just a file name, it's an object containing full data about the file)
#             return HttpResponseRedirect("/profiles")
        
#         return render(request, "profiles/create_profile.html", {
#             "form": submitted_form
#         })


class ProfilesView(ListView):
    model = UserProfile
    template_name = "profiles/user_profiles.html"
    context_object_name = "profiles"