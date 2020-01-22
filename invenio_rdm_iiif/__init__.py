# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 Data Futures.
#
# Invenio RDM IIIF is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Full IIIF support for InvenioRDM"""

from __future__ import absolute_import, print_function

from .ext import InvenioRDMIIIF
from .version import __version__

__all__ = ('__version__', 'InvenioRDMIIIF')
