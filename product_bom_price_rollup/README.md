# MRP Auto Merge by Product

Module for Odoo 17 that automatically updates the **Sales Price** of
products based on the sales prices of their Bill of Materials (BoM)
components.

## Features

- When the sales price of any product or variant changes,
  all parent products that use it as a BoM component have
  their Sales Price recalculated.
- The new Sales Price of a parent product is the sum of  
  `component_price * component_quantity` for all its BoM lines.
- Supports multi-level BoMs (price changes are propagated
  upwards through all parent products).
- Works with BoMs of type *Kit* and *Manufacture*.

## Installation

1. Copy the folder `mrp_auto_merge_by_product` into your Odoo
   `custom_addons` directory.
2. Restart the Odoo server.
3. Activate **Developer Mode**.
4. Go to **Apps**, click **Update Apps List**.
5. Search for **MRP Auto Merge by Product** and install it.

## Usage

- Change the **Sales Price** of any product or variant.
- All products that contain this product as a BoM component
  will automatically get their Sales Price updated to reflect
  the new component prices.

## Compatibility

- Odoo 17 Community / Enterprise.

## License

This module is licensed under the **LGPL-3.0** license.
See the `LICENSE` file for details.
