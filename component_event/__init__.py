# -*- coding: utf-8 -*-
from . import components
from . import core
from . import models
# allow public API 'from odoo.addons.component_event import skip_if'
from .components.event import skip_if  # noqa
