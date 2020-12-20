from django.db import models
from core import models as core_models
from users import models as user_models


class AbstractItem(core_models.AbstractTimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=50)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Tag(AbstractItem):

    """ Tags Model Definition """

    pass


class Room(core_models.AbstractTimeStampedModel):

    """ Room Model Definition """

    title = models.CharField(max_length=100)
    creater = models.CharField(max_length=50)
    tag = models.ManyToManyField(Tag, blank=True)
    upload_user = models.ForeignKey(
        user_models.User, on_delete=models.CASCADE, default=""
    )

    def __str__(self):
        return self.title


class Photo(core_models.AbstractTimeStampedModel):

    """ Photo Model Definition """

    caption = models.CharField(max_length=50)
    file = models.ImageField()
    room = models.ForeignKey(Room, on_delete=models.PROTECT)

    def __str__(self):
        return self.caption