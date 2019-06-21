/*
function writeSummary() {
  $("#summary").append("Your vacation is to: " + $("#where_1")[0].value + ", "
+ $("#where_2")[0].value);
}

$("#summaryButton").click(writeSummary); */
function converMsToDays(input){
  input = input/1000 / 60 /60 /24;
  return input;
}


let timeTotal = 0;

function writeSummary() {
  let place1 = $("#where_1")[0].value;
  let time1 = converMsToDays($("#end1")[0].valueAsNumber - $("#start1")[0].valueAsNumber);
  timeTotal = timeTotal + time1;
  let text = "";
  text = place1 + " for " +time1 + " days";

  $("#summary").append(text+ ", ");
  $("#days").empty();
  $("#days").append("You will be gone for " + timeTotal + " days in total");
}



function initializeJs() {
  $("#summaryButton").click(writeSummary);
}
$(document).ready(initializeJs);
