from unittest import TestCase
import json
import responses
import requests


class TestMaintenance(TestCase):

    def _getTargetClass(self):
        from zabbix_api_client.maintenance import Maintenance
        return Maintenance

    def _makeOne(self, *args, **kw):
        return self._getTargetClass()(*args, **kw)

    @responses.activate
    def test_get_with_valid_params(self):
        responses.add(
            responses.POST, 'https://example.com/zabbix/api_jsonrpc.php',
            body=json.dumps({
                'result': 'authentication_token',
                'id': 1,
                'jsonrpc': '2.0'
            }),
            status=200,
            content_type='application/json'
        )
        m = self._makeOne(
            host='https://example.com',
            user='osamunmun',
            password='foobar')
        maintenance_id = '22'
        responses.reset()
        responses.add(responses.POST, 'https://example.com/zabbix/api_jsonrpc.php',
                     body=json.dumps({'result': [{'description': '', 'maintenance_type': '0', 'maintenanceid': maintenance_id, 'hosts': [{'templateid': '0', 'ipmi_disable_until': '0', 'lastaccess': '0', 'error': '', 'disable_until': '0', 'proxy_hostid': '0', 'snmp_disable_until': '0', 'jmx_errors_from': '0', 'host': 'host_example1', 'flags': '0', 'hostid': '10365', 'maintenance_type': '0', 'available': '1', 'ipmi_username': '', 'jmx_disable_until': '0', 'maintenances': [], 'maintenance_from': '0', 'jmx_error': '', 'jmx_available': '0', 'name': 'dsif1car01ta', 'snmp_errors_from': '0', 'maintenanceid': '0', 'ipmi_error': '', 'ipmi_errors_from': '0', 'ipmi_password': '', 'ipmi_available': '0', 'status': '0', 'snmp_error': '', 'snmp_available': '0', 'maintenance_status': '0', 'ipmi_privilege': '2', 'errors_from': '0', 'ipmi_authtype': '0'}], 'active_till': '1952830200', 'name': 'Test3', 'timeperiods': [{'timeperiod_type': '3', 'start_time': '64800', 'month': '0', 'start_date': '0', 'timeperiodid': '30', 'day': '0', 'every': '1', 'period': '3600', 'dayofweek': '64'}], 'groups': [], 'active_since': '1917924600'}], 'jsonrpc': '2.0', 'id': 2}),
                     status=200,
                     content_type='application/json')
        r = m.get()
        self.assertEqual(r[0]['maintenanceid'], maintenance_id)
