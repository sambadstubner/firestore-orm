from firebase_admin import credentials, initialize_app

cred = credentials.Certificate("example/tokens.json")
initialize_app(cred)

from user import User

user_id = "user_id"
user = User(user_id) # Instantiate the model to match the User data in Firestore
print("Get as dict: ", user.get_dict()) # Display the model in dictionary form
user.listings = ["listings/test1", "listings/test2", "listings/test3"] # Edit a member of the model
user.save() # Save the changes made to the model to reflect in Firestore

user.get()
print("Get as dict after saving: ", user.get_dict())
