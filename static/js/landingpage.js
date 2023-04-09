const signup = document.getElementById('signup')
const signin = document.getElementById('signin')

const signupButton = document.getElementById('signup-button')
const signinButton = document.getElementById('signin-button')
const joinusButton = document.getElementById('joinus-button')

const demoButton = document.getElementById('live-demo-button')
const pricingButton = document.getElementById('pricing-button')
const contactButton = document.getElementById('contact-us-button')

signupButton.addEventListener('click', (e) => {
    e.stopImmediatePropagation();
    signup.classList.toggle('un-signup');
    signin.classList.remove('un-signin');
})

signinButton.addEventListener('click', (e) => {
    e.stopImmediatePropagation();
    signin.classList.toggle('un-signin');
    signup.classList.remove('un-signup');
})

const my_body = [signup, signin, demoButton, pricingButton, contactButton]

// my_body.forEach(item => {
//     item.addEventListener('click', (e) => {
//         e.stopImmediatePropagation();
//         signin.classList.remove('un-signin');
//         signup.classList.remove('un-signup');
//     });
// });

// Toggle the event instead