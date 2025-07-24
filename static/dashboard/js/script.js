document.addEventListener("DOMContentLoaded", () => {
  const themeToggle = document.getElementById("theme-toggle");
  const html = document.documentElement;
  const userbar = document.getElementById("userbar");
  const userDropdown = document.getElementById("user-dropdown");

  // === Theme toggle ===
  const savedTheme = localStorage.getItem("theme") || "light";
  html.setAttribute("data-theme", savedTheme);
  if (themeToggle) {
    themeToggle.textContent = savedTheme === "dark" ? "☀️" : "🌙";
    themeToggle.addEventListener("click", () => {
      const next = html.getAttribute("data-theme") === "dark" ? "light" : "dark";
      html.setAttribute("data-theme", next);
      localStorage.setItem("theme", next);
      themeToggle.textContent = next === "dark" ? "☀️" : "🌙";
    });
  }

  // === Dropdown toggle ===
  if (userbar && userDropdown) {
    userbar.addEventListener("click", (e) => {
      e.stopPropagation();
      userDropdown.classList.toggle("open");
    });

    document.addEventListener("click", (e) => {
      if (!userbar.contains(e.target)) {
        userDropdown.classList.remove("open");
      }
    });
  }
});
