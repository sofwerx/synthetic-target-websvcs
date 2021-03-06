"""ws URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from LocateTarget.views import LocateTarget
from GetObjectLoB.views import GetObjectLoB
from PushCoT.views import PushCoT
from DTA.views import DTA
from WriteToGeopkg.views import WriteToGeopkg

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^LocateTarget/$', LocateTarget),
    url(r'^GetObjectLoB/$', GetObjectLoB),
    url(r'^PushCoT/$', PushCoT),
    url(r'^DTA/$', DTA),    
    url(r'^WriteToGeopkg/$', WriteToGeopkg)
]
