from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    role_warehouse_ids = fields.Many2many(
        comodel_name="stock.warehouse",
        string="Role Warehouses",
        compute="_compute_role_warehouse_ids",
        compute_sudo=True,
        help="Warehouses allowed by the user's enabled roles. Empty means no restriction.",
    )

    @api.depends("role_line_ids.role_id.warehouse_ids")
    def _compute_role_warehouse_ids(self):
        for user in self:
            user.role_warehouse_ids = user._get_enabled_roles().role_id.warehouse_ids
