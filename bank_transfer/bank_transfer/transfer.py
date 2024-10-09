import frappe
import json
from frappe.model.document import Document


class Transfer(Document):
    def __init__(self,payeeId,bankAccountNumber,amount,customerRefId,purpose,transferType,notes):
        self.payeeId=payeeId
        self.bankAccountNumber=bankAccountNumber
        self.amount=amount
        self.customerRefId=customerRefId
        self.purpose=purpose
        self.transferType=transferType
        self.notes=notes
        
    def transfer(self):    
        self.validate()
        self.check_payeeId()
        self.Transfer_type()
        self.check_notes()
        doc=frappe.new_doc('Transfer')
        doc.payeeId=self.payeeId
        doc.bankAccountNumber=self.bankAccountNumber
        doc.amount=sellf.amount
        doc.customerRefId=self.customerRefId
        doc.purpose=self.purpose
        doc.transferType=self.transferType
        doc.save()
        frappe.local.response["http_status_code"] = 201
               
    def validate(self):  
        if  not self.payeeId:
            frappe.throw("Payment Id is Mandatory")                 
        if not self.bankAccountNumber:
            frappe.throw("Bank Account is Mandatory")
        if not self.amount and self.amount<=0:
            frappe.throw("Enter a valid amount")
            
    def check_payeeId(self):
        if frappe.db.exists("Transfer", {"payeeId": self.payeeId}):
            frappe.throw("Payment Id already exist")
            
    def Transfer_type(self):
        if self.transferType=="IMPS":
            if  self.notes.get('subscription') is None:
                frappe.throw("subscription is manditatory")
                
    def check_notes(self):
        if len(self.notes)>15:
            frappe.throw("maximum 15 other details")
        for i in self.notes:
            if len(self.notes[i])>256:
                frappe.throw("Limit exceeded")

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
    transfer=Transfer(
    payee_id=payee_id,
    bank_account_number=bank_account_number,
    amount=amount,
    customer_ref_id=customer_ref_id,
    purpose=purpose,
    transfer_type=transfer_type,
    notes=notes)
    transfer.transfer()
                                    
                
                        
                