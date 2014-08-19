from openerp.osv import osv, fields
from openerp.tools.translate import _

class res_partner(osv.Model):
    _name = "res.partner"
    _inherit = "res.partner"
    _columns = {
        'instruction1': fields.char('Instruction 1', size=64),
        'instruction2': fields.char('Instruction 2', size=64),
    }
