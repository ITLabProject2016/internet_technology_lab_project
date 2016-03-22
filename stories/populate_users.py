import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zombies_on_campus.settings')
django.setup()

from django.contrib.auth.models import User


def populate():
	leifos = add_user("leifos", "leifos", "leifos@leifos.com")
	laura = add_user("laura", "laura", "laura@laura.com")
	david = add_user("david", "david", "david@david.com")


def add_user(uname, pwd, em):
	user = User.objects.create_user(username=uname, 
		email=em)
	user.set_password(pwd)
	user.is_superuser=True
	user.is_staff=True
	user.save()
	return user


if __name__ == '__main__':
    print "Populating users..."
    populate()