function toggleMenu() {
    document.getElementById('navLinks').classList.toggle('show');
}

function updateAuthButton() {
    const btn = document.getElementById('authBtn');
    if (!btn) return;
    const customer = localStorage.getItem('customerName');
    if (customer) {
        btn.textContent = customer;
        btn.href = '#';
        btn.onclick = function() {
            if (confirm('Logout?')) {
                localStorage.clear();
                window.location.href = 'index.html';
            }
        };
    }
}

function updateCartCount() {
    const badge = document.getElementById('cartCount');
    if (!badge) return;
    const customer = localStorage.getItem('customerName');
    if (!customer) { badge.textContent = ''; return; }
    fetch('/api/cart/?customer=' + encodeURIComponent(customer))
        .then(res => res.json())
        .then(data => {
            badge.textContent = data.length > 0 ? data.length : '';
        });
}

function getCustomer() {
    return localStorage.getItem('customerName');
}

function isLoggedIn() {
    return !!localStorage.getItem('customerName');
}
