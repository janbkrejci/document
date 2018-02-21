# -*- coding: utf-8 -*-
# Copyright 2018 janbkrejci@gmail.com
# indexing moved to external tools for better results
# requires installed linux packages libreoffice and poppler-utils
import io
import logging
import os
import tempfile
import subprocess
import xml.dom.minidom
import zipfile

from odoo import api, models

_logger = logging.getLogger(__name__)

FTYPES = ['DOC', 'DOCX', 'PPT', 'PPTX', 'XLS', 'XLSX', 'WPS', 'RTF', 'ODT', 'ODP', 'ODS']

class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    def _delete_file(self, path):
        os.remove(path)

    def _index_pdf(self, bin_data):
        '''Index PDF documents'''

        filename = self._get_temp_filename() + ".pdf"
        self._save_buffer_to_file(bin_data, filename)

        o = ""

        try:
            result = subprocess.run(['pdftotext', filename, '-'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            o = result.stdout.decode('utf-8')
        except:
            o = 'Error: no "pdftotext" binary found, please install poppler-utils first.'

        self._delete_file(filename)
        return o

    def _index_office(self, ext, bin_data):

        tmp_filename = self._get_temp_filename()
        in_filename = tmp_filename + '.' + ext.lower() + '_'
        pdf_filename = tmp_filename + '.pdf'
        out_filename = tmp_filename + '.txt'
        self._save_buffer_to_file(bin_data, in_filename)

        o = ""

        try:
            result = subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', tempfile._get_default_tempdir() , in_filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            result = subprocess.run(['pdftotext', pdf_filename, out_filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            result = subprocess.run(['cat', out_filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            o = result.stdout.decode('utf-8')
        except:
            o = 'Error: no "soffice" binary found, please install LibreOffice first.'

        self._delete_file(in_filename)
        self._delete_file(pdf_filename)
        self._delete_file(out_filename)
        return o

    def _get_temp_filename(self):
        return tempfile._get_default_tempdir() + "/" + next(tempfile._get_candidate_names())

    def _save_buffer_to_file(self, buffer, path):
        file = open(path, "wb")
        file.write(buffer)
        file.close()

    def _save_buffer_to_file_txt(self, buffer, path):
        file = open(path, "w")
        file.write(buffer)
        file.close()

    @api.model
    def _index(self, bin_data, datas_fname, mimetype):
        fname = ""
        if type(datas_fname).__name__ == 'str':
            fname = datas_fname

        filename, file_extension = os.path.splitext(fname)
        ext = file_extension[1:].upper()
        if ext == 'PDF':
            return self._index_pdf(bin_data)

        if ext in FTYPES:
            return self._index_office(ext, bin_data)

        return super(IrAttachment, self)._index(bin_data, datas_fname, mimetype)
