#!/usr/bin/python3
"""
Datadog's API
-------------t
Get all dashboards returns "OK" response.

Usage:  DD_SITE="datadoghq.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" ./example.py
        Must install datadog-api-client first:  pip3 install datadog-api-client
"""

if __name__ == "__main__":
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.dashboards_api import DashboardsApi

    configuration = Configuration()
    with ApiClient(configuration) as api_client:
        api_instance = DashboardsApi(api_client)
        response = api_instance.list_dashboards(
                filter_shared=False,
                )

    print(response)   # print all dashboards.
    print('id:  ', response.get('dashboards')[0].get('id'))  # print dashboard id of first dashboard
