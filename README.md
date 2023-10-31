# Firestore ORM
An Object Relational Mapper for Google Firestore, a NoSQL database

## Purpose
While NoSQL is supposed to be flexible, managing the database can be cumbersome without further abstraction. I wanted to take the models approach common in SQLAlchemy and apply it to Firestore to clean up backend code and make the schema more consistent.

## Usage

**See example/user.py for creating a model**
1. Create a class which inherits the Base class
2. Set the variable ```_collection``` to match the name of the collection in firestore
3. Create variables with the default values
4. Add any desired functionality to the model.

**See example/main.py for accessing a model**
