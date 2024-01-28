// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();

var myModal = document.getElementById('myModal')
var myInput = document.getElementById('myInput')

myModal.addEventListener('shown.bs.modal', function () {
  myInput.focus()
})

var toastElist = [].slice.call(document.querySelectorAll('.toast'))
var toastlist = toastElist.map(function(toastEL){
  return new bootstrap.Toast(ToastEL,option)
})
