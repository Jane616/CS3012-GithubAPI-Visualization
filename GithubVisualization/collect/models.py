from django.db import models

class User(models.Model):
    company = models.CharField(max_length = 10)
    login = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.company + ' - ' + self.login

class Repo(models.Model):
    """def __init__(self, user, repo, star):
        self.username = user
        self.repo_name = repo
        self.stargazer = star
"""
    username = models.CharField(max_length = 255)
    repo_name = models.CharField(max_length = 255)
    stargazer = models.IntegerField(default=0)



    def __str__(self):
        return self.username + ' - ' + self.repo_name + ' - ' + str(self.stargazer)

class Lang(models.Model):
    '''
    def __init__(self, repo, language, count):
        self.repo = repo
        self.language = language
        self.count = count
        '''


    repo = models.CharField(max_length = 255)
    language = models.CharField(max_length = 50)
    count = models.IntegerField(default=0)


    def __str__(self):
        return self.repo + ' - ' + self.language + " - " + str(self.count)
