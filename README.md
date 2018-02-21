# document-jbk
Experimental module for Odoo 11

Indexes attachments using external tools.

Can index: .doc, .docx, .odp, .ods, .odt, .wps, .rtf, .ppt, .pdf, .xls, .xlsx

## How to install under docker image with odoo11

1) download and run odoo image
2) docker exec -it -u root odoo11 /bin/bash
3) cd /usr/lib/python3/dist-packages/odoo/addons
4) apt-get update
5) apt-get install git libreoffice poppler-utils
6) git clone https://github.com/janbkrejci/document
7) exit bash
8) docker restart odoo11
9) done - test it

Please clean up /tmp directory from time to time, some files may stay there if the conversion fails.

Office documents are indexed by converting them first to .pdf using soffice --headless command.

Then, .pdf files are converted to text using pdftotext from poppler-utils.

enjoy!
