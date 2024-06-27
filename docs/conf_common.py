# The content below is copied from the esp-hdg repo and modified acc to the esp-chip-errata repo

from esp_docs.conf_docs import *  # noqa: F403,F401

languages = ['en', 'zh_CN']
idf_targets = ['esp32', 'esp32s2', 'esp32s3', 'esp32c3', 'esp32c6', 'esp32h2', 'esp32c2']
extensions += ['sphinx_copybutton',
               # Note: order is important here, events must
               # be registered by one extension before they can be
               # connected to another extension
               'esp_docs.esp_extensions.dummy_build_system',
               ]

# link roles config
github_repo = 'espressif/esp-chip-errata'

# context used by sphinx_idf_theme
html_context['github_user'] = 'espressif'
html_context['github_repo'] = 'esp-chip-errata'

html_static_path = ['../_static']

# Extra options required by sphinx_idf_theme
project_slug = 'esp-chip-errata'

# Contains info used for constructing target and version selector
# Can also be hosted externally, see esp-idf for example
versions_url = './_static/docs_version.js'

# Final PDF filename will contains target and version
pdf_file_prefix = u'esp-chip-errata'

# disable the check for link anchors
linkcheck_anchors = False

# Measurement ID for Google Analytics
google_analytics_id = 'G-RP8SCKE54N'
