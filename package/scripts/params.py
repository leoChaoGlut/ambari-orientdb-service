#!/usr/bin/env python
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

from resource_management.libraries.script.script import Script

# config object that holds the configurations declared in the config xml file
config = Script.get_config()

custom_properties = config['configurations']['custom.properties']

automatic_backup_json = config['configurations']['automatic-backup.json']
custom_sql_functions_json = config['configurations']['custom-sql-functions.json']
default_distributed_db_config_json = config['configurations']['default-distributed-db-config.json']
hazelcast_xml = config['configurations']['hazelcast.properties']
jdbc_drivers_json = config['configurations']['jdbc-drivers.json']
orientdb_client_log_properties = config['configurations']['orientdb-client-log.properties']
orientdb_etl_log_properties = config['configurations']['orientdb-etl-log.properties']
orientdb_server_config_xml = config['configurations']['orientdb-server-config.properties']
orientdb_server_log_properties = config['configurations']['orientdb-server-log.properties']
security_json = config['configurations']['security.json']

host_info = config['clusterHostInfo']
host_level_params = config['hostLevelParams']
java_home = host_level_params['java_home']
