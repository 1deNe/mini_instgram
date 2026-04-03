import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from hello.models import User # Өзіңіздің User моделіңізді көрсетіңіз

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin12345')
    print("Админ сәтті құрылды: login: admin, pass: admin12345")
else:
    print("Админ бұрыннан бар.")