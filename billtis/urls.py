from django.contrib import admin
from django.urls import path, re_path
from . import views

"""
urlpatterns = [
	path("", views.home, name="home"),
	path("singup/", views.signUp, name='sign_up'),
	path("signin/", SignInView.as_view(), name='sign_in'),
	path("singout/", SignOutView.as_view(), name='sign_out'),
	path("place/<int:id>/", views.place, name="place"),
	path("login/", views.login, name="login"),
	path("ecomm/", views.eCommerce, name='ecom'),
	path("menu/<int:id>/", views.menu, name="menu"),
	path("items/<int:id>/", views.items, name="items"),
	path("add/<int:id>/<int:place>/", views.addItemCart, name="add"),
	path("del/<int:id>", views.delItemCart, name="del"),
	path("sub/<int:id>", views.deductItemCart, name="sub"),
	path("clean/", views.cleanCart, name="clean"),
]

"""
urlpatterns = [
	path('admin/', admin.site.urls),
    re_path(r'^api/billtis/$', views.home),
    re_path(r'^api/place/([0-9])$', views.place),
	re_path(r'^api/product/([0-9])$', views.product),
	re_path(r'^api/menu/([0-9])$', views.menu),
]

