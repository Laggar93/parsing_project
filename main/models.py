from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class GoodsModel(models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    code = models.CharField('Код', blank=True, max_length=255)
    name = models.CharField('Наименование', max_length=255, blank=True)
    first_level = models.CharField('Первый уровень', max_length=255, blank=True)
    second_level = models.CharField('Второй уровень', max_length=255, blank=True)
    third_level = models.CharField('Третий уровень', max_length=255, blank=True)
    price = models.PositiveIntegerField('Цена', blank=True, null=True)
    price_sp = models.PositiveIntegerField('ЦенаСП', blank=True, null=True)
    count = models.IntegerField('Количество', blank=True, null=True)
    property_fields = RichTextUploadingField('Поля свойств', blank=True)
    purchases = models.TextField('Совместные покупки', blank=True)
    unit = models.CharField('Единица измерения', max_length=255)
    image = models.ImageField('Картинка', upload_to='home', blank=True)
    is_on_index = models.BooleanField('Вывод на главную страницу', default=False)
    description = RichTextUploadingField('Описание', blank=True)

    def __str__(self):
        return str(self.name)



