{
    'name': "Library",
    'summary': "Módulo relaciona a Produtos",
    'author':  "Vinicius Miranda",
    "contributors": [
    ],
    'website': "",
    'category': 'Uncategorized',
    'version': '16.0',
    'depends': ['base'],
    'data': [
        "security/groups.xml",
        "security/ir.model.access.csv",
        "views/library_book.xml",
        "views/res_partner.xml",
        "views/library_member.xml",
        "views/library_book_categ.xml",
        ],
    'installable': True,
    'application': True,
}