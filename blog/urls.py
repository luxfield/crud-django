from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
		path('',views.index,name="index"),
		path('hapus/<int:input>', views.hapus, name="hapus"),
		path('edit/<int:input>', views.edit, name="edit"),
		

]