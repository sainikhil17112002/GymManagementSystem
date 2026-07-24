from .models import UserProfile
from .storage import Storage
from datetime import datetime


def user_context(request):

    if "user" not in request.session:
        return {}

    user = request.session["user"]

    profile, created = UserProfile.objects.get_or_create(
        username=user["username"]
    )

    # Read members
    members = Storage.read("members.json")

    notifications = []

    # -------------------------------
    # New Members
    # -------------------------------
    for member in sorted(
        members,
        key=lambda x: x.get("join_date", ""),
        reverse=True
    )[:10]:

        notifications.append({
            "title": "New Member Joined",
            "message": f"{member['full_name']} joined the gym.",
            "icon": "fa-user-plus",
            "color": "success",
            "badge": "Member",
            "time": member.get("join_date", ""),
            "url": "#",
        })

    # -------------------------------
    # Membership Expiring
    # -------------------------------
    today = datetime.today().date()

    for member in members:

        expiry = member.get("membership_expiry_date")

        if expiry:
            try:
                expiry_date = datetime.strptime(
                    expiry,
                    "%Y-%m-%d"
                ).date()

                days_left = (expiry_date - today).days

                if 0 <= days_left <= 7:

                    notifications.append({
                        "title": "Membership Expiring",
                        "message": f"{member['full_name']}'s membership expires in {days_left} day(s).",
                        "icon": "fa-clock",
                        "color": "warning",
                        "badge": "Membership",
                        "time": expiry,
                        "url": "#",
                    })

            except ValueError:
                pass

    # Sort latest first
    notifications = sorted(
        notifications,
        key=lambda x: x["time"],
        reverse=True
    )

    return {
        "user": user,
        "profile": profile,
        "notifications": notifications,
        "notification_count": len(notifications),
    }