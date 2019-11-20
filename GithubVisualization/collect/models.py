from django.db import models

class User(models.Model):
    company = models.CharField(max_length = 10)
    login = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.company + ' - ' + self.login

class Repo(models.Model):
    login = models.ForeignKey(User, on_delete=models.CASCADE)
    repo_name = models.CharField(max_length = 255)
    stargazer = models.IntegerField

class Lang(models.Model):
    repo_name = models.ForeignKey(Repo, on_delete=models.CASCADE)
    language = models.CharField(max_length = 50)
    count = models.IntegerField
