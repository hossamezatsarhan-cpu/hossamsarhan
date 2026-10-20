let currentLang = "ar";
try { currentLang = localStorage.getItem("site_lang") === "en" ? "en" : "ar"; } catch (_) {}
function applyLanguage() {
  document.documentElement.lang = currentLang;
  document.documentElement.dir = currentLang === "ar" ? "rtl" : "ltr";
  const css = document.getElementById("bootstrap-css");
  if (css) css.href = `https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap${currentLang === "ar" ? ".rtl" : ""}.min.css`;
  document.querySelectorAll("[data-ar][data-en]").forEach(el => { el.textContent = el.getAttribute(`data-${currentLang}`); });
  document.querySelectorAll(".ar-features").forEach(el => el.classList.toggle("d-none", currentLang !== "ar"));
  document.querySelectorAll(".en-features").forEach(el => el.classList.toggle("d-none", currentLang !== "en"));
  document.querySelectorAll(".lang-btn").forEach(el => el.setAttribute("aria-label", currentLang === "ar" ? "Switch to English" : "التبديل إلى العربية"));
  const toggler = document.querySelector(".navbar-toggler");
  if (toggler) toggler.setAttribute("aria-label", currentLang === "ar" ? "فتح القائمة" : "Toggle navigation");
}
function switchLanguage() {
  currentLang = currentLang === "ar" ? "en" : "ar";
  try { localStorage.setItem("site_lang", currentLang); } catch (_) {}
  applyLanguage();
}
document.addEventListener("DOMContentLoaded", () => {
  applyLanguage();
  document.querySelectorAll("#mainNav a").forEach(link => link.addEventListener("click", () => {
    const menu = document.getElementById("mainNav");
    if (menu && window.bootstrap) window.bootstrap.Collapse.getInstance(menu)?.hide();
  }));
});
