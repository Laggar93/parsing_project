import csv
import io

from django import forms
from django.core.exceptions import ValidationError
from django.forms import FileField

from main.models import GoodsModel


class CsvFileForm(forms.Form):
    file = FileField()

    def save(self):
        file_data = self.cleaned_data['file']

        GoodsModel.objects.bulk_create([
          GoodsModel(**item) for item in file_data
        ])

    def clean_file(self):
        file = self.cleaned_data['file']

        self.validate_file_type(file=file)

        reader = csv.reader(io.StringIO(file.read().decode('utf-8')))
        file_data = list()

        for i, row in enumerate(reader):
            if i > 0:
                row_data = ''.join(row).split(';')

                self.validate_number(price=row_data[5], message=f"Price value is invalid on row {i + 1}")
                self.validate_number(price=row_data[6], message=f"Price SP value is invalid on row {i + 1}")
                self.validate_number(price=row_data[7], message=f"Count value is invalid on row {i + 1}")

                file_data.append(dict(
                    code=row_data[0],
                    name=row_data[1],
                    first_level=row_data[2],
                    second_level=row_data[3],
                    third_level=row_data[4],
                    price=float(row_data[5]),
                    price_sp=float(row_data[6]),
                    count=float(row_data[7]),
                    property_fields=row_data[8],
                    purchases=row_data[9],
                    unit=row_data[10],
                    image=row_data[11],
                    is_on_index=bool(row_data[12]),
                    description=row_data[13],
                ))

        return file_data

    def validate_number(self, price, message):
        try:
            float(price)
        except ValueError:
            raise ValidationError(message)

    def validate_file_type(self, file):
        pass
