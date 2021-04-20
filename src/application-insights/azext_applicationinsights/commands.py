# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long

from azure.cli.core.commands import CliCommandType

from azext_applicationinsights._client_factory import (
    cf_events,
    cf_metrics,
    cf_query,
    cf_components,
    cf_web_tests,
    cf_api_key,
    cf_component_billing,
    cf_component_linked_storage_accounts,
    cf_export_configuration
)


def load_command_table(self, _):

    metrics_sdk = CliCommandType(
        operations_tmpl='azext_applicationinsights.vendored_sdks.applicationinsights.operations.metrics_operations#MetricsOperations.{}',
        client_factory=cf_metrics
    )

    events_sdk = CliCommandType(
        operations_tmpl='azext_applicationinsights.vendored_sdks.applicationinsights.operations.events_operations#EventsOperations.{}',
        client_factory=cf_events
    )

    query_sdk = CliCommandType(
        operations_tmpl='azext_applicationinsights.vendored_sdks.applicationinsights.operations.query_operations#QueryOperations.{}',
        client_factory=cf_query
    )

    components_custom_sdk = CliCommandType(
        operations_tmpl='azext_applicationinsights.custom#{}',
        client_factory=cf_components
    )

    components_billing_custom_sdk = CliCommandType(
        operations_tmpl='azext_applicationinsights.custom#{}',
        client_factory=cf_component_billing
    )

    api_key_custom_sdk = CliCommandType(
        operations_tmpl='azext_applicationinsights.custom#{}',
        client_factory=cf_api_key
    )

    component_linked_storage_accounts_custom_sdk = CliCommandType(
        operations_tmpl='azext_applicationinsights.custom#{}',
        client_factory=cf_component_linked_storage_accounts
    )

    export_configurations_custom_sdk = CliCommandType(
        operations_tmpl='azext_applicationinsights.custom#{}',
        client_factory=cf_export_configuration
    )

    web_tests_custom_sdk = CliCommandType(
        operations_tmpl='azext_applicationinsights.custom#{}',
        client_factory=cf_web_tests
    )

    with self.command_group('monitor app-insights component', custom_command_type=components_custom_sdk) as g:
        g.custom_command('create', 'create_or_update_component')
        g.custom_command('update', 'update_component')
        g.custom_show_command('show', 'show_components')
        g.custom_command('delete', 'delete_component')
        g.custom_command('update-tags', 'update_component_tags')
        g.custom_command('connect-webapp', 'connect_webapp')
        g.custom_command('connect-function', 'connect_function')

    with self.command_group('monitor app-insights component billing', custom_command_type=components_billing_custom_sdk) as g:
        g.custom_command('update', 'update_component_billing')
        g.custom_show_command('show', 'show_component_billing')

    with self.command_group('monitor app-insights api-key', custom_command_type=api_key_custom_sdk) as g:
        g.custom_command('create', 'create_api_key')
        g.custom_show_command('show', 'show_api_key')
        g.custom_command('delete', 'delete_api_key')

    with self.command_group('monitor app-insights metrics', metrics_sdk) as g:
        g.custom_show_command('show', 'get_metric')
        g.custom_command('get-metadata', 'get_metrics_metadata')

    with self.command_group('monitor app-insights events', events_sdk) as g:
        g.custom_show_command('show', 'get_events')

    with self.command_group('monitor app-insights', query_sdk) as g:
        g.custom_command('query', 'execute_query')

    with self.command_group('monitor app-insights component linked-storage', custom_command_type=component_linked_storage_accounts_custom_sdk) as g:
        g.custom_show_command('show', 'get_component_linked_storage_account')
        g.custom_command('link', 'create_component_linked_storage_account')
        g.custom_command('update', 'update_component_linked_storage_account')
        g.custom_command('unlink', 'delete_component_linked_storage_account')

    with self.command_group('monitor app-insights component continues-export', custom_command_type=export_configurations_custom_sdk) as g:
        g.custom_command('list', 'list_export_configurations')
        g.custom_show_command('show', 'get_export_configuration')
        g.custom_command('create', 'create_export_configuration')
        g.custom_command('update', 'update_export_configuration')
        g.custom_command('delete', 'delete_export_configuration', confirmation=True)

    with self.command_group('monitor app-insights web-tests', custom_command_type=web_tests_custom_sdk) as g:
        g.custom_command('list', 'list_web_tests')
        g.custom_show_command('show', 'get_web_test')
        g.custom_command('delete', 'delete_web_test')
