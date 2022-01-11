#----------------- a ver si si
crdl = service_account.Credentials.from_service_account_file('../settings/st.json')
# crdl = credentials.Certificate("../settings/storage-david-vasquez.json")

db=firestore.Client(project='lw-looker',credentials=crdl)

result = db.collection(u'clientDatamart').document("").get()
result.to_dict()

docs = db.collection(u'clientDatamart').stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')
    break
    
 # see what iits inside the doc
type(doc.to_dict())
pd.DataFrame.from_dict(doc.to_dict(), orient='index')
