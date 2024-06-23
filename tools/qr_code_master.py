# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
import qrcode


class QrCodeMaster:

    def __init__(self):
        self._qr = qrcode

    def create_qr_code_file(self, data, file_name):
        img = self._qr.make(data)
        img.save(file_name)
