const menu = document.querySelector('#menu');
const more_button = document.querySelector('#more_button');
const sidebar = document.querySelector('.sidebar');
const subsidebar = document.querySelector('.sidebar_more');
const div_register = document.getElementById("div_register");
menu.addEventListener('click', function () {
  sidebar.classList.toggle('shortly-sidebar');
  if(sidebar.classList.contains('shortly-sidebar')){
     if(window.innerWidth>2559){
     setTimeout('div_register.style.width = "97%";',1);
     setTimeout('div_register.style.position ="fixed";',175);
     setTimeout('div_register.style.left ="60px";',175);
     setTimeout('div_register.style.zIndex = "0";',175);
     }else if(window.innerWidth > 1439 && window.innerWidth < 2560){
      setTimeout('div_register.style.width = "94.8%";',1);
      setTimeout('div_register.style.position ="fixed";',175);
      setTimeout('div_register.style.left ="60px";',175);
      setTimeout('div_register.style.zIndex = "0";',175);
    }else if(window.innerWidth > 1023 && window.innerWidth < 1440){
     setTimeout('div_register.style.width = "93.5%";',1);
     setTimeout('div_register.style.position ="fixed";',175);
     setTimeout('div_register.style.left ="60px";',175);
     setTimeout('div_register.style.zIndex = "0";',175);
     }
     else if(window.innerWidth >768 &&window.innerWidth <1024){
     setTimeout('div_register.style.width = "94.6%";',1);
     setTimeout('div_register.style.position ="fixed";',175);
     setTimeout('div_register.style.left ="60px";',175);
     setTimeout('div_register.style.zIndex = "0";',175);
     }else if(window.innerWidth > 425 && window.innerWidth < 769) {
      setTimeout('div_register.style.width = "90.2%";',1);
      setTimeout('div_register.style.position ="fixed";',175);
      setTimeout('div_register.style.left ="60px";',175);
      setTimeout('div_register.style.zIndex = "0";',175);
     }else if(window.innerWidth < 426){
      div_register.style.width = "92%";
      div_register.style.position ="fixed";
     }
  }else{
    setTimeout('div_register.style.width = "";',270);
    div_register.style.position ="";
    div_register.style.left ="";
    div_register.style.zIndex = "";
  }
});

// more_button.addEventListener('click', function(){
//   subsidebar.classList.toggle('open-moretab');
//   if(more_button.innerText === "More"){
//     document.getElementById("test_more").innerHTML = "Less";
//   } else {
//     document.getElementById("test_more").innerHTML = "More";
//   }
// });

var btnContainer = document.getElementById("sidebar");
var btns = btnContainer.getElementsByClassName("btn");

for(var i =0; i<btns.length;i++){
  btns[i].addEventListener('click', function(){
  var current = document.getElementsByClassName("active");
  current[0].className = current[0].className.replace(" active");
  this.className += " active";
  })
}

const triangle_head = document.querySelector('#triangle_head');
const div_test = document.querySelectorAll('.picture_header');
triangle_head.addEventListener('click', function(){
  div_test[1].classList.toggle('open_header_icon');
});

$(document).ready(function () {
  $('#example').DataTable();
});



