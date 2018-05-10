# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8ed0u)mi=+u6h5&o!91!j_lw*go8=@3!)ib&h8w()w0t1df9$*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'labinnovacion',
        'USER': 'lab',
        'PASSWORD': 'laboratorio',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

BASE_URL_FIXED = 'http://169.254.10.232:8000'

#DISQUS_API_KEY = 'P0F8utRQcfKjLNxZs9U6oeI5KqnShs9xUqDRBrJgwFCK70slnPCn9GdEEO2KOpIV'
#DISQUS_WEBSITE_SHORTNAME = 'labinnovacion'
