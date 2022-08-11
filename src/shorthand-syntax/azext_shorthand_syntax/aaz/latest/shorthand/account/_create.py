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

    def __handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

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
            options=['line1']
        )



__all__ = ["Create"]
