from unittest import TestCase

class TestMaintenance(TestCase):

    def _getTargetClass(self):
        from zabbix_api_client.maintenance import Maintenance
        return Maintenance


    def  _makeOne(self, *args, **kw):
        return self._getTargetClass()(*args, **kw)


    def test_get(self):
        m = self._makeOne(host='http://example.com', user='osamunmun', password='foobar')
        self.assertEqual(m.get(), 1)
