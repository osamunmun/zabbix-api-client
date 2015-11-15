import requests
import json
import ipdb


class Borg(object):
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state


class Client(Borg):
    """Zabbix API"""

    def __init__(self, host='', user='', password=''):
        """ Client instance Constructor

        :param host: zabbix host name
        :param user: access user
        :param password: access user's password
        """
        Borg.__init__(self)
        self.host = host
        self.request_id = 1
        if not hasattr(self, 'auth'):
            self.auth = self.request('user.login', {'user': user, 'password': password})

    def request(self, method, params):
        headers = {"Content-Type": "application/json-rpc"}
        data = json.dumps({'jsonrpc': '2.0',
                           'method': method,
                           'params': params,
                           'auth': (self.auth if hasattr(self, 'auth') else None),
                           'id': self.request_id})
        r = requests.post(self.host, data=data, headers=headers).json()
        return r['result']

