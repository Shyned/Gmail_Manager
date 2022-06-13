# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*@nxf5@i!q$*vl6w1-%ao%&9(6%^ukbt1f-_@p1^05ftf^e!pn'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'email_user_manager',
        'HOST': 'localhost',
        'USER':'root',
        'PASSWORD':'Password',
        
    }
}