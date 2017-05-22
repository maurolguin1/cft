# coding=utf-8
##############################################################################
#
#    account_auto_fy_sequence module for Odoo
#    Copyright (C) 2014 ACSONE SA/NV (<http://acsone.eu>)
#    @author Stéphane Bidoul <stephane.bidoul@acsone.eu>
#
#    account_auto_fy_sequence is free software:
#    you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License v3 or later
#    as published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    account_auto_fy_sequence is distributed
#    in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License v3 or later for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    v3 or later along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    sales_invoice_percent_ids = fields.One2many(
        'sales.invoice.percent', 'company_ids',
        string='Salesperson Invoice Percent',
    )
    teams_invoice_percent_ids = fields.One2many(
        'teams.invoice.percent', 'company_ids',
        string='Sales Teams Invoice Percent',
    )
    sales_kpi_pass = fields.Float(
        string='Passed',
    )
    sales_kpi_fail = fields.Float(
        string='Failed',
    )
    teams_kpi_pass = fields.Float(
        string='Passed',
    )
    teams_kpi_fail = fields.Float(
        string='Failed',
    )
