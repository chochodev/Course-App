const menuButton = document.getElementById('menu-bar');
const closeMenuButton = document.getElementById('menu-bar');

const menulist = document.getElementById('menu-list');
const my_linksButton = document.querySelectorAll('.link');
const my_body = document.getElementById('bg-modal');


const ToggleMenubar = () => {
    menulist.classList.toggle('unmenu-list');
    my_body.classList.toggle('unbg-modal');
};

const RemoveMenubar = () => {
    menulist.classList.remove('unmenu-list');
    my_body.classList.remove('unbg-modal');
};

// For Menu action on link click
const list = [menuButton, ...my_linksButton]

list.forEach(item => {
    item.addEventListener('click', () => {
        RemoveMenubar();
    })
});

// For Menu action on body click
my_body.addEventListener('click', (e) => {
    RemoveMenubar();
});

menuButton.addEventListener('click', ToggleMenubar);
// my_links.addEventListener('click', RemoveMenubar);


// NOTIFICATION SECTION
const notification = document.getElementById('notification');
const addBtn = document.getElementById('notification-link');
const removeBtn = document.getElementById('cancel-btn');
const notificationContent = document.getElementById('notification-body');

// Toggle the display of the notification when the toggle button is clicked
addBtn.addEventListener('click', () => {
    notification.classList.add('show');
});

removeBtn.addEventListener('click', () => {
    notification.classList.remove('show');
});

notification.addEventListener('click', (event) => {
    if (event.target === notification){
        notification.classList.remove('show');
    }
});