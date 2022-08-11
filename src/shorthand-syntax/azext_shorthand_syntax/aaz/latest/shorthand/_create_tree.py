# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "shorthand create-tree"
)
class CreateTree(AAZCommand):
    """ Create the demo tree

    """

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.ctx.args.to_serialized_data()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema

        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        _args_schema = cls._args_schema
        _args_schema.value = AAZIntArg(
            options=['-v', '--value'],
            help="The value of root node",
            required=True,
        )
        _args_schema.nodes = AAZListArg(
            options=['--nodes', '-n'],
            help="Sub nodes of the root"
        )

        _args_schema.leaves = AAZListArg(
            options=['--leaves', '-l'],
            help="Sub leaves of the root"
        )

        leaf = AAZObjectArg()
        leaf.value = AAZIntArg(
            options=['v', 'value'],
            help="The value of leaf",
            required=True
        )

        _args_schema.leaves.Element = leaf

        node = AAZObjectArg()
        node.value = AAZIntArg(
            options=['v', 'value'],
            help="The value of node",
            required=True
        )

        node.nodes = AAZListArg(
            options=['nodes', 'n'],
            help="Sub nodes"
        )

        node.nodes.Element = node

        node.leaves = AAZListArg(
            options=['leaves', 'l'],
            help="Sub leaves"
        )

        node.leaves.Element = leaf

        _args_schema.nodes.Element = node

        return cls._args_schema


__all__ = ["CreateTree"]


