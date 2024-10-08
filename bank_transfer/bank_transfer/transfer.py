import frappe
import json
from frappe.model.document import Document


class Transfer(Document):
    @frappe.whitelist(allow_guest=True)
    def create_transfer(self):
        try:
            json=frappe.request.get_json()
        except Exception as e:
            frappe.throw("Inavlid json")
            
        payeeId= json.get_data('payeeId') 
        bankAccountNumber=json.get_data('bankAccountNumber')
        amount=json.get_data('amount')
        notes=json.get_data('notes')
        customerRefId=json.get_data('customerRefId')
        purpose=json.get_data('purpose')
        transferType=json.get_data('transferType')
        
        self.validate()
        self.check_payeeId()
        self.Transfer_type()
        self.check_notes()
        doc=frappe.new_doc('Transfer')
        doc.payeeId=payeeId
        doc.bankAccountNumber=bankAccountNumber
        doc.amount=amount
        doc.customerRefId=customerRefId
        doc.purpose=purpose
        doc.transferType=transferType
        doc.save()
        frappe.local.response["http_status_code"] = 201
               
    def validate(self):  
        if  not payeeId:
            frappe.throw("Payment Id is Mandatory")                 
        if not bankAccountNumber:
            frappe.throw("Bank Account is Mandatory")
        if not amount and amount<=0:
            frappe.throw("Enter a valid amount")
            
    def check_payeeId(self):
        if frappe.db.exists("Transfer", {"payeeId": payeeId}):
            frappe.throw("Payment Id already exist")
            
    def Transfer_type(self):
        if transferType=="IMPS":
            if  notes.get('subscription') is None:
                frappe.throw("subscription is manditatory")
                
    def check_notes(self):
        if len(notes)>15:
            frappe.throw("maximum 15 other details")
        for i in notes:
            if len(notes[i])>256:
                frappe.throw("Limit exceeded")
                                
                 
                         
                