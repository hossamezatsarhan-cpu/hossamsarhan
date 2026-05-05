let currentLang = localStorage.getItem("site_lang") || "ar";

function applyLanguage() {
  document.documentElement.lang = currentLang;
  document.documentElement.dir = currentLang === "ar" ? "rtl" : "ltr";

  const bootstrapCss = document.getElementById("bootstrap-css");
  if (bootstrapCss) {
    bootstrapCss.href = currentLang === "ar"
      ? "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.rtl.min.css"
      : "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css";
  }

  document.querySelectorAll("[data-ar]").forEach(el => {
    el.innerText = el.getAttribute(`data-${currentLang}`);
  });

  document.querySelectorAll(".ar-features").forEach(el => {
    el.classList.toggle("d-none", currentLang !== "ar");
  });

  document.querySelectorAll(".en-features").forEach(el => {
    el.classList.toggle("d-none", currentLang !== "en");
  });
}

function switchLanguage() {
  currentLang = currentLang === "ar" ? "en" : "ar";
  localStorage.setItem("site_lang", currentLang);
  applyLanguage();
}

document.addEventListener("DOMContentLoaded", applyLanguage);
