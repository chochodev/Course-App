const coursesNavbar = document.getElementById('courses-navbar');
const coursesMenubar = document.getElementById('courses-menubar');
const coursesNavbarClose = document.getElementById('close-courses-navbar');
const coursesPage = document.getElementById('courses-page');

coursesMenubar.addEventListener('click', ()=>{
    coursesNavbar.classList.toggle('uncourse-nav');
    coursesPage.style.overflow == 'hidden';
});

coursesNavbarClose.addEventListener('click', ()=>{
    coursesNavbar.classList.remove('uncourse-nav');
});