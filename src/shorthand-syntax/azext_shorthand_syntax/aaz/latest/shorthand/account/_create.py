# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "shorthand account create"
)
class Create(AAZCommand):
    """ Create the demo account object

    """

    def _handler(self, command_args):
        super()._handler(command_args)
        return self._execute_operations()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema

        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        _args_schema = cls._args_schema
        _args_schema.name = AAZStrArg(
            options=['-n', '--name'],
            help="The name of the account",
            required=True,
        )
        _args_schema.full_name = AAZStrArg(
            options=['--full-name'],
            help="The full name of the account",
        )
        _args_schema.emails = AAZListArg(
            options=['--emails'],
            help="The account email addresses",
            required=True,
            fmt=AAZListArgFormat(min_length=1),
        )
        _args_schema.age = AAZIntArg(
            options=['--age'],
            help="The age of account owner",
            required=True,
            fmt=AAZIntArgFormat(minimum=1),
        )
        _args_schema.married = AAZBoolArg(
            options=['--married'],
            help="Whether account owner married or not",
        )
        _args_schema.address = AAZObjectArg(
            options=['--address'],
            help="Working address information"
        )
        _args_schema.family = AAZListArg(
            options=['--family', '--family-members'],
            help="Family members",
        )

        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            help="Tags: key=value [key=value ...]",
        )

        emails = cls._args_schema.emails
        emails.Element = AAZStrArg(
            fmt=AAZStrArgFormat(
                pattern=r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            )
        )

        address = cls._args_schema.address
        address.country = AAZStrArg(
            options=['country'],
            help="Country of address",
            enum={"USA": "USA", "CN": "CN"},
            required=True,
        )
        address.company = AAZStrArg(
            options=['company'],
            help="Company name",
            required=True
        )
        address.details = AAZObjectArg(
            options=['details'],
            help="Detail address information",
            required=True
        )

        details = cls._args_schema.address.details
        details.line1 = AAZStrArg(
            options=['line1'],
            help="Primary address information"
        )
        details.line2 = AAZStrArg(
            options=['line2'],
            help="Secondary address information"
        )

        family = cls._args_schema.family
        family.Element = AAZObjectArg()

        _element = cls._args_schema.family.Element
        _element.name = AAZStrArg(
            options=['name'],
            help="The name of family member",
            required=True
        )
        _element.role = AAZStrArg(
            options=['role'],
            help="Role in family",
            enum={"Children": "Children", "Wife": "Wife", "Husband": "Husband"}
        )
        _element.age = AAZIntArg(
            options=['age'],
            help="The age of account owner",
            required=True,
            fmt=AAZIntArgFormat(minimum=1),
        )
        _element.blog = AAZStrArg(
            options=['blog'],
            help="Blog homepage link",
        )
        _element.motto = AAZStrArg(
            options=['motto'],
            help="A short sentence chosen as encapsulating the beliefs or ideals"
        )
        _element.emails = AAZListArg(
            options=['emails'],
            help="The member email addresses",
        )

        emails = cls._args_schema.family.Element.emails

        emails.Element = AAZStrArg(
            fmt=AAZStrArgFormat(
                pattern=r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            )
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        _content_value, _builder = AAZHttpOperation.new_content_builder(
            self.ctx.args,
            typ=AAZObjectType,
            typ_kwargs={"flags": {"required": True, "client_flatten": True}}
        )

        _builder.set_prop("name", AAZStrType, ".name")
        _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
        _builder.set_prop("tags", AAZDictType, ".tags")

        properties = _builder.get(".properties")
        if properties is not None:
            properties.set_prop("fullName", AAZStrType, ".full_name")
            properties.set_prop("emails", AAZListType, ".emails")
            properties.set_prop("age", AAZIntType, ".age")
            properties.set_prop("married", AAZBoolType, ".married")
            properties.set_prop("address", AAZObjectType, ".address")
            properties.set_prop("family", AAZListType, ".family")

        emails = _builder.get(".properties.emails")
        if emails is not None:
            emails.set_elements(AAZStrType, '.')

        address = _builder.get(".properties.address")
        if address is not None:
            address.set_prop("country", AAZStrType, ".country")
            address.set_prop("company", AAZStrType, ".company")
            address.set_prop("details", AAZObjectType, ".details")

        details = _builder.get(".properties.address.details")
        if details is not None:
            details.set_prop("line1", AAZStrType, ".line1")
            details.set_prop("line2", AAZStrType, ".line2")

        family = _builder.get(".properties.family")
        if family is not None:
            family.set_elements(AAZObjectType, ".")

        _element = _builder.get(".properties.family[]")
        if _element is not None:
            _element.set_prop("name", AAZStrType, ".name")
            _element.set_prop("role", AAZStrType, ".role")
            _element.set_prop("age", AAZIntType, ".age")
            _element.set_prop("blog", AAZStrType, ".blog")
            _element.set_prop("motto", AAZStrType, ".motto")
            _element.set_prop("emails", AAZListType, ".emails")

        emails = _builder.get(".properties.family[].emails")
        if emails is not None:
            emails.set_elements(AAZStrType, '.')

        tags = _builder.get(".tags")
        if tags is not None:
            tags.set_elements(AAZStrType, ".")

        return AAZHttpOperation.serialize_content(_content_value)


__all__ = ["Create"]
