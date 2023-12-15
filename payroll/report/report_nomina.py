from odoo import api, models


class PayslipDetailsReport(models.AbstractModel):
    _name = "report.payroll.report_nomina_document"
    _description = "Nomina full report"

    @api.model
    def _get_report_values(self, docids, data=None):
        payslips = self.env["hr.payslip.run"].browse(docids)
        return {
            "doc_ids": docids,
            "doc_model": "hr.payslip.run",
            "docs": payslips,
            "data": data
        }