from django.apps import AppConfig

# Define a custom app configuration class for the 'website' app


class TablesConfig(AppConfig):
    # Set the default auto-generated field for models to BigAutoField
    default_auto_field = 'django.db.models.BigAutoField'

    # Specify the name of the app 
    name = 'website'
