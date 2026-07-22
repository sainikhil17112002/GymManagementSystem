from django.urls import path
from . import views
from gymove import gymove_views

app_name = 'gymove'


urlpatterns = [

    path('', gymove_views.index, name="index"),
    path('index/', gymove_views.index, name="index"),
    path('index_2/', gymove_views.index_2, name="index_2"),


    path('app-profile/', gymove_views.app_profile, name="app-profile"),
    path('app-calender/', gymove_views.app_calender, name="app-calender"),


    path('ecom-product-grid/', gymove_views.ecom_product_grid, name="ecom-product-grid"),
    path('ecom-product-list/', gymove_views.ecom_product_list, name="ecom-product-list"),
    path('ecom-product-detail/', gymove_views.ecom_product_detail, name="ecom-product-detail"),
    path('ecom-product-order/', gymove_views.ecom_product_order, name="ecom-product-order"),
    path('ecom-checkout/', gymove_views.ecom_checkout, name="ecom-checkout"),
    path('ecom-invoice/', gymove_views.ecom_invoice, name="ecom-invoice"),
    path('ecom-customers/', gymove_views.ecom_customers, name="ecom-customers"),


    path('chart-morris/', gymove_views.chart_morris, name="chart-morris"),


    path('content/', gymove_views.content, name="content"),
    path('add_content/', gymove_views.add_content, name="add_content"),


    path('uc-lightgallery/', gymove_views.uc_lightgallery, name="uc-lightgallery"),

    path('widget-basic/', gymove_views.widget_basic, name="widget-basic"),

    path(
        'table-datatable-basic/',
        gymove_views.table_datatable_basic,
        name="table-datatable-basic"
    ),


    path('page-login/', gymove_views.page_login, name="page-login"),
    path('page-register/', gymove_views.page_register, name="page-register"),
    path('page-forgot-password/', gymove_views.page_forgot_password, name="page-forgot-password"),
    path('page-logout/', gymove_views.page_logout, name="page-logout"),



    # ======================
    # TRAINERS
    # ======================

    path(
        'add-trainer/',
        gymove_views.add_trainer,
        name="add-trainer"
    ),


    path(
        'trainer-list/',
        gymove_views.trainer_list,
        name="trainer-list"
    ),


    path(
        'trainer-profile/<int:id>/',
        gymove_views.trainer_profile,
        name="trainer-profile"
    ),


    path(
        'edit-trainer/<int:id>/',
        gymove_views.edit_trainer,
        name="edit-trainer"
    ),


    path(
        'assign-member/<int:id>/',
        gymove_views.assign_member,
        name="assign-member"
    ),


    path(
        'remove-member-trainer/<int:id>/',
        gymove_views.remove_member_trainer,
        name="remove-member-trainer"
    ),

path(
    'delete-trainer/<str:id>/',
    gymove_views.delete_trainer,
    name="delete-trainer"
),


    # ======================
    # MEMBERSHIP PLANS
    # ======================


    path(
        'add-membership-plan/',
        gymove_views.add_membership_plan,
        name="add-membership-plan"
    ),


    path(
        'membership-plan-list/',
        gymove_views.membership_plan_list,
        name="membership-plan-list"
    ),

path(
    'edit-membership-plan/<str:id>/',
    gymove_views.edit_membership_plan,
    name="edit-membership-plan"
),

path(
    'delete-membership-plan/<str:id>/',
    gymove_views.delete_membership_plan,
    name="delete-membership-plan"
),


# ==========================
# MEMBERS
# ==========================


path(
    'add-member/',
    gymove_views.add_member,
    name="add-member"
),


path(
    'member-list/',
    gymove_views.member_list,
    name="member-list"
),


path(
    'member-profile/<str:id>/',
    gymove_views.member_profile,
    name="member-profile"
),


path(
    'edit-member/<str:id>/',
    gymove_views.edit_member,
    name="edit-member"
),

path(
    'delete-member/<str:id>/',
    gymove_views.delete_member,
    name="delete-member"
),


path(
    "login/",
    views.login_view,
    name="login"
),

path(
    "upload-profile-photo/",
    gymove_views.upload_profile_photo,
    name="upload-profile-photo"
),

path(
    "remove-profile-photo/",
    gymove_views.remove_profile_photo,
    name="remove-profile-photo",
),

path(
    "remove-profile-photo/",
    gymove_views.remove_profile_photo,
    name="remove-profile-photo",
),

path(
    "save-lock-password/",
    gymove_views.save_lock_password,
    name="save-lock-password",
),


]