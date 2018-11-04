// Copyright 2018 Bowen Zhang
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

function calculateSum() {
	var service = new proto.CalculatorClient('http://' + window.location.hostname + ':50052');
	var request = new proto.Request();
	request.setClientName(document.getElementById('ClientName').value);
	request.setValuesList(document.getElementById('Values').value.split(',').map(x => parseInt(x)));
	console.log(request);
	service.sum(request, {}, function(err, response) {
		console.log(err);
		document.getElementById('Result').innerText = response.getMessage();
	});
}

document.getElementById('Sum').addEventListener('click', calculateSum);
