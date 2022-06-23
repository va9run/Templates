from requests import request


def _generalapi(API):
    response = requests.get(API)
    data = response.json()['data']
    finaldata = pd.json_normalize(data, sep='_')
    return finaldata

def _moredefinedapi(API, record_path=[], meta =[]):
    response = requests.get(API)
    data = response.json()['data']
    finaldata = pd.json_normalize(data, sep='_', record_path=[], meta=[])
    # finaldata = pd.json_normalize(data, sep='_', record_path=['lineItems'], meta=['reference','invoiceNumber',['contact','contactID'],['contact','name']])
    return finaldata