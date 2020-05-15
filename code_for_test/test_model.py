'''
I have a post model in which i have post type field. I want that when user select post type = assignment 
this it ask for submission deadline other wise it does not ask anything. and how can i display it in template.

'''



class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank = True)
    content = models.TextField()
    choice = (
        ('post','post'),
        ('anouncement','anouncement'),
        ('question', 'question'),
        ('assignment', 'assignment')
        )
    post_type = models.CharField(choices = choice, default = 'post', max_length = 12)
    classroom = models.ForeignKey(Classroom)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)



    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"slug": self.slug})