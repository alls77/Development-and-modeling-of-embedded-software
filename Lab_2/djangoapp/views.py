import os
import json
from django.views import generic
from django.conf import settings
from djangoapp.models import Measurement
from django.urls import reverse_lazy
from djangoapp.forms import MeasurementForm

from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


class ChartMixin(object):
    file_path = os.path.join(settings.BASE_DIR, 'test_data.txt')

    def get_providers(self):
        return ["Light"]

    def get_labels(self):
        dates = [day.strftime("%Y-%m-%d %H:%M:%S")
                 for day in Measurement.objects.all().order_by('time').values_list('time', flat=True)]
        return dates

    def get_data(self):
        values = [value
                  for value in Measurement.objects.all().order_by('time').values_list('value', flat=True)]
        return [values]


class LineChartJSONView(ChartMixin, BaseLineChartView):
    pass


class MeasurementCreate(generic.CreateView):
    form_class = MeasurementForm
    template_name = 'create_measurement.html'
    success_url = reverse_lazy('measurement_list')


class MeasurementList(generic.ListView):
    model = Measurement
    context_object_name = 'measurements'
    template_name = 'measurement_list.html'

    def get(self, request, *args, **kwargs):
        file_path = os.path.join(settings.BASE_DIR, 'test_data.txt')
        with open(file_path, 'r') as measurement_file:
            for line in measurement_file.readlines():
                dct = json.loads(line)
                Measurement.objects.get_or_create(value=dct['value'], time=dct['time'])

        return super().get(request, *args, **kwargs)
