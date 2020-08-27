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

import os

import ConfigParser

script_dir = os.path.dirname(os.path.realpath(__file__))
config = ConfigParser.ConfigParser()
config.readfp(open(os.path.join(script_dir, 'download.ini')))

orientdbHome = '/data/orientdb'
orientdbConfPath = orientdbHome + '/config'

orientdbTarUrl = config.get('download', 'orientdb_tar_url')
orientdbTarName = orientdbTarUrl.split('/')[-1]

# 使用阿里云ECS时,挂载的硬盘不支持ftruncate的情况下,需要加-Dstorage.disk.useNativeOsAPI=false,详情 https://github.com/orientechnologies/orientdb/issues/9278
startCmd = 'nohup ./bin/dserver.sh -Dstorage.disk.useNativeOsAPI=false > orientdb.out 2>&1 &'
