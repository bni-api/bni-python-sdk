from bnipython.lib.net.httpClient import HttpClient
from bnipython.lib.util.utils import generateBniDirectKey, generateSignature, getTimestamp
from bnipython.lib.util.response import responseBniDirect

class BNIDirect():
    def __init__(self, client):
        self.client = client.config
        self.baseUrl = client.getBaseUrl()
        self.config = client.getConfig()
        self.token = client.getToken()
        self.httpClient = HttpClient()

    def _make_request(self, path, method, timeStamp, payload=None):
        signaturePayload = {**payload, **{ 'timestamp': timeStamp}}
        signature = generateSignature(
            {'body': signaturePayload, 'apiSecret': self.client['apiSecret']}
        )
        bniDirectKey = generateBniDirectKey({
            'corporateId': payload['corporateId'], 
            'userId': payload['userId'], 
            'bniDirectApiKey': self.client['bniDirectApiKey'],
            })
        res = self.httpClient.requestV2BniDirect({
            'method': method,
            'apiKey': self.client['apiKey'],
            'accessToken': self.token,
            'url': f'{self.baseUrl}',
            'path': path,
            'signature': signature.split('.')[2],
            'timestamp': timeStamp,
            'data': payload,
            'bniDirectKey': bniDirectKey
        })
        return responseBniDirect(params={'res': res})

    def createMPNG2BillingID(self, payload=None):
        """
        Create MPN G2 billing ID

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID - Required.
                - userId (str): User ID - Required.
                - npwp (str): NPWP - Required.
                - taxPayerName (str): taxPayerName - Required.
                - taxPayerAddress1 (str): taxPayerAddress(1) - Required.
                - taxPayerAddress2 (str): taxPayerAddress(2) - Optional.
                - taxPayerAddress3 (str): taxPayerAddress(3) - Optional.
                - taxPayerCity (str): taxPayerCity - Required.
                - NOP (str): Tax Object Number(NOP) - Optional.
                - MAPCode (str): MAP/Akun Code - Required.
                - depositTypeCode (str): Deposit Type Code - Required.
                - wajibPungutNPWP (str): Wajib Pungut NPWP - Optional.
                - wajibPungutName (str): Wajib Pungut Name - Optional.
                - wajibPungutAddress1 (str): Wajib Pungut Address (1) - Optional.
                - wajibPungutAddress2 (str): Wajib Pungut Address (2) - Optional.
                - wajibPungutAddress3 (str): Wajib Pungut Address (3) - Optional.
                - participantId (str): Participant ID - Optional.
                - assessmentTaxNumber (str): Assessment Tax Number - Optional.
                - amountCurrency (str): Amount Currency - Required.
                - amount (str): Amount - Required.
                - monthFrom (str): Month (From), e.g. 1-12 - Required.
                - monthTo (str): Month (To), e.g. 1-12 - Required.
                - year (str): year - Required.
                - confirmNumber (str): Confirm Number - Required.
                - traceId (str): Trace ID - Optional.
                - kelurahan (str): kelurahan - Optional.
                - kecamatan (str): kecamatan - Optional.
                - provinsi (str): provinsi - Optional.
                - kota (str): kota - Optional.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/MPNG2/CreateBilling'
        return self._make_request(path, method, timeStamp, payload)

    def inquiryNPWP(self, payload=None):
        """
        inquiry NPWP MPN G2.

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (max 40 characters ) - Required.
                - userId (str): User ID (max 40 characters ) - Required.
                - npwp (str): NPWP (max 15 characters ) - Required.
                - NOP (str): Tax Object Number (NOP) (max 18 characters ) - Optional.
                - MAPCode (str): MAP/Account Code (max 6 characters ) - Required.
                - depositTypeCode (str): Deposit Type Code (max 40 characters ) - Required.
                - currency (str): Currency Code (max 3 characters ) - Required.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/MPNG2/InquiryNPWP'
        return self._make_request(path, method, timeStamp, payload)
    
    def inquiryInHouseAndVABeneficiaryName(self, payload=None):
        """
        Inquiry InHouse and VA Beneficiary Name.

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (max 40 characters ) - Required.
                - userId (str): User ID (max 40 characters ) - Required.
                - accountNo (str): Account No. (max 16 characters ) - Required.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/InHouse/InquiryBeneficiaryName'
        return self._make_request(path, method, timeStamp, payload)
    
    def inquiryLLGRTGSOnlineBenefiacyName(self, payload=None):
        """
        Service untuk melakukan inquiry nama rekening Bank lain (LLG/ RTGS/ Online).

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (max 40 characters ) - Required.
                - userId (str): User ID (max 40 characters ) - Required.
                - beneficiaryAccountNo (str): Beneficiary Account No. (max 16 characters ) - Required.
                - beneficiaryBankCode (str): Beneficiary Bank Code (max 40 characters ) - Required.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/Online/InquiryBeneficiaryName'
        return self._make_request(path, method, timeStamp, payload)
    
    def inquiryAccountStatement(self, payload=None):
        """
        Service untuk melakukan inquiry transaksi dari account.

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (max 40 characters ) - Required.
                - userId (str): User ID (max 40 characters ) - Required.
                - fromDate (str): From Posting Date (yyyyMMdd format, max 8 characters ) - Required.
                - toDate (str): To Posting Date (yyyyMMdd format, max 8 characters ) - Required.
                - transactionType (str): Transaction Type (All, Db (debit), Cr (credit)) - Required.
                - accountList (lists): Account List 
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/Account/InquiryAccountStatement'
        return self._make_request(path, method, timeStamp, payload)
    
    def inquiryBilling(self, payload=None):
        """
        Service untuk melakukan inquiry tagihan (billing) dari institusi yang ada di BNI Direct

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (max 40 characters ) - Required.
                - userId (str): User ID (max 40 characters ) - Required.
                - debitedAccountNo (str): Debited Account (max 16 characters ) - Required.
                - institution (str): Institution (max 40 characters ) - Required.
                - customerInformation1 (str): Customer Information (1) - Required.
                - customerInformation2 (str): Customer Information (2) - Optional.
                - customerInformation3 (str): Customer Information (3) - Optional.
                - customerInformation4 (str): Customer Information (4) - Optional.
                - customerInformation5 (str): Customer Information (5) - Optional.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/Billing/Inquiry'
        return self._make_request(path, method, timeStamp, payload)
    
    def inquiryBNIPopsCashAndCarry(self, payload=None):
        """
        Service untuk melakukan inquiry detail Cash and Carry.

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (max 40 characters ) - Required.
                - userId (str): User ID (max 40 characters ) - Required.
                - debitAccountNo (str): Debited Account (max 16 characters ) - Required.
                - salesOrganizationCode (str): Sales Organization Code (max 40 characters ) - Required.
                - distributionChannelCode (str): Distribution Channel Code (max 40 characters ) - Required.
                - productCode (str): Product Code (max 40 characters ) - Required.
                - shipTo (str): Ship To (max 100 characters ) - Required.
                - debitOrCreditNoteNo (numeric): Debit / Credit Note Number (up to 18 digits) - Optional.
                - productInformationDetail (list of dict): Product Information Detail - Optional. Each object in the array should have its own structure defined.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/BNIPOPS/CashandCarry/Inquiry'
        return self._make_request(path, method, timeStamp, payload)
    
    def inquiryBNIPopsProductAllocation(self, payload=None):
        """
        Service untuk melakukan transaksi Product Allocation.

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (max 40 characters ) - Required.
                - userId (str): User ID (max 40 characters ) - Required.
                - debitAccountNo (str): Debited Account (max 16 characters ) - Required.
                - salesOrganizationCode (str): Sales Organization Code (max 40 characters ) - Required.
                - distributionChannelCode (str): Distribution Channel Code (max 40 characters ) - Required.
                - productCode (str): Product Code (max 40 characters ) - Required.
                - shipTo (str): Ship To (max 100 characters ) - Required.
                - scheduleAgreementNo (str): Schedule Agreement Number (max 100 characters ) - Required.
                - debitOrCreditNoteNo (str): Debit / Credit Note Number (up to max 18 characters ) - Optional.
                - productInformationDetail (list of dict): Product Information Detail - Optional. Each object in the array should have its own structure defined.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/BNIPOPS/ProductAllocation/Inquiry'
        return self._make_request(path, method, timeStamp, payload)
    
    def getPaymentStatus(self, payload=None):
        """
        Service untuk melakukan inquiry Transaction Status dari transaksi yang sudah dilakukan.

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (max 40 characters ) - Required.
                - userId (str): User ID (max 40 characters ) - Required.
                - transactionReferenceNo (str): Transaction Reference No. (max 40 characters ) - Required.
                - remitterReferenceNo (str): Remitter Reference No. (max 16 characters ) - Optional.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/InquiryTransactionStatus'
        return self._make_request(path, method, timeStamp, payload)
    
    def inhouseTransfer(self, payload=None):
        """
        Service untuk melakukan transaksi InHouse Transfer.

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (max 40 characters ) - Required.
                - userId (str): User ID (max 40 characters ) - Required.
                - debitedAccountNo (str): Debited Account No. (max 16 characters ) - Optional.
                - amountCurrency (str): Amount Currency (max 3 characters ) - Required.
                - amount (str): Amount (up to max 15 characters ) - Required.
                - treasuryReferenceNo (str): Treasury Reference No. (max 40 characters ) - Optional.
                - transactionPurposeCode (str): Transaction Purpose Code (max 40 characters ) - Required.
                - remark1 (str): Remark 1 (up to max 40 characters ) - Optional.
                - remark2 (str): Remark 2 (up to max 40 characters ) - Optional.
                - remark3 (str): Remark 3 (up to max 40 characters ) - Optional.
                - remitterReferenceNo (str): Remitter Reference No. (max 16 characters ) - Required.
                - finalizePaymentFlag (str): Finalize Payment Flag (1 character) - Required.
                - beneficiaryReferenceNo (str): Beneficiary Reference No. (max 16 characters ) - Optional.
                - toAccountNo (str): To Account No. (max 16 characters ) - Required.
                - notificationFlag (str): Notification Flag (1 character) - Required.
                - beneficiaryEmail (str): Beneficiary Email (max 100 characters ) - Optional.
                - transactionInstructionDate (str): Transaction Instruction Date (yyyyMMdd format, max 8 characters ) - Required.
                - docUniqueId (str): Unique ID (max 40 characters ) - Optional.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/InHouse/Transfer'
        return self._make_request(path, method, timeStamp, payload)
    
    def LLGTransfer(self, payload=None):
        """
        Service untuk melakukan transaksi LLG Transfer. 

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (max 40 characters ) - Required.
                - userId (str): User ID (max 40 characters ) - Required.
                - debitedAccountNo (str): Debited Account No. (max 16 characters ) - Required.
                - amountCurrency (str): Amount Currency (max 3 characters ) - Required.
                - amount (str): Amount (up to max 15 characters ) - Required.
                - treasuryReferenceNo (str): Treasury Reference No. (max 40 characters ) - Optional.
                - chargeTo (str): Charge To (max 3 characters ) - Required.
                - remark1 (str): Remark 1 (up to max 40 characters ) - Optional.
                - remark2 (str): Remark 2 (up to max 40 characters ) - Optional.
                - remark3 (str): Remark 3 (up to max 40 characters ) - Optional.
                - remitterReferenceNo (str): Remitter Reference No. (max 16 characters ) - Required.
                - finalizePaymentFlag (str): Finalize Payment Flag (1 character) - Required.
                - beneficiaryReferenceNo (str): Beneficiary Reference No. (max 16 characters ) - Optional.
                - beneficiaryAccountNo (str): Beneficiary Account No. (max 34 characters ) - Required.
                - beneficiaryAccountName (str): Beneficiary Account Name (max 70 characters ) - Required.
                - beneficiaryAddress1 (str): Beneficiary Address (1) (max 50 characters ) - Optional.
                - beneficiaryAddress2 (str): Beneficiary Address (2) (max 50 characters ) - Optional.
                - beneficiaryAddress3 (str): Beneficiary Address (3) (max 50 characters ) - Optional.
                - beneficiaryResidentshipCountryCode (str): Beneficiary Residentship Country Code (max 40 characters ) - Required.
                - beneficiaryCitizenshipCountryCode (str): Beneficiary Citizenship Country Code (max 40 characters ) - Required.
                - beneficiaryType (str): Beneficiary Type (max 2 characters ) - Required.
                - beneficiaryBankCode (str): Beneficiary Bank Code (max 40 characters ) - Required.
                - beneficiaryBankName (str): Beneficiary Bank Name (max 100 characters ) - Required.
                - beneficiaryBankBranchCode (str): Beneficiary Bank Branch Code (max 40 characters ) - Optional.
                - beneficiaryBankBranchName (str): Beneficiary Bank Branch Name (max 100 characters ) - Optional.
                - beneficiaryBankCityName (str): Beneficiary Bank City Name (max 100 characters ) - Required.
                - notificationFlag (str): Notification Flag (1 character) - Required.
                - beneficiaryEmail (str): Beneficiary Email (max 100 characters ) - Optional.
                - transactionInstructionDate (str): Transaction Instruction Date (yyyyMMdd format, 8-max 18 characters ) - Required.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/LLG/Transfer'
        return self._make_request(path, method, timeStamp, payload)
    
    def RTGSTransfer(self, payload=None):
        """
        Service untuk melakukan transaksi RTGS Transfer. 

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (max 40 characters ) - Required.
                - userId (str): User ID (max 40 characters ) - Required.
                - debitedAccountNo (str): Debited Account No. (max 3 characters ) - Required.
                - amountCurrency (str): Amount Currency (max 16 characters ) - Required.
                - amount (str): Amount (max 15 characters ) - Required.
                - treasuryReferenceNo (str): Treasury Reference No. (max 40 characters ) - Optional.
                - chargeTo (str): Charge To (max 3 characters ) - Required.
                - remark1 (str): Remark 1 (up to max 40 characters ) - Optional.
                - remark2 (str): Remark 2 (up to max 40 characters ) - Optional.
                - remark3 (str): Remark 3 (up to max 40 characters ) - Optional.
                - remitterReferenceNo (str): Remitter Reference No. (max 16 characters ) - Required.
                - finalizePaymentFlag (str): Finalize Payment Flag (1 character) - Required.
                - beneficiaryReferenceNo (str): Beneficiary Reference No. (max 16 characters ) - Optional.
                - beneficiaryAccountNo (str): Beneficiary Account No. (max 17 characters ) - Required.
                - beneficiaryAccountName (str): Beneficiary Account Name (max 80 characters ) - Required.
                - beneficiaryAddress1 (str): Beneficiary Address (1) (max 50 characters ) - Optional.
                - beneficiaryAddress2 (str): Beneficiary Address (2) (max 50 characters ) - Optional.
                - beneficiaryAddress3 (str): Beneficiary Address (3) (max 50 characters ) - Optional.
                - beneficiaryResidentshipCountryCode (str): Beneficiary Residentship Country Code (max 40 characters ) - Required.
                - beneficiaryCitizenshipCountryCode (str): Beneficiary Citizenship Country Code (max 40 characters ) - Required.
                - beneficiaryBankCode (str): Beneficiary Bank Code (max 40 characters ) - Required.
                - beneficiaryBankName (str): Beneficiary Bank Name (max 100 characters ) - Required.
                - beneficiaryBankBranchCode (str): Beneficiary Bank Branch Code (max 40 characters ) - Optional.
                - beneficiaryBankBranchName (str): Beneficiary Bank Branch Name (max 100 characters ) - Optional.
                - beneficiaryBankCityName (str): Beneficiary Bank City Name (max 100 characters ) - Required.
                - notificationFlag (str): Notification Flag (1 character) - Required.
                - beneficiaryEmail (str): Beneficiary Email (max 100 characters ) - Optional.
                - transactionInstructionDate (str): Transaction Instruction Date (yyyyMMdd format, max 8 characters ) - Required.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/RTGS/Transfer'
        return self._make_request(path, method, timeStamp, payload)
    
    def onlineTransfer(self, payload=None):
        """
        Service untuk melakukan transaksi Domestic Online Transfer. 

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (max 40 characters ) - Required.
                - userId (str): User ID (max 40 characters ) - Required.
                - debitedAccountNo (str): Debited Account No. (max 16 characters ) - Required.
                - amountCurrency (str): Amount Currency (max 3 characters ) - Required.
                - amount (str): Amount (max 15 characters ) - Required.
                - treasuryReferenceNo (str): Treasury Reference No. (max 40 characters ) - Optional.
                - chargeTo (str): Charge To (max 3 characters ) - Required.
                - remark1 (str): Remark 1 (up to max 40 characters ) - Optional.
                - remark2 (str): Remark 2 (up to max 40 characters ) - Optional.
                - remark3 (str): Remark 3 (up to max 40 characters ) - Optional.
                - remitterReferenceNo (str): Remitter Reference No. (max 16 characters ) - Required.
                - finalizePaymentFlag (str): Finalize Payment Flag (1 character) - Required.
                - beneficiaryReferenceNo (str): Beneficiary Reference No. (max 16 characters ) - Optional.
                - beneficiaryAccountNo (str): Beneficiary Account No. (max 17 characters ) - Required.
                - beneficiaryBankCode (str): Beneficiary Bank Code (max 40 characters ) - Required.
                - beneficiaryBankName (str): Beneficiary Bank Name (max 100 characters ) - Required.
                - notificationFlag (str): Notification Flag (1 character) - Required.
                - beneficiaryEmail (str): Beneficiary Email (max 100 characters ) - Optional.
                - transactionInstructionDate (str): Transaction Instruction Date (yyyyMMdd format, max 8 characters ) - Required.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/Online/Transfer'
        return self._make_request(path, method, timeStamp, payload)
    
    def internationalTransfer(self, payload=None):
        """
        Service untuk melakukan transaksi International Transfer. 

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (max 40 characters ) - Required.
                - userId (str): User ID (max 40 characters ) - Required.
                - debitedAccountNo (str): Debited Account No. (max 16 characters ) - Required.
                - amountCurrency (str): Amount Currency (max 3 characters ) - Required.
                - amount (str): Amount (max 15 characters ) - Required.
                - treasuryReferenceNo (str): Treasury Reference No. (max 40 characters ) - Optional.
                - chargeTo (str): Charge To (max 3 characters ) - Required.
                - remark1 (str): Remark 1 (up to max 40 characters ) - Optional.
                - remark2 (str): Remark 2 (up to max 40 characters ) - Optional.
                - remark3 (str): Remark 3 (up to max 40 characters ) - Optional.
                - remitterReferenceNo (str): Remitter Reference No. (max 16 characters ) - Required.
                - finalizePaymentFlag (str): Finalize Payment Flag (1 character) - Required.
                - beneficiaryReferenceNo (str): Beneficiary Reference No. (max 16 characters ) - Optional.
                - beneficiaryAccountNo (str): Beneficiary Account No. (max 17 characters ) - Required.
                - beneficiaryAccountName (str): Beneficiary Account Name (max 80 characters ) - Required.
                - beneficiaryAddress1 (str): Beneficiary Address (1) (max 50 characters ) - Optional.
                - beneficiaryAddress2 (str): Beneficiary Address (2) (max 50 characters ) - Optional.
                - beneficiaryAddress3 (str): Beneficiary Address (3) (max 50 characters ) - Optional.
                - organizationDirectoryCode (str): Organization Directory Code (max 40 characters ) - Required.
                - beneficiaryBankCode (str): Beneficiary Bank Code (max 40 characters ) - Required.
                - beneficiaryBankName (str): Beneficiary Bank Name (max 100 characters ) - Required.
                - beneficiaryBankBranchName (str): Beneficiary Bank Branch Name (max 100 characters ) - Optional.
                - beneficiaryBankAddress1 (str): Beneficiary Bank Address (1) (max 35 characters ) - Optional.
                - beneficiaryBankAddress2 (str): Beneficiary Bank Address (2) (max 35 characters ) - Optional.
                - beneficiaryBankAddress3 (str): Beneficiary Bank Address (3) (max 35 characters ) - Optional.
                - beneficiaryBankCountryName (str): Beneficiary Bank Country Name (max 100 characters ) - Optional.
                - correspondentBankName (str): Correspondent Bank Name (max 100 characters ) - Optional.
                - identicalStatusFlag (str): Identical Status Flag (1 character) - Required.
                - beneficiaryResidentshipCode (str): Beneficiary Residentship Code (max 40 characters ) - Required.
                - beneficiaryCitizenshipCode (str): Beneficiary Citizenship Code (max 40 characters ) - Required.
                - beneficiaryCategoryCode (str): Beneficiary Category Code (max 40 characters ) - Optional.
                - transactorRelationship (str): Transactor Relationship (Affiliated) Flag (1 character) - Required.
                - transactionPurposeCode (str): Transaction Purpose Code (max 40 characters ) - Required.
                - transactionDescription (str): Transaction Description (max 100 characters ) - Optional.
                - notificationFlag (str): Notification Flag (1 character) - Required.
                - beneficiaryEmail (str): Beneficiary Email (max 100 characters ) - Optional.
                - transactionInstructionDate (str): Transaction Instruction Date (yyyyMMdd format, max 8 characters ) - Required.
                - docUniqueId (str): Unique underlying ID (max 40 characters ) - Required if transaction exceeds PIB 18 or WIC limits.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/International/Transfer'
        return self._make_request(path, method, timeStamp, payload)
    
    def billPayment(self, payload=None):
        """
        Service untuk melakukan transaksi Bill Payment dari institusi yang ada di BNI Direct. 

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (max 40 characters ) - Required.
                - userId (str): User ID (max 40 characters ) - Required.
                - debitedAccountNo (str): Debited Account No. (max 16 characters ) - Required.
                - institution (str): Institution (max 40 characters ) - Required.
                - payeeName (str): Payee Name (max 40 characters ) - Required.
                - customerInformation1 (str): Customer Information (1) (max 40 characters ) - Optional.
                - customerInformation2 (str): Customer Information (2) (max 40 characters ) - Optional.
                - customerInformation3 (str): Customer Information (3) (max 40 characters ) - Optional.
                - customerInformation4 (str): Customer Information (4) (max 40 characters ) - Optional.
                - customerInformation5 (str): Customer Information (5) (max 40 characters ) - Optional.
                - billPresentmentFlag (str): Bill Presentment Flag (1 character) - Required.
                - remitterRefNo (str): Remitter Reference No. (max 16 characters ) - Required.
                - finalizePaymentFlag (str): Finalize Payment Flag (1 character) - Required.
                - beneficiaryRefNo (str): Beneficiary Reference No. (max 16 characters ) - Optional.
                - notificationFlag (str): Notification Flag (1 character) - Required.
                - beneficiaryEmail (str): Beneficiary Email (max 100 characters ) - Optional.
                - transactionInstructionDate (str): Transaction Instruction Date (yyyyMMdd format, max 8 characters ) - Required.
                - amountCurrency (str): Amount Currency (max 3 characters ) - Required.
                - amount (str): Amount (max 18 characters ) - Required.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/Billing/Payment'
        return self._make_request(path, method, timeStamp, payload)
    
    def bniPopsCashAndCarry(self, payload=None):
        """
       Service untuk melakukan transaksi Cash and Carry. 

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (max 40 characters ) - Required.
                - userId (str): User ID (max 40 characters ) - Required.
                - debitedAccountNo (str): Debited Account No. (max 16 characters ) - Required.
                - salesOrganizationCode (str): Sales Organization Code (max 40 characters ) - Required.
                - distributionChannelCode (str): Distribution Channel Code (max 40 characters ) - Required.
                - productCode (str): Product Code (max 40 characters ) - Required.
                - shipTo (str): Ship To (max 100 characters ) - Required.
                - debitOrCreditNoteNo (str): Debit / Credit Note Number (max 18 characters ) - Optional.
                - productInformationDetail (list of dict): Product Information Detail - Optional.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/BNIPOPS/CashandCarry/Payment'
        return self._make_request(path, method, timeStamp, payload)
    
    def bniPopsProductAllocation(self, payload=None):
        """
        Service untuk melakukan transaksi Product Allocation.

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (max 40 characters ) - Required.
                - userId (str): User ID (max 40 characters ) - Required.
                - debitedAccountNo (str): Debited Account No. (max 16 characters ) - Required.
                - salesOrganizationCode (str): Sales Organization Code (max 40 characters ) - Required.
                - distributionChannelCode (str): Distribution Channel Code (max 40 characters ) - Required.
                - productCode (str): Product Code (max 40 characters ) - Required.
                - shipTo (str): Ship To (max 100 characters ) - Required.
                - scheduleAggreementNo (str): Schedule Agreement Number (max 100 characters ) - Required.
                - debitOrCreditNoteNo (str): Debit / Credit Note Number (max 18 characters ) - Optional.
                - productInformationDetail (list of dict): Product Information Detail - Optional.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/BNIPOPS/ProductAllocation/Payment'
        return self._make_request(path, method, timeStamp, payload)
    
    def bniPopsResubmitCashAndCarry(self, payload=None):
        """
        Service untuk melakukan Resubmit transaksi Cash and Carry. 

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (max 40 characters) - Required.
                - userId (str): User ID (max 40 characters) - Required.
                - transactionReferenceNo (str): Transaction Reference No. (max 40 characters) - Required.
                - SONumber (str): SO Number (max 40 characters) - Optional.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/BNIPOPS/CashandCarry/Resubmit'
        return self._make_request(path, method, timeStamp, payload)
 
    def bniPopsResubmitProductAllocation(self, payload=None):
        """
        Service untuk melakukan Resubmit transaksi Product Allocation. 

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (max 40 characters) - Required.
                - userId (str): User ID (max 40 characters) - Required.
                - transactionReferenceNo (str): Transaction Reference No. (max 40 characters) - Required.
                - SONumber (str): SO Number (max 40 characters) - Optional.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/BNIPOPS/ProductAllocation/Resubmit'
        return self._make_request(path, method, timeStamp, payload)
    
    def createVirtualAccount(self, payload=None):
        """
        Service untuk melakukan create virtual account.

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (max 40 characters) - Required.
                - userId (str): User ID (max 40 characters) - Required.
                - companyCode (str): Company Code (max 20 characters) - Required.
                - virtualAccountNo (str): Virtual Account No. (variable length) - Required.
                - virtualAccountName (str): Virtual Account Name (max 80 characters) - Required.
                - virtualAccountTypeCode (str): Virtual Account Type Code (max 2 characters) - Required.
                - billingAmount (str): Billing Amount (max 12v2 characters) - Required (conditional).
                - varAmount1 (str): Var Amount 1 (max 12v2 characters) - Required (conditional).
                - varAmount2 (str): Var Amount 2 (max 12v2 characters) - Required (conditional).
                - expiryDate (str): Expiry Date (max 8 characters) - Required (conditional).
                - expiryTime (str): Expiry Time (max 8 characters) - Required (conditional).
                - mobilePhoneNo (str): Mobile Phone No. (max 100 characters) - Required (conditional).
                - statusCode (str): Status Code (max 1 character). 1 = Active, 2 = Inactive - Required.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/VirtualAccount/Create'
        return self._make_request(path, method, timeStamp, payload)
    
    def updateVirtualAccount(self, payload=None):
        """
        Service untuk melakukan update virtual account.

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (max 40 characters) - Required.
                - userId (str): User ID (max 40 characters) - Required.
                - companyCode (str): Company Code (max 20 characters) - Required.
                - virtualAccountNo (str): Virtual Account No. (variable length) - Required.
                - virtualAccountName (str): Virtual Account Name (max 80 characters) - Required.
                - virtualAccountTypeCode (str): Virtual Account Type Code (max 2 characters) - Required.
                - billingAmount (str): Billing Amount (max 12v2 characters) - Required (conditional).
                - varAmount1 (str): Var Amount 1 (max 12v2 characters) - Required (conditional).
                - varAmount2 (str): Var Amount 2 (max 12v2 characters) - Required (conditional).
                - expiryDate (str): Expiry Date (max 8 characters) - Required (conditional).
                - expiryTime (str): Expiry Time (max 8 characters) - Required (conditional).
                - mobilePhoneNo (str): Mobile Phone No. (max 100 characters) - Required (conditional).
                - statusCode (str): Status Code (max 1 character). 1 = Active, 2 = Inactive - Required.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/VirtualAccount/Update'
        return self._make_request(path, method, timeStamp, payload)
    
    def inquiryVirtualAccountTransaction(self, payload=None):
        """
        Service untuk melakukan inquiry virtual account transaction.

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (max 40 characters) - Required.
                - userId (str): User ID (max 40 characters) - Required.
                - virtualAccountNo (str): Virtual Account No. (max 40 characters) - Required.
                - fromDate (str): From Date (yyyyMMdd format, max 8 characters) - Required.
                - toDate (str): To Date (yyyyMMdd format, max 8 characters) - Required.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/VirtualAccount/InquiryTransaction'
        return self._make_request(path, method, timeStamp, payload)
    
    def bulkGetStatus(self, payload=None):
        """
        Service to request or find out the status of the current bulk api position. 

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (max 40 characters) - Required.
                - userId (str): User ID (max 40 characters) - Required.
                - fileRefNo (str): File Reference No. (max 40 characters) - Optional.
                - apiRefNo (str): API Reference (max 1996 characters) - Required.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/Account/BulkGetStatus'
        return self._make_request(path, method, timeStamp, payload)
    
    def balanceInquiry(self, payload=None):
        """
        Services for checking balances.

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID - Required.
                - userId (str): User ID - Required.
                - accountList (float): List of Account (1 … n) - Required.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/Account/InquiryBalance'
        return self._make_request(path, method, timeStamp, payload)
    
    def inquiryForexRate(self, payload=None):
        """
        Service to request foreign exchange rates.

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (max 40 characters) - Required.
                - userId (str): User ID (max 40 characters) - Required.
                - currencyList (list of str): List of Account currencies - Required.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/Account/InquiryForexRate'
        return self._make_request(path, method, timeStamp, payload)
    
    def bulkPaymentMixed(self, payload=None):
        """
        Services for conducting Mixed Bulk Payment transactions.

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (max 40 characters) - Required.
                - userId (str): User ID (max 40 characters) - Required.
                - apiRefNo (str): API Reference No. (max 1996 characters) - Required.
                - instructionDate (str): Transaction Instruction Date (yyyyMMdd format, max 8 characters) - Required.
                - session (str): Instruction session (max 1 character) - Optional.
                - serviceType (str): Bulk service type (max 10 characters) - Required.
                - debitAcctNo (str): Debit account (max 16 characters) - Required.
                - amount (str): Transaction amount (max 18 characters with 7 decimal places) - Required.
                - currency (str): Currency transactions (max 3 characters) - Required.
                - chargeTo (str): Charge To (max 3 characters) - Required.
                - residenceCode (str): Remitter Country of Residence Code (max 40 characters) - Required.
                - citizenCode (str): Citizenship code (max 40 characters) - Optional.
                - category (str): Remitter category (max 40 characters) - Optional.
                - transactionType (str): Transaction type (max 1 character) - Required.
                - remark (str): Description (max 100 characters) - Optional.
                - accountNmValidation (str): Beneficiary account name validation flag (max 1 character) - Required.
                - childContent (str): List of transaction details (child of bulk) - Required.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/MassPayment/BulkPaymentMixed'
        return self._make_request(path, method, timeStamp, payload)
    
    def payrollMixed(self, payload=None):
        """
        Service for conducting Payroll Mixed transactions. 

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (max 40 characters) - Required.
                - userId (str): User ID (max 40 characters) - Required.
                - apiRefNo (str): API Reference No. (max 1996 characters) - Required.
                - instructionDate (str): Transaction Instruction Date (yyyyMMdd format, 8 characters) - Required.
                - session (str): Instruction session (max 1 character) - Optional.
                - serviceType (str): Bulk service type (max 10 characters) - Required.
                - debitAcctNo (str): Debit account (max 16 characters) - Optional.
                - totalAmount (str): Total transaction amount (max 18 characters with 7 decimal places) - Optional.
                - totalAmountCurrencyCode (str): Total amount currency code - Optional.
                - currency (str): Currency transactions (max 3 characters) - Optional.
                - chargeTo (str): Charge To (max 3 characters) - Optional.
                - residenceCode (str): Remitter Country of Residence Code (max 40 characters) - Optional.
                - citizenCode (str): Citizenship code (max 40 characters) - Optional.
                - remitterCategory (str): Remitter category (max 40 characters) - Optional.
                - transactionType (str): Transaction type (max 1 character) - Required.
                - remark (str): Description (max 100 characters) - Optional.
                - accountNmValidation (str): Beneficiary account name validation flag (max 1 character) - Required.
                - childContent (str): List of transaction details (child of bulk) - Required.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/MassPayment/PayrollMixed'
        return self._make_request(path, method, timeStamp, payload)

    def domesticSingleBIFastTransfer(self, payload=None):
        """
        Service for conducting domestic single BI-FAST transfers.

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (max 40 characters) - Required.
                - userId (str): User ID (max 40 characters) - Required.
                - debitedAccountNo (str): Registered account number on the “Account Group” menu associated with the User Group of the Maker User ID. Must have the flag Allow Debit = Y (max 16 characters) - Required.
                - amountCurrency (str): Currency code inputted must be “IDR” (max 3 characters) - Required.
                - amount (str): Transaction amount. Decimals not allowed if transaction uses the currency matrix “local to local” (max 15 characters) - Required.
                - exchangeRateCode (str): Exchange rate type. Options: -“Cr”: Counter rate -“Sr”: Special rate (max 2 characters) - Required.
                - treasuryReferenceNo (str): Special rate ticket number. If inputted, the transaction will be assumed to be using “special rate” (max 40 characters) - Optional.
                - chargeTo (str): -“OUR”: Remitter -“BEN”: Beneficiary (max 3 characters) - Required.
                - remark1 (str): Remark (max 40 characters) - Optional.
                - remark2 (str): Remark (max 40 characters) - Optional.
                - remark3 (str): Remark (max 40 characters) - Optional.
                - remitterReferenceNo (str): Remitter’s reference number (max 16 characters) - Optional.
                - finalizePaymentFlag (str): Can only be filled with “Y” or “N” (max 1 character) - Required.
                - beneficiaryReferenceNo (str): Beneficiary’s reference number (max 16 characters) - Optional.
                - usedProxy (str): -“Y”: Proxy ID -“N”: Account no. (max 1 character) - Required.
                - beneficiaryAccountNo (str): Account no. for beneficiary info. Only if account no. (“N”) is picked (max 16 characters) - Required if usedProxy = “N”.
                - proxyId (str): E-mail or phone no. for beneficiary info. Only if proxy ID (“Y”) is picked (max 100 characters) - Required if usedProxy = “Y”.
                - beneficiaryBankCode (str): Data must match BIC/RTGS Code or BIFAST Bank Code (max 40 characters) - Required.
                - beneficiaryBankName (str): Name of the beneficiary bank (max 100 characters) - Required.
                - notificationFlag (str): -“Y”: Send -“N”: Don’t send (max 1 character) - Required.
                - beneficiaryEmail (str): Data must match e-mail format. Multiple e-mails are allowed using delimiter (;) (max 100 characters) - Required if notificationFlag = “Y”.
                - transactionInstructionDate (str): Immediate/Current date (in yyyyMMdd format) (max 8 characters) - Required.
                - transactionPurposeCode (str): Kode tujuan transaksi BIFAST (max 2 characters) - Required.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/BIFAST/Transfer'
        return self._make_request(path, method, timeStamp, payload)

    def inquiryBIFastBeneficiaryName(self, payload=None):
        """
        Service for conducting BI-FAST beneficiary name inquiry. 

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (max 40 characters) - Required.
                - userId (str): User ID (max 40 characters) - Required.
                - usedProxy (str): -“Y”: Proxy ID -“N”: Account no. (max 1 character) - Required.
                - beneficiaryAccountNo (str): Account number (max 16 characters) - Required if usedProxy = “N”.
                - proxyId (str): Proxy ID (max 100 characters) - Required if usedProxy = “Y”.
                - beneficiaryBankCode (str): Data must match BIC/RTGS Code or BIFAST Bank Code (max 40 characters) - Required.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/BIFAST/InquiryBeneficiaryName'
        return self._make_request(path, method, timeStamp, payload)

    def singleBulkPayment(self, payload=None):
        """
        Services for conducting Single Bulk Payment transactions. 

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (max 40 characters) - Required.
                - userId (str): User ID (max 40 characters) - Required.
                - apiRefNo (str): Api Reference No (max 1996 characters) - Required.
                - instructionDate (str): Transaction Instruction Date (yyyyMMdd format) - Required (conditional).
                - session (str): Instruction session (max 1 character) - Required.
                - serviceType (str): Bulk service type (max 10 characters) - Required.
                - isSTP (str): Flag STP (Y/N) (max 1 character) - Required.
                - transactionType (str): Transaction type (max 1 character) - Required.
                - remark (str): Description (max 100 characters) - Optional.
                - accountNmValidation (str): Beneficiary account name validation flag (max 1 character) - Required.
                - transactionDetail (list of objects): List of transaction details (child of bulk) - Required.
                * child of transactionDetail is down below:
                - creditAcctNo (str): Credit Account No (max 40 characters) - Required.
                - creditAcctNm (str): Credit Account Name (max 100 characters) - Required.
                - amount (str): Amount transaction (max 15 characters) - Required.
                - treasury (str): Treasury reference no (max 40 characters) - Optional.
                - remark1 (str): Keterangan 1 (max 100 characters) - Optional.
                - remark2 (str): Keterangan 2 (max 100 characters) - Optional.
                - remark3 (str): Keterangan 3 (max 100 characters) - Optional.
                - benAddr1 (str): Alamat penerima 1 (max 50 characters) - Optional.
                - benAddr2 (str): Alamat penerima 2 (max 50 characters) - Optional.
                - benAddr3 (str): Alamat penerima 3 (max 50 characters) - Optional.
                - benBankCode (str): Kode Bank Penerima (max 40 characters) - Required.
                - benBankNm (str): Nama Bank Penerima (max 100 characters) - Required.
                - benBranchNm (str): Nama Cabang Bank Penerima (max 100 characters) - Optional.
                - benBankAddr1 (str): Alamat Bank Penerima 1 (max 50 characters) - Optional.
                - benBankAddr2 (str): Alamat Bank Penerima 2 (max 50 characters) - Optional.
                - benBankAddr3 (str): Alamat Bank Penerima 3 (max 50 characters) - Optional.
                - benBankCityNm (str): Kota Bank Penerima (max 100 characters) - Optional.
                - benBankCountryNm (str): Negara Bank Penerima (max 100 characters) - Required.
                - benResidenceCd (str): Kode kependudukan penerima (max 40 characters) - Required.
                - benCountryCd (str): Kode kewarganegaraan penerima (max 40 characters) - Required.
                - benEmail (str): Email penerima (max 100 characters) - Optional.
                - benPhone (str): Nomor telp penerima (max 100 characters) - Optional.
                - benFax (str): Nomor fax penerima (max 100 characters) - Optional.
                - correspondentBank (str): Nama Bank Koresponden (max 40 characters) - Optional.
                - purposeCode (str): Kode tujuan transaksi (max 40 characters) - Required.
                - affiliate (str): Relasi pelaku transaksi (Y/N) - Optional.
                - identical (str): Keidentikan status (Y/N) - Optional.
                - benCategory (str): Kode kategori penerima (max 40 characters) - Optional.
                - lldDescription (str): Deskripsi LLD (max 500 characters) - Optional.
                - orderPartyRefNo (str): Nomor referensi pengirim (max 16 characters) - Required.
                - finalizePayment (str): Nomor referensi final? (Y/N) - Optional.
                - counterPartyRefNo (str): Nomor referensi penerima (max 16 characters) - Optional.
                - extraDetail1-5 (str): Extra details 1-5 (max 2000 characters each) - Optional.
                - typeCode (str): Jenis penerima (1/2/3/4) - Optional.
                - mixedServiceCode (str): Kode service transaksi (max 40 characters) - Required.
                - mixedCurrency (str): Mata uang untuk transaksi - Required.
                - mixedDebitAcctNo (str): Debit account (max 16 characters) - Required.
                - mixedChargeTo (str): Biaya transaksi dikenakan kepada (max 3 characters) - Required.
                - mixedRemCountryCode (str): Kode kependudukan (max 40 characters) - Required.
                - mixedRemCitizenCode (str): Kode kewarganegaraan (max 40 characters) - Required.
                - mixedRemCategory (str): Kode kategori pengirim (max 40 characters) - Optional.
                - proxyId (str): Kode Proxy Id Penerima (untuk BI Fast) (max 50 characters) - Optional.
                - proxyFlag (str): Pilihan untuk menggunakan proxyId atau creditAcctNo (Y/N) - Optional.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/MassPayment/SingleBulkPaymentMixed'
        return self._make_request(path, method, timeStamp, payload)

    def singlePayroll(self, payload=None):
        """
        Services for conducting Single Payroll transactions.

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (max 40 characters) - Required.
                - userId (str): User ID (max 40 characters) - Required.
                - apiRefNo (str): Api Reference No (max 1996 characters) - Required.
                - instructionDate (str): Transaction Instruction Date (yyyyMMdd format) - Required (conditional).
                - session (str): Instruction session (max 1 character) - Optional.
                - serviceType (str): Bulk service type (max 10 characters) - Required.
                - isSTP (str): Flag STP (Y/N) (max 1 character) - Required.
                - transactionType (str): Transaction type (max 1 character) - Required.
                - remark (str): Description (max 100 characters) - Optional.
                - accountNmValidation (str): Beneficiary account name validation flag (max 1 character) - Required.
                - transactionDetail (list of objects): List of transaction details (child of bulk) - Required.
                * child of transactionDetail is down below:
                - creditAcctNo (str): Credit Account No (max 40 characters) - Required.
                - creditAcctNm (str): Credit Account Name (max 100 characters) - Required.
                - amount (str): Amount transaction (max 15 characters) - Required.
                - treasury (str): Treasury reference no (max 40 characters) - Optional.
                - remark1 (str): Remark 1 (max 100 characters) - Optional.
                - remark2 (str): Remark 2 (max 100 characters) - Optional.
                - remark3 (str): Remark 3 (max 100 characters) - Optional.
                - benAddr1 (str): Beneficiary Address 1 (max 50 characters) - Optional.
                - benAddr2 (str): Beneficiary Address 2 (max 50 characters) - Optional.
                - benAddr3 (str): Beneficiary Address 3 (max 50 characters) - Optional.
                - benBankCode (str): Beneficiary Bank Code (max 40 characters) - Required.
                - benBankNm (str): Beneficiary Bank Name (max 100 characters) - Required.
                - benBranchNm (str): Beneficiary Bank Branch Name (max 100 characters) - Optional.
                - benBankAddr1 (str): Beneficiary Bank Address 1 (max 50 characters) - Optional.
                - benBankAddr2 (str): Beneficiary Bank Address 2 (max 50 characters) - Optional.
                - benBankAddr3 (str): Beneficiary Bank Address 3 (max 50 characters) - Optional.
                - benBankCityNm (str): Beneficiary Bank City Name (max 100 characters) - Optional.
                - benBankCountryNm (str): Beneficiary Bank Country Name (max 100 characters) - Required.
                - benResidenceCd (str): Beneficiary Residence Code (max 40 characters) - Required.
                - benCountryCd (str): Beneficiary Country Code (max 40 characters) - Required.
                - benEmail (str): Beneficiary Email (max 100 characters) - Optional.
                - benPhone (str): Beneficiary Phone Number (max 100 characters) - Optional.
                - benFax (str): Beneficiary Fax Number (max 100 characters) - Optional.
                - correspondentBank (str): Correspondent Bank Name (max 40 characters) - Optional.
                - purposeCode (str): Purpose Code (max 40 characters) - Required.
                - affiliate (str): Affiliate Relationship (Y/N) - Optional.
                - identical (str): Identical Status (Y/N) - Optional.
                - benCategory (str): Beneficiary Category Code (max 40 characters) - Optional.
                - lldDescription (str): LLD Description (max 500 characters) - Optional.
                - orderPartyRefNo (str): Order Party Reference Number (max 16 characters) - Required.
                - finalizePayment (str): Finalize Payment Reference Number (Y/N) - Optional.
                - counterPartyRefNo (str): Counter Party Reference Number (max 16 characters) - Optional.
                - extraDetail1-5 (str): Extra Details 1-5 (max 2000 characters each) - Optional.
                - typeCode (str): Type Code (1/2/3/4) - Optional.
                - mixedServiceCode (str): Mixed Service Code (IHT/LLG/OT/RTGS/BIFAST/IFT) (max 40 characters) - Required.
                - mixedCurrency (str): Mixed Currency for Transaction (max 40 characters) - Required.
                - mixedDebitAcctNo (str): Mixed Debit Account Number (max 16 characters) - Required.
                - mixedChargeTo (str): Mixed Charge To (max 3 characters) - Required.
                - mixedRemCountryCode (str): Mixed Remitter Country Code (max 40 characters) - Required.
                - mixedRemCitizenCode (str): Mixed Remitter Citizenship Code (max 40 characters) - Required.
                - mixedRemCategory (str): Mixed Remitter Category Code (max 40 characters) - Optional.
                - proxyId (str): Proxy ID for Beneficiary (max 50 characters) - Optional.
                - proxyFlag (str): Proxy Flag (Y/N) to use proxyId or creditAcctNo (mandatory for BIFast) - Optional.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/MassPayment/SinglePayrollMixed'
        return self._make_request(path, method, timeStamp, payload)

    def singleBulkPaymentSubmit(self, payload=None):
        """
        Service for confirming submission of Single Bulk Payment transactions. 

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (max 40 characters) - Required.
                - userId (str): User ID (max 40 characters) - Required.
                - apiRefNo (str): API Reference No (max 1996 characters) - Required.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/MassPayment/SingleBulkPaymentMixed/Submit'
        return self._make_request(path, method, timeStamp, payload)

    def singlePayrollSubmit(self, payload=None):
        """
        Service for confirming submission of Single Payroll transactions. 

        Parameters:
            payload (dict): A dictionary containing the following keys:
                - corporateId (str): Corporate ID (max 40 characters) - Required.
                - userId (str): User ID (max 40 characters) - Required.
                - apiRefNo (str): API Reference No (max 1996 characters) - Required.
        """
        if payload is None:
            payload = {}
        timeStamp = getTimestamp()
        method='POST'
        path='/bnidirect/api/MassPayment/SinglePayrolMixed/Submit'
        return self._make_request(path, method, timeStamp, payload)
