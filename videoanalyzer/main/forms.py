from django import forms
from .models import CircleDetectionModel, TriangleAndSquareDetectionModel, ColorHSVDetectionModel, ColorRGBDetectionModel


class CircleDetectionForm(forms.ModelForm):
    class Meta:
        model = CircleDetectionModel
        fields = '__all__'


class TriangleAndSquareCDetectionForm(forms.ModelForm):
    class Meta:
        model = TriangleAndSquareDetectionModel
        fields = '__all__'


class ColorHSVDetectionForm(forms.ModelForm):
    class Meta:
        model = ColorHSVDetectionModel
        fields = '__all__'


class ColorRGBDetectionForm(forms.ModelForm):
    class Meta:
        model = ColorRGBDetectionModel
        fields = '__all__'
