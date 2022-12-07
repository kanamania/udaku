from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "0$#kke(6&dt68hf+xhk=&(pi-rp+v&4(1p@ou@izy-=e_qauyi"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", False)

ALLOWED_HOSTS += os.environ.get("DJANGO_ALLOWED_HOSTS", "").split(" ")

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.environ.get("SQL_USER", "develop"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST_MYSQL", "mysql_db"),
        "PORT": os.environ.get("SQL_PORT_MYSQL", "3306"),
        "TEST": {"NAME": "enerlly_test_db"},
    }
}
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
REDIS_USER = os.environ.get("REDIS_USER", "")
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", "")
REDIS_HOST = os.environ.get("REDIS_HOST", "redis_server")
REDIS_PORT = os.environ.get("REDIS_PORT", 6379)
CACHEOPS_REDIS = {
    "host": REDIS_HOST,  # redis-server is on same machine
    "port": REDIS_PORT,  # default redis port
    "db": 1,
    "socket_timeout": 3,  # connection timeout in seconds, optional
    "password": REDIS_PASSWORD,
}

# Cache disabled for local development.
CACHEOPS_ENABLED = False

# Celery connection details for local
CELERY_BROKER_URL = f"redis://{REDIS_USER}:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}"
CELERY_RESULT_BACKEND = f"redis://{REDIS_USER}:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}"

# Health check redis url
REDIS_URL = f"redis://{REDIS_USER}:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}"


JAZZMIN_SETTINGS = {
    "site_title": os.environ.get('ADMIN_SITE_NAME', 'ADMIN_SITE_NAME'),
    "site_header": os.environ.get('ADMIN_SITE_NAME', 'ADMIN_SITE_NAME'),
    "site_brand": os.environ.get('ADMIN_SITE_NAME', 'ADMIN_SITE_NAME'),
    "site_icon": None,
    # Add your own branding here
    # "site_logo": "vendor/boilerplate/img/fireicon.png",
    "site_logo": None,
    "welcome_sign": os.environ.get('ADMIN_SITE_WELCOME', 'ADMIN_SITE_WELCOME'),
    # Copyright on the footer
    "copyright": os.environ.get('ADMIN_SITE_NAME', 'ADMIN_SITE_NAME'),
    "user_avatar": None,
    ############
    # Top Menu #
    ############
    # Links to put along the top menu
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {"name": os.environ.get('ADMIN_SITE_NAME', 'ADMIN_SITE_NAME'), "url": "home", "permissions": ["auth.view_user"]},
        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},
        {"model": "Post"},
        {"model": "Comment"},
        {"model": "Setting"},
    ],
    #############
    # Side Menu #
    #############
    # Whether to display the side menu
    "show_sidebar": True,
    # Whether to aut expand the menu
    "navigation_expanded": True,
    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "users.User": "fas fa-user",
        "auth.Group": "fas fa-users",
        "admin.LogEntry": "fas fa-file",
    },
    # # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-arrow-circle-right",
    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,
    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    # Uncomment this line once you create the bootstrap-dark.css file
    # "custom_css": "css/bootstrap-dark.css",
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,
    ###############
    # Change view #
    ###############
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
}

JAZZMIN_UI_TWEAKS = {
    "theme": "simplex",
    "dark_mode_theme": "superhero",
}