from django.db import models
import uuid

# model to store file and their _metadata
class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(upload_to='uploads/')
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    size = models.IntegerField()
    file_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name
