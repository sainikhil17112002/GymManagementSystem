from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages

from .forms import (
    MemberForm,
    TrainerForm,
    MembershipPlanForm,
    LockPasswordForm,
)

from .models import (
    UserProfile,
    Announcement,
)

from .storage import Storage


# ==========================================================
# HELPERS
# ==========================================================

def load_members():
    return Storage.read("members.json")


def save_members(data):
    Storage.write("members.json", data)


def load_trainers():
    return Storage.read("trainers.json")


def save_trainers(data):
    Storage.write("trainers.json", data)


def load_plans():
    return Storage.read("membership_plans.json")


def save_plans(data):
    Storage.write("membership_plans.json", data)


def load_users():
    return Storage.read("user.json")


def save_users(data):
    Storage.write("user.json", data)


def today():
    return date.today()

def login_required_json(view_func):

    def wrapper(request, *args, **kwargs):

        if "user" not in request.session:
            return redirect("gymove:page-login")

        return view_func(request, *args, **kwargs)

    return wrapper

# ==========================================================
# DASHBOARD
# ==========================================================

@login_required_json
def index(request):

    members = load_members()
    trainers = load_trainers()
    plans = load_plans()
    payments = load_payments()


    total_members = len(members)


    active_members = len([
        m for m in members
        if m.get("status", "").lower() == "active"
    ])


    total_trainers = len(trainers)

    total_plans = len(plans)


        # ==============================
    # REVENUE GROWTH CHART
    # ==============================

    revenue_chart = {
        "months": [],
        "revenue": [],
    }


    monthly_revenue = {}


    for payment in payments:

        if payment.get("status", "").lower() != "paid":
            continue


        date = payment.get("date", "")


        if date:

            month = date[:7]


            if month not in monthly_revenue:
                monthly_revenue[month] = 0


            monthly_revenue[month] += int(
                payment.get("amount", 0)
            )


    for month, amount in sorted(monthly_revenue.items()):

        revenue_chart["months"].append(month)

        revenue_chart["revenue"].append(amount)


    # ==============================
    # MONTH REVENUE
    # ==============================

    month_revenue = 0

    current_month = datetime.now().strftime("%Y-%m")


    for payment in payments:

        if payment.get("status", "").lower() != "paid":
            continue


        payment_date = payment.get("date", "")


        if payment_date.startswith(current_month):

            try:
                month_revenue += int(
                    payment.get("amount", 0)
                )

            except:
                pass



    # ==============================
    # TRAINERS
    # ==============================

    recommended_trainers = [
        t for t in trainers
        if t.get("status", "").lower() == "active"
    ][:4]



    # ==============================
    # EXPIRING MEMBERS
    # ==============================

    today_date = today()

    next_7_days = today_date + timedelta(days=7)


    expiring_members = []

    new_members = sorted(
    members,
    key=lambda x: x.get("join_date", ""),
    reverse=True
)[:5]


    for member in members:

        expiry = member.get("membership_expiry_date")


        if not expiry:
            continue


        try:

            expiry_date = datetime.strptime(
                expiry,
                "%Y-%m-%d"
            ).date()


            if today_date <= expiry_date <= next_7_days:
                expiring_members.append(member)


        except:
            continue

        print("=" * 50)
        print("Total members:", len(members))
        print("New members:", len(new_members))
        print(new_members)
        print("=" * 50)




    latest_announcements = Announcement.objects.filter(
    is_active=True
).order_by(
    "-is_featured",
    "-created_at"
)

    context = {

        "page_title": "Dashboard",

        "total_members": total_members,

        "active_members": active_members,

        "total_trainers": total_trainers,

        "total_plans": total_plans,

        "month_revenue": month_revenue,

        "revenue_chart": revenue_chart,

        "recommended_trainers": recommended_trainers,

        "expiring_members": expiring_members,

        "new_members": new_members,

        "latest_announcements": latest_announcements,

    }


    return render(
        request,
        "gymove/index.html",
        context,
    )


@login_required_json
def index_2(request):

    context = {
        "page_title": "Dashboard",
    }

    return render(
        request,
        "gymove/index-2.html",
        context,
    )



@login_required_json
def index_2(request):

    context = {
        "page_title": "Dashboard",
    }

    return render(
        request,
        "gymove/index-2.html",
        context,
    )




# ==========================================================
# STATIC PAGES
# ==========================================================

def distance_map(request):
    return render(
        request,
        "gymove/distance-map.html",
        {
            "page_title": "Distance Map",
        },
    )


def food_menu(request):
    return render(
        request,
        "gymove/index.html",
        {
            "page_title": "Food Menu",
        },
    )


def personal_record(request):
    return render(
        request,
        "gymove/personal-record.html",
        {
            "page_title": "Personal Record",
        },
    )


# ==========================================================
# PROFILE
# ==========================================================


@login_required_json
def app_profile(request):

    username = request.session["user"]["username"]

    profile, created = UserProfile.objects.get_or_create(
        username=username
    )

    context = {
        "page_title": "My Account",
        "profile": profile,
        "user": request.session["user"],
    }

    return render(
        request,
        "gymove/apps/app-profile.html",
        context,
    )

    

# ==========================================================
# BLOG / POSTS
# ==========================================================

def post_details(request):
    return render(
        request,
        "gymove/apps/index.html",
        {
            "page_title": "Post Details",
        },
    )


# ==========================================================
# EMAIL
# ==========================================================

def email_compose(request):
    return render(
        request,
        "gymove/apps/email/email-compose.html",
        {
            "page_title": "Compose",
        },
    )


def email_inbox(request):
    return render(
        request,
        "gymove/apps/email/index.html",
        {
            "page_title": "Inbox",
        },
    )


def email_read(request):
    return render(
        request,
        "gymove/apps/email/email-read.html",
        {
            "page_title": "Read",
        },
    )


# ==========================================================
# CALENDAR
# ==========================================================

def app_calender(request):
    return render(
        request,
        "gymove/apps/app-calender.html",
        {
            "page_title": "Calendar",
        },
    )


# ==========================================================
# SHOP
# ==========================================================

def ecom_product_grid(request):
    return render(
        request,
        "gymove/apps/shop/ecom-product-grid.html",
        {
            "page_title": "Product Grid",
        },
    )


def ecom_product_list(request):
    return render(
        request,
        "gymove/apps/shop/ecom-product-list.html",
        {
            "page_title": "Product List",
        },
    )


def ecom_product_detail(request):
    return render(
        request,
        "gymove/apps/shop/ecom-product-detail.html",
        {
            "page_title": "Product Detail",
        },
    )


def ecom_product_order(request):
    return render(
        request,
        "gymove/apps/shop/ecom-product-order.html",
        {
            "page_title": "Product Order",
        },
    )


def ecom_checkout(request):
    return render(
        request,
        "gymove/apps/shop/ecom-checkout.html",
        {
            "page_title": "Checkout",
        },
    )


def ecom_invoice(request):
    return render(
        request,
        "gymove/apps/shop/ecom-invoice.html",
        {
            "page_title": "Invoice",
        },
    )


def ecom_customers(request):
    return render(
        request,
        "gymove/apps/shop/ecom-customers.html",
        {
            "page_title": "Customers",
        },
    )



# ==========================================================
# ICONS
# ==========================================================

def flat_icons(request):
    return render(
        request,
        "gymove/flat-icons.html",
        {
            "page_title": "Flat Icons",
        },
    )


def svg_icons(request):
    return render(
        request,
        "gymove/svg-icons.html",
        {
            "page_title": "SVG Icons",
        },
    )


def feather_icons(request):
    return render(
        request,
        "gymove/feather-icons.html",
        {
            "page_title": "Feather Icons",
        },
    )

# ==========================================================
# CMS
# ==========================================================

def announcement_history(request):

    announcements = Announcement.objects.all().order_by(
        "-created_at"
    )

    return render(
        request,
        "gymove/pages/announcement_history.html",
        {
            "announcements": announcements,
            "page_title": "Announcement History",
        },
    )

def content(request):
    return render(
        request,
        "gymove/cms/content.html",
        {
            "page_title": "Content",
        },
    )

def create_announcement(request):

    if request.method == "POST":

        title = request.POST.get("title")
        description = request.POST.get("description")

        Announcement.objects.create(
            title=title,
            description=description,
            is_active=True,
            is_featured=False,
        )

        return redirect("gymove:index")


    return render(
        request,
        "gymove/pages/create_announcement.html"
    )

def add_content(request):
    return render(
        request,
        "gymove/cms/add-content.html",
        {
            "page_title": "Add Content",
        },
    )


def menu(request):
    return render(
        request,
        "gymove/cms/menu.html",
        {
            "page_title": "Menu",
        },
    )

def email_template(request):
    return render(
        request,
        "gymove/cms/email-template.html",
        {
            "page_title": "Email Template",
        },
    )


def add_email(request):
    return render(
        request,
        "gymove/cms/add-email.html",
        {
            "page_title": "Add Email",
        },
    )


def blog(request):
    return render(
        request,
        "gymove/cms/blog.html",
        {
            "page_title": "Blog",
        },
    )


def add_blog(request):
    return render(
        request,
        "gymove/cms/add-blog.html",
        {
            "page_title": "Add Blog",
        },
    )


def blog_category(request):
    return render(
        request,
        "gymove/cms/blog-category.html",
        {
            "page_title": "Blog Category",
        },
    )


# ==========================================================
# CHARTS
# ==========================================================

def chart_flot(request):
    return render(
        request,
        "gymove/charts/chart-flot.html",
        {
            "page_title": "Chart Flot",
        },
    )


def chart_morris(request):
    return render(
        request,
        "gymove/charts/chart-morris.html",
        {
            "page_title": "Chart Morris",
        },
    )


def chart_chartjs(request):
    return render(
        request,
        "gymove/charts/chart-chartjs.html",
        {
            "page_title": "Chart.js",
        },
    )


def chart_chartist(request):
    return render(
        request,
        "gymove/charts/chart-chartist.html",
        {
            "page_title": "Chartist",
        },
    )


def chart_sparkline(request):
    return render(
        request,
        "gymove/charts/chart-sparkline.html",
        {
            "page_title": "Sparkline",
        },
    )


def chart_peity(request):
    return render(
        request,
        "gymove/charts/chart-peity.html",
        {
            "page_title": "Peity",
        },
    )



# ==========================================================
# BOOTSTRAP UI
# ==========================================================

def ui_accordion(request):
    return render(request, "gymove/bootstrap/ui-accordion.html", {
        "page_title": "Accordion",
    })


def ui_alert(request):
    return render(request, "gymove/bootstrap/ui-alert.html", {
        "page_title": "Alert",
    })


def ui_badge(request):
    return render(request, "gymove/bootstrap/ui-badge.html", {
        "page_title": "Badge",
    })


def ui_button(request):
    return render(request, "gymove/bootstrap/ui-button.html", {
        "page_title": "Button",
    })


def ui_modal(request):
    return render(request, "gymove/bootstrap/ui-modal.html", {
        "page_title": "Modal",
    })


def ui_button_group(request):
    return render(request, "gymove/bootstrap/ui-button-group.html", {
        "page_title": "Button Group",
    })


def ui_list_group(request):
    return render(request, "gymove/bootstrap/ui-list-group.html", {
        "page_title": "List Group",
    })


def ui_media_object(request):
    return render(request, "gymove/bootstrap/ui-media-object.html", {
        "page_title": "Media Object",
    })


def ui_card(request):
    return render(request, "gymove/bootstrap/ui-card.html", {
        "page_title": "Card",
    })


def ui_carousel(request):
    return render(request, "gymove/bootstrap/ui-carousel.html", {
        "page_title": "Carousel",
    })


def ui_dropdown(request):
    return render(request, "gymove/bootstrap/ui-dropdown.html", {
        "page_title": "Dropdown",
    })


def ui_popover(request):
    return render(request, "gymove/bootstrap/ui-popover.html", {
        "page_title": "Popover",
    })


def ui_progressbar(request):
    return render(request, "gymove/bootstrap/ui-progressbar.html", {
        "page_title": "Progressbar",
    })


def ui_tab(request):
    return render(request, "gymove/bootstrap/ui-tab.html", {
        "page_title": "Tab",
    })


def ui_typography(request):
    return render(request, "gymove/bootstrap/ui-typography.html", {
        "page_title": "Typography",
    })


def ui_pagination(request):
    return render(request, "gymove/bootstrap/ui-pagination.html", {
        "page_title": "Pagination",
    })


def ui_grid(request):
    return render(request, "gymove/bootstrap/ui-grid.html", {
        "page_title": "Grid",
    })


# ==========================================================
# PLUGINS
# ==========================================================

def uc_select2(request):
    return render(request, "gymove/plugins/uc-select2.html", {
        "page_title": "Select2",
    })


def uc_nestable(request):
    return render(request, "gymove/plugins/uc-nestable.html", {
        "page_title": "Nestable",
    })


def uc_noui_slider(request):
    return render(request, "gymove/plugins/uc-noui-slider.html", {
        "page_title": "UI Slider",
    })



def uc_sweetalert(request):
    return render(request, "gymove/plugins/uc-sweetalert.html", {
        "page_title": "Sweet Alert",
    })


def uc_toastr(request):
    return render(request, "gymove/plugins/uc-toastr.html", {
        "page_title": "Toastr",
    })


def map_jqvmap(request):
    return render(request, "gymove/plugins/map-jqvmap.html", {
        "page_title": "JQV Map",
    })


def uc_lightgallery(request):
    return render(request, "gymove/plugins/uc-lightgallery.html", {
        "page_title": "Light Gallery",
    })


# ==========================================================
# WIDGETS
# ==========================================================

def widget_basic(request):
    return render(request, "gymove/widget-basic.html", {
        "page_title": "Widget",
    })


# ==========================================================
# FORMS
# ==========================================================

def form_element(request):
    return render(request, "gymove/forms/form-element.html", {
        "page_title": "Form Element",
    })


def form_wizard(request):
    return render(request, "gymove/forms/form-wizard.html", {
        "page_title": "Form Wizard",
    })


def form_editor(request):
    return render(request, "gymove/forms/form-editor.html", {
        "page_title": "CKEditor",
    })


def form_pickers(request):
    return render(request, "gymove/forms/form-pickers.html", {
        "page_title": "Pickers",
    })


def form_validation(request):
    return render(request, "gymove/forms/form-validation.html", {
        "page_title": "Form Validation",
    })


# ==========================================================
# TABLES
# ==========================================================

def table_bootstrap_basic(request):
    return render(request, "gymove/table/table-bootstrap-basic.html", {
        "page_title": "Bootstrap Table",
    })


def table_datatable_basic(request):
    return render(request, "gymove/table/table-datatable-basic.html", {
        "page_title": "DataTable",
    })


# ==========================================================
# AUTHENTICATION
# ==========================================================


def page_register(request):

    if request.method == "POST":

        users = load_users()

        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")

        if any(u.get("username") == username for u in users):
            messages.error(request, "Username already exists.")
            return redirect("gymove:page-register")

        users.append({
            "username": username,
            "email": email,
            "password": password,
            "joined_on": datetime.now().strftime("%d %b %Y"),
            "last_login": "Never",
        })

        save_users(users)

        messages.success(request, "Account created successfully.")
        return redirect("gymove:page-login")

    return render(
        request,
        "gymove/pages/page-register.html",
        {
            "page_title": "Admin Sign Up",
        },
    )

def page_login(request):

    if request.method == "POST":

        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        users = load_users()

        user = next(
            (
                u for u in users
                if u.get("username") == username
                and u.get("password") == password
            ),
            None,
        )

        if user:
            user["last_login"] = datetime.now().strftime("%d %b %Y %I:%M %p")
            save_users(users)

            request.session["user"] = user

            return redirect("gymove:index")

        messages.error(
            request,
            "Invalid username or password."
        )

    return render(
        request,
        "gymove/pages/page-login.html",
        {
            "page_title": "Login",
        },
    )

def page_forgot_password(request):
    return render(
        request,
        "gymove/pages/page-forgot-password.html",
    )


def page_logout(request):
    request.session.flush()
    return redirect("gymove:page-login")

# ==========================================================
# ERROR PAGES
# ==========================================================

def page_error_400(request):
    return render(request, "400.html")


def page_error_403(request):
    return render(request, "403.html")


def page_error_404(request):
    return render(request, "404.html")


def page_error_500(request):
    return render(request, "500.html")


def page_error_503(request):
    return render(request, "503.html")


# ==========================================================
# MEMBERS
# ==========================================================

@login_required_json
def add_member(request):

    plans = load_plans()

    if request.method == "POST":

        members = load_members()

        join_date = request.POST.get("join_date")
        plan_id = request.POST.get("membership_plan")

        expiry_date = ""

        selected_plan = next(
            (
                p for p in plans
                if str(p.get("plan_id")) == str(plan_id)
            ),
            None
        )


        if selected_plan and join_date:

            try:

                duration = int(selected_plan.get("duration", 0))

                expiry = datetime.strptime(
                    join_date,
                    "%Y-%m-%d"
                )

                expiry = expiry + relativedelta(
                    months=duration
                )

                expiry_date = expiry.strftime(
                    "%Y-%m-%d"
                )

            except Exception:

                expiry_date = ""


        member = {

            "member_id": request.POST.get("member_id"),

            "first_name": request.POST.get("first_name"),

            "last_name": request.POST.get("last_name"),

            "full_name":
                request.POST.get("first_name")
                + " "
                + request.POST.get("last_name"),

            "gender": request.POST.get("gender"),

            "date_of_birth":
                request.POST.get("date_of_birth"),

            "phone":
                request.POST.get("phone"),

            "email":
                request.POST.get("email"),

            "address":
                request.POST.get("address"),

            "emergency_contact":
                request.POST.get("emergency_contact"),

            "join_date":
                join_date,

            "membership_plan":
                plan_id,

            "membership_expiry_date":
                expiry_date,

            "status":
                "Active",

            "trainer_id":
                request.POST.get("trainer_id"),

        }


        members.append(member)

        save_members(members)


        payments = load_payments()


        if selected_plan:

            payment = {

                "member_id": member.get("member_id"),

                "member": member.get("full_name"),

                "plan": selected_plan.get("name"),

                "amount": int(
                    selected_plan.get("price", 0)
                ),

                "date": join_date,

                "status": "Paid",

            }


            payments.append(payment)

            save_payments(payments)


        messages.success(
            request,
            "Member added successfully."
        )


        return redirect(
            "gymove:member-list"
        )


    return render(
        request,
        "gymove/pages/add-member.html",
        {
            "plans": plans,
            "trainers": load_trainers(),
            "page_title": "Add Member",
        },
    )


@login_required_json
def member_list(request):

    members = load_members()

    plans = load_plans()

    trainers = load_trainers()


    for member in members:


        # ==========================
        # MEMBERSHIP PLAN NAME
        # ==========================

        plan = next(
            (
                p for p in plans
                if str(p.get("plan_id")) == str(member.get("membership_plan"))
            ),
            None
        )


        if plan:

            member["membership_plan_name"] = plan.get(
                "plan_name"
            )

        else:

            member["membership_plan_name"] = "No Plan"



        # ==========================
        # TRAINER NAME
        # ==========================

        trainer = next(
            (
                t for t in trainers
                if str(t.get("trainer_id")) == str(member.get("trainer_id"))
            ),
            None
        )


        if trainer:

            member["trainer_name"] = trainer.get(
                "full_name"
            )

        else:

            member["trainer_name"] = "Not Assigned"



        # ==========================
        # AUTO STATUS
        # ==========================

        expiry = member.get(
            "membership_expiry_date"
        )


        if expiry:

            try:

                expiry_date = datetime.strptime(
                    expiry,
                    "%Y-%m-%d"
                ).date()


                if expiry_date < today():

                    member["status"] = "Expired"

                else:

                    member["status"] = "Active"


            except:

                member["status"] = "Active"


        else:

            member["status"] = "Active"



    return render(
        request,
        "gymove/pages/member-list.html",
        {
            "members": members,
            "page_title": "Member List",
        },
    )


@login_required_json
def member_profile(request, id):

    members = load_members()
    plans = load_plans()
    trainers = load_trainers()


    member = next(
        (
            m for m in members
            if str(m.get("member_id")) == str(id)
        ),
        None,
    )


    if not member:

        messages.error(
            request,
            "Member not found."
        )

        return redirect(
            "gymove:member-list"
        )



    # Get membership plan name

    plan = next(
        (
            p for p in plans
            if str(p.get("plan_id")) == str(member.get("membership_plan"))
        ),
        None
    )


    if plan:

        member["membership_plan_name"] = plan.get(
            "plan_name"
        )

    else:

        member["membership_plan_name"] = "No Plan"



    # Get trainer name

    trainer = next(
        (
            t for t in trainers
            if str(t.get("trainer_id")) == str(member.get("trainer_id"))
        ),
        None
    )


    if trainer:

        member["trainer_name"] = trainer.get(
            "full_name"
        )

    else:

        member["trainer_name"] = "Not Assigned"



    # Auto status

    expiry = member.get(
        "membership_expiry_date"
    )


    if expiry:

        try:

            expiry_date = datetime.strptime(
                expiry,
                "%Y-%m-%d"
            ).date()


            if expiry_date < today():

                member["status"] = "Expired"

            else:

                member["status"] = "Active"


        except:

            member["status"] = "Active"



    return render(
        request,
        "gymove/pages/member-profile.html",
        {
            "member": member,
            "page_title": "Member Profile",
        },
    )

@login_required_json
def edit_member(request, id):

    members = load_members()

    member = next(
        (
            m for m in members
            if str(m.get("member_id")) == str(id)
        ),
        None
    )

    if not member:
        messages.error(request, "Member not found.")
        return redirect("gymove:member-list")

    plans = load_plans()
    trainers = load_trainers()

    if request.method == "POST":

        join_date = request.POST.get("join_date")
        plan_id = request.POST.get("membership_plan")

        expiry_date = ""

        selected_plan = next(
            (
                p for p in plans
                if str(p.get("plan_id")) == str(plan_id)
            ),
            None
        )

        if selected_plan and join_date:
            try:
                duration = int(selected_plan.get("duration", 0))
                expiry = datetime.strptime(join_date, "%Y-%m-%d")
                expiry = expiry + relativedelta(months=duration)
                expiry_date = expiry.strftime("%Y-%m-%d")
            except:
                expiry_date = ""

        member.update({

            "first_name": request.POST.get("first_name"),
            "last_name": request.POST.get("last_name"),
            "full_name": request.POST.get("full_name"),
            "gender": request.POST.get("gender"),
            "date_of_birth": request.POST.get("date_of_birth"),
            "phone": request.POST.get("phone"),
            "email": request.POST.get("email"),
            "address": request.POST.get("address"),
            "emergency_contact": request.POST.get("emergency_contact"),
            "join_date": join_date,
            "trainer_id": request.POST.get("trainer"),
            "membership_plan": plan_id,
            "membership_expiry_date": expiry_date,
            "status": "Active",

        })

        save_members(members)

        messages.success(
            request,
            "Member updated successfully."
        )

        return redirect("gymove:member-list")

    return render(
        request,
        "gymove/pages/edit-member.html",
        {
            "member": member,
            "plans": plans,
            "trainers": trainers,
            "page_title": "Edit Member",
        },
    )


@login_required_json
def delete_member(request, id):

    members = load_members()


    members = [
        m for m in members
        if str(m.get("member_id")) != str(id)
    ]


    save_members(
        members
    )


    messages.success(
        request,
        "Member deleted successfully."
    )


    return redirect(
        "gymove:member-list"
    )

    # ==============================
    # REVENUE GROWTH CHART  ✅ PASTE HERE
    # ==============================

    revenue_chart = {
        "months": [],
        "revenue": [],
    }

    monthly_revenue = {}


    for payment in payments:

        if payment.get("status", "").lower() != "paid":
            continue


        date = payment.get("date", "")


        if date:

            month = date[:7]


            if month not in monthly_revenue:
                monthly_revenue[month] = 0


            monthly_revenue[month] += int(
                payment.get("amount", 0)
            )


    for month, amount in sorted(monthly_revenue.items()):

        revenue_chart["months"].append(month)
        revenue_chart["revenue"].append(amount)


# ==========================================================
# TRAINERS
# ==========================================================
@login_required_json
def add_trainer(request):

    if request.method == "POST":

        trainers = load_trainers()


        trainer = {

            "trainer_id":
                request.POST.get("trainer_id"),


            "full_name":
                request.POST.get("full_name"),


            "gender":
                request.POST.get("gender"),


            "phone":
                request.POST.get("phone"),


            "email":
                request.POST.get("email"),


            "specialization":
                request.POST.get("specialization"),


            "experience":
                request.POST.get("experience"),


            "salary":
                request.POST.get("salary"),


            "joining_date":
                request.POST.get("joining_date"),


            "status":
                request.POST.get(
                    "status",
                    "Active"
                ),

        }



        # Check duplicate trainer ID

        if any(
            str(t.get("trainer_id")) == str(trainer["trainer_id"])
            for t in trainers
        ):

            messages.error(
                request,
                "Trainer ID already exists."
            )

            return redirect(
                "gymove:add-trainer"
            )



        trainers.append(trainer)


        save_trainers(
            trainers
        )



        messages.success(
            request,
            "Trainer added successfully."
        )


        return redirect(
            "gymove:trainer-list"
        )



    return render(
        request,
        "gymove/pages/add-trainer.html",
        {
            "page_title": "Add Trainer",
        },
    )

@login_required_json
def trainer_list(request):

    trainers = sorted(
        load_trainers(),
        key=lambda x: str(x.get("trainer_id"))
    )

    return render(
        request,
        "gymove/pages/trainer-list.html",
        {
            "trainers": trainers,
            "page_title": "Trainer List",
        },
    )


@login_required_json
def trainer_profile(request, id):

    trainers = load_trainers()
    members = load_members()


    trainer = next(
        (
            t for t in trainers
            if str(t.get("trainer_id")) == str(id)
        ),
        None
    )


    if not trainer:

        messages.error(
            request,
            "Trainer not found."
        )

        return redirect(
            "gymove:trainer-list"
        )


    assigned_members = [
        m for m in members
        if str(m.get("trainer_id")) == str(id)
    ]


    return render(
        request,
        "gymove/pages/trainer-profile.html",
        {
            "trainer": trainer,
            "members": assigned_members,
            "page_title": "Trainer Profile",
        },
    )

@login_required_json
def edit_trainer(request, id):

    trainers = load_trainers()


    trainer = next(
        (
            t for t in trainers
            if str(t.get("trainer_id")) == str(id)
        ),
        None
    )


    if not trainer:

        messages.error(
            request,
            "Trainer not found."
        )

        return redirect(
            "gymove:trainer-list"
        )



    if request.method == "POST":


        trainer.update({

            "full_name":
                request.POST.get(
                    "full_name"
                ),


            "gender":
                request.POST.get(
                    "gender"
                ),


            "phone":
                request.POST.get(
                    "phone"
                ),


            "email":
                request.POST.get(
                    "email"
                ),


            "specialization":
                request.POST.get(
                    "specialization"
                ),


            "experience":
                request.POST.get(
                    "experience"
                ),


            "salary":
                request.POST.get(
                    "salary"
                ),


            "joining_date":
                request.POST.get(
                    "joining_date"
                ),


            "status":
                request.POST.get(
                    "status"
                ),

        })



        save_trainers(
            trainers
        )


        messages.success(
            request,
            "Trainer updated successfully."
        )


        return redirect(
            "gymove:trainer-list"
        )



    return render(
        request,
        "gymove/pages/edit-trainer.html",
        {
            "trainer": trainer,
            "page_title": "Edit Trainer",
        },
    )


@login_required_json
def assign_member(request, id):

    trainers = load_trainers()
    members = load_members()


    trainer = next(
        (
            t for t in trainers
            if str(t.get("trainer_id")) == str(id)
        ),
        None
    )


    if not trainer:

        messages.error(
            request,
            "Trainer not found."
        )

        return redirect(
            "gymove:trainer-list"
        )



    available_members = [
        m for m in members
        if not m.get("trainer_id")
    ]



    if request.method == "POST":

        member_id = request.POST.get(
            "member"
        )


        member = next(
            (
                m for m in members
                if str(m.get("member_id")) == str(member_id)
            ),
            None
        )


        if member:

            member["trainer_id"] = str(id)

            save_members(
                members
            )

            messages.success(
                request,
                "Member assigned successfully."
            )


        return redirect(
            "gymove:trainer-profile",
            id=id
        )



    return render(
        request,
        "gymove/pages/assign-member.html",
        {
            "trainer": trainer,
            "members": available_members,
            "page_title": "Assign Member",
        },
    )

@login_required_json
def remove_member_trainer(request, id):

    members = load_members()


    member = next(
        (
            m for m in members
            if str(m.get("member_id")) == str(id)
        ),
        None
    )


    if not member:

        messages.error(
            request,
            "Member not found."
        )

        return redirect(
            "gymove:member-list"
        )



    trainer_id = member.get(
        "trainer_id"
    )


    member["trainer_id"] = ""



    save_members(
        members
    )


    messages.success(
        request,
        "Member removed from trainer."
    )


    return redirect(
        "gymove:trainer-profile",
        id=trainer_id
    )



# DELETE TRAINER

@login_required_json
def delete_trainer(request, id):

    trainers = load_trainers()


    trainers = [
        t for t in trainers
        if str(t.get("trainer_id")) != str(id)
    ]


    save_trainers(
        trainers
    )


    members = load_members()


    for member in members:

        if str(member.get("trainer_id")) == str(id):

            member["trainer_id"] = ""



    save_members(
        members
    )


    messages.success(
        request,
        "Trainer deleted successfully."
    )


    return redirect(
        "gymove:trainer-list"
    )

# ==========================================================
# MEMBERSHIP PLANS
# ==========================================================

@login_required_json
def add_membership_plan(request):

    if request.method == "POST":

        plans = load_plans()


        plan = {

            "plan_id":
                request.POST.get("plan_id"),


            "plan_name":
                request.POST.get("plan_name"),


            "duration":
                request.POST.get("duration"),


            "price":
                request.POST.get("price"),


            "description":
                request.POST.get("description"),

        }



        if any(
            str(p.get("plan_id")) == str(plan["plan_id"])
            for p in plans
        ):

            messages.error(
                request,
                "Plan ID already exists."
            )

            return redirect(
                "gymove:add-membership-plan"
            )



        plans.append(plan)

        save_plans(plans)



        messages.success(
            request,
            "Membership plan added successfully."
        )


        return redirect(
            "gymove:membership-plan-list"
        )



    return render(
        request,
        "gymove/pages/add-membership-plan.html",
        {
            "page_title": "Add Membership Plan",
        },
    )


@login_required_json
def membership_plan_list(request):

    plans = sorted(
        load_plans(),
        key=lambda x: str(x.get("plan_id"))
    )

    return render(
        request,
        "gymove/pages/membership-plan-list.html",
        {
            "plans": plans,
            "page_title": "Membership Plans",
        },
    )


@login_required_json
def edit_membership_plan(request, id):

    plans = load_plans()


    plan = next(
        (
            p for p in plans
            if str(p.get("plan_id")) == str(id)
        ),
        None
    )


    if not plan:

        messages.error(
            request,
            "Membership plan not found."
        )

        return redirect(
            "gymove:membership-plan-list"
        )



    if request.method == "POST":

        plan.update({

            "plan_name":
                request.POST.get("plan_name"),


            "duration":
                request.POST.get("duration"),


            "price":
                request.POST.get("price"),


            "description":
                request.POST.get("description"),

        })


        save_plans(plans)



        messages.success(
            request,
            "Membership plan updated successfully."
        )


        return redirect(
            "gymove:membership-plan-list"
        )



    return render(
        request,
        "gymove/pages/edit-membership-plan.html",
        {
            "plan": plan,
            "page_title": "Edit Membership Plan",
        },
    )


@login_required_json
def delete_membership_plan(request, id):

    plans = load_plans()

    plans = [
        p for p in plans
        if str(p.get("plan_id")) != str(id)
    ]

    save_plans(plans)

    messages.success(request, "Membership plan deleted successfully.")

    return redirect("gymove:membership-plan-list")


    # ==========================================================
# PROFILE PHOTO
# ==========================================================

@login_required_json
def upload_profile_photo(request):

    if request.method == "POST" and request.FILES.get("profile_image"):

        username = request.session["user"]["username"]

        profile, created = UserProfile.objects.get_or_create(
            username=username
        )

        profile.profile_image = request.FILES["profile_image"]
        profile.save()

        messages.success(
            request,
            "Profile photo updated successfully."
        )

    return redirect("gymove:app-profile")


@login_required_json
def remove_profile_photo(request):

    if request.method == "POST":

        username = request.session["user"]["username"]

        profile, created = UserProfile.objects.get_or_create(
            username=username
        )

        profile.profile_image = "profile_pics/default.png"
        profile.save()

        return JsonResponse({
            "success": True
        })

    return JsonResponse({
        "success": False
    })


# ==========================================================
# LOCK PASSWORD
# ==========================================================

@login_required_json
def save_lock_password(request):

    if request.method == "POST":

        password = request.POST.get("lock_password", "")

        username = request.session["user"]["username"]

        profile, created = UserProfile.objects.get_or_create(
            username=username
        )

        profile.lock_password = password
        profile.save()

        messages.success(
            request,
            "Lock password saved."
        )

    return redirect("gymove:app-profile")


def load_revenue_history():
    return Storage.read("revenue_history.json")


def save_revenue_history(data):
    Storage.write("revenue_history.json", data)


def load_payments():
    return Storage.read("payments.json")


def save_payments(data):
    Storage.write("payments.json", data)


def load_expenses():
    return Storage.read("expenses.json")


def save_expenses(data):
    Storage.write("expenses.json", data)


# ==========================================================
# REVENUE HISTORY
# ==========================================================

@login_required_json
def revenue_history(request):

    payments = load_payments()
    expenses = load_expenses()

    now = datetime.now()

    current_month_key = now.strftime("%Y-%m")


    total_revenue = 0
    transactions = []


    for payment in payments:

        if payment.get("status", "").lower() != "paid":
            continue


        payment_date = payment.get("date", "")


        if payment_date.startswith(current_month_key):

            try:

                amount = int(
                    payment.get("amount", 0)
                )

                total_revenue += amount

                transactions.append(payment)


            except:
                pass



    total_expense = 0
    expense_list = []


    for expense in expenses:

        expense_date = expense.get("date", "")


        if expense_date.startswith(current_month_key):

            try:

                amount = int(
                    expense.get("amount", 0)
                )

                total_expense += amount

                expense_list.append(expense)


            except:
                pass



    current_month = {

        "month": now.strftime("%B"),

        "year": now.year,

        "status": "OPEN",

        "total_revenue": total_revenue,

        "total_expense": total_expense,

        "net_profit": total_revenue - total_expense,

    }



    context = {

        "page_title": "Revenue History",

        "current_month": current_month,

        "closed_months": [],

        "transactions": transactions,

        "expenses": expense_list,


    }



    return render(
    request,
    "gymove/pages/revenue-history.html",
    context
)


@login_required_json
def add_expense(request):

    if request.method == "POST":

        expenses = load_expenses()


        expense = {

            "title": request.POST.get("title"),

            "amount": int(
                request.POST.get("amount", 0)
            ),

            "category": request.POST.get("category"),

            "date": request.POST.get("date"),

        }


        expenses.append(expense)

        save_expenses(expenses)


        messages.success(
            request,
            "Expense added successfully."
        )


        return redirect("gymove:revenue_history")


    return render(
        request,
        "gymove/pages/add-expense.html",
        {
            "page_title": "Add Expense"
        }
    )


@login_required_json
def delete_expense(request, index):

    expenses = load_expenses()

    try:

        expenses.pop(index)

        save_expenses(expenses)

        messages.success(
            request,
            "Expense deleted successfully."
        )

    except:
        pass


    return redirect("gymove:revenue_history")



