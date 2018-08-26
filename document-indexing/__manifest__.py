# -*- coding: utf-8 -*-
# Copyright 2018 janbkrejci@gmail.com

{
    'name': 'Document Indexing using external tools',
    'version': '1.0',
    'price': 100,
    'currency': 'EUR',
    'category': 'Document Management',
    'author': 'Jan B. Krejčí',
    'external-dependencies': {'bin': ['soffice', 'pdftotext']},
    'description': """
Better document indexing using external tools
=============================================

This module replaces the default attachment indexing logic using
calls to external tools. This enables Odoo to index much more
file types for fulltext search, moreover the indexing of .pdf
files is far more reliable.

In order to use this module, you have to install libreoffice and
poppler-utils to your operating system, first.

Make sure you can run "soffice" and "pdftotext" from command line.

The module indexes these document types:

* .doc,
* .docx,
* .pdf,
* .xls,
* .xlsx,
* .odp,
* .ods,
* .odt,
* .wps (MS Works),
* .rtf,
* .ppt,
* .pptx

all other types are passed to default processing by ir.attachment model.

The indexing works in two steps. First, the document is translated do .pdf using
"soffice --headless" command, then the text is extracted from the .pdf by using
"pdftotext" from poppler-utils.

Please take a look into /tmp directory from time to time, since there can
stil be some orphan files that you may want delete manually. These files can remain
in /tmp if the conversion crashes for some reason.

""",
    'depends': ['document'],
    'data': [],
    'installable': True,
}
