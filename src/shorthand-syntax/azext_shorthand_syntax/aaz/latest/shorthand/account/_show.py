# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "shorthand account show"
)
class Show(AAZCommand):
    """ Show the demo account object

    """

    def _handler(self, command_args):
        super()._handler(command_args)
        return self._execute_operations()

    def _execute_operations(self):
        data = {
            "name": "Bill",
            "properties": {
                "address": {
                    "company": "Microsoft",
                    "country": "USA",
                    "details": {
                        "line1": "15590 NE 31st St",
                        "line2": "Redmond, WA"
                    }
                },
                "age": 43,
                "emails": [
                    "billw@microsoft.com",
                    "bill.wang@outlook.com"
                ],
                "family": [
                    {
                        "age": 18,
                        "blog": "https://blog.twitter.com/tom12345",
                        "emails": [
                            "tom.wang@gmail.com"
                        ],
                        "motto": "One man's bug is another man's lesson.",
                        "name": "Tom",
                        "role": "Children"
                    },
                    {
                        "age": 42,
                        "name": "Emma",
                        "role": "Wife"
                    }
                ],
                "fullName": "Bill Wang",
                "married": True
            }
        }
        self.ctx.set_var(
            "instance",
            data,
            schema_builder=self._build_schema
        )

        return self.deserialize_output(self.ctx.vars.instance)

    _schema = None

    @classmethod
    def _build_schema(cls):
        if cls._schema is not None:
            return cls._schema

        cls._schema = AAZObjectType()

        _schema = cls._schema
        _schema.name = AAZStrType()
        _schema.properties = AAZObjectType(flags={"client_flatten": True})
        _schema.tags = AAZDictType()

        properties = cls._schema.properties
        properties.full_name = AAZStrType(serialized_name='fullName')
        properties.emails = AAZListType()
        properties.age = AAZIntType()
        properties.married = AAZBoolType()
        properties.address = AAZObjectType()
        properties.family = AAZListType()

        emails = cls._schema.properties.emails
        emails.Element = AAZStrType()

        address = cls._schema.properties.address
        address.country = AAZStrType()
        address.company = AAZStrType()
        address.details = AAZObjectType()

        details = cls._schema.properties.address.details
        details.line1 = AAZStrType()
        details.line2 = AAZStrType()

        family = cls._schema.properties.family
        family.Element = AAZObjectType()

        _element = cls._schema.properties.family.Element
        _element.name = AAZStrType()
        _element.role = AAZStrType()
        _element.age = AAZIntType()
        _element.blog = AAZStrType()
        _element.motto = AAZStrType()
        _element.emails = AAZListType()

        emails = cls._schema.properties.family.Element.emails
        emails.Element = AAZStrType()

        tags = cls._schema.tags
        tags.Element = AAZStrType()

        return cls._schema


__all__ = ["Show"]
