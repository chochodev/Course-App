const bgOverlay = document.getElementById('signing-background-overlay');

const signup = document.getElementById('signup');
const signin = document.getElementById('signin');

const signupButton = document.getElementById('signup-button');
const signinButton = document.getElementById('signin-button');
const joinusButton = document.getElementById('joinus-button');

const demoButton = document.getElementById('live-demo-button');
const pricingButton = document.getElementById('pricing-button');
const contactButton = document.getElementById('contact-us-button');

// FOR TOGGLING THE FORMS
signupButton.addEventListener('click', (e) => {
    signup.classList.toggle('un-signup');
    signin.classList.remove('un-signin');
    updateBackgroundOverlay();
})

signinButton.addEventListener('click', (e) => {
    signin.classList.toggle('un-signin');
    signup.classList.remove('un-signup');
    updateBackgroundOverlay();
})

// FOR REMOVING THE FORMS
const my_body = [bgOverlay, demoButton, pricingButton, contactButton]

my_body.forEach(item => {
    item.addEventListener('click', (e) => {
        e.stopPropagation();
        console.log('click triggered')
        signin.classList.remove('un-signin');
        signup.classList.remove('un-signup');
        updateBackgroundOverlay();
    });
});

// FOR SHOWING THE BACKGROUND OVERLAY
const updateBackgroundOverlay = () => {
    if (signup.classList.contains('un-signup') || signin.classList.contains('un-signin')) {
        bgOverlay.classList.add('show-signing-background-overlay');
        console.log('active')
    } else {
        bgOverlay.classList.remove('show-signing-background-overlay');
    }
}

// Toggle the event instead


// FOR THE TOGGLING TO MENUBAR TOGGLE MENU LIST

const menubarBtn = document.getElementById('menu-bar-btn');
const barsIcon = document.getElementById('bars-icon');
const closeIcon = document.getElementById('close-icon');
const menuList = document.getElementById('menu-list');
const menuLinks = document.querySelectorAll('.link');

myArray = [barsIcon, closeIcon, menuList];

[menubarBtn, ...menuLinks].forEach(clickItem => {
    clickItem.addEventListener('click', () => {
        myArray.forEach(item => {
            item.classList.toggle('close');
        });
    });
});


// FOR THE SIGNUP and SIGNIN ERRORS
const errorMessagesDiv = document.getElementById('server_messages');
const errorMessages = document.querySelector('#server_messages.message');

if (errorMessagesDiv) {
    setTimeout(() => {
        errorMessagesDiv.remove()
    }, 5000);
}