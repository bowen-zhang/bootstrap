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
