from django.shortcuts import render
from django.http import HttpResponse
import azure.cognitiveservices.speech as speechsdk
from .models import Transcribe

def from_mic():
    speech_key, service_region = "7b1930a5b862497dae4b1878b72b6be0", "eastus"
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    print("Speak into your microphone.")
    result = speech_recognizer.recognize_once_async().get()
    print(result.text)
    return str(result.text)

def button(request):
    return render(request,'speechTotext/home.html')

def output(request):
    data = from_mic()
    transcribe_obj = Transcribe(content=data)
    transcribe_obj.save()
    return render(request,'speechTotext/home.html', {'data':data})
