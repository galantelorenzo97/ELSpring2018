var count = 0;

setInterval(()=>{
	$.getJSON('/count', function(data) {
		if(count < data['data']) createTables();
	})
}, 5000)

function createTables() {
    $.getJSON('/catch', function(data) {
	    
	var doorTable = $('<table></table>').attr({ id: "doorTable" });
    
    var head = $('<tr></tr>').attr({ class: ['head'].join(' ')}).appendTo(doorTable);
		$('<td></td>').text('Time').appendTo(head);
		$('<td></td>').text('State').appendTo(head);	

	state = "";
	var total_in_room = data[0][2];

	$("doorTable tr").remove();
	$("#count").remove();

	for (var line in data) {
		var row = $('<tr></tr>').attr({ class: "row-class" }).appendTo(doorTable);
			row.appendTo(doorTable)
			$('<td></td>').text(data[line][0]).appendTo(row);
			$('<td></td>').text(data[line][1]).appendTo(row);
			$('<td></td>').text(data[line][2]).appendTo(row);

		console.log(data[line]);
		count++;            
        }
    
    var count = $("<h1></h1>").text("Current state: " + "").attr({id: '#count'}).appendTo("#table");
	doorTable.appendTo("#doorTable")
    })
}
