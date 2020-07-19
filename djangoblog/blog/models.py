from django.db import models

STATUS= (
    (0,"Draft"),
    (1,"Publish")
)

class Author(models.Model):
    name = models.CharField(max_length=20,unique=True)
    email = models.EmailField(blank=False,unique=True)
    info = models.TextField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    content = models.TextField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS,default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title
