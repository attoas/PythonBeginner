import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('helloworldfirebase-5d847-firebase-adminsdk-ncbqi-f4d3c643d3.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://helloworldfirebase-5d847.firebaseio.com/'
})

# Get a database reference to our posts
#ref1 = db.reference('AppName')
#ref2 = db.reference('text')
#ref3 = db.reference('textDemo')
#ref4 = db.reference('Users/Sommai/age')
#ref5 = db.reference('Users/Sommai/email')
#ref6 = db.reference('Users')
#ref7 = db.reference('Users')

# Read the data at the posts reference (this is a blocking operation)
#print(ref1.get())
#print(ref2.get())
#print(ref3.get())
#print(ref4.get())
#print(ref5.get())
#print(ref6.get())


#ref7.update({
#    'Sommai2': {
#        'age':'43','email':'Sommai@gmail.com','tel':'99999999'
#
#    },
#    'Somsong2': {
#        'age':'55',
#        'tel':'09999999',
#        'email':'Somsong@gmail.com'
#    }
#})

#ref = db.reference('')
#posts_ref = ref.child('Users')

#new_post_ref = posts_ref.push()
#new_post_ref.set({
#    'author': 'gracehop',
#    'title': 'Announcing COBOL, a New Programming Language'
#})

# We can also chain the two calls together
#posts_ref.push().set({
#    'author': 'alanisawesome',
#    'title': 'The Turing Machine'
#})

#ref9 = db.reference('Users')
#print(ref9.get('Users/author/gracehop'))


#ref10 = db.reference('Users/Somsong2')
#ref10.delete()
#ref10 = db.reference()
#print(ref10.get())
