from zeep import Client

client = Client('https://fsdata.hach.com/FSDataService/FSDataService.svc?singleWsdl')
client.service.ping()
