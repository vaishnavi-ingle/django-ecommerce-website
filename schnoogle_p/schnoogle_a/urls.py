from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.store, name="store"),
    path('cart_detail/', views.cart_detail, name='cart_detail'),
    path('checkout/', views.checkout, name="checkout"),
    path('toys/', views.toys, name="toys"),
    path('diapering/', views.diapering, name="diapering"),
    path('tshirtsB/', views.tshirtsB, name="tshirtsB"),
    path('footwearB/', views.footwearB, name="footwearB"),
    path('winterB/', views.winterB, name="winterB"),
    path('nightwearB/', views.nightwearB, name="nightwearB"),
    path('casualwearG/', views.casualwearG, name="casualwearG"),
    path('weddingwearG/', views.weddingwearG, name="weddingwearG"),
    path('partyB/', views.partyB, name="partyB"),
    path('footwearG/', views.footwearG, name="footwearG"),
    path('winterG/', views.winterG, name="winterG"),
    path('nightwearG/', views.nightwearG, name="nightwearG"),
    path('parenting/', views.parenting, name="parenting"),
    path('signup/', views.signUp, name="signup"),
    path('feedback/', views.feedback, name="feedback"),
    path('login/', auth_views.LoginView.as_view(template_name='schnoogle_a/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='store'), name='logout'),
    path('contact/', views.contact, name="contact"),
    path('privacy/', views.privacy, name="privacy"),
    path('about/', views.about, name="about"),
     path('newsletter/signup/', views.newsletter_signup, name='newsletter_signup'),
]