# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import io
import logging
import PyPDF2
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

        result = subprocess.run(['pdftotext', filename, '-'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self._delete_file(filename)
        return result.stdout.decode('utf-8')

    def _index_office(self, ext, bin_data):

        tmp_filename = self._get_temp_filename()
        in_filename = tmp_filename + "." + ext.lower()
        out_filename = tmp_filename + '.txt'
        self._save_buffer_to_file(bin_data, in_filename)

        result = subprocess.run(['soffice', '--headless', '--convert-to', 'txt', '--outdir', tempfile._get_default_tempdir() , in_filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = subprocess.run(['cat', out_filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self._delete_file(in_filename)
        self._delete_file(out_filename)
        return result.stdout.decode('utf-8')

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
        filename, file_extension = os.path.splitext(datas_fname)
        ext = file_extension[1:].upper()
        if ext == 'PDF':
            return self._index_pdf(bin_data)

        if ext in FTYPES:
            return self._index_office(ext, bin_data)

        return "oldd" + super(IrAttachment, self)._index(bin_data, datas_fname, mimetype)
