# -*- coding: utf-8 -*-
from odoo import models


class ProductProduct(models.Model):
    _inherit = "product.product"

    def write(self, vals):
        # Κρατάμε τα templates πριν το write
        templates = self.mapped("product_tmpl_id")
        res = super().write(vals)

        # Αν άλλαξε lst_price (Sales Price σε product.product) και
        # δεν είμαστε ήδη μέσα σε rollup, τρέχουμε rollup στα templates.
        if (
            "lst_price" in vals
            and not self.env.context.get("skip_bom_price_rollup")
            and templates
        ):
            templates._rollup_bom_sale_price_from_components()

        return res
