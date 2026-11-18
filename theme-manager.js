(function () {
    // 1. Get saved theme or default to 'normal'
    let currentTheme = localStorage.getItem('site-theme') || 'normal';

    // 2. Inject dynamic styles based on theme
    function applyTheme() {
        // Remove existing theme style if any
        const existing = document.getElementById('dynamic-theme-style');
        if (existing) existing.remove();

        // Update data-theme and class on root html element
        document.documentElement.setAttribute('data-theme', currentTheme);
        if (currentTheme === 'dark') {
            document.documentElement.classList.add('theme-dark');
        } else {
            document.documentElement.classList.remove('theme-dark');
        }

        if (currentTheme !== 'normal') {
            const style = document.createElement('style');
            style.id = 'dynamic-theme-style';
            let css = '';

            if (currentTheme === 'dark') {
                // Dark mode via inversion (0.9 makes it dark slate instead of pure black)
                css = `
                    html {
                        filter: invert(0.9) hue-rotate(180deg);
                    }
                    /* Re-invert media and elements that already have balanced dark tones */
                    img, video, iframe, pre, canvas, .bg-slate-900, .bg-slate-800, .bg-darker, .bg-dark, .no-invert, #ai-widget-container, .no-invert-dark, #oop-welcome-modal, #oop-share-modal {
                        filter: invert(1) hue-rotate(180deg);
                    }
                `;
            } else if (currentTheme === 'reading') {
                // Reading mode via sepia and slightly reduced brightness
                css = `
                    html {
                        filter: sepia(0.5) brightness(0.95);
                    }
                `;
            }

            style.textContent = css;
            document.head.appendChild(style);
        }
        updateThemeIcon();

        // Dispatch a custom event in case components want to listen to theme changes
        window.dispatchEvent(new CustomEvent('siteThemeChanged', { detail: { theme: currentTheme } }));
    }

    // 3. Update the floating button icon based on state (if present on index.html)
    function updateThemeIcon() {
        const btn = document.getElementById('theme-toggle-btn');
        if (!btn) return;
        
        let iconHtml = '';
        if (currentTheme === 'normal') {
            iconHtml = '☀️';
        } else if (currentTheme === 'dark') {
            iconHtml = '🌙';
        } else {
            iconHtml = '📖';
        }
        btn.innerHTML = iconHtml;
    }

    // 4. Expose functions globally
    window.toggleTheme = function() {
        if (currentTheme === 'normal') {
            currentTheme = 'dark';
        } else if (currentTheme === 'dark') {
            currentTheme = 'reading';
        } else {
            currentTheme = 'normal';
        }
        localStorage.setItem('site-theme', currentTheme);
        applyTheme();
    };

    window.applyTheme = applyTheme;

    // Apply immediately on load to prevent FOUC (Flash of Unstyled Content)
    applyTheme();
    
    // Make sure icon updates once DOM is ready
    window.addEventListener('DOMContentLoaded', updateThemeIcon);

    // Listen to storage changes so toggling from index.html instantly updates all open chapter tabs
    window.addEventListener('storage', function (e) {
        if (e.key === 'site-theme') {
            currentTheme = e.newValue || 'normal';
            applyTheme();
        }
    });

    // Auto-load course-modals.js across all course pages
    if (!document.querySelector('script[src*="course-modals.js"]')) {
        const modalScript = document.createElement('script');
        modalScript.src = 'course-modals.js';
        modalScript.async = true;
        document.head.appendChild(modalScript);
    }
})();
