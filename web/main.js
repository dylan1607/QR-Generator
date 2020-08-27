function addition(){
    var data1 = document.getElementById("num1").value
    var data2 = document.getElementById("num2").value
    eel.add()(callBack)
}
function callBack(result){
    document.getElementById("ans").value=result
}