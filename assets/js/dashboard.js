document.addEventListener("DOMContentLoaded", function () {
    const sidebar = document.getElementById("sidebar");
    const toggleButton = document.getElementById("sidebarToggle");

    toggleButton.addEventListener("click", function () {
        if (window.innerWidth <= 768) {
            sidebar.classList.toggle("mobile-show");
        } else {
            sidebar.classList.toggle("collapsed");
        }
    });

    document.addEventListener("click", function (event) {
        if (
            window.innerWidth <= 768 &&
            sidebar.classList.contains("mobile-show") &&
            !sidebar.contains(event.target) &&
            !toggleButton.contains(event.target)
        ) {
            sidebar.classList.remove("mobile-show");
        }
    });
});