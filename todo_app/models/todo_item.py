from odoo import fields, models


class TodoItem(models.Model):
    """
    Model untuk menyimpan To-Do Item.

    _name:
        Technical name model baru.

    _description:
        Deskripsi model yang digunakan dalam metadata Odoo.

    _order:
        Urutan default record saat dibaca tanpa ordering lain.
    """

    _name = "todo.item"
    _description = "To-Do Item"
    _order = "id desc"

    # =====================================
    # Description
    # =====================================

    # OPSI 1 (DIPAKAI):
    # Char cocok untuk deskripsi singkat, satu baris.
    description = fields.Char(
        string="Description",
        required=True,
        help="Describe the task to be completed.",
    )

    # OPSI 2:
    # Text cocok untuk deskripsi panjang dan multiline.
    #
    # description = fields.Text(
    #     string="Description",
    #     required=True,
    # )

    # OPSI 3:
    # Html digunakan jika perlu rich-text editor.
    # Untuk data yang hanya berupa tugas singkat,
    # kompleksitas ini belum diperlukan.
    #
    # description = fields.Html(
    #     string="Description",
    #     sanitize=True,
    # )

    # =====================================
    # Completion Status
    # =====================================

    # OPSI 1 (DIPAKAI):
    # Semua tugas baru dianggap belum selesai.
    is_done = fields.Boolean(
        string="Is Done?",
        default=False,
        help="Mark this task as completed.",
    )

    # OPSI 2:
    # Tidak menuliskan default.
    # Boolean yang belum diberi nilai akan bernilai False.
    #
    # is_done = fields.Boolean(
    #     string="Is Done?",
    # )

    # =====================================
    # Work Team
    # =====================================

    # Many2many memungkinkan satu tugas mempunyai
    # beberapa Contact sebagai anggota Work Team.
    #
    # Satu Contact juga bisa tergabung dalam banyak tugas.

    work_team_ids = fields.Many2many(
        comodel_name="res.partner",
        relation="todo_item_res_partner_rel",
        column1="todo_item_id",
        column2="partner_id",
        string="Work Team",
        domain=[("is_work_team", "=", True)],
        help="Select contacts marked as Work Team members.",
    )

    # OPSI 2:
    # Many2many menggunakan positional arguments.
    # Hasilnya setara dengan konfigurasi di atas.
    #
    # work_team_ids = fields.Many2many(
    #     "res.partner",
    #     "todo_item_res_partner_rel",
    #     "todo_item_id",
    #     "partner_id",
    #     string="Work Team",
    #     domain=[("is_work_team", "=", True)],
    # )

    # OPSI 3:
    # Biarkan ORM menentukan nama relation table.
    # Lebih singkat, tetapi kurang eksplisit.
    #
    # work_team_ids = fields.Many2many(
    #     "res.partner",
    #     string="Work Team",
    #     domain=[("is_work_team", "=", True)],
    # )