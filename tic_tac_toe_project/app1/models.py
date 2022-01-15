from django.db import models
from django.db.models.enums import Choices

# Create your models here.


class Room(models.Model):
    Room_Name = models.CharField( max_length=50 ,unique= True )
    Player_1 = models.CharField( max_length=50 , default= 'Player 1')
    Player_2 = models.CharField( max_length=50 , default= 'Player 2')
    Last_Played = models.IntegerField(default= 2 )
    def __str__(self):
        return self.Room_Name

class game(models.Model):
    row_choice =[
        ('X' , 'X'),
        ('O' ,'O')
    ]
    row00=models.CharField(max_length=1,choices=row_choice,blank=True,null=True)
    row01=models.CharField(max_length=1,choices= row_choice ,blank=True,null=True)
    row02=models.CharField(max_length=1,choices=row_choice,blank=True,null=True)
    row10=models.CharField(max_length=1,choices=row_choice,blank=True,null=True)
    row11=models.CharField(max_length=1,choices=row_choice,blank=True,null=True)
    row12=models.CharField(max_length=1,choices=row_choice,blank=True,null=True)
    row20=models.CharField(max_length=1,choices=row_choice,blank=True,null=True)
    row21=models.CharField(max_length=1,choices=row_choice,blank=True,null=True)
    row22=models.CharField(max_length=1,choices=row_choice,blank=True,null=True)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)

