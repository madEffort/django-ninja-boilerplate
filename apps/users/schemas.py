from ninja import ModelSchema, Schema
from .models import User


class UserSchema(ModelSchema):

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name"]


class Error(Schema):
    detail: str
