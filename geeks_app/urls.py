
from django.urls import path
from .import views

app_name = "geeks_app"

urlpatterns = [
    # bloging url showing 
    path('',views.geeksView,name="blogMain"),
    path('addingBlog/',views.addingBlog,name="addingBlog"),
    path('BlogBackend/',views.BlogBackend,name="BlogBackend"),
    path('contact_us/',views.contact_us,name="contact_us"),
    # authentication system create 
    path('login_handle/', views.login_handle, name="login_handle"),
    path('register_handle/', views.register_handle, name="register_handle"),
    path('logout_handle/', views.logout_handle, name="logout_handle"),
    # Admin Panel Operations
    path('admin_panel/',views.admin_panel,name="admin_panel"),
    path('Edit_admin_data/',views.Edit_admin_data,name="Edit_admin_data"),
    path('Delete_admin_data/',views.Delete_admin_data,name="Delete_admin_data"),
    path('Update_admin_value/',views.Update_admin_value,name="Update_admin_value"),
    
]
