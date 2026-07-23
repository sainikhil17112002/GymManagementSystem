from django import forms

from .models import (
    Member,
    Trainer,
    MembershipPlan,
    UserProfile,
)


# ==========================
# MEMBER FORM
# ==========================

class MemberForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = "__all__"

        widgets = {
            "member_id": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Member ID"
            }),

            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "First Name"
            }),

            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Last Name"
            }),

            "gender": forms.Select(attrs={
                "class": "form-select"
            }),

            "date_of_birth": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Phone Number"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Email Address"
            }),

            "address": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Address"
            }),

            "emergency_contact": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Emergency Contact"
            }),

            "join_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),

            "status": forms.Select(attrs={
                "class": "form-select"
            }),

            "photo": forms.ClearableFileInput(attrs={
                "class": "form-control"
            }),

            "trainer": forms.Select(attrs={
                "class": "form-select"
            }),

            "membership_plan": forms.Select(attrs={
                "class": "form-select"
            }),

            "membership_start_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),

            "membership_expiry_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),
        }


# ==========================
# TRAINER FORM
# ==========================

class TrainerForm(forms.ModelForm):

    class Meta:
        model = Trainer
        fields = "__all__"

        widgets = {
            "trainer_id": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Trainer ID"
            }),

            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "First Name"
            }),

            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Last Name"
            }),

            "gender": forms.Select(attrs={
                "class": "form-select"
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Phone Number"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Email Address"
            }),

            "specialization": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Specialization"
            }),

            "experience": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Experience Years"
            }),

            "join_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),

            "salary": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Salary"
            }),

            "address": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Address"
            }),

            "status": forms.Select(attrs={
                "class": "form-select"
            }),

            "photo": forms.ClearableFileInput(attrs={
                "class": "form-control"
            }),
        }


# ==========================
# MEMBERSHIP PLAN FORM
# ==========================

class MembershipPlanForm(forms.ModelForm):

    class Meta:
        model = MembershipPlan
        fields = "__all__"

        widgets = {
            "plan_id": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Plan ID"
            }),

            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Plan Name"
            }),

            "duration": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Duration (Months)"
            }),

            "price": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Price"
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Plan Description"
            }),

            "features": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Plan Features"
            }),

            "status": forms.Select(attrs={
                "class": "form-select"
            }),
        }


# ==========================
# ADMIN REGISTER FORM
# ==========================

# ==========================
# LOCK PASSWORD FORM
# ==========================

class LockPasswordForm(forms.ModelForm):

    lock_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Lock Password"
        })
    )

    class Meta:
        model = UserProfile
        fields = ["lock_password"]