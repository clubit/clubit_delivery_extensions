from openerp.osv import osv, fields
from openerp.tools.translate import _

class stock_picking(osv.Model):
    _name = "stock.picking"
    _inherit = "stock.picking"
    _description = "Delivery extensions"
    _columns = {
        'incoterm': fields.many2one('stock.incoterms', 'Incoterm', help="International Commercial Terms are a series of predefined commercial terms used in international transactions."),
        'crossdock_overrule': fields.selection([('yes','Yes'), ('no','No')], 'Crossdock Overrule'),
        'groupage_overrule': fields.selection([('yes','Yes'), ('no','No')], 'Groupage Overrule'),
        'instruction1': fields.char('Instruction 1', size=64),
        'instruction2': fields.char('Instruction 2', size=64),
    }

class stock_picking_out(osv.Model):
    _name = "stock.picking.out"
    _inherit = "stock.picking.out"
    _description = "Delivery extensions"
    _columns = {
        'incoterm': fields.many2one('stock.incoterms', 'Incoterm', help="International Commercial Terms are a series of predefined commercial terms used in international transactions."),
        'crossdock_overrule': fields.selection([('yes','Yes'), ('no','No')], 'Crossdock Overrule'),
        'groupage_overrule': fields.selection([('yes','Yes'), ('no','No')], 'Groupage Overrule'),
        'instruction1': fields.char('Instruction 1', size=64),
        'instruction2': fields.char('Instruction 2', size=64),
    }

class stock_move(osv.Model):
    _name = "stock.move"
    _inherit = "stock.move"
    _description = "Delivery Move extensions"
    _columns = {
        'status_code': fields.char('Status Code', size=64),
        'storage_location': fields.selection([('0','Available'), ('B','Back To Back'), ('V','New Product Version'), ('Q','Quality Control')], 'Storage Location'),
        'edi_sequence': fields.char('Sequence', size=6, help="EDI sequence order."),
    }

    _defaults = {
      'storage_location': '0',
    }

