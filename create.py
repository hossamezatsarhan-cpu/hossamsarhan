from pathlib import Path

PROJECT_PATH = Path(r"E:\app\hossam")

css_path = PROJECT_PATH / "assets" / "css"
js_path = PROJECT_PATH / "assets" / "js"
apps_path = PROJECT_PATH / "apps"

css_path.mkdir(parents=True, exist_ok=True)
js_path.mkdir(parents=True, exist_ok=True)
apps_path.mkdir(parents=True, exist_ok=True)

index_html = r'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>مهندس / حسام عزت سرحان</title>

  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.rtl.min.css" rel="stylesheet" id="bootstrap-css">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/style.css" />
</head>

<body>

<nav class="navbar navbar-expand-lg fixed-top modern-nav">
  <div class="container">
    <a class="navbar-brand brand" href="index.html">
      <span class="brand-icon">HS</span>
      <span data-ar="حسام عزت سرحان" data-en="Hossam Ezzat Sarhan">حسام عزت سرحان</span>
    </a>

    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#mainNav">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="mainNav">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0 nav-links">
        <li class="nav-item"><a class="nav-link" href="#home" data-ar="الرئيسية" data-en="Home">الرئيسية</a></li>
        <li class="nav-item"><a class="nav-link" href="#about" data-ar="نبذة" data-en="About">نبذة</a></li>
        <li class="nav-item"><a class="nav-link" href="#apps" data-ar="التطبيقات" data-en="Apps">التطبيقات</a></li>
      </ul>

      <button class="btn lang-btn" onclick="switchLanguage()">
        <i class="bi bi-translate"></i>
        <span>AR / EN</span>
      </button>
    </div>
  </div>
</nav>

<header id="home" class="hero-section">
  <div id="heroSlider" class="carousel slide carousel-fade" data-bs-ride="carousel">

    <div class="carousel-indicators">
      <button type="button" data-bs-target="#heroSlider" data-bs-slide-to="0" class="active"></button>
      <button type="button" data-bs-target="#heroSlider" data-bs-slide-to="1"></button>
    </div>

    <div class="carousel-inner">

      <div class="carousel-item active">
        <div class="hero-slide">
          <img src="assets/images/h1.webp" class="hero-bg" alt="Profile">
          <div class="hero-overlay"></div>

          <div class="container hero-content">
            <div class="row align-items-center min-vh-100">
              <div class="col-lg-7">
                <div class="hero-card animate-up">
                  <span class="hero-badge" data-ar="مهندس تطبيقات ونظم" data-en="Applications & Systems Engineer">
                    مهندس تطبيقات ونظم
                  </span>

                  <h1 data-ar="مهندس / حسام عزت سرحان" data-en="Eng. Hossam Ezzat Sarhan">
                    مهندس / حسام عزت سرحان
                  </h1>

                  <h2 data-ar="مهندس حاسبات ونظم" data-en="Computer and Systems Engineer">
                    مهندس حاسبات ونظم
                  </h2>

                  <p data-ar="كلية الهندسة - جامعة المنصورة" data-en="Faculty of Engineering - Mansoura University">
                    كلية الهندسة - جامعة المنصورة
                  </p>

                  <div class="hero-actions">
                    <a href="#apps" class="btn primary-btn" data-ar="استعراض الأعمال" data-en="View Projects">استعراض الأعمال</a>
                    <a href="#about" class="btn secondary-btn" data-ar="نبذة عني" data-en="About Me">نبذة عني</a>
                  </div>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>

      <div class="carousel-item">
        <div class="hero-slide">
          <img src="assets/images/h2.webp" class="hero-bg" alt="Team Work">
          <div class="hero-overlay"></div>

          <div class="container hero-content">
            <div class="row align-items-center min-vh-100">
              <div class="col-lg-7">
                <div class="hero-card animate-up">
                  <span class="hero-badge" data-ar="قيادة فرق العمل التقنية" data-en="Technical Team Leadership">
                    قيادة فرق العمل التقنية
                  </span>

                  <h1 data-ar="تطوير وتصميم تطبيقات احترافية" data-en="Professional Application Design & Development">
                    تطوير وتصميم تطبيقات احترافية
                  </h1>

                  <p data-ar="حلول رقمية متكاملة تجمع بين جودة التصميم، قوة البرمجة، وتحليل احتياجات المستخدمين لبناء تطبيقات فعالة وقابلة للتطوير."
                     data-en="Integrated digital solutions combining design quality, strong development, and user-focused analysis to build efficient and scalable applications.">
                    حلول رقمية متكاملة تجمع بين جودة التصميم، قوة البرمجة، وتحليل احتياجات المستخدمين لبناء تطبيقات فعالة وقابلة للتطوير.
                  </p>

                  <div class="hero-actions">
                    <a href="#apps" class="btn primary-btn" data-ar="مشاهدة التطبيقات" data-en="Explore Apps">مشاهدة التطبيقات</a>
                  </div>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>

    </div>

    <button class="carousel-control-prev" type="button" data-bs-target="#heroSlider" data-bs-slide="prev">
      <span class="carousel-control-prev-icon"></span>
    </button>

    <button class="carousel-control-next" type="button" data-bs-target="#heroSlider" data-bs-slide="next">
      <span class="carousel-control-next-icon"></span>
    </button>

  </div>
</header>

<section id="about" class="about-section section-padding">
  <div class="container">
    <div class="section-heading">
      <span data-ar="نبذة احترافية" data-en="Professional Profile">نبذة احترافية</span>
      <h2 data-ar="خبرة في بناء حلول برمجية متكاملة" data-en="Experience in Building Integrated Software Solutions">
        خبرة في بناء حلول برمجية متكاملة
      </h2>
      <p data-ar="أمتلك خبرة في تطوير تطبيقات الويب والجوال، وتحليل المتطلبات، وتصميم الأنظمة، وإدارة فرق العمل لتنفيذ حلول رقمية احترافية في التعليم والإدارة والخدمات."
         data-en="Experienced in web and mobile development, requirements analysis, system design, and team leadership to deliver professional digital solutions for education, management, and services.">
        أمتلك خبرة في تطوير تطبيقات الويب والجوال، وتحليل المتطلبات، وتصميم الأنظمة، وإدارة فرق العمل لتنفيذ حلول رقمية احترافية في التعليم والإدارة والخدمات.
      </p>
    </div>

    <div class="row g-4 mt-4">
      <div class="col-md-4">
        <div class="skill-box">
          <i class="bi bi-code-slash"></i>
          <h4 data-ar="تطوير البرمجيات" data-en="Software Development">تطوير البرمجيات</h4>
          <p data-ar="تصميم وتنفيذ تطبيقات ويب وجوال قابلة للتطوير." data-en="Designing scalable web and mobile applications.">
            تصميم وتنفيذ تطبيقات ويب وجوال قابلة للتطوير.
          </p>
        </div>
      </div>

      <div class="col-md-4">
        <div class="skill-box">
          <i class="bi bi-diagram-3"></i>
          <h4 data-ar="تحليل وتصميم الأنظمة" data-en="System Analysis & Design">تحليل وتصميم الأنظمة</h4>
          <p data-ar="تحويل المتطلبات إلى حلول عملية واضحة ومنظمة." data-en="Transforming requirements into clear practical solutions.">
            تحويل المتطلبات إلى حلول عملية واضحة ومنظمة.
          </p>
        </div>
      </div>

      <div class="col-md-4">
        <div class="skill-box">
          <i class="bi bi-people"></i>
          <h4 data-ar="إدارة فرق العمل" data-en="Team Management">إدارة فرق العمل</h4>
          <p data-ar="تنظيم المهام وقيادة فرق التطوير لتحقيق أفضل النتائج." data-en="Organizing tasks and leading teams to achieve high-quality results.">
            تنظيم المهام وقيادة فرق التطوير لتحقيق أفضل النتائج.
          </p>
        </div>
      </div>
    </div>
  </div>
</section>

<section id="apps" class="apps-section section-padding">
  <div class="container">
    <div class="section-heading light">
      <span data-ar="أعمالي" data-en="My Work">أعمالي</span>
      <h2 data-ar="البرامج والتطبيقات المطورة" data-en="Developed Applications & Systems">
        البرامج والتطبيقات المطورة
      </h2>
    </div>

    <div class="row g-4 mt-4">

      <div class="col-lg-4 col-md-6">
        <a href="apps/lms.html" class="project-card">
          <div class="project-img">
            <img src="assets/images/h1.webp" alt="LMS">
          </div>
          <div class="project-content">
            <span class="project-tag" data-ar="تطبيق جوال" data-en="Mobile App">تطبيق جوال</span>
            <h3 data-ar="تطبيق LMS" data-en="LMS Application">تطبيق LMS</h3>
            <p data-ar="إدارة العملية التعليمية للطلاب من خلال الجداول والاختبارات والنتائج والإشعارات."
               data-en="Managing student learning through schedules, exams, results, and notifications.">
              إدارة العملية التعليمية للطلاب من خلال الجداول والاختبارات والنتائج والإشعارات.
            </p>
            <strong data-ar="منصة تعليمية ذكية للطلاب" data-en="Smart learning platform for students">
              منصة تعليمية ذكية للطلاب
            </strong>
          </div>
        </a>
      </div>

      <div class="col-lg-4 col-md-6">
        <a href="apps/smart-exams.html" class="project-card">
          <div class="project-img">
            <img src="assets/images/h2.webp" alt="Smart Exams">
          </div>
          <div class="project-content">
            <span class="project-tag" data-ar="ويب + جوال" data-en="Web + Mobile">ويب + جوال</span>
            <h3 data-ar="تطبيق الاختبارات الذكية" data-en="Smart Exams System">تطبيق الاختبارات الذكية</h3>
            <p data-ar="إدارة الاختبارات إلكترونياً وإنشاء الاختبارات بالذكاء الاصطناعي وإدارة بنك الأسئلة."
               data-en="Electronic exam management with AI exam generation and question bank control.">
              إدارة الاختبارات إلكترونياً وإنشاء الاختبارات بالذكاء الاصطناعي وإدارة بنك الأسئلة.
            </p>
            <strong data-ar="اختبارات رقمية أكثر ذكاءً واحترافية" data-en="Smarter professional digital exams">
              اختبارات رقمية أكثر ذكاءً واحترافية
            </strong>
          </div>
        </a>
      </div>

      <div class="col-lg-4 col-md-6">
        <a href="apps/quran.html" class="project-card">
          <div class="project-img">
            <img src="assets/images/h2.webp" alt="Quran">
          </div>
          <div class="project-content">
            <span class="project-tag" data-ar="ويب + جوال" data-en="Web + Mobile">ويب + جوال</span>
            <h3 data-ar="إدارة حلقات القرآن" data-en="Quran Circles Management">إدارة حلقات القرآن</h3>
            <p data-ar="إدارة الطلاب والحضور والحفظ والمراجعة وتقارير الأداء والمتابعة اليومية."
               data-en="Managing students, attendance, memorization, revision, reports, and daily tracking.">
              إدارة الطلاب والحضور والحفظ والمراجعة وتقارير الأداء والمتابعة اليومية.
            </p>
            <strong data-ar="متابعة دقيقة لحلقات التحفيظ" data-en="Accurate tracking for Quran circles">
              متابعة دقيقة لحلقات التحفيظ
            </strong>
          </div>
        </a>
      </div>

    </div>
  </div>
</section>

<footer class="footer">
  <div class="container">
    <h4 data-ar="مهندس / حسام عزت سرحان" data-en="Eng. Hossam Ezzat Sarhan">مهندس / حسام عزت سرحان</h4>
    <p data-ar="مهندس حاسبات ونظم - تطوير تطبيقات ويب وجوال" data-en="Computer and Systems Engineer - Web & Mobile Development">
      مهندس حاسبات ونظم - تطوير تطبيقات ويب وجوال
    </p>
    <small>© 2026</small>
  </div>
</footer>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
<script src="assets/js/main.js"></script>
</body>
</html>
'''

style_css = r'''@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&display=swap');

:root {
  --primary: #2563eb;
  --secondary: #06b6d4;
  --dark: #07111f;
  --dark-2: #0f172a;
  --text: #334155;
  --muted: #64748b;
  --light: #f8fafc;
  --white: #ffffff;
  --radius: 28px;
  --shadow: 0 24px 80px rgba(15, 23, 42, 0.18);
}

* {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  font-family: 'Cairo', Tahoma, Arial, sans-serif;
  background: var(--light);
  color: var(--text);
  overflow-x: hidden;
}

.modern-nav {
  padding: 16px 0;
  background: rgba(7, 17, 31, 0.75);
  backdrop-filter: blur(18px);
  border-bottom: 1px solid rgba(255,255,255,0.08);
}

.navbar-toggler {
  border: 0;
  filter: invert(1);
}

.brand {
  display: flex;
  align-items: center;
  gap: 12px;
  color: white !important;
  font-weight: 900;
}

.brand-icon {
  width: 46px;
  height: 46px;
  border-radius: 16px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  color: white;
  font-weight: 900;
  box-shadow: 0 12px 28px rgba(37,99,235,0.35);
}

.nav-links .nav-link {
  color: rgba(255,255,255,0.82) !important;
  font-weight: 700;
  margin: 0 6px;
}

.nav-links .nav-link:hover {
  color: white !important;
}

.lang-btn {
  border: 1px solid rgba(255,255,255,0.25);
  color: white;
  border-radius: 999px;
  padding: 10px 18px;
  font-weight: 800;
}

.lang-btn:hover {
  background: white;
  color: var(--dark);
}

.hero-section,
.hero-slide {
  position: relative;
  min-height: 100vh;
}

.hero-bg {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100vh;
  object-fit: cover;
  transform: scale(1.02);
}

.hero-overlay {
  position: absolute;
  inset: 0;
  background:
    radial-gradient(circle at 20% 35%, rgba(37,99,235,0.35), transparent 34%),
    linear-gradient(90deg, rgba(7,17,31,0.92), rgba(7,17,31,0.68), rgba(7,17,31,0.26));
}

html[dir="rtl"] .hero-overlay {
  background:
    radial-gradient(circle at 80% 35%, rgba(37,99,235,0.35), transparent 34%),
    linear-gradient(270deg, rgba(7,17,31,0.92), rgba(7,17,31,0.68), rgba(7,17,31,0.26));
}

.hero-content {
  position: relative;
  z-index: 2;
}

.hero-card {
  max-width: 760px;
  padding: 46px;
  border-radius: 34px;
  background: rgba(255,255,255,0.10);
  border: 1px solid rgba(255,255,255,0.16);
  backdrop-filter: blur(18px);
  color: white;
  box-shadow: 0 30px 90px rgba(0,0,0,0.26);
}

.hero-badge {
  display: inline-flex;
  padding: 10px 18px;
  border-radius: 999px;
  background: rgba(14,165,233,0.18);
  border: 1px solid rgba(125,211,252,0.35);
  color: #e0f2fe;
  font-weight: 800;
  margin-bottom: 22px;
}

.hero-card h1 {
  font-size: clamp(34px, 5vw, 62px);
  line-height: 1.25;
  font-weight: 900;
  margin-bottom: 18px;
}

.hero-card h2 {
  font-size: clamp(22px, 3vw, 34px);
  color: #bfdbfe;
  font-weight: 800;
  margin-bottom: 14px;
}

.hero-card p {
  font-size: 20px;
  line-height: 1.9;
  color: rgba(255,255,255,0.88);
}

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  margin-top: 28px;
}

.primary-btn,
.secondary-btn {
  border-radius: 999px;
  padding: 13px 28px;
  font-weight: 900;
}

.primary-btn {
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  color: white;
  border: 0;
  box-shadow: 0 18px 38px rgba(37,99,235,0.35);
}

.primary-btn:hover {
  color: white;
  transform: translateY(-2px);
}

.secondary-btn {
  color: white;
  border: 1px solid rgba(255,255,255,0.35);
}

.secondary-btn:hover {
  background: white;
  color: var(--dark);
}

.carousel-control-prev,
.carousel-control-next {
  width: 7%;
}

.carousel-indicators [data-bs-target] {
  width: 34px;
  height: 6px;
  border-radius: 999px;
}

.section-padding {
  padding: 95px 0;
}

.section-heading {
  max-width: 900px;
  margin: auto;
  text-align: center;
}

.section-heading span {
  display: inline-block;
  color: var(--primary);
  background: #dbeafe;
  padding: 9px 18px;
  border-radius: 999px;
  font-weight: 900;
  margin-bottom: 18px;
}

.section-heading h2 {
  font-size: clamp(28px, 4vw, 46px);
  font-weight: 900;
  color: var(--dark-2);
  margin-bottom: 18px;
}

.section-heading p {
  font-size: 21px;
  line-height: 2;
  color: var(--muted);
}

.skill-box {
  height: 100%;
  padding: 34px;
  border-radius: var(--radius);
  background: white;
  box-shadow: 0 20px 55px rgba(15,23,42,0.08);
  transition: 0.35s ease;
  border: 1px solid rgba(226,232,240,0.9);
}

.skill-box:hover {
  transform: translateY(-10px);
  box-shadow: var(--shadow);
}

.skill-box i {
  width: 64px;
  height: 64px;
  border-radius: 22px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  color: white;
  font-size: 30px;
  margin-bottom: 22px;
}

.skill-box h4 {
  font-weight: 900;
  color: var(--dark-2);
  margin-bottom: 12px;
}

.skill-box p {
  color: var(--muted);
  line-height: 1.9;
  margin: 0;
}

.apps-section {
  background:
    radial-gradient(circle at top right, rgba(37,99,235,0.22), transparent 30%),
    linear-gradient(135deg, #07111f, #0f172a);
}

.section-heading.light span {
  color: #e0f2fe;
  background: rgba(14,165,233,0.18);
}

.section-heading.light h2 {
  color: white;
}

.project-card {
  display: block;
  height: 100%;
  overflow: hidden;
  border-radius: 30px;
  text-decoration: none;
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.12);
  box-shadow: 0 30px 80px rgba(0,0,0,0.22);
  transition: 0.35s ease;
  backdrop-filter: blur(14px);
}

.project-card:hover {
  transform: translateY(-12px);
  background: rgba(255,255,255,0.12);
}

.project-img {
  height: 260px;
  overflow: hidden;
}

.project-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: 0.45s ease;
}

.project-card:hover .project-img img {
  transform: scale(1.08);
}

.project-content {
  padding: 28px;
}

.project-tag {
  display: inline-flex;
  padding: 7px 14px;
  border-radius: 999px;
  background: rgba(6,182,212,0.18);
  color: #a5f3fc;
  font-weight: 900;
  margin-bottom: 14px;
}

.project-content h3 {
  color: white;
  font-weight: 900;
  margin-bottom: 12px;
}

.project-content p {
  color: rgba(255,255,255,0.78);
  line-height: 1.9;
}

.project-content strong {
  color: #bfdbfe;
}

.footer {
  padding: 50px 0;
  background: #020617;
  color: white;
  text-align: center;
}

.footer h4 {
  font-weight: 900;
}

.footer p {
  color: rgba(255,255,255,0.72);
}

.app-hero {
  min-height: 70vh;
  padding-top: 130px;
  display: flex;
  align-items: center;
  color: white;
  background:
    radial-gradient(circle at 20% 20%, rgba(37,99,235,0.45), transparent 30%),
    linear-gradient(135deg, #07111f, #0f172a);
}

.app-hero h1 {
  font-size: clamp(34px, 5vw, 58px);
  font-weight: 900;
}

.app-hero p {
  font-size: 21px;
  line-height: 2;
  color: rgba(255,255,255,0.82);
}

.app-image-box img {
  width: 100%;
  border-radius: 34px;
  box-shadow: var(--shadow);
}

.feature-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.feature-list li {
  padding: 18px 20px;
  margin-bottom: 14px;
  background: white;
  border-radius: 18px;
  box-shadow: 0 12px 30px rgba(15,23,42,0.08);
  font-weight: 800;
}

.feature-list li::before {
  content: "✓";
  display: inline-flex;
  width: 28px;
  height: 28px;
  margin-left: 10px;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  background: #dcfce7;
  color: #15803d;
  font-weight: 900;
}

html[dir="ltr"] .feature-list li::before {
  margin-left: 0;
  margin-right: 10px;
}

.animate-up {
  animation: animateUp 0.8s ease both;
}

@keyframes animateUp {
  from {
    opacity: 0;
    transform: translateY(35px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (max-width: 991px) {
  .hero-card {
    padding: 32px;
  }

  .hero-overlay,
  html[dir="rtl"] .hero-overlay {
    background: linear-gradient(180deg, rgba(7,17,31,0.88), rgba(7,17,31,0.72));
  }
}

@media (max-width: 576px) {
  .hero-card {
    padding: 24px;
  }

  .hero-card p {
    font-size: 17px;
  }

  .section-padding {
    padding: 70px 0;
  }
}
'''

main_js = r'''let currentLang = localStorage.getItem("site_lang") || "ar";

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
'''

def app_page(title_ar, title_en, desc_ar, desc_en, image, features_ar, features_en):
    ar_items = "\n".join([f"<li>{x}</li>" for x in features_ar])
    en_items = "\n".join([f"<li>{x}</li>" for x in features_en])

    return f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title_ar}</title>

  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.rtl.min.css" rel="stylesheet" id="bootstrap-css">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css" />
</head>

<body>

<nav class="navbar navbar-expand-lg fixed-top modern-nav">
  <div class="container">
    <a class="navbar-brand brand" href="../index.html">
      <span class="brand-icon">HS</span>
      <span data-ar="حسام عزت سرحان" data-en="Hossam Ezzat Sarhan">حسام عزت سرحان</span>
    </a>

    <button class="btn lang-btn" onclick="switchLanguage()">
      <i class="bi bi-translate"></i>
      <span>AR / EN</span>
    </button>
  </div>
</nav>

<section class="app-hero">
  <div class="container">
    <div class="row g-5 align-items-center">
      <div class="col-lg-6">
        <span class="hero-badge" data-ar="مشروع برمجي احترافي" data-en="Professional Software Project">مشروع برمجي احترافي</span>
        <h1 data-ar="{title_ar}" data-en="{title_en}">{title_ar}</h1>
        <p data-ar="{desc_ar}" data-en="{desc_en}">{desc_ar}</p>
        <a href="../index.html#apps" class="btn primary-btn mt-3" data-ar="العودة للتطبيقات" data-en="Back to Apps">العودة للتطبيقات</a>
      </div>

      <div class="col-lg-6">
        <div class="app-image-box">
          <img src="../assets/images/{image}" alt="{title_ar}">
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section-padding">
  <div class="container">
    <div class="section-heading">
      <span data-ar="المميزات" data-en="Features">المميزات</span>
      <h2 data-ar="أهم وظائف ومميزات التطبيق" data-en="Main Application Features">أهم وظائف ومميزات التطبيق</h2>
    </div>

    <div class="row justify-content-center mt-5">
      <div class="col-lg-9">
        <ul class="feature-list ar-features">
          {ar_items}
        </ul>

        <ul class="feature-list en-features d-none">
          {en_items}
        </ul>
      </div>
    </div>
  </div>
</section>

<footer class="footer">
  <div class="container">
    <h4 data-ar="مهندس / حسام عزت سرحان" data-en="Eng. Hossam Ezzat Sarhan">مهندس / حسام عزت سرحان</h4>
    <small>© 2026</small>
  </div>
</footer>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
<script src="../assets/js/main.js"></script>
</body>
</html>
'''

pages = {
    "lms.html": app_page(
        "تطبيق LMS لإدارة العملية التعليمية",
        "LMS Educational Management Application",
        "تطبيق جوال لإدارة خدمات الطلاب التعليمية، ويعرض الجداول الدراسية وجداول الاختبارات والنتائج والإشعارات بطريقة سهلة واحترافية.",
        "A mobile application for managing student educational services, including schedules, exam timetables, results, and notifications in a professional user experience.",
        "h1.webp",
        [
            "عرض الجداول الدراسية للطلاب",
            "عرض جداول الاختبارات",
            "عرض النتائج بشكل منظم",
            "إرسال واستقبال إشعارات الطلاب",
            "دعم تجربة استخدام سهلة واحترافية",
        ],
        [
            "Student timetable display",
            "Exam timetable display",
            "Organized results display",
            "Student notifications",
            "Simple and professional user experience",
        ],
    ),
    "smart-exams.html": app_page(
        "تطبيق الاختبارات الذكية",
        "Smart Exams System",
        "منصة ويب وتطبيق جوال لإدارة الاختبارات إلكترونياً، وإنشاء الاختبارات باستخدام الذكاء الاصطناعي وإدارة بنك الأسئلة والتصحيح.",
        "A web and mobile platform for electronic exam management, AI-based exam generation, question bank management, and auto-correction.",
        "h2.webp",
        [
            "إنشاء الاختبارات باستخدام الذكاء الاصطناعي",
            "رفع وإدارة بنك الأسئلة",
            "مراجعة واعتماد الأسئلة",
            "إنشاء نماذج اختبارات متنوعة مطبوعة",
            "إجراء الاختبار والتصحيح إلكترونياً",
            "حسابات لمدير الاختبارات والطالب وولي الأمر",
        ],
        [
            "AI-based exam generation",
            "Question bank upload and management",
            "Question review and approval",
            "Multiple printable exam models",
            "Online exams and auto-correction",
            "Accounts for exam manager, student, and parent",
        ],
    ),
    "quran.html": app_page(
        "تطبيق إدارة حلقات تحفيظ القرآن",
        "Quran Memorization Circles Management",
        "منصة ويب وتطبيق جوال لإدارة حلقات التحفيظ، تسجيل الطلاب، تقييم الحفظ والمراجعة، وتسجيل الحضور والتقارير اليومية.",
        "A web and mobile platform for managing Quran circles, students, attendance, memorization evaluation, revision, and daily reports.",
        "h2.webp",
        [
            "تسجيل الطلاب وإدارة بياناتهم",
            "تقييم الحفظ والمراجعة",
            "تسجيل الحضور اليومي",
            "تقارير أداء تفصيلية",
            "متابعة يومية للطلاب والحلقات",
        ],
        [
            "Student registration and management",
            "Memorization and revision evaluation",
            "Daily attendance tracking",
            "Detailed performance reports",
            "Daily tracking for students and circles",
        ],
    ),
}

(PROJECT_PATH / "index.html").write_text(index_html, encoding="utf-8")
(PROJECT_PATH / "assets" / "css" / "style.css").write_text(style_css, encoding="utf-8")
(PROJECT_PATH / "assets" / "js" / "main.js").write_text(main_js, encoding="utf-8")

for name, content in pages.items():
    (PROJECT_PATH / "apps" / name).write_text(content, encoding="utf-8")

print("✅ تم تحديث التصميم بنجاح")
print("افتح الملف:")
print(PROJECT_PATH / "index.html")