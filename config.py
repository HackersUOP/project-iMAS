# Copyright 2016 Hackers' Club, University Of Peradeniya
# Author : Tharinda Ehelepola, E/11/105
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
from modules.image_analytic_app.app import *
from modules.serverapp.app import *

image_analytic_app.config.from_object(__name__)
image_analytic_app.secret_key = os.urandom(24)
image_analytic_app.debug = True

server_app.config.from_object(__name__)
server_app.secret_key = os.urandom(24)
server_app.debug = True

