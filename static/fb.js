function year() {

    var year = new Date().getFullYear()
    var yroptions = "<option value='0'>year</option>";
    for (i = 1950; i < year + 1; i++) {
        yroptions += "<option value='" + i + "'>" + i + "</option>";
    }

    document.getElementById('dropdownYear').innerHTML = yroptions




    var day = "<option value='0'>day</option>";

    for (i = 1; i < 32; i++) {
        day += "<option value='" + i + "'>" + i + "</option>";
    }
    document.getElementById('day').innerHTML = day


    console.log("hello")


}























// var monthh = "<option value='0'>month</option>";

// var month = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
// var len = month.length
// for (i = 0; i <= 12; i++) {
//     month += "<option value='" + month[i] + "'>" + month[i] + "</option>";
//     console.log(month[i])
// }

// document.getElementById('month').innerHTML = monthh