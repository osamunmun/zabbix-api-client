from client import Client


class Maintenance(Client):
    """Zabbix Maintenance API"""

    def create(self, params={}):
        return self.request('maintenance.create', params)

    def delete(self, params={}):
        return self.request('maintenance.delete', params)

    def exists(self, params={}):
        return self.request('maintenance.exists', params)

    def get(self, params={}):
        return self.request('maintenance.get', params)

    def update(self, params={}):
        return self.request('maintenance.update', params)
