{
    "name": "User Roles: Warehouse Restriction",
    "summary": "Restrict stock levels visible to a role to selected warehouses",
    "version": "19.0.1.0.0",
    "category": "Tools",
    "author": "Maksym Koriahin",
    "license": "LGPL-3",
    "depends": ["base_user_role", "stock", "mrp_company_setup"],
    "data": [
        "security/stock_security.xml",
        "views/res_users_role_views.xml",
        "data/res_users_role_data.xml",
    ],
    "installable": True,
}
