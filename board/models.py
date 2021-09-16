from django.core.exceptions import ValidationError
from django.db import models

from utils import models_utils

KINDS = (
    (
        'type 1', (
            ('n', 'numbers'),
            ('c', 'chars'),
        ),
    ),
    (
        'type 2', (
            ('m', 'mixed'),
        ),
    ),
    (None, 'choose type'),
)
KEYS = models_utils.get_choises_keys(KINDS)


# but this validator exists :)
def validate_kinds(val):
    if val not in KEYS:
        raise ValidationError(f'kind "{val}" not in {KEYS}')
    # if val == 'm':
    #     raise ValidationError('just check')


class Board(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    actual = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=True, editable=False)
    rubric = models.ForeignKey('Rubric', on_delete=models.PROTECT, null=True, blank=True)

    # class Kinds(models.TextChoices):
    #     type1 = 'n', 'numbers'
    #     type2 = 'c', 'chars'
    #     type3 = 'm'
    #     __empty__ = 'choose type and value'

    kind = models.CharField(
        max_length=1, 
        choices=KINDS,  # Kinds.choices
        null=True,
        # validators=[validate_kinds],
    )


    def get_absolute_url(self):
        return f'/board/{self.pk}/'


class Rubric(models.Model):
    type = models.CharField(max_length=120)
