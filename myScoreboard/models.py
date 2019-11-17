from django.db import models
from django.contrib.auth.models import User


class flag(models.Model):
    flag_value = models.CharField(max_length=30)
    point_value = models.IntegerField()
    
    def __str__(self):
        return str(self.flag_value)

class team(models.Model):
    members = models.ManyToManyField(User)
    team_name = models.CharField(max_length=50)
    team_points = models.IntegerField(default=0)
    flags_gotten = models.ManyToManyField(flag)
    

    def __str__(self):
        return self.team_name + ": " + str(self.team_points)

    class Meta:
        ordering = ['-team_points']

class Player(models.Model):
    team = models.ForeignKey(team, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.user)
