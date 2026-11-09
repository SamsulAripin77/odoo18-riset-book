{
    # Nama yang akan terlihat pada daftar Apps Odoo.
    "name": "To-Do App",

    # Versi modul, bukan versi Python.
    # Konvensi yang digunakan: versi Odoo + versi modul.
    "version": "18.0.1.0.0",

    # Ringkasan yang terlihat pada informasi aplikasi.
    "summary": "Personal To-Do List with Work Team",

    "description": """
        To-Do application for learning Odoo 18 development.
        Adapted from Odoo 15 Development Essentials.
    """,

    "author": "Samsul Aripin",

    # Kategori modul di Apps.
    "category": "Productivity",

    # LGPL-3 merupakan salah satu lisensi yang didukung Odoo.
    "license": "LGPL-3",

    # OPSI 1 (DIPAKAI):
    # Dependensi pada base dan Contacts.
    # Modul contacts memastikan aplikasi Contacts tersedia.
    "depends": ["base", "contacts"],

    # OPSI 2:
    # Gunakan ini jika hanya membutuhkan model res.partner
    # dan tidak perlu aplikasi Contacts secara eksplisit.
    # "depends": ["base"],

    # Odoo memproses file berikut secara berurutan.
    # External ID yang direferensikan harus sudah tersedia.
    "data": [
        # 1. Group dan Record Rule
        "security/todo_security.xml",

        # 2. Izin akses model
        "security/ir.model.access.csv",

        # 3. Tampilan To-Do dan Window Action
        "views/todo_item_views.xml",

        # 4. Menu menggunakan Action dari file sebelumnya
        "views/todo_menu.xml",

        # 5. Ekstensi tampilan Contacts
        "views/res_partner_views.xml",
    ],

    # False berarti modul tidak bisa diinstal.
    "installable": True,

    # True membuat modul dikategorikan sebagai aplikasi.
    "application": True,

    # True berarti modul otomatis diinstal jika
    # seluruh dependencies terpenuhi.
    # Kita sengaja memilih False untuk instalasi manual.
    "auto_install": False,
}