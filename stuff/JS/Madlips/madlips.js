
let adj = ["attractive", "giant","tiny", "bald", "fat", "beautiful" , "chubby", "clean", "stocky","ugly", "unkempt", "unsightly"];
let noun = ["cat", "dog", "cow", "mouse", "bird", "ant"];
function randomWord(word){
  i = Math.floor((Math.random() * word.length - 1) + 1);
  return word[i];
}

function generateSentence (){
    $("#sentence").empty();
  let sentence = "A " + randomWord(adj) + " " + randomWord(adj) +  " "
  + $("#noun")[0].value + " " + $("#verb")[0].value + "s a " + randomWord(adj) +" " + randomWord(noun);
  $("#sentence").append(sentence);
}




function initializeJs() {
  $("#submitbutton").click(generateSentence);
}
$(document).ready(initializeJs);
