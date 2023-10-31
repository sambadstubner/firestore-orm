from firebase_admin import firestore


class Base:
    _firestore = firestore.client()
    id = None

    # Get the members of the model in dictionary form
    def get_dict(self) -> dict:
        attributes = {
            key: value
            for key, value in self.__dict__.items()
            if not key.startswith("_") and not callable(value) and key != "id"
        }
        return attributes

    # Save changes made to the model to firebase either by creating a new document
    # or updating a previous one. Returns the id of the object
    def save(self):
        document_ref = self.get_document_reference()
        obj_dict = self.get_dict()
        if not document_ref.get().exists:
            self.id = document_ref.id
            document_ref.set(obj_dict)

        else:
            document_ref.update(obj_dict)

        return self.id

    # Get the object from firebase and populate the model
    def get(self):
        document = self.get_document()
        self.set(document.to_dict())
        return self.__dict__

    #  Map values of dictionary to variables in the model
    def set(self, data):
        for key, value in data.items():
            self.__dict__[key] = value

    # Get the document from firebase
    def get_document(self):
        return self.get_document_reference().get()

    # Get the document reference from firebase
    def get_document_reference(self):
        if not self._collection:
            raise Exception("_collection attribute not set in model class")
        return self._firestore.collection(self._collection).document(self.id)

    # Get all documents in the collection and their variables as a dict
    def get_all_as_dict(self) -> dict:
        if not self._collection:
            raise Exception("_collection attribute not set in model class")
        documents = self._firestore.collection(self._collection).stream()
        result = {
            document.id: self._dict_formatter_from_object(document.to_dict())
            for document in documents
        }
        return result

    # Format the dictionary for usage by the model.
    @staticmethod
    def _dict_formatter_from_object(input_dict) -> dict:
        for key, value in input_dict.items():
            if type(value) == list:
                input_dict[key] = Base._parse_doc_list(value)

        return input_dict

    # Format a list object to a readable format. This handles cases when it
    # is a list of document references
    @staticmethod
    def _parse_doc_list(input_list) -> list:
        attributes = []
        for attribute in input_list:
            if type(attribute) == firestore.firestore.DocumentReference:
                attributes.append(attribute.path)
            else:
                attributes.append(attribute)

        return attributes

    # Checks if the document already exists in firebase
    def exists(self) -> bool:
        return self.get_document().exists
