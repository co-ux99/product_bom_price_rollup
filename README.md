# MRP Auto Merge by Product

Odoo 17 module that automatically updates the **Sales** Price of products
based on the sales prices of their Bill of Materials (BoM) components.

---

## Overview

When the sales price of any BoM component changes, this module
recalculates the Sales Price of all parent products that use it in
their BoMs.  
Price changes are propagated through multi‑level BoMs so that complex
assemblies always reflect the latest component prices.

---

## Features

- Automatic roll‑up of Sales Price from BoM components.
- Triggered whenever the Sales Price of a product or variant changes.
- New Sales Price of a parent product equals the sum of  
  `component_price * component_quantity` for all BoM lines.
- Supports multi‑level BoMs (recursively updates all parent products).
- Works with BoMs of type *Kit* and *Manufacture*.
- No extra buttons or cron jobs required; runs transparently on price
  changes.

---

## Technical details

- Inherits from `product.template` and `product.product`.
- Listens to `write` on price fields and searches all `mrp.bom.line`
  records where the product is used as a component.
- For each affected `mrp.bom`, the module recomputes the total Sales
  Price and writes it back to the parent product template.
- Uses a visited‑set and context flags to avoid infinite recursion and
  duplicate computations.

---

## Installation

1. Download this repository or the latest tagged release.
2. Copy the `product_bom_price_rollup` folder into your Odoo
   `custom_addons` directory.
3. Restart the Odoo server.
4. Activate **Developer** Mode in Odoo.
5. Go to **Apps** → click **Update Apps List**.
6. Search for **MRP Auto Merge by Product** and install the module.

---

## Usage

1. Ensure your finished products have BoMs defined (type *Kit* or
   *Manufacture*) and that each component has a Sales Price set.
2. Change the Sales Price of any component product or variant from the
   standard Odoo Product form.
3. After saving, open any parent product that uses this component in
   a BoM:
   - Its Sales Price will have been updated automatically to the sum of
     `component_price * quantity` for all BoM components.
4. For multi‑level assemblies, repeat the check on higher‑level
   products; their prices are also updated transitively.

No additional configuration is required.  
If needed, the module can be extended to work with cost price
(`standard_price`) or to apply a margin on top of the computed amount.

---

## Compatibility

- Odoo 17 Community
- Odoo 17 Enterprise

Other versions of Odoo are not officially supported but may work with
minor adjustments.

---

## Development & contributions

Issues, suggestions and pull requests are welcome.  
When opening an issue, please include:

- Odoo edition and version.
- Exact module version tag (for example `v17.0.1.0.0`).
- Steps to reproduce the problem and expected behavior.
- Any relevant logs or stack traces.

---

## License

This module is licensed under the **LGPL‑3.0** (GNU Lesser General
Public License v3.0).  
See the `LICENSE` file in this repository for the full license text.
