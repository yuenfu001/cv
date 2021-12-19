from django.db import models

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return f'{self.name}'
class Name(models.Model):
    first_name = models.CharField(max_length=50, null=False, help_text="please your first name is actually your own name")
    last_name = models.CharField(max_length=50, null=False, help_text="please your last name is actually your surname name")
    state_of_origin = models.ForeignKey(State,on_delete =models.PROTECT,related_name="soo", null=False)
    summary = models.TextField(null=True, help_text="Tell us all little about yourself")
    date_of_birth = models.DateField(null=False)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} ({self.last_name} {self.date_of_birth}) ({self.date_created} {self.date_updated})"
