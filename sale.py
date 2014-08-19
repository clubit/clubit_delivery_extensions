from openerp.osv import osv
from openerp.tools.translate import _

class sale_order(osv.Model):
    _name = "sale.order"
    _inherit = "sale.order"


    ''' sale.order:_prepare_order_picking()
        -----------------------------------
        This method is extended to make sure the Sales Order reference is
        chained during the automated Delivery Order creation. This automated
        creation happens in the sale.order:__create_pickings_and_procurements()
        method.
        ----------------------------------------------------------------------- '''
    def _prepare_order_picking(self, cr, uid, order, context=None):

        result = super(sale_order,self)._prepare_order_picking(cr, uid, order, context)
        result['incoterm'] = order.incoterm.id
        result['instruction1'] = order.partner_id.instruction1
        result['instruction2'] = order.partner_id.instruction2
        return result