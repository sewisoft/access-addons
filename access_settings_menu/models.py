from odoo import models, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def fields_get(self, fields=None, attributes=None):
        """ If an addon is already installed, set it to readonly as
        res.config.installer doesn't handle uninstallations of already
        installed addons
        """
        return super(ResUsers, self.sudo()).fields_get(fields, attributes=attributes)
