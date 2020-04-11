from django.db import models

COVERS = (
    ('P', 'Paperback'),
    ('C', 'Case Wrap'),
    ('D', 'Dust Jacket')
)



# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    pages = models.IntegerField()

    def __str__(self):
        return self.name




class Print(models.Model):
    date = models.DateField()
    cover = models.CharField(
        max_length=1,
            choices=COVERS,
            default=COVERS[0][0]
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_cover_display()} on {self.date}"
