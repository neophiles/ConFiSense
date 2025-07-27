function showDashboard() {
    const home = document.getElementById('home');
    const dashboard = document.getElementById('dashboard');

    home.classList.add('hidden');
    dashboard.classList.remove('hidden');
}

function showHome() {
    const home = document.getElementById('home');
    const dashboard = document.getElementById('dashboard');

    home.classList.remove('hidden');
    dashboard.classList.add('hidden');
}