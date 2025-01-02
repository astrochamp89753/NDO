from django.db import models

class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ToDoItem(models.Model):
    toDoList = models.ForeignKey(ToDoList, on_delete=models.CASCADE) # django ne ve podatkovnega tipa, zato ForeignKey
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text