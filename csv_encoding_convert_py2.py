#! python2
# -*- coding=utf-8 -*-

import chardet
stream = open(u'成员分组及每周工作进度.csv', 'r').read()
charset = chardet.detect(stream)['encoding']
open(u'成员分组及每周工作进度.csv', 'w').write(stream.decode(charset).encode('utf_8_sig'))
print u'原编码为%s，已经调整为UTF8-BOM' % (charset if charset != 'UTF-8-SIG' else 'UTF8-BOM')
