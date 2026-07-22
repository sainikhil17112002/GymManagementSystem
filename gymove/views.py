import os

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import MemberForm
from gymove.models import UserProfile


def add_member(request):
    if request.method == "POST":
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("add_member")
    else:
        form = MemberForm()

    return render(request, "add_member.html", {"form": form})


def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("gymove:index")

    return render(
        request,
        "gymove/pages/page-login.html"
    )


@login_required
def remove_profile_photo(request):

    if request.method == "POST":

        profile, created = UserProfile.objects.get_or_create(
            user=request.user
        )

        if (
            profile.profile_image
            and profile.profile_image.name != "profile_pics/default.png"
        ):
            if os.path.exists(profile.profile_image.path):
                os.remove(profile.profile_image.path)

        profile.profile_image = "profile_pics/default.png"
        profile.save()

        return JsonResponse({
            "success": True
        })

    return JsonResponse({
        "success": False
    })