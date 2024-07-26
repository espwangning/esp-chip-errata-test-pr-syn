# The content below is copied from the esp-hdg repo and modified acc to the esp-chip-errata repo

from esp_docs.conf_docs import *  # noqa: F403,F401

languages = ['en', 'zh_CN']
idf_targets = ['esp32', 'esp32s2', 'esp32s3', 'esp32c3', 'esp32c6', 'esp32h2', 'esp32c2']
extensions += ['sphinx_copybutton',
               # Note: order is important here, events must
               # be registered by one extension before they can be
               # connected to another extension
               'esp_docs.esp_extensions.dummy_build_system',
               'linuxdoc.rstFlatTable', #https://return42.github.io/linuxdoc/linuxdoc-howto/table-markup.html#flat-table
               'sphinx_tags', #https://sphinx-tags.readthedocs.io/en/latest/quickstart.html
               'sphinx_design', #https://sphinx-design.readthedocs.io/en/latest/get_started.html
               ]

ESP32C3_DOCS = ['01-chip-identification/esp32c3/*.rst',
                '02-errata-summary/esp32c3-errata-summary.rst',
                '03-errata-description/esp32c3/*.rst',
                '03-errata-description/shared/sar-adc-adc2-not-work.rst',
                ]
ESP32C2_DOCS = ['01-chip-identification/esp32c2/*.rst',
                '02-errata-summary/esp32c2-errata-summary.rst',
                '03-errata-description/esp32c2/*.rst',
                ]
ESP32S3_DOCS = ['01-chip-identification/esp32s3/*.rst',
                '02-errata-summary/esp32s3-errata-summary.rst',
                '03-errata-description/esp32s3/*.rst',
                ]
ESP32C6_DOCS = ['01-chip-identification/esp32c6/*.rst',
                '02-errata-summary/esp32c6-errata-summary.rst',
                '03-errata-description/esp32c6/*.rst',
                '03-errata-description/shared/clock-rc-fast-clk-inaccurate.rst',
                '03-errata-description/shared/cpu-load-store.rst',
                '03-errata-description/shared/rmt-idle-level-cannot-be-controlled.rst',
                ]
ESP32S2_DOCS = ['01-chip-identification/esp32s2/*.rst',
                '02-errata-summary/esp32s2-errata-summary.rst',
                '03-errata-description/esp32s2/*.rst',
                ]
ESP32H2_DOCS = ['01-chip-identification/esp32h2/*.rst',
                '02-errata-summary/esp32h2-errata-summary.rst',
                '03-errata-description/esp32h2/*.rst',
                ]
ESP32_DOCS = ['01-chip-identification/esp32/*.rst',
              '02-errata-summary/esp32-errata-summary.rst',
              '03-errata-description/esp32/*.rst',
              ]

conditional_include_dict = {'esp32':ESP32_DOCS,
                            'esp32c2':ESP32C2_DOCS,
                            'esp32c3':ESP32C3_DOCS,
                            'esp32c6':ESP32C6_DOCS,
                            'esp32s2':ESP32S2_DOCS,
                            'esp32s3':ESP32S3_DOCS,
                            'esp32h2':ESP32H2_DOCS}

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
google_analytics_id = ''

# Configuration for sphinx_tags
tags_create_tags = True
tags_extension = ["rst"]
tags_create_badges = True
tags_badge_colors = {
    "*": "secondary",
}

# Customized LaTeX configurations

titlepage = ''
with open('../_static/titlepage.tex') as f:
    titlepage = f.read()

latex_elements = {
    'papersize': 'a4paper',

    # Latex figure (float) alignment
    'figure_align': 'H',

    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    'fncychap': '''
\\usepackage[Sonny]{fncychap}
    ''',

    'preamble': preamble,

    'maketitle': titlepage,

    # Font configuration
     'fontpkg': r'''
    ''',
    
    # Remove empty pages after ToC and end of chapter
    'extraclassoptions': 'openany,oneside',

    # Set table header color
    'sphinxsetup': r'''
TableMergeColorHeader={gray!25},
TableRowColorHeader={gray!25},
TableRowColorOdd={white!0},
TableRowColorEven={white!0},
TableMergeColorOdd={white!0},
TableMergeColorEven={white!0},
noteBorderColor={RGB}{16, 32, 160},
    ''',
}

# Start a document from Section instead of Chapter
latex_docclass = {
    'howto': 'article',
    'manual': 'article',
}

latex_toplevel_sectioning = 'section'

# Configure latex table style
latex_table_style = ['colorrows']

latex_logo = '../_static/esp-logo-standard-vertical.pdf'

# Table, figure, and section numbering configurations
numfig = True
