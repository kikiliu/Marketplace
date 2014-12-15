function newEvent() {
	var eventType = document.getElementById("event-type").value;
	var eventTitle = document.getElementById("event-title").value;
	var eventDescription = document.getElementById("event-description").value;
	var coinAmount = document.getElementById("coin-amount").value;
	var startDate = document.getElementById("start-date").value;
	var startTime = document.getElementById("start-time").value;
	var endDate = document.getElementById("end-date").value;
	var endTime = document.getElementById("end-time").value;
	var eventCity = document.getElementById("event-city").value;
	var eventState = document.getElementById("event-state").value;


	document.getElementById("event-type").value = "";
	document.getElementById("event-title").value = "";
	document.getElementById("event-description").value = "";
	document.getElementById("coin-amount").value = "";
	document.getElementById("start-date").value = "";
	document.getElementById("start-time").value = "";
	document.getElementById("end-date").value = "";
	document.getElementById("end-time").value = "";
	document.getElementById("event-city").value = "";
	document.getElementById("event-state").value = "";


	var table = document.getElementById("event_table");
	var row = table.insertRow(1);
	var cell0 = row.insertCell(0);
	var cell1 = row.insertCell(1);
	var cell2 = row.insertCell(2);
	var cell3 = row.insertCell(3);


	cell0.innerHTML = eventTitle;
	cell1.innerHTML = coinAmount;
	cell2.innerHTML = document.getElementById("td1").innerHTML;
	cell3.innerHTML = endTime;
};


function showProfile() {
	document.getElementById("event").style.display = 'none';
	document.getElementById("profile").style.display = 'inline';
};


function showEvent() {
	document.getElementById("event").style.display = 'inline';
	document.getElementById("profile").style.display = 'none';	
}

function editProfile(){
	document.getElementById("first-name").value = document.getElementById("td1").innerHTML;
	document.getElementById("last-name").value = document.getElementById("td2").innerHTML;
	document.getElementById("email").value = document.getElementById("td3").innerHTML;
	document.getElementById("phone-number").value = document.getElementById("td5").innerHTML;
	document.getElementById("address-1").value = document.getElementById("td6").innerHTML;
	document.getElementById("address-2").value = document.getElementById("td7").innerHTML;
	document.getElementById("profile-postal").value = document.getElementById("td8").innerHTML;
	document.getElementById("profile-city").value = document.getElementById("td9").innerHTML;
	document.getElementById("profile-state").value = document.getElementById("td10").innerHTML;
}

function updateProfile(){
	document.getElementById("td1").innerHTML = document.getElementById("first-name").value;
	document.getElementById("td2").innerHTML = document.getElementById("last-name").value;
	document.getElementById("td3").innerHTML = document.getElementById("email").value;
	document.getElementById("td5").innerHTML = document.getElementById("phone-number").value;
	document.getElementById("td6").innerHTML = document.getElementById("address-1").value;
	document.getElementById("td7").innerHTML = document.getElementById("address-2").value;
	document.getElementById("td8").innerHTML = document.getElementById("profile-postal").value;
	document.getElementById("td9").innerHTML = document.getElementById("profile-city").value;
	document.getElementById("td10").innerHTML = document.getElementById("profile-state").value;

}
