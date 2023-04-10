from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    # slug is an address for a URL
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    image = models.FileField(upload_to="media/images", null=True, blank=True)
    intro = RichTextUploadingField(blank=False, null=False)
    body = RichTextUploadingField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    class Meta:
        ordering = ["-pk"]
    
#    @property
#    def image_url(self):
#       if self.image and hasattr(self.image, 'url'):
#          return self.image_url
#       else:

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

#    def __str__(self):
#        return self.text

    def __str__(self):
        return '%s - %s' % (self.post.title, self.author)
    

