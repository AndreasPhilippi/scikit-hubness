# -*- coding: utf-8 -*-
# SPDX-License-Identifier: BSD-3-Clause
# Author: Roman Feldbauer
from logging import warning
from tempfile import mkstemp, NamedTemporaryFile

__all__ = ['create_tempfile_preferably_in_dir']


def create_tempfile_preferably_in_dir(suffix=None, prefix=None, directory=None, persistent: bool = False, ):
    """ Create a temporary file with precedence for directory if possible, in TMP otherwise.
    For example, this is useful to try to save into /dev/shm.
    """
    temp_file = mkstemp if persistent else NamedTemporaryFile
    try:
        handle = temp_file(suffix=suffix, prefix=prefix, dir=directory)
    except FileNotFoundError:
        handle = temp_file(suffix=suffix, prefix=prefix, dir=None)
        warning(f'Could not create temp file in {directory}. '
                f'Instead, the path is {handle}.')
    try:
        path = handle.name
    except AttributeError:
        _, path = handle
    return path
