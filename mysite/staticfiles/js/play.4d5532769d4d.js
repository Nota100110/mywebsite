const options = {
  //root: null;
  //root: document.documentElement
  //threshold: 0.5,
  //rootMargin: "-150px"
};

//navbar
const menu = document.querySelector('#mobile-menu');
const menuLinks = document.querySelector('.navbar__menu');

menu.addEventListener('click', () => {
    console.log('Menu clicked');
    menu.classList.toggle('is-active');
    menuLinks.classList.toggle('active');
});

window.addEventListener('click', (event) => {
    if (!menuLinks.contains(event.target) && !menu.contains(event.target)) {
      console.log('Clicked outside of menu');
      menu.classList.remove('is-active');
      menuLinks.classList.remove('active');
    }
});

// Get the circular cursor element
var cursor = document.getElementById("circularcursor");

// Set the body cursor to none
document.body.style.cursor = "none";

// Set the position of the circular cursor based on mouse movement
document.addEventListener("mousemove", function(e) {
  var x = e.clientX;
  var y = e.clientY;
  cursor.style.left = x + "px";
  cursor.style.top = y + window.pageYOffset + "px";
});

// scrolling animation
function reveal() {
    var reveals = document.querySelectorAll(".reveal");
  
    for (var i = 0; i < reveals.length; i++) {
      var windowHeight = window.innerHeight;
      var elementTop = reveals[i].getBoundingClientRect().top;
      var elementVisible = 150;
  
      if (elementTop < windowHeight - elementVisible) {
        reveals[i].classList.add("active");
      } else {
        reveals[i].classList.remove("active");
      }
    }

    var textBoxSpans = document.querySelectorAll('.text-box span');

    for (var i = 0; i < textBoxSpans.length; i++) {
      var windowHeight = window.innerHeight;
      var elementTop = textBoxSpans[i].getBoundingClientRect().top;
      var elementVisible = 150;
  
      if (elementTop < windowHeight - elementVisible) {
        textBoxSpans[i].classList.add("visible");
      } else {
        textBoxSpans[i].classList.remove("visible");
      }
    }

}

window.addEventListener("scroll", reveal);

//animate text

// Select the text box span elements
//const textBoxSpans = document.querySelectorAll('.text-box span');

// Create a new Intersection Observer
//const observer = new IntersectionObserver(function (entries, observer) {
//  entries.forEach(entry => {
//    //console.log(entry);
//    if(entry.isIntersecting) {
//      entry.target.classList.add('visible');
//    } else {
//      entry.target.classList.remove('visible');
//    }
//  });
//}, options);

// Loop through each text box span element and observe it
//textBoxSpans.forEach(textBoxSpan => {
//  observer.observe(textBoxSpan);
//});

//textBoxSpans.addEventListener("scroll", ;
