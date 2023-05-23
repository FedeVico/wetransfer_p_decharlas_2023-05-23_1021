from django.db import models

class Message(models.Model):
    content = models.TextField()
    date = models.DateTimeField()
    isimg = models.BooleanField()
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)

    def __str__(self):
        return self.author.name + " -> " + self.content


class Room(models.Model):
    name = models.TextField(max_length=100)
    # Date,
    creator = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " -> " + self.creator.name


class Room_Register(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return self.user.name + " -> " + self.room.name


class Room_Vote(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    vote = models.BooleanField()

    def __str__(self):
        if self.vote:
            value = "like"
        else:
            value = "dislike"
        return self.room.name + " | " + self.user.name + "->" + value



class User(models.Model):

    FONT_OPT = [
        ("Arial", "Arial"),
        ("Verdana", "Verdana"),
        ("Tahoma", "Tahoma"),
        ("Trebuchet MS", "Trebuchet MS"),
        ("Times New Roman", "Times New Roman"),
        ("Georgia", "Georgia"),
        ("Garamond", "Garamond"),
        ("Helvetica", "Helvetica"),
        ("Gill Sans", "Gill Sans"),
    ]

    SIZE_OPT = [
        ("Small", "small"),
        ("Medium", "medium"),
        ("Large", "large"),
    ]

    name = models.TextField(max_length=100)
    userID = models.IntegerField()
    font_type = models.TextField(choices=FONT_OPT, default="Verdana", null=True)
    font_size = models.TextField(choices=SIZE_OPT, default="Medium", null=True)

    def __str__(self):
        return self.name + " -> " + str(self.userID)


class Password(models.Model):
    valid_pwd = models.TextField(max_length=10)

    def __str__(self):
        return "Password -> " + self.valid_pwd
