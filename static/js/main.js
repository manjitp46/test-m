$(document).ready(function() {
	$(window).load(function() {
		$('#myModal').modal('show');
	});
	
});
var host = "http://localhost:8000";
var port = "8000";	

function submitCity(city_id) {
	$('#city').val=city_id;
	return false;
	//	data = {
//			'id': city_id
//	}
//	$.ajax({
//        url: host+"/listmovie/index",
//        method:'post',
//        data: JSON.stringify(data),
//        dataType: 'json',
//        success: function(data){
//        	console.log(data);
//        	windows.reload()
//        },
//        error: function(err){
//        	console.log(host+"/listmovie/index")
//        	console.log(err)
//        }
//    });
}
function makeCalender() {
	div = $('date-container')
	date = new Date();
	today = date.getDate();
	for(var i = 0; i<7; i++) {
		dayname = nameOfDay((date.getDay)+i);
		dateInDigit = today+i;
		console.log(dateInDigit, dayname)
	}
	
	
}

function nameOfDay(day){
	var days = ['SUN', 'MON', 'TUE', 'WED', 'THRU', 'FIR', 'SAT'];
	return days[day%7]
}


