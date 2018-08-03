# document-indexing
A module for Odoo 11.

Indexes attachments using external tools.

Can index: .doc, .docx, .odp, .ods, .odt, .wps, .rtf, .ppt, .pdf, .xls, .xlsx

## Licensing information

This module is licensed under MIT license. You can use it as you wish. The module is and always will be free. If you like it and fell like you want to support it, a small donation will be appreciated.

<form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
<input type="hidden" name="cmd" value="_s-xclick">
<input type="hidden" name="hosted_button_id" value="XSJGWES2VMSJL">
<input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" border="0" name="submit" alt="PayPal - The safer, easier way to pay online!">
<img alt="" border="0" src="https://www.paypalobjects.com/cs_CZ/i/scr/pixel.gif" width="1" height="1">
</form>


## How to install under docker image with odoo11

1) download and run odoo image
2) docker exec -it -u root odoo11 /bin/bash
3) cd /var/lib/odoo/addons/11.0
4) apt-get update
5) apt-get install git libreoffice poppler-utils
6) git clone https://github.com/janbkrejci/document-indexing
7) in Odoo, update modules list and install the module
8) done - test it

## How to install to on-premise Odoo installation under linux

1) apt-get install git libreoffice poppler-utils
2) cd addons path
3) git clone https://github.com/janbkrejci/document-indexing
4) in Odoo, update modules list and install the module
5) done - test it

## How to install to on-premise Odoo installation under Windows

..no idea, just try to make sure that you have everything needed
to be able to run "soffice" and "pdftotext" commands from command line.

## Note for an administrator

Please clean up /tmp directory from time to time, some files may stay there if the conversion fails.

## How the module works

The supported documents are indexed by converting them first to .pdf using soffice --headless command,
then, .pdf files are converted to text using pdftotext from poppler-utils.

The list of words is placed into "index_content" field of "ir.attachment" model.

You can add this field to default search form of "ir.attachment" model in order to be able to search in it's content.

Also, a menu item for model "ir.attachment" will come handy - you can create it manually in development mode (Settings/Database structure/Models, search model for "ir.attachment", click "Create menu" button on the bottom of the form view).

enjoy!
