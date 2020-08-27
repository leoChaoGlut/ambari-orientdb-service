# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os.path as path

from common import orientdbHome, orientdbConfPath, orientdbTarUrl, orientdbTarName, startCmd
from resource_management.core.exceptions import ExecutionFailed, ComponentIsNotRunning
from resource_management.core.resources.system import Execute
from resource_management.libraries.script.script import Script


class WebServer(Script):
    def install(self, env):
        tmpOrientdbTarPath = '/tmp/' + orientdbTarName
        Execute('mkdir -p {0}'.format(orientdbHome))
        Execute('wget --no-check-certificate {0} -O {1}'.format(orientdbTarUrl, tmpOrientdbTarPath))
        Execute('tar -xf {0} -C {1} --strip-components=1'.format(tmpOrientdbTarPath, orientdbHome))

    def stop(self, env):
        Execute(orientdbHome + '/bin/shutdown.sh')

    def start(self, env):
        self.configure(env)

        Execute('cd ' + orientdbHome + ' && ' + startCmd)

    def status(self, env):
        try:
            Execute(orientdbHome + '/bin/orientdb.sh status')
        except ExecutionFailed as ef:
            if ef.code == 3:
                raise ComponentIsNotRunning("ComponentIsNotRunning")
            else:
                raise ef

    def configure(self, env):
        from params import automatic_backup_json, custom_sql_functions_json, \
            default_distributed_db_config_json, hazelcast_xml, jdbc_drivers_json, orientdb_client_log_properties, \
            orientdb_etl_log_properties, orientdb_server_config_xml, orientdb_server_log_properties, security_json

        with open(path.join(orientdbConfPath, 'automatic-backup.json.xml'), 'w') as f:
            if automatic_backup_json.has_key('content'):
                f.write(str(automatic_backup_json['content']))

        with open(path.join(orientdbConfPath, 'custom-sql-functions.json.xml'), 'w') as f:
            if custom_sql_functions_json.has_key('content'):
                f.write(str(custom_sql_functions_json['content']))

        with open(path.join(orientdbConfPath, 'default-distributed-db-config.json.xml'), 'w') as f:
            if default_distributed_db_config_json.has_key('content'):
                f.write(str(default_distributed_db_config_json['content']))

        with open(path.join(orientdbConfPath, 'hazelcast.xml.xml'), 'w') as f:
            if hazelcast_xml.has_key('content'):
                f.write(str(hazelcast_xml['content']))

        with open(path.join(orientdbConfPath, 'jdbc-drivers.json.xml'), 'w') as f:
            if jdbc_drivers_json.has_key('content'):
                f.write(str(jdbc_drivers_json['content']))

        with open(path.join(orientdbConfPath, 'orientdb-client-log.properties.xml'), 'w') as f:
            if orientdb_client_log_properties.has_key('content'):
                f.write(str(orientdb_client_log_properties['content']))

        with open(path.join(orientdbConfPath, 'orientdb-etl-log.properties.xml'), 'w') as f:
            if orientdb_etl_log_properties.has_key('content'):
                f.write(str(orientdb_etl_log_properties['content']))

        with open(path.join(orientdbConfPath, 'orientdb-server-config.xml.xml'), 'w') as f:
            if orientdb_server_config_xml.has_key('content'):
                f.write(str(orientdb_server_config_xml['content']))

        with open(path.join(orientdbConfPath, 'orientdb-server-log.properties.xml'), 'w') as f:
            if orientdb_server_log_properties.has_key('content'):
                f.write(str(orientdb_server_log_properties['content']))

        with open(path.join(orientdbConfPath, 'security.json.xml'), 'w') as f:
            if security_json.has_key('content'):
                f.write(str(security_json['content']))


if __name__ == '__main__':
    WebServer().execute()
