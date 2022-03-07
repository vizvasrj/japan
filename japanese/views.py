
# Create your views here.
from rest_framework import generics
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import NagisaSerializer
from rest_framework.exceptions import APIException
import spacy
nlp = spacy.load("ja_core_news_md")
import time


class Success(APIException):
    status_code = status.HTTP_202_ACCEPTED
    default_detail = 'Success .'
    default_code = 'success'


class NagisaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = NagisaSerializer



    def update(self, request, *args, **kwargs):
        text = request.data['text']
        print(text)
        start_time = time.time()
        # k2 = [y + " " if y.isascii() else y for y in nagisa.tagging(text).words]
        doc = nlp(text)                
        k2 = [x.text for x in doc]
        endtime = time.time() - start_time
        data = {'words': k2, 'time': endtime}
        raise Success(data)
    

    def get(self, request, *args, **kwargs):
        raise Success('a')

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
