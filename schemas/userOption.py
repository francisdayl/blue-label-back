from app import ma


class UserOptionSchema(ma.Schema):
    name = ma.String(required=True)
    email = ma.Email(required=True)
    option = ma.String(required=True)


user_option_schema = UserOptionSchema()
