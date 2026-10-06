from odoo.tests import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestQuantVisibility(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.shop_manager = cls.env.ref("mrp_company_setup.user_shop_manager")
        cls.admin = cls.env.ref("base.user_admin")
        cls.wh_k1 = cls.env.ref("mrp_company_setup.warehouse_k1")
        cls.wh_k2 = cls.env.ref("mrp_company_setup.warehouse_k2")
        cls.component_3 = cls.env.ref("mrp_company_setup.product_component_3")

    def _visible_warehouses(self, user):
        quants = self.env["stock.quant"].with_user(user).search(
            [("location_id.usage", "=", "internal")]
        )
        return quants.location_id.warehouse_id

    def test_shop_manager_sees_only_k1(self):
        self.assertEqual(self._visible_warehouses(self.shop_manager), self.wh_k1)
        self.assertEqual(self.component_3.with_user(self.shop_manager).qty_available, 0)

    def test_admin_sees_all(self):
        warehouses = self._visible_warehouses(self.admin)
        self.assertIn(self.wh_k1, warehouses)
        self.assertIn(self.wh_k2, warehouses)
        self.assertEqual(self.component_3.with_user(self.admin).qty_available, 150)

    def test_role_without_warehouses_is_unrestricted(self):
        self.env.ref("mrp_company_setup.role_shop_manager").warehouse_ids = False
        self.assertIn(self.wh_k2, self._visible_warehouses(self.shop_manager))
