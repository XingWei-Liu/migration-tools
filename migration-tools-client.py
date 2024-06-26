# SPDX-FileCopyrightText: 2023 UnionTech Software Technology Co., Ltd.
# SPDX-License-Identifier:   MulanPubL-2.0-or-later
import json
from flask import Flask, request, Response
from func.share import *
from urls import agent_mods

app = Flask(__name__)


def check_methods():
    if request.method == 'POST':
        data = request.get_data()
        json_data = json.loads(data)
        mod = agent_mods.get(json_data['mod'])
        if mod:
            response_str = mod(data)
            return response_str


@app.route('/check_environment', methods=['GET', 'POST'])
def mt_check_environment():
    mod = check_methods()
    if mod:
        return Response(mod, content_type='application/json')


@app.route('/check_storage', methods=['GET', 'POST'])
def mt_check_storage():
    mod = check_methods()
    if mod:
        return Response(mod, content_type='application/json')


@app.route('/check_os', methods=['GET', 'POST'])
def mt_check_os():
    mod = check_methods()
    if mod:
        return Response(mod, content_type='application/json')


@app.route('/check_progress', methods=['GET', 'POST'])
def mt_check_progress():
    mod = check_methods()
    if mod:
        return Response(mod, content_type='application/json')


@app.route('/check_user', methods=['GET', 'POST'])
def mt_check_user():
    mod = check_methods()
    if mod:
        return Response(mod, content_type='application/json')


@app.route('/check_repo', methods=['GEt', 'POST'])
def mt_check_repo():
    mod = check_methods()
    if mod:
        return Response(mod, content_type='application/json')


@app.route('/check_os_kernel', methods=['GET', 'POST'])
def mt_check_os_kernel():
    mod = check_methods()
    if mod:
        return Response(mod, content_type='application/json')


@app.route('/check_repo_kernel', methods=['GET', 'POST'])
def mt_check_repo_kernel():
    mod = check_methods()
    if mod:
        return Response(mod, content_type='application/json')


@app.route('/check_migration_progress', methods=['GET', 'POST'])
def mt_check_migration_progress():
    mod = check_methods()
    if mod:
        return Response(mod, content_type='application/json')


@app.route('/export_migration_reports', methods=['GET', 'POST'])
def mt_export_migration_reports():
    mod = check_methods()
    if mod:
        return Response(mod, content_type='application/json')


@app.route('/migration_details', methods=['GET', 'POST'])
def mt_migration_details():
    mod = check_methods()
    if mod:
        return Response(mod, content_type='application/json')


@app.route('/system_migration', methods=['GET', 'POST'])
def mt_system_migration():
    mod = check_methods()
    if mod:
        return Response(mod, content_type='application/json')


if __name__ == '__main__':
    app.config["JSON_AS_ASCII"] = False
    uos_sysmig_conf = json.loads(get_sysmig_conf())
    ip = json.loads(uos_sysmig_conf).get('agentip').strip()[1:-1]
    port = int(json.loads(uos_sysmig_conf).get('agentport').strip()[1:-1])
    app.run(debug=True, host=ip, port=port)
