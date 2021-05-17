function populate(s1,s2){
    var s1=document.getElementById(s1);
    var s2=document.getElementById(s2);
	console.log(s1);
	console.log(s2);
    s2.innerHTML="";
    if(s1.value=="Pakistan"){
        var optionArray=['lahore|Lahore','karachi|Karachi','islamabad|Islamabad','peshawar|Peshawar'];
    }
	else if(s1.value=="Turkey"){
		var optionArray=['istanbul|Istanbul','ankara|Ankara','izmir|Izmir','bursa|Bursa'];
	}
	for(var option in optionArray){
		var pair=optionArray[option].split("|");
		var newoption=document.createElement("option");
		newoption.value=pair[0];
		newoption.innerHTML=pair[1];
		s2.options.add(newoption);
	}


}