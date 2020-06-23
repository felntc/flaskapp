//
// Calculator
//
function plotbtc() {
// Buid query parameter
    var param = {};
    param["start"] = document.getElementById("start").value;
    param["end"] = document.getElementById("end").value;
    var query = jQuery.param(param);

// Query with a new parameter 
    $.get("/plot/btc" + "?" + query, function(data) {
        document.getElementById("plotimg").src = data;
    });
};
//
// Register Event handler
//
document.getElementById("plot").addEventListener("click", function(){
    plotbtc();
}, false);
plotbtc();
