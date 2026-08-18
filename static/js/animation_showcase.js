/* ============================================
   PORTFOLIO ANIMATION SHOWCASE - JAVASCRIPT
   Handles counter animation, text reveal, and interactions
   ============================================ */

document.addEventListener('DOMContentLoaded', function() {
    // ============================================
    // COUNTER ANIMATION (0 to 100)
    // ============================================
    
    const counterElement = document.getElementById('counter');
    const nameContainer = document.getElementById('nameContainer');
    const subtitle = document.getElementById('subtitle');
    const nameLetters = document.querySelectorAll('.letter');
    
    // Animate counter from 0 to 100
    function animateCounter() {
        const duration = 3000; // 3 seconds (ease-out)
        const startTime = Date.now();
        
        function update() {
            const elapsed = Date.now() - startTime;
            const progress = Math.min(elapsed / duration, 1);
            
            // Ease-out cubic easing function for natural deceleration
            const easeProgress = 1 - Math.pow(1 - progress, 3);
            
            // Calculate current number
            const currentNumber = Math.floor(easeProgress * 100);
            
            counterElement.textContent = currentNumber;
            
            if (progress < 1) {
                requestAnimationFrame(update);
            } else {
                // Counter complete - trigger name reveal
                counterElement.textContent = '100';
                setTimeout(() => {
                    triggerNameReveal();
                }, 200);
            }
        }
        
        requestAnimationFrame(update);
    }
    
    // ============================================
    // NAME REVEAL ANIMATION
    // ============================================
    
    function triggerNameReveal() {
        // The CSS animation handles the reveal via animation-delay
        // This function is called when counter completes
        console.log('✨ Counter complete - VIVEK RAY name revealed');

        if (nameContainer && nameLetters.length) {
            nameContainer.addEventListener('pointermove', function(e) {
                const rect = nameContainer.getBoundingClientRect();
                const px = (e.clientX - rect.left) / rect.width - 0.5;
                const py = (e.clientY - rect.top) / rect.height - 0.5;

                const moveX = px * 40;
                const moveY = py * 40;
                const rotateY = px * 26;
                const rotateX = -py * 26;

                nameContainer.style.transform = `translate(-50%, -50%) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;

                nameLetters.forEach((letter, index) => {
                    const spread = (index - (nameLetters.length - 1) / 2) * 4;
                    const delayFactor = index * 0.8;
                    const driftX = moveX * (1.1 + index * 0.18) + spread;
                    const driftY = moveY * (1.2 + index * 0.2) - spread * 0.3;
                    const rotation = moveX * (5 + index * 0.8) + spread * 2.4;
                    const scale = 1 + Math.abs(px) * 0.12 + index * 0.01;

                    letter.style.transform = `translate(${driftX}px, ${driftY}px) rotate(${rotation}deg) scale(${scale})`;
                    letter.style.filter = `drop-shadow(${moveX * 0.9}px ${moveY * 0.9}px 18px rgba(255, 120, 60, 0.35))`;
                    letter.style.transition = `transform ${120 + delayFactor}ms ease-out, filter ${120 + delayFactor}ms ease-out`;
                });
            });

            nameContainer.addEventListener('pointerleave', function() {
                nameContainer.style.transform = 'translate(-50%, -50%) rotateX(0deg) rotateY(0deg)';

                nameLetters.forEach((letter) => {
                    letter.style.transform = '';
                    letter.style.filter = '';
                });
            });
        }
    }
    
    // ============================================
    // BUTTON INTERACTIONS
    // ============================================
    
    const buttons = document.querySelectorAll('.btn');
    
    buttons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-3px) scale(1.02)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
        
        button.addEventListener('click', function(e) {
            // Ripple effect
            const rect = this.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            const ripple = document.createElement('span');
            ripple.style.position = 'absolute';
            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';
            ripple.style.width = '0';
            ripple.style.height = '0';
            ripple.style.borderRadius = '50%';
            ripple.style.background = 'rgba(255, 120, 60, 0.5)';
            ripple.style.pointerEvents = 'none';
            ripple.style.transform = 'translate(-50%, -50%)';
            
            this.appendChild(ripple);
            
            // Animate ripple
            ripple.animate([
                { width: '0', height: '0', opacity: 1 },
                { width: '300px', height: '300px', opacity: 0 }
            ], {
                duration: 600,
                easing: 'cubic-bezier(0.25, 0.46, 0.45, 0.94)'
            });
            
            setTimeout(() => ripple.remove(), 600);
        });
    });
    
    // ============================================
    // SCROLL INTERACTIONS
    // ============================================
    
    window.addEventListener('scroll', function() {
        const scrollProgress = window.scrollY / (document.documentElement.scrollHeight - window.innerHeight);
        const glowBg = document.querySelector('.glow-background');
        
        // Subtle glow movement on scroll
        glowBg.style.transform = `translate(-50%, calc(-50% + ${scrollProgress * 30}px))`;
    });
    
    // ============================================
    // SMOOTH PAGE LOAD SEQUENCE
    // ============================================
    
    // Wait for DOM to be fully ready
    setTimeout(() => {
        // Start counter animation after 500ms delay
        animateCounter();
    }, 500);
    
    // ============================================
    // SCROLL TO PORTFOLIO REDIRECT
    // ============================================

    const portfolioScrollPrompt = document.getElementById('portfolioScrollPrompt');
    let hasRedirectedToPortfolio = false;

    function redirectToPortfolio() {
        if (hasRedirectedToPortfolio) return;
        hasRedirectedToPortfolio = true;
        window.location.href = '/portfolio/';
    }

    window.addEventListener('wheel', function(e) {
        if (Math.abs(e.deltaY) > 20) {
            redirectToPortfolio();
        }
    }, { passive: true });

    window.addEventListener('touchmove', function() {
        redirectToPortfolio();
    }, { passive: true });

    window.addEventListener('keydown', function(e) {
        if (e.key === 'PageDown' || e.key === 'ArrowDown' || e.key === ' ') {
            redirectToPortfolio();
        }
    });

    if (portfolioScrollPrompt) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 10) {
                redirectToPortfolio();
            }
        });
    }
    
    // ============================================
    // KEYBOARD SHORTCUT
    // ============================================
    
    document.addEventListener('keydown', function(e) {
        // Press 'R' to restart animation
        if (e.key === 'r' || e.key === 'R') {
            location.reload();
        }
    });
    
    // ============================================
    // PARALLAX EFFECT (Optional Enhancement)
    // ============================================
    
    const heroSection = document.querySelector('.portfolio-hero');
    
    window.addEventListener('mousemove', function(e) {
        if (!heroSection) return;
        
        const x = e.clientX / window.innerWidth;
        const y = e.clientY / window.innerHeight;
        
        const moveX = (x - 0.5) * 10;
        const moveY = (y - 0.5) * 10;
        
        heroSection.style.transform = `perspective(1000px) rotateX(${moveY}deg) rotateY(${moveX}deg)`;
    });
    
    window.addEventListener('mouseleave', function() {
        if (heroSection) {
            heroSection.style.transform = 'perspective(1000px) rotateX(0) rotateY(0)';
        }
    });
    
    // ============================================
    // TOUCH SUPPORT FOR MOBILE
    // ============================================
    
    let touchStartX = 0;
    let touchStartY = 0;
    
    document.addEventListener('touchstart', function(e) {
        touchStartX = e.touches[0].clientX;
        touchStartY = e.touches[0].clientY;
    });
    
    document.addEventListener('touchmove', function(e) {
        if (!heroSection) return;
        
        const touchX = e.touches[0].clientX;
        const touchY = e.touches[0].clientY;
        
        const diffX = (touchX - touchStartX) * 0.05;
        const diffY = (touchY - touchStartY) * 0.05;
        
        heroSection.style.transform = `perspective(1000px) rotateX(${diffY}deg) rotateY(${diffX}deg)`;
    });
    
    document.addEventListener('touchend', function() {
        if (heroSection) {
            heroSection.style.transform = 'perspective(1000px) rotateX(0) rotateY(0)';
        }
    });
    
    // ============================================
    // CONSOLE MESSAGE
    // ============================================
    
    console.log('%c🎨 Portfolio Animation Showcase', 'font-size: 20px; font-weight: bold; color: #ff7a60;');
    console.log('%cPress "R" to restart the animation', 'font-size: 14px; color: #a0a0a0;');
    console.log('%cHover over buttons for interactions', 'font-size: 14px; color: #a0a0a0;');
});
