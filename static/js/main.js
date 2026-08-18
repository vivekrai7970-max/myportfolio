document.addEventListener('DOMContentLoaded', function () {
  const themeToggle = document.getElementById('themeToggle');
  const htmlElement = document.documentElement;
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const storedTheme = localStorage.getItem('portfolioTheme');

  if (themeToggle && htmlElement) {
    function applyTheme(theme) {
      if (theme === 'light') {
        htmlElement.classList.remove('dark');
        htmlElement.setAttribute('data-theme', 'light');
        themeToggle.innerHTML = '<i class="fa-solid fa-sun"></i>';
      } else {
        htmlElement.classList.add('dark');
        htmlElement.setAttribute('data-theme', 'dark');
        themeToggle.innerHTML = '<i class="fa-solid fa-moon"></i>';
      }
    }

    const initialTheme = storedTheme || (prefersDark ? 'dark' : 'light');
    applyTheme(initialTheme);

    themeToggle.addEventListener('click', () => {
      const nextTheme = htmlElement.classList.contains('dark') ? 'light' : 'dark';
      applyTheme(nextTheme);
      localStorage.setItem('portfolioTheme', nextTheme);
    });
  }

  const progressBar = document.getElementById('scrollProgress');
  window.addEventListener('scroll', () => {
    if (progressBar) {
      const totalHeight = Math.max(document.body.scrollHeight - window.innerHeight, 1);
      const progress = (window.pageYOffset / totalHeight) * 100;
      progressBar.style.width = `${Math.min(Math.max(progress, 0), 100)}%`;
    }

    // Subtle parallax effect on hero elements
    const scrollY = window.pageYOffset;
    const heroGraphics = document.querySelectorAll('.hero-graphic');
    heroGraphics.forEach(el => {
      el.style.transform = `translateY(${scrollY * 0.05}px)`;
    });
  });

  if (typeof AOS !== 'undefined') {
    // Configure AOS with cinematic timing
    AOS.init({ 
      duration: 1000,
      once: true,
      easing: 'ease-out-cubic',
      delay: 100,
      offset: 100
    });
  }
});

