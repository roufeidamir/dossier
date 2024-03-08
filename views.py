# myapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .models import PredictionInput

class PredictionInputForm(forms.ModelForm):
    class Meta:
        model = PredictionInput
        fields = ['nom', 'prenom', 'tel1', 'tel2', 'email', 'file_upload']

def predict_list(request):
    prediction_inputs = PredictionInput.objects.all()
    return render(request, 'myapp/predict_list.html', {'prediction_inputs': prediction_inputs})

def predict_create(request):
    if request.method == 'POST':
        form = PredictionInputForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('predict_list')
    else:
        form = PredictionInputForm()

    return render(request, 'myapp/predict_create.html', {'form': form})

def predict_update(request, pk):
    instance = get_object_or_404(PredictionInput, pk=pk)
    if request.method == 'POST':
        form = PredictionInputForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('predict_list')
    else:
        form = PredictionInputForm(instance=instance)

    return render(request, 'myapp/predict_update.html', {'form': form, 'instance': instance})

def predict_delete(request, pk):
    instance = get_object_or_404(PredictionInput, pk=pk)
    instance.delete()
    return redirect('predict_list')
