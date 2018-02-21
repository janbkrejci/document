# document-external-indexing
A module for Odoo 11.

Indexes attachments using external tools.

Can index: .doc, .docx, .odp, .ods, .odt, .wps, .rtf, .ppt, .pdf, .xls, .xlsx

## How to install under docker image with odoo11

1) download and run odoo image
2) docker exec -it -u root odoo11 /bin/bash
3) cd /usr/lib/python3/dist-packages/odoo/addons
4) apt-get update
5) apt-get install git libreoffice poppler-utils
6) git clone https://github.com/janbkrejci/document-external-indexing
7) exit bash
8) docker restart odoo11
9) in Odoo, update modules list and install the module
10) done - test it

## How to install to on-premise Odoo installation

1) apt-get install git libreoffice poppler-utils
2) cd addons path
3) git clone https://github.com/janbkrejci/document-external-indexing
4) service restart odoo
5) in Odoo, update modules list and install the module
6) done - test it

## Note for an administrator

Please clean up /tmp directory from time to time, some files may stay there if the conversion fails.

## How the module works

Office documents are indexed by converting them first to .pdf using soffice --headless command.

Then, .pdf files are converted to text using pdftotext from poppler-utils.

enjoy!
