{
    # App information
    'name': "Odoo Magento 2 Connector",
    'version': '14.0.7.2',
    'category': 'Sales',
    'license': 'OPL-1',
    'summary': 'Odoo Magento 2 Connector helps you integrate your Magento 2.x website with Odoo '
               'and automates various operations between Odoo and Magento.',
    # Author
    'author': 'Emipro Technologies Pvt. Ltd.',
    'website': 'http://www.emiprotechnologies.com/',
    'maintainer': 'Emipro Technologies Pvt. Ltd.',

    # Dependencies
    'depends': ['common_connector_library'],
    # Views
    'data': [
        'security/security.xml',
        'data/import_order_status.xml',
        'views/common_log_book_ept.xml',
        'views/magento_instance_view.xml',
        'views/magento_website_view.xml',
        'views/magento_storeview_view.xml',
        'views/magento_inventory_locations_view.xml',
        'views/magento_payment_method_view.xml',
        'views/delivery_carrier_view.xml',
        'views/view_magento_process_log.xml',
        'wizard_views/magento_import_export_operation_view.xml',
        'wizard_views/magento_cron_configuration_view.xml',
        'wizard_views/res_config_magento_instance.xml',
        'wizard_views/res_config_settings.xml',
        'data/ir_sequence_data.xml',
        'views/magento_product_product_view.xml',
        'views/magento_product_template_view.xml',
        'views/magento_product_image_view.xml',
        'wizard_views/magento_queue_process_wizard_view.xml',
        'views/res_partner_view.xml',
        'views/sale_order_view.xml',
        'views/sale_order_cancel_view.xml',
        'views/magento_order_data_queue_ept.xml',
        'views/magento_order_data_queue_line_ept.xml',
        'views/sync_import_magento_product_queue.xml',
        'views/sync_import_magento_product_queue_line.xml',
        'data/magento_data_cron.xml',
        'data/ir_cron_data.xml',
        'views/stock_picking_view.xml',
        'views/account_move_view.xml',
        'views/magento_dashboard_view.xml',
        'views/financial_status_view.xml',
        'views/magento_delivery_carrier.xml',
        'views/magento_instances_onboarding_panel_view.xml',
        'wizard_views/magento_instance_configuration_wizard.xml',
        'wizard_views/basic_configuration_onboarding.xml',
        'wizard_views/financial_status_onboarding_view.xml',
        'wizard_views/magento_onboarding_confirmation_ept.xml',
        'data/ecommerce_data.xml',
        'security/ir.model.access.csv',
        'data/update_magento_partner.xml'
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],

    # Odoo Store Specific

    'images': ['static/description/Magento-2-v14.png'],
    'installable': True,
    'auto_install': False,
    'application': True,
    'live_test_url': 'https://www.emiprotechnologies.com/free-trial?app=odoo-magento2-ept&version=14',
    'price': 379.00,
    'currency': 'EUR',

}
