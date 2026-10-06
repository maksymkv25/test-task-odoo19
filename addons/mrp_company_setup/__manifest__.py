{
    "name": "Manufacturing Company Setup",
    "summary": "Warehouses K1/K2, components with initial stock, shop manager role",
    "version": "19.0.1.0.0",
    "category": "Manufacturing",
    "author": "maksym",
    "license": "LGPL-3",
    "depends": ["stock", "mrp", "base_user_role"],
    "data": [
        "data/stock_warehouse_data.xml",
        "data/product_data.xml",
        "security/user_role_data.xml",
    ],
    "post_init_hook": "post_init_hook",
    "installable": True,
}
