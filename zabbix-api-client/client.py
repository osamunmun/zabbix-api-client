import requests
import json
import logging


class Borg(object):
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state


class Client(Borg):
    """Zabbix API"""

    def __init__(self, host='', user='', password='', log_level='WARNING'):
        """ Client instance Constructor

        :param host: zabbix host name
        :param user: access user
        :param password: access user's password
        """
        Borg.__init__(self)
        if not hasattr(self, 'logger'):
            self.logger = logging.getLogger(__name__)
            loglevel_obj = getattr(logging, log_level.upper())
            self.logger.setLevel(loglevel_obj)
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)
            self.logger.addHandler(ch)
        self.logger.info('Start initializing')
        self.host = host
        self.request_id = 1
        if not hasattr(self, 'auth') or not self.auth:
            self.auth = self.request('user.login', {'user': user, 'password': password})


    def request(self, method, params):
        self.request_id += 1
        headers = {"Content-Type": "application/json-rpc"}
        data = json.dumps({'jsonrpc': '2.0',
                           'method': method,
                           'params': params,
                           'auth': (self.auth if hasattr(self, 'auth') else None),
                           'id': self.request_id})
        self.logger.info('URL:%s\tMETHOD:%s\tPARAM:%s', self.host, method, str(params))
        try:
            r = requests.post(self.host, data=data, headers=headers)
            self.logger.info('STATUS_CODE:%s', r.status_code)
            return r.json()['result']
        except Exception as e:
            self.logger.error('TYPE:%s\tMESSAGE:%s', str(type(e)), e.args)

