if (window.location.pathname === '/') {
    document.body.classList.add('hide-sidebar');
}

const blogHeader = document.getElementById('__nav_2_label');
if (blogHeader) {
    blogHeader.remove();
}