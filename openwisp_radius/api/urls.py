from django.urls import path

from . import views


def get_api_urls(api_views=None):
    if not api_views:
        api_views = views
    return [
        path('freeradius/authorize/', api_views.authorize, name='authorize'),
        path('freeradius/postauth/', api_views.postauth, name='postauth'),
        path('freeradius/accounting/', api_views.accounting, name='accounting'),
        # registration differentiated by organization
        path('<slug:slug>/account/', api_views.register, name='rest_register'),
        # password reset
        path(
            '<slug:slug>/account/password/reset/confirm/',
            api_views.password_reset_confirm,
            name='rest_password_reset_confirm',
        ),
        path(
            '<slug:slug>/account/password/reset/',
            api_views.password_reset,
            name='rest_password_reset',
        ),
        path(
            '<slug:slug>/account/password/change/',
            api_views.password_change,
            name='rest_password_change',
        ),
        # obtaining the user token is also different for every org
        path(
            '<slug:slug>/account/token/',
            api_views.obtain_auth_token,
            name='user_auth_token',
        ),
        path(
            '<slug:slug>/account/token/validate/',
            api_views.validate_auth_token,
            name='validate_auth_token',
        ),
        path(
            '<slug:slug>/account/session/',
            api_views.user_accounting,
            name='user_accounting',
        ),
        # generate new sms phone token
        path(
            '<slug:slug>/account/phone/token/',
            api_views.create_phone_token,
            name='phone_token_create',
        ),
        path(
            '<slug:slug>/account/phone/verify/',
            api_views.validate_phone_token,
            name='phone_token_validate',
        ),
        # allow changing phone number
        path(
            '<slug:slug>/account/phone/change/',
            api_views.change_phone_number,
            name='phone_number_change',
        ),
        path('radiusbatch/', api_views.batch, name='batch'),
        path(
            '<slug:slug>/radiusbatch/<uuid:radbatch>/pdf/',
            api_views.download_rad_batch_pdf,
            name='download_rad_batch_pdf',
        ),
    ]
