from mongoengine import Document, StringField, DateTimeField, ListField, ReferenceField

class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author, reverse_delete_rule=2)
    quote = StringField()