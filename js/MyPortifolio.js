const navMenu = document.getElementById('nav-menu'),
    navToggle = document.getElementById('nav-toggle'),
    navClose = document.getElementById('nav-close');

if (navToggle) {
    navToggle.addEventListener('click', () => { navMenu.classList.add('show-menu') })
}
if (navClose) {
    navClose.addEventListener('click', () => { navMenu.classList.remove('show-menu') })
}

const navLink = document.querySelector('.nav-link');

function linkAcao() {
    const navMenu = document.getElementById('nav-menu')
    navMenu.classlist.remove('show-menu')
}
navLink.forEach(n => n.addEventListener('click', linkAcao))