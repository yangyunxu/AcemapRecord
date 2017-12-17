#! python3
# -*- coding=utf-8 -*-

import chardet
stream = open('成员分组及每周工作进度.csv', 'rb').read()
charset = chardet.detect(stream)['encoding']
if charset == 'GB2312':
	charset = 'GBK'
open('成员分组及每周工作进度.csv', 'wb').write(stream.decode(charset).encode('utf_8_sig'))
print('原编码为%s，已经调整为UTF8-BOM' % (charset if charset != 'UTF-8-SIG' else 'UTF8-BOM'))
