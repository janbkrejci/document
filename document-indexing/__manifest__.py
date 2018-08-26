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

Installation
============

How to install under docker image with odoo11
---------------------------------------------

1) download and run odoo image
2) docker exec -it -u root odoo11 /bin/bash
3) cd /var/lib/odoo/addons/11.0
4) apt-get update
5) apt-get install libreoffice poppler-utils
6) unpack the module into addons directory
7) in Odoo, update modules list and install the module
8) done - test it

How to install to on-premise Odoo installation under linux
----------------------------------------------------------

1) apt-get install git libreoffice poppler-utils
2) cd addons path
3) unpack the module into addons directory
4) in Odoo, update modules list and install the module
5) done - test it

How to install to on-premise Odoo installation under Windows
------------------------------------------------------------

..no idea, just try to make sure that you have everything needed
to be able to run "soffice" and "pdftotext" commands from command line.

""",
    'depends': ['document'],
    'data': [],
    'installable': True,
}
