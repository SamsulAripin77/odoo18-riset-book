from odoo import fields, models


class ResPartner(models.Model):
    """
    Extend the existing Contact model.

    models.Model:
        Base class ORM untuk persistent model.

    _inherit:
        Memperluas model yang sudah tersedia.

    res.partner:
        Technical name model Contacts bawaan Odoo.
    """

    _inherit = "res.partner"

    # OPSI 1 (DIPAKAI):
    # Field Boolean dengan label eksplisit.
    is_work_team = fields.Boolean(
        string="Is Work Team?",
        default=False,
        help="Enable this contact as a To-Do work team member.",
    )

    # OPSI 2:
    # Deklarasi paling sederhana.
    # Odoo bisa membuat label otomatis dari nama field.
    #
    # is_work_team = fields.Boolean()

    # OPSI 3:
    # Jika status perlu dihitung dari data lain.
    # Ini hanya contoh alternatif, bukan implementasi kita.
    #
    # is_work_team = fields.Boolean(
    #     string="Is Work Team?",
    #     compute="_compute_is_work_team",
    #     store=True,
    # )