function differenceMinMax(array){
  for (i=0; i < array.length; i++){
    var smallestNum = array[i] < array[i+1] ? array[i] : array[i+1];
    var biggestNum = array[i] > array[i+1] ? array[i] : array[i+1];
  }
  document.getElementById(yep , smallestNum + " " + biggestNum);
  return Math.abs(biggestNum-smallestNum);
}

differenceMinMax([1,2,3]);