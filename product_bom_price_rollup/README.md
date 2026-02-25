============================
MRP Auto Merge by Product
============================

Automatic Sales Price roll-up from BoM components for Odoo 17.

.. contents::
   :local:

Overview
========

This module automatically updates the *Sales Price* of products
based on the sales prices of their Bill of Materials (BoM)
components.

Whenever the sales price of any BoM component changes, all parent
products that use this component have their Sales Price
recalculated. Price changes are propagated through multi-level BoMs
so that complex assemblies always reflect the latest component
prices.

Key Features
============

* Automatic roll-up of Sales Price from BoM components.
* Triggered on price changes of products and variants.
* Parent Sales Price = sum of ``component_price * component_qty``
  for all BoM lines.
* Supports multi-level BoMs (recursive update of all parents).
* Works with BoMs of type **Kit** and **Manufacture**.
* No extra buttons or cron jobs required.

Usage
=====

1. Configure BoMs for your finished products (type *Kit* or
   *Manufacture*).
2. Ensure all component products (and variants) have a Sales Price.
3. Change the Sales Price of any component product in the Product
   form view.
4. Save the record. All parent products that use this component
   will automatically get an updated Sales Price equal to the sum of
   their components' prices multiplied by the corresponding
   quantities.
5. For multi-level assemblies, higher-level products are updated
   transitively.

Configuration
=============

No additional configuration is required.

If needed, the module can be extended to:

* Use cost price (``standard_price``) instead of Sales Price.
* Apply a margin on top of the computed amount.
* Restrict the behavior to specific BoM types or product categories.

Technical Information
=====================

* Inherits from ``product.template`` and ``product.product``.
* Hooks into the ``write`` method to listen for price changes.
* Searches all ``mrp.bom.line`` entries where the product is used as
  a component.
* Recomputes and writes the parent template Sales Price.
* Uses context flags and a visited set to avoid infinite recursion
  and redundant computations.

Compatibility
=============

* Odoo 17 Community
* Odoo 17 Enterprise

Other Odoo versions are not officially supported and may require
adjustments.

License
=======

This module is licensed under the **LGPL-3.0** license.

See the ``LICENSE`` file at the root of the repository for the full
license text.
