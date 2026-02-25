# -*- coding: utf-8 -*-
from odoo import models, api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    def _rollup_bom_sale_price_from_components(self):
        """
        Επαναϋπολογίζει τις Sales Prices όλων των προϊόντων που έχουν
        ΤΑ ΣΥΓΚΕΚΡΙΜΕΝΑ προϊόντα ως components στα BoMs τους.
        Χρησιμοποιεί lst_price (sales price) των product.product (variants)
        και γράφει το άθροισμα στο list_price του parent template.
        """
        BomLine = self.env["mrp.bom.line"]
        visited_templates = self.env["product.template"]
        to_process = self

        while to_process:
            tmpl = to_process[0]
            to_process = to_process[1:]

            if tmpl in visited_templates:
                continue
            visited_templates |= tmpl

            # Όλοι οι variants του template
            variant_ids = tmpl.product_variant_ids.ids
            if not variant_ids:
                continue

            # BoM lines όπου οι variants είναι components
            bom_lines = BomLine.search([("product_id", "in", variant_ids)])
            parent_boms = bom_lines.mapped("bom_id")

            parent_templates = self.env["product.template"]
            for bom in parent_boms:
                # Parent template: είτε product_tmpl_id είτε από product_id
                parent_tmpl = bom.product_tmpl_id or (
                    bom.product_id and bom.product_id.product_tmpl_id
                )
                if not parent_tmpl:
                    continue

                # Υπολογισμός τιμής: άθροισμα (lst_price component * qty)
                total = 0.0
                for line in bom.bom_line_ids:
                    component = line.product_id
                    qty = line.product_qty or 0.0
                    # lst_price = Sales Price σε product.product [web:39][web:40]
                    price = component.lst_price or 0.0
                    total += price * qty

                # Γράφουμε τη νέα τιμή στον parent template
                # με context για να ΜΗΝ ξαναμπεί στο write‑trigger.
                parent_tmpl.with_context(skip_bom_price_rollup=True).write(
                    {"list_price": total}
                )

                parent_templates |= parent_tmpl

            # Συνέχισε αναδρομικά στους parent templates
            to_process |= parent_templates

    def write(self, vals):
        # Αρχικά κανονικό write
        res = super().write(vals)

        # Αν άλλαξε Sales Price (list_price) και ΔΕΝ τρέχουμε ήδη από rollup,
        # τότε ξεκινάμε τον επαναϋπολογισμό προς τα "πάνω".
        if (
            "list_price" in vals
            and not self.env.context.get("skip_bom_price_rollup")
        ):
            self._rollup_bom_sale_price_from_components()

        return res
