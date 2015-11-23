from unittest import TestCase
import responses


class TestMaintenance(TestCase):

    @responses.active
    def setUp(self):
        responses


    def _getTargetClass(self):
        from zabbix_api_client.maintenance import Maintenance
        return Maintenance

    def _makeOne(self, *args, **kw):
        return self._getTargetClass()(*args, **kw)

    def test_get_with_valid_params(self):
        m = self._makeOne(
            host='http://example.com',
            user='osamunmun',
            password='foobar')
        m.get()
        self.assertEqual(1, 1)
