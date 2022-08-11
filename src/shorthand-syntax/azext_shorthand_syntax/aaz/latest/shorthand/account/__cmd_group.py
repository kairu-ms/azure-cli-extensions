# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command_group(
    "shorthand account",
)
class __CMDGroup(AAZCommandGroup):
    """Demo to manage account objects.
    """
    pass


__all__ = ["__CMDGroup"]
