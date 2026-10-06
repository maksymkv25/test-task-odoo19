from odoo import api, fields, models


class ResUsersRole(models.Model):
    _inherit = "res.users.role"

    warehouse_ids = fields.Many2many(
        comodel_name="stock.warehouse",
        relation="res_users_role_warehouse_rel",
        column1="role_id",
        column2="warehouse_id",
        string="Allowed Warehouses",
        help="Users with this role see stock levels of these warehouses only. "
        "Leave empty for no restriction.",
    )

    def write(self, vals):
        res = super().write(vals)
        if "warehouse_ids" in vals:
            # Record rule domains are cached per user
            self.env.registry.clear_cache()
        return res


class ResUsersRoleLine(models.Model):
    _inherit = "res.users.role.line"

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        self.env.registry.clear_cache()
        return records

    def write(self, vals):
        res = super().write(vals)
        self.env.registry.clear_cache()
        return res

    def unlink(self):
        res = super().unlink()
        self.env.registry.clear_cache()
        return res
