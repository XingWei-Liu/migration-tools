# SPDX-FileCopyrightText: 2023 UnionTech Software Technology Co., Ltd.
# SPDX-License-Identifier:   MulanPubL-2.0-or-later
import webview
import json
from func.share import get_sysmig_conf

uos_sysmig_conf = json.loads(get_sysmig_conf())
ip = json.loads(uos_sysmig_conf).get('serverip').strip()[1:-1]
port = int(json.loads(uos_sysmig_conf).get('serverport').strip()[1:-1])
url = 'http://%s' % ip + ':%s' % port
title = '统信服务器系统迁移软件'
webview.create_window(title, url, width=1200, height=525)
webview.start()

