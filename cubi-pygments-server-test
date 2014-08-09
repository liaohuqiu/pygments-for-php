import time

import gevent.monkey
gevent.monkey.patch_all()
import cubi.proxy as proxy
import cubi.logger as logger

if __name__ == '__main__':
    logger.enable_debug_log()
    endp = 'pygments@tcp::2016'
    print 'start test for ', endp
    prx = proxy.Proxy(endp, True)

    data = {'code': '<?php phpinfo?>', 'lang': 'php'}
    r = prx.request('highlight', data)
    print r
