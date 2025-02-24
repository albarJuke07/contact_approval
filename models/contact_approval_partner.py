from odoo import models, fields, api

class ContactApprovalPartner(models.Model):
    _inherit = 'res.partner'
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('cancel', 'Cancel'),
    ], default='draft')
    approver_id = fields.Many2one('res.users', string='Approved By', readonly=True)
    
    def action_approve(self):
      for rec in self:
        rec.approver_id = self.env.user
        rec.state = 'approved'
    
    def action_cancel(self):
      for rec in self:
        rec.approver_id = self.env.user
        rec.state = 'cancel'
    
    def action_reset(self):
      for rec in self:
        rec.approver_id = False
        rec.state = 'draft'