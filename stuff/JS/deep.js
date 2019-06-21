let numbers =[2,5,6,7,1231,634];
let people = ["a", "b", "c","d", "e", "f", "g"];
function reverseList(list){
  let result = [];
  for(let i = list.length -1; i >= 0; i--){
      result.push(list[i]);
  }
  return result;
}

function findMinimumValue(list) {
  //given any array named list
  //find the max value in the list
  let maxSoFar = 0;
  for(let i = 0; i < list.length; i++){
    while (maxSoFar < list[i]){
      maxSoFar = list[i];
    }
  }
  let minSoFar = maxSoFar;
  for(let k = 0; k < list.length; k++){
    if(minSoFar > list[k]){
      minSoFar= list[k];
    }
  }
  return minSoFar;
}


function niceRegularBox(lines) {
  let maxSoFar = 0;
  for(let i = 0; i < lines.length; i++){
    if (maxSoFar < lines[i].length){
      maxSoFar=lines[i].length;
    }
  }

  let line1 = "-";
  let space = " ";
    line1 = line1.repeat(maxSoFar + 2);
  console.log("+" +line1 + "+");
  for(let k = 0; k < lines.length; k++){
    let space1 = maxSoFar - lines[k].length;
    console.log("+ "+lines[k]+ space.repeat(space1) + " +");
  }
  console.log("+" +line1 + "+");
}


 function square(square){
   let results = 2 ** (square -1);
   return results;
 }
function total(number){
  let results = 2 ** number -1;
  return results;
  }
/*
function pressFloorNumber(floor){
  elevatorLine.push(floor);
  return ("Position " + elevatorLine.length);
}

function goToNextFloor(input){
  if(elevatorLine.length > 0){
    console.log("Floor " + elevatorLine[0]);
    elevatorLine.splice(0 ,1);
  }else{
    console.log("There are no more floors to go to!");
  }
}

function currentLine(input1){
  if(elevatorLine.length > 0){
    let hehe = [];
    for(let i = 0; i < input1.length; i++){
      hehe.push(" Floor " + input1[i]);
    }
    console.log("The Line is currently:" + hehe);
  }else{
    console.log("The line is currently empty!");
}
} */
function pressFloorNumber(floor){
  elevatorLine.push(floor);
  return ("Position " + elevatorLine.length);
}

function goToNextFloor(input){
  if(elevatorLine.length > 0){
    console.log("Floor " + elevatorLine[elevatorLine.length - 1]);
    elevatorLine.splice(elevatorLine.length - 1 ,1);
  }else{
    console.log("There are no more floors to go to!");
  }
}

function currentLine(input1){
  if(elevatorLine.length > 0){
    let hehe = [];
    for(let i = input1.length - 1; i >= 0; i--){
      hehe.push(" Floor " + input1[i]);
    }
    console.log("The Line is currently:" + hehe);
  }else{
    console.log("The line is currently empty!");
  }
}
