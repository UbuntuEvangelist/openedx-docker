import json

from lms.envs.fun.utils import Configuration

from ..common import *


# Load custom configuration parameters from yaml files
config = Configuration(os.path.dirname(__file__))

# Fun-apps configuration
INSTALLED_APPS += (
    "fun",
    "videoproviders",
    "teachers",
    "courses",
    "haystack",
    "universities",
    "easy_thumbnails",
    "ckeditor",
    "selftest",
    "raven.contrib.django.raven_compat",
)

ROOT_URLCONF = "fun.cms.urls"

# This constant as nothing to do with github.
# Path is used to store tar.gz courses before import process
GITHUB_REPO_ROOT = DATA_DIR

# ### THIRD-PARTY SETTINGS ###

# Haystack configuration (default is minimal working configuration)
HAYSTACK_CONNECTIONS = config(
    "HAYSTACK_CONNECTIONS",
    default={
        "default": {"ENGINE": "courses.search_indexes.ConfigurableElasticSearchEngine"}
    },
    formatter=json.loads,
)

CKEDITOR_UPLOAD_PATH = "./"

# ### FUN-APPS SETTINGS ###
# -- Base --
FUN_BASE_ROOT = path(os.path.dirname(imp.find_module("funsite")[1]))

# Add 'theme/cms/templates' directory to MAKO template finder to override some
# CMS templates
MAKO_TEMPLATES["main"] = [FUN_BASE_ROOT / "fun/templates/cms"] + MAKO_TEMPLATES["main"]

# Generic LTI configuration
LTI_XBLOCK_CONFIGURATIONS = [{"display_name": "LTI consumer"}]