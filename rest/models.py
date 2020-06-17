from django.db import models

# Manufacturer
#     name: str
#     website: url
class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField()
    
    def __str__(self):
        return self.name

# ShoeType
#     style: str
class ShoeType(models.Model):
    style = models.CharField(max_length=100)
    
    def __str__(self):
        return self.style

class ShoeColor(models.Model):
    SHOE_COLOR_CHOICES = [
        ('(255,0,0)', 'Red'),
        ('(255,165,0)', 'Orange'),
        ('(255,255,0)', 'Yellow'),
        ('(0,255,0)', 'Green'),
        ('(0,0,255)', 'Blue'),
        ('(29,0,51)', 'Indigo'),
        ('(238,130,230)', 'Violet'),
        ('(255,255,255)', 'White'),
        ('(0,0,0)', 'Black'),
    ]
    color_name = models.CharField(
        max_length=13,
        choices=SHOE_COLOR_CHOICES,
        default="(0,0,0)"
    )

    def __str__(self):
        return self.color_name
# ShoeColor
#     color_name: str (ROYGBIV + white / black) --> hint: https://docs.djangoproject.com/en/3.0/ref/models/fields/#choices (Links to an external site.)Links to an external site.

class Shoe(models.Model):
    size = models.IntegerField()
    brand_name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=100)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=100)
# Shoe
#     size: int
#     brand name: str
#     manufacturer: FK (Foreign Key)
#     color: FK
#     material: str
#     shoe_type: FK
#     fasten_type: str
