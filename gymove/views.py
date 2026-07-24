import os

from django.shortcuts import render, redirect
from django.http import JsonResponse

from .forms import MemberForm
from gymove.models import UserProfile
from .storage import Storage


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

        users = Storage.read("user.json")

        for user in users:
            if (
                user["username"] == username
                and user["password"] == password
            ):
                request.session["user"] = user
                return redirect("gymove:index")

    return render(
        request,
        "gymove/pages/page-login.html"
    )


def remove_profile_photo(request):

    if request.method == "POST":

        if "user" not in request.session:
            return JsonResponse({"success": False})

        username = request.session["user"]["username"]

        profile, created = UserProfile.objects.get_or_create(
            username=username
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


from datetime import datetime, timedelta

def notifications(request):
    members = Storage.read("members.json")

    # Latest joined members
    new_members = sorted(
        members,
        key=lambda x: x.get("join_date", ""),
        reverse=True
    )

    # Members expiring within 7 days
    today = datetime.today().date()
    expiring_members = []

    for member in members:
        expiry = member.get("membership_expiry_date")

        if expiry:
            try:
                expiry_date = datetime.strptime(
                    expiry,
                    "%Y-%m-%d"
                ).date()

                days = (expiry_date - today).days

                if 0 <= days <= 7:
                    member["days_left"] = days
                    expiring_members.append(member)

            except ValueError:
                pass

    context = {
        "page_title": "Notifications",
        "new_members": new_members,
        "expiring_members": expiring_members,
    }

    return render(
        request,
        "gymove/notifications.html",
        context,
    )


def notifications(request):
    members = Storage.read("members.json")

    new_members = sorted(
        members,
        key=lambda x: x.get("join_date", ""),
        reverse=True
    )

    expiring_members = []

    context = {
        "page_title": "Notifications",
        "new_members": new_members,
        "expiring_members": expiring_members,
    }

    return render(
        request,
        "gymove/pages/notifications.html",
        context,
    )