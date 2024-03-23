from django.db import models
import datetime

class Users(models.Model):
   id= models.AutoField(primary_key=True)
   name = models.CharField(max_length=50)
   email = models.CharField(max_length=50)
   password= models.TextField(max_length=50)
   secret= models.TextField(default="")
   role= models.TextField()
   is_active= models.BooleanField(default=True)

   def __str__(self):
      return self.email

class Tickets(models.Model):
   id= models.AutoField(primary_key=True)
   #user_email = models.TextField(default="")
   user= models.ForeignKey(Users, on_delete=models.CASCADE, null=True, related_name='tickets')
   #date= models.TextField(blank=True)
   date = models.DateField(blank=True)
   description = models.TextField()
   solution= models.TextField(blank=True)
   is_open= models.BooleanField(default=True)

   def __str__(self):
      return self.description


class Messages(models.Model):
   id= models.AutoField(primary_key=True)
   message= models.TextField()
   date = models.DateField(blank=True, null=True)
   is_read= models.BooleanField(default=False)
   user= user= models.ForeignKey(Users, on_delete=models.CASCADE, null=True)





# class Schrijver(models.Model):
#    schrijver_id= models.AutoField(primary_key=True)
#    voornaam = models.CharField(length=50)
#    achternaam = models.CharField(length=50)

#    class Meta:
#       db_table= "schrijvers"
#       unique_together = ["voornaam", "achternaam"]

# class Boeken:
#    boek_id= models.AutoField(primary_key=True)
#    titel= models.CharField(length=50)

                                                                                                                              