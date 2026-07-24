from django.db import models



class Trainer(models.Model):

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    ]


    trainer_id = models.CharField(
        max_length=20,
        unique=True
    )

    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    phone = models.CharField(
        max_length=15
    )

    email = models.EmailField(
        blank=True
    )

    specialization = models.CharField(
        max_length=100
    )

    experience = models.IntegerField(
        help_text="Experience in years"
    )

    join_date = models.DateField()

    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    address = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Active"
    )

    photo = models.ImageField(
        upload_to="trainers/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return f"{self.first_name} {self.last_name}"





class Member(models.Model):


    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]


    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Expired", "Expired"),
        ("Inactive", "Inactive"),
    ]



    member_id = models.CharField(
        max_length=20,
        unique=True
    )


    first_name = models.CharField(
        max_length=100
    )


    last_name = models.CharField(
        max_length=100
    )


    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )


    date_of_birth = models.DateField()



    phone = models.CharField(
        max_length=15
    )


    email = models.EmailField(
        blank=True
    )


    address = models.TextField(
        blank=True
    )


    emergency_contact = models.CharField(
        max_length=15
    )


    join_date = models.DateField()



    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Active"
    )



    photo = models.ImageField(
        upload_to="members/",
        blank=True,
        null=True
    )



    # Assign Trainer

    trainer = models.ForeignKey(
        Trainer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="members"
    )



    # Assign Membership Plan

    membership_plan = models.ForeignKey(
        "MembershipPlan",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="members"
    )



       # Membership Period

    membership_start_date = models.DateField(
        null=True,
        blank=True
    )


    membership_expiry_date = models.DateField(
        null=True,
        blank=True
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def save(self, *args, **kwargs):

        if self.membership_plan and self.membership_start_date:

            from dateutil.relativedelta import relativedelta

            self.membership_expiry_date = (
                self.membership_start_date +
                relativedelta(
                    months=self.membership_plan.duration
                )
            )

        super().save(*args, **kwargs)



    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        

# ==========================
# MEMBERSHIP PLANS
# ==========================


class MembershipPlan(models.Model):


    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    ]



    plan_id = models.CharField(
        max_length=20,
        unique=True
    )


    name = models.CharField(
        max_length=100
    )


    duration = models.IntegerField(
        help_text="Duration in months"
    )


    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )


    description = models.TextField(
        blank=True
    )


    features = models.TextField(
        blank=True
    )


    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Active"
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )



    def __str__(self):
        return self.name



  

class UserProfile(models.Model):

    username = models.CharField(
        max_length=150,
        unique=True
    )

    profile_image = models.ImageField(
        upload_to="profile_pics/",
        default="profile_pics/default.png",
        blank=True
    )

    lock_password = models.CharField(
        max_length=128,
        blank=True,
        default=""
    )

    def __str__(self):
        return self.username



from django.db import models
from django.contrib.auth.models import User

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_featured', '-created_at']

    def __str__(self):
        return self.title