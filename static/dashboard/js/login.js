document.addEventListener("DOMContentLoaded", () => {
  const html = document.documentElement;
  const themeToggle = document.getElementById("theme-toggle");
  const togglePasswordBtn = document.getElementById("toggle-password");
  const passwordInput = document.getElementById("password");
  const confirmInput = document.getElementById("confirm_password");
  const toggleConfirm = document.getElementById("toggle-confirm");

  // 🌙 1. Restore saved theme
  const savedTheme = localStorage.getItem("theme") || "light";
  html.setAttribute("data-theme", savedTheme);
  if (themeToggle) {
    themeToggle.textContent = savedTheme === "dark" ? "☀️" : "🌙";

    // Toggle light/dark
    themeToggle.addEventListener("click", () => {
      const current = html.getAttribute("data-theme");
      const next = current === "dark" ? "light" : "dark";
      html.setAttribute("data-theme", next);
      localStorage.setItem("theme", next);
      themeToggle.textContent = next === "dark" ? "☀️" : "🌙";
    });
  }

  // 🔐 2. Toggle password visibility
  if (togglePasswordBtn && passwordInput) {
    togglePasswordBtn.addEventListener("click", () => {
      const type = passwordInput.type === "password" ? "text" : "password";
      passwordInput.type = type;
      togglePasswordBtn.textContent = type === "password" ? "👁" : "🙈";
    });
  }

  // 🔐 3. Toggle confirm password visibility
  if (toggleConfirm && confirmInput) {
    toggleConfirm.addEventListener("click", () => {
      const type = confirmInput.type === "password" ? "text" : "password";
      confirmInput.type = type;
      toggleConfirm.textContent = type === "password" ? "👁" : "🙈";
    });
  }
});
