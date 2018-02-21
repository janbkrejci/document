# -*- coding: utf-8 -*-
# Copyright 2018 janbkrejci@gmail.com

{
    'name': 'Document Indexation using external tools',
    'version': '1.0',
    'category': 'Document Management',
    'description': """
Document indexation using external tools
========================================

Prerequisities: installed packages libreoffice and poppler-utils

Indexes .doc, .docx, .odp, .ods, .odt, .wps, .rtf, .ppt, .pdf, .xls, .xlsx

At first, translates the attachment using soffice --headless to .pdf,
then uses pdftotext from poppler-utils.

Please have a look into /tmp directory from time to time, since there can
be some orphan files to delete. These files can stay in /tmp if the
conversion crashes.

""",
    'depends': [],
    'data': [],
    'installable': True,
}
