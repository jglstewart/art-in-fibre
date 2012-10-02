from django.conf import settings # import the settings file

def site_root(context):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'SITE_ROOT': settings.SITE_ROOT}
