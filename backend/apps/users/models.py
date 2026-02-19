from django.db import models

class User(models.Model):
    ROLE_CHOICES = (
        ('ADMIN', 'Administrador VIT'),
        ('CONSULTANT', 'Consultor'),
        ('CLIENT', 'Cliente'),
    )
    
    # Campos básicos
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    
    # Campos personalizados
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='CLIENT')
    phone = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=True)
    #company = models.ForeignKey('companies.Company', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    class Meta:
        db_table = 'users_user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.get_role_display()})'
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'