from unittest import TestCase
import json
import responses
import jsonschema


def get_response(maintenance_id):
    return {
        "jsonrpc": "2.0",
        "result": [
            {
                "maintenanceid": maintenance_id,
                "name": "Sunday maintenance",
                "maintenance_type": "0",
                "description": "",
                "active_since": "1358844540",
                "active_till": "1390466940",
                "groups": [
                    {
                        "groupid": "4",
                        "name": "Zabbix servers",
                        "internal": "0"
                    }
                ],
                "timeperiods": [
                    {
                        "timeperiodid": "4",
                        "timeperiod_type": "3",
                        "every": "1",
                        "month": "0",
                        "dayofweek": "1",
                        "day": "0",
                        "start_time": "64800",
                        "period": "3600",
                        "start_date": "2147483647"
                    }
                ]
            }
        ],
        "id": 1
    }

def update_response(maintenance_id):
    return {
        "jsonrpc": "2.0",
        "result": {
            "maintenanceids": [
                maintenance_id
            ]
        },
        "id": 1
    }


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
                     body=json.dumps(get_response(maintenance_id)),
                     status=200,
                     content_type='application/json')
        r = m.get()
        self.assertEqual(r[0]['maintenanceid'], maintenance_id)


    @responses.activate
    def test_get_with_invalid_mentenanceid(self):
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
                     body=json.dumps(get_response(maintenance_id)),
                     status=200,
                     content_type='application/json')
        with self.assertRaises(TypeError):
            m.get(maintenance_id=22)


    @responses.activate
    def test_update_with_valid_mentenanceid(self):
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
                     body=json.dumps(update_response(maintenance_id)),
                     status=200,
                     content_type='application/json')
        r = m.update({'maintenanceid': maintenance_id,
                      'name': 'test',
                      'active_since': '2004-04-01T12:00+09:00',
                      'active_till': '2014-04-01T12:00+09:00'})
        self.assertEqual(r[0]['maintenanceid'], maintenance_id)


    @responses.activate
    def test_get_with_invalid_mentenanceid(self):
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
                     body=json.dumps(get_response(maintenance_id)),
                     status=200,
                     content_type='application/json')
        with self.assertRaises(TypeError):
            m.get(maintenance_id=22)


    @responses.activate
    def test_update_with_valid_mentenanceid(self):
        def request_callback(request):
            method = json.loads(request.body)['method']
            if method == 'maintenance.get':
                return (200, {}, json.dumps(get_response('22')))
            else:
                return (200, {}, json.dumps(update_response('22')))

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
        responses.add_callback(responses.POST, 'https://example.com/zabbix/api_jsonrpc.php',
                     callback=request_callback,
                     content_type='application/json')
        r = m.update({'maintenanceid': maintenance_id,
                      'name': 'test',
                      'active_since': '2004-04-01T12:00+09:00',
                      'active_till': '2014-04-01T12:00+09:00'})
        self.assertEqual(r['maintenanceids'], [maintenance_id])


    @responses.activate
    def test_update_with_invalid_mentenanceid(self):
        def request_callback(request):
            method = json.loads(request.body)['method']
            if method == 'maintenance.get':
                return (200, {}, json.dumps(get_response('22')))
            else:
                return (200, {}, json.dumps(update_response('22')))

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
        responses.add_callback(responses.POST, 'https://example.com/zabbix/api_jsonrpc.php',
                     callback=request_callback,
                     content_type='application/json')
        for key in ('maintenanceid', 'name', 'active_since', 'active_till'):
            required_params = {'maintenanceid': maintenance_id,
                               'name': 'test',
                               'active_since': '2004-04-01T12:00+09:00',
                               'active_till': '2014-04-01T12:00+09:00'}
            with self.assertRaises(jsonschema.exceptions.ValidationError):
                required_params.pop(key)
                m.update(required_params)
