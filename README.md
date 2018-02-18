# document-jbk
Experimental module for Odoo 11

1) identifikovat typ souboru
2) DOC, RTF, WPS prohnat soffice —headless —convert-to txt
3) XLSX, PPTX, ODT, ODS, ODP, DOCX zpracovat jako XML
4) PDF prohnat pdftotext file -


cd

mkdir filestore

chmod a+rwx filestore

start-odoo-11

docker exec -it -u root odoo11 /bin/bash

cd /usr/lib/python3/dist-packages/odoo/addons

apt-get update

apt-get install git libreoffice poppler-utils mc

git clone https://github.com/janbkrejci/document-jbk

service odoo restart


install module document-jbk

