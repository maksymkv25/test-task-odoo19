INITIAL_STOCK = [
    ("product_component_1", "warehouse_k1", 100),
    ("product_component_2", "warehouse_k1", 200),
    ("product_component_3", "warehouse_k2", 150),
    ("product_component_4", "warehouse_k2", 50),
]


def post_init_hook(env):
    """Put initial quantities on stock via inventory adjustments and bind the BoM to K1."""
    for product_ref, warehouse_ref, qty in INITIAL_STOCK:
        product = env.ref(f"mrp_company_setup.{product_ref}")
        warehouse = env.ref(f"mrp_company_setup.{warehouse_ref}")
        env["stock.quant"].with_context(inventory_mode=True).create(
            {
                "product_id": product.id,
                "location_id": warehouse.lot_stock_id.id,
                "inventory_quantity": qty,
            }
        ).action_apply_inventory()

    env.ref("mrp_company_setup.bom_product_1").picking_type_id = env.ref(
        "mrp_company_setup.warehouse_k1"
    ).manu_type_id
