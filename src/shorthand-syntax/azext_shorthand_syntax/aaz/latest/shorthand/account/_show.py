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

    def __handler(self, command_args):
        pass



__all__ = ["Show"]
