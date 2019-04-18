function search()
{
	//var sql = require('sql.js');
	//var db = new sql.Database('../../doorLog/doorLog.db')

	var hrs = $("#timeH").val();
	var mins = $("#timeM").val();
	var secs = $("#timeS").val();
	console.log(hrs + ":" + mins + ":" + secs);

	var d = new Date();
	var dateToSearch = new Date(d.getFullYear(), d.getMonth(), d.getDate(), hrs, mins, secs, 0);
	var uDateToSearch = dateToSearch.toUTCString();
	uDateToSearch = Date.parse(uDateToSearch);
	uDateToSearch = uDateToSearch/1000;

	console.log(uDateToSearch);

	$.getJSON('/searchResults?nixTime=' + uDateToSearch, function(data) {
		var push = $("<h1></h1>").text("Result :" + data).attr({id: '#push'});
		push.appendTo("#resultShower");
	})

	//var res = db.exec(sqlStr);

	//console.log(res);

}
