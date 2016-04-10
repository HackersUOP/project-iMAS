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

# libraries
from flask import Flask
from flask_restful import Api

# files
from restfulServices.index import *

app = Flask(__name__)
api = Api(app)

api.add_resource(index, '/')

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
