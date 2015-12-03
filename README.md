[![Circle CI](https://circleci.com/gh/osamunmun/zabbix-api-client/tree/master.svg?style=svg)](https://circleci.com/gh/osamunmun/zabbix-api-client/tree/master)


# zabbix-api-client
- zabbix 2.2.9 confirmed

# Sample
##CLI

```mode_change.py
#!/usr/bin/env python
from zabbix_api_client.maintenance import Maintenance
import sys

#'active_since': '2030-10-11T13:50:40+09:00'
#'active_till': '2030-11-19T13:50:40+09:00'
def main(active_since, active_till):
    c = Maintenance(host='https://example.com', user='foo', password='bar', groupids='', log_level='INFO')
    c.update({'maintenanceid': '20','name': 'Test', 'active_since': active_since, 'active_till': active_till})


if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2])
```

# Refrence
- [zabbix api Reference](https://www.zabbix.com/documentation/2.2/manual/api/reference)
