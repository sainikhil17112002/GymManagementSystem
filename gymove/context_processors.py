from .models import UserProfile


def user_context(request):

    if "user" not in request.session:
        return {}

    user = request.session["user"]

    profile, created = UserProfile.objects.get_or_create(
        username=user["username"]
    )

    return {
        "user": user,
        "profile": profile,
    }