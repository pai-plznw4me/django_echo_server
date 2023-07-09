from django.urls import path
from echo.views import hello

app_name = 'echo'
urlpatterns = {
    path('hello', hello, name='hello')

}
