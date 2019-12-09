// from data.js
var tableData = data;

// YOUR CODE HERE!
var tbody = d3.select("tbody");

console.log(data);

data.forEach(function(UFOreport) {
	console.log(UFOreport);
	var row = tbody.append("tr");
	Object.entries(UFOreport).forEach(function([key, value]) {
		console.log(key, value);
		var cell = tbody.append("td");
		cell.text(value)
	});
});

var button = d3.select("#filter-btn");
var emptyInput = d3.select("tbody");
button.on("click", function() {
	emptyInput.html("");
	d3.event.preventDefault();
	var inputElement = d3.select("#datetime");
	var inputValue = inputElement.property("value");

	console.log(inputValue);
	console.log(tableData);

	var filteredData = tableData.filter(date => date.datetime === inputValue);
	console.log(filteredData);

	filteredData.forEach(function(tablefilter) {
		console.log(tablefilter);
		var row = tbody.append("tr");
		Object.entries(tablefilter).forEach(function([key, value]) {
			console.log(key, value);
			var cell = tbody.append("td");
			cell.text(value);
		});
	});
});