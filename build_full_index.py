# -*- coding: utf-8 -*-
import sys

# Read base64 background string
with open('base64_bg.txt', 'r', encoding='utf-8') as f:
    b64_bg = f.read().strip()

# Read footer snippet
with open('footer_snippet.html', 'r', encoding='utf-8') as f:
    footer_html = f.read().strip()

html_content = f'''<!DOCTYPE html>
<html lang="he" dir="rtl" class="scroll-smooth">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <meta name="ai-document-summary"
        content="פורטל הלמידה הראשי ומפת הקורס האינטראקטיבית לקורס תכנות מונחה עצמים (20906) באוניברסיטה הפתוחה (Smalltalk-80 & Squeak). מפת דרכים אינטראקטיבית מבוססת סמל סקוויק (Squeak Mouse) עם פסי אור זוהרים בסגול, ורוד וכתום, 9 פרקי הליבה ומבוא, סיכום הקורס המלא ומאגר בחינות ותרגול.">
    <title>תכנות מונחה עצמים (20906) • מפת הקורס והלמידה האינטראקטיבית | האוניברסיטה הפתוחה</title>

    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script src="theme-manager.js"></script>
    <!-- Google Fonts: Heebo & JetBrains Mono -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link
        href="https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700;800&display=swap"
        rel="stylesheet">

    <script>
        if (typeof tailwind !== 'undefined') tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['Heebo', 'system-ui', '-apple-system', 'sans-serif'],
                        mono: ['JetBrains Mono', 'Consolas', 'monospace'],
                    }},
                    colors: {{
                        primary: {{
                            50: '#fdf2f8',
                            100: '#fce7f3',
                            200: '#fbcfe8',
                            300: '#f472b6',
                            400: '#e879f9',
                            500: '#c026d3',
                            600: '#9333ea',
                            700: '#7e22ce',
                            800: '#581c87',
                            900: '#3b0764',
                            950: '#4c0519',
                        }}
                    }}
                }}
            }}
        }};
    </script>

    <style>
        /* =====================================================================
           BASE PORTAL STYLES & DIRECT VISIBILITY OF THE BASE64 BACKGROUND IMAGE
           ===================================================================== */
        body {{
            background-color: #f8f6fb;
            background-image:
                radial-gradient(circle at 1px 1px, rgba(147, 51, 234, 0.07) 1px, transparent 0),
                radial-gradient(1200px circle at 15% 10%, rgba(243, 232, 255, 0.35), transparent 60%),
                radial-gradient(1100px circle at 85% 85%, rgba(254, 215, 170, 0.25), transparent 60%);
            background-size: 24px 24px, 100% 100%, 100% 100%;
            font-family: 'Heebo', sans-serif;
            overflow-x: hidden;
            color: #0f172a;
            min-height: 100vh;
            margin: 0;
            position: relative;
        }}

        /* The authentic base64 background image, completely visible behind the canvas */
        body::before {{
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-image: url('data:image/jpeg;base64,{b64_bg}');
            background-repeat: no-repeat;
            background-size: cover;
            background-position: center;
            filter: grayscale(100%) contrast(1.22) brightness(1.0);
            opacity: 0.24;
            z-index: -2;
            pointer-events: none;
        }}

        /* Spinning Conic Border for Top-Left Button (Bordeaux, Purple, Pink, Orange) */
        @keyframes spin-conic-accent {{
            0% {{ transform: rotate(0deg); }}
            100% {{ transform: rotate(360deg); }}
        }}

        .accent-spin-bg {{
            position: absolute;
            inset: -55%;
            background: conic-gradient(from 0deg, #4c0519, #831843, #db2777, #f97316, #a855f7, #581c87, #4c0519);
            animation: spin-conic-accent 5s linear infinite;
        }}

        @keyframes silver-waves {{
            0% {{
                background-position: 200% center;
            }}

            100% {{
                background-position: -200% center;
            }}
        }}

        .silver-waves-bg {{
            background: linear-gradient(105deg,
                    transparent 20%,
                    rgba(255, 255, 255, 0.4) 25%,
                    transparent 30%,
                    rgba(255, 255, 255, 0.8) 45%,
                    rgba(255, 255, 255, 0.4) 50%,
                    transparent 55%,
                    rgba(255, 255, 255, 0.3) 70%,
                    transparent 75%);
            background-size: 200% 100%;
            animation: silver-waves 3s linear infinite;
        }}

        @keyframes spin-rainbow {{
            0% {{
                transform: rotate(0deg);
            }}

            100% {{
                transform: rotate(360deg);
            }}
        }}

        .rainbow-spin-bg {{
            position: absolute;
            inset: 0;
            border-radius: 50%;
            padding: 3px;
            background: conic-gradient(from 0deg, #7c3aed, #9333ea, #c026d3, #d946ef, #ec4899, #f43f5e, #f472b6, #c084fc, #7c3aed);
            -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
            -webkit-mask-composite: xor;
            mask-composite: exclude;
            animation: spin-rainbow 4s linear infinite;
            pointer-events: none;
            z-index: 0;
        }}

        /* Rotating Glowing Light Beam Gradient (Purple, Pink, Orange) */
        @keyframes rotateBeamGrad {{
            0% {{ transform: rotate(0deg); }}
            100% {{ transform: rotate(360deg); }}
        }}

        #light-beam-grad {{
            transform-origin: 512px 365px;
            animation: rotateBeamGrad 10s linear infinite;
        }}

        /* Flowing dash animation for SVG lines and frame (Computational Models Style) */
        @keyframes dashFlow {{
            to {{ stroke-dashoffset: -280; }}
        }}

        @keyframes dashFlowReverse {{
            to {{ stroke-dashoffset: 280; }}
        }}

        .flowing-frame {{
            animation: dashFlow 20s linear infinite;
        }}

        .flowing-pipe {{
            animation: dashFlow 14s linear infinite;
        }}

        .flowing-path-dash {{
            animation: dashFlow 10s linear infinite;
        }}

        .flowing-feeder {{
            animation: dashFlowReverse 6s linear infinite;
        }}

        /* Light beam stroke transitions - absolutely zero layout shift */
        .light-beam-path {{
            transition: stroke 0.3s ease, stroke-width 0.25s ease, filter 0.25s ease;
        }}

        .squeak-hitbox {{
            cursor: pointer;
            outline: none;
            -webkit-tap-highlight-color: transparent;
        }}

        /* Numbers stay completely anchored with zero movement/jumping */
        .node-circle {{
            transition: stroke 0.2s ease, stroke-width 0.2s ease, filter 0.2s ease;
        }}

        .squeak-node {{
            cursor: pointer;
        }}

        .squeak-node:hover .node-circle,
        .squeak-node.active .node-circle {{
            stroke: #f97316;
            stroke-width: 3.5;
            filter: drop-shadow(0 0 8px rgba(249, 115, 22, 0.7));
        }}

        /* Pupil movement */
        .pupil-group {{
            transition: transform 0.08s cubic-bezier(0.25, 1, 0.5, 1);
        }}

        .eye-container {{
            cursor: pointer;
            outline: none;
        }}

        .eye-container:hover .eye-socket {{
            filter: drop-shadow(0 0 14px rgba(236, 72, 153, 0.8));
        }}

        /* =====================================================================
           THE CAT NOSE PILL - ORGANIC OVAL SHAPE WITH PARTIAL TRANSPARENCY
           ===================================================================== */
        #cat-nose-pill {{
            transition: width 0.38s cubic-bezier(0.34, 1.56, 0.64, 1), 
                        height 0.38s cubic-bezier(0.34, 1.56, 0.64, 1),
                        border-radius 0.38s ease,
                        box-shadow 0.38s ease, 
                        border-color 0.38s ease, 
                        background 0.38s ease;
        }}

        /* Resting State: Small cute cat nose */
        .nose-collapsed {{
            width: 90px !important;
            height: 56px !important;
            border-radius: 28px !important;
            background: rgba(24, 8, 40, 0.8) !important;
            backdrop-filter: blur(12px) !important;
            -webkit-backdrop-filter: blur(12px) !important;
            border: 2px solid rgba(244, 114, 182, 0.75) !important;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2) !important;
        }}

        /* Expanded State: Smooth organic oval card with soft luminous frosted glass */
        #cat-nose-container:hover #cat-nose-pill,
        #cat-nose-pill.nose-expanded {{
            width: 420px !important;
            min-height: 215px !important;
            height: auto !important;
            border-radius: 36px !important;
            background: rgba(255, 255, 255, 0.96) !important;
            backdrop-filter: blur(24px) !important;
            -webkit-backdrop-filter: blur(24px) !important;
            border: 2px solid rgba(244, 114, 182, 0.6) !important;
            box-shadow: 0 25px 60px -10px rgba(124, 58, 237, 0.22), 0 0 0 1px rgba(255, 255, 255, 0.9) !important;
            padding: 1.1rem 1.25rem !important;
        }}

        @media (max-width: 640px) {{
            #cat-nose-container:hover #cat-nose-pill,
            #cat-nose-pill.nose-expanded {{
                width: min(350px, 92vw) !important;
                min-height: 200px !important;
                border-radius: 30px !important;
                padding: 0.9rem 1rem !important;
            }}
        }}

        #cat-nose-container:hover #nose-default-view,
        #cat-nose-pill.nose-expanded #nose-default-view {{
            opacity: 0 !important;
            pointer-events: none !important;
        }}

        #cat-nose-container:hover #nose-expanded-view,
        #cat-nose-pill.nose-expanded #nose-expanded-view {{
            opacity: 1 !important;
            pointer-events: auto !important;
        }}

        #cat-nose-container:hover .accent-spin-bg,
        #cat-nose-pill.nose-expanded .accent-spin-bg {{
            display: none !important;
        }}

        /* =====================================================================
           CREEPY CAT NIGHT MODE - SCARY RED EYES & MISCHIEVOUS CHESHIRE SMILE
           ===================================================================== */
        .no-invert-dark {{
            filter: invert(1) hue-rotate(180deg);
        }}

        .creepy-eye-normal {{
            transition: opacity 0.5s ease;
        }}
        .creepy-eye-night {{
            opacity: 0;
            transition: opacity 0.5s ease;
        }}
        .creepy-mouth {{
            opacity: 0;
            transform-origin: 512px 610px;
            transform: scale(0.85);
            transition: opacity 0.6s cubic-bezier(0.16, 1, 0.3, 1), transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
        }}

        html[data-theme="dark"] .creepy-eye-normal,
        html.theme-dark .creepy-eye-normal {{
            opacity: 0 !important;
        }}
        html[data-theme="dark"] .creepy-eye-night,
        html.theme-dark .creepy-eye-night {{
            opacity: 1 !important;
        }}
        html[data-theme="dark"] .creepy-mouth,
        html.theme-dark .creepy-mouth {{
            opacity: 1 !important;
            transform: scale(1) !important;
        }}

        @keyframes creepyGlow {{
            0%, 100% {{ filter: drop-shadow(0 0 10px #ff0033) drop-shadow(0 0 20px rgba(255, 0, 51, 0.6)); }}
            50% {{ filter: drop-shadow(0 0 16px #ff1744) drop-shadow(0 0 30px rgba(255, 23, 68, 0.85)); }}
        }}

        @keyframes pulseSlit {{
            0%, 100% {{ transform: scaleX(1); }}
            50% {{ transform: scaleX(0.7); }}
        }}

        .creepy-slit {{
            animation: pulseSlit 3s ease-in-out infinite;
            transform-origin: center;
        }}

        .creepy-glow {{
            animation: creepyGlow 2.5s ease-in-out infinite;
        }}
    </style>
</head>

<body class="min-h-screen flex flex-col selection:bg-purple-200 selection:text-purple-950 text-slate-800">

    <!-- ========================================================================= -->
    <!-- TOP-RIGHT FIXED CONTROLS: THEME TOGGLE BUTTON                             -->
    <!-- ========================================================================= -->
    <div class="fixed top-4 right-4 sm:top-6 sm:right-6 z-50 flex items-center gap-2">
        <button id="theme-toggle-btn" onclick="toggleTheme()" title="החלפת ערכת נושא (רגיל -> כהה -> קריאה)"
            class="w-12 h-12 sm:w-14 sm:h-14 rounded-2xl flex items-center justify-center text-xl sm:text-2xl bg-white/80 backdrop-blur-xl border border-white/90 text-slate-800 shadow-lg hover:scale-110 hover:bg-white transition-all cursor-pointer">
            ☀️
        </button>
    </div>

    <!-- ========================================================================= -->
    <!-- TOP-LEFT FIXED BUTTON: OTHER COURSES (MATCHES OPERATING SYSTEMS STYLE)    -->
    <!-- ========================================================================= -->
    <a href="https://all-the-courses.pages.dev/"
        class="fixed top-4 left-4 sm:top-6 sm:left-6 z-50 group block bg-transparent rounded-full p-[3px] transition-all duration-500 hover:shadow-2xl hover:shadow-purple-400/30 hover:-translate-y-1 hover:scale-105 w-32 h-32 sm:w-40 sm:h-40 overflow-hidden"
        title="מעבר לפורטל כל הקורסים">

        <!-- Spinning Conic Border in Purple, Pink & Rose Palette -->
        <div class="rainbow-spin-bg"></div>

        <div
            class="bg-white/20 backdrop-blur-xl rounded-full w-full h-full relative z-10 flex flex-col items-center justify-center border border-white/30 hover:bg-white/30 transition-all duration-500 shadow-[0_8px_32px_rgba(255,255,255,0.05)] text-center p-2 overflow-hidden">
            <!-- Silver waves animation layer -->
            <div class="absolute inset-0 silver-waves-bg pointer-events-none z-0"></div>

            <div
                class="w-12 h-12 sm:w-14 sm:h-14 mb-2 rounded-full bg-white/30 flex items-center justify-center text-purple-700 group-hover:bg-gradient-to-br group-hover:from-purple-500 group-hover:to-pink-500 group-hover:text-white transition-all duration-500 shadow-inner relative z-20">
                <i data-lucide="library" class="w-6 h-6 sm:w-8 sm:h-8"></i>
            </div>
            <span
                class="text-sm sm:text-base font-bold text-slate-700 group-hover:text-purple-900 transition-colors leading-tight relative z-20">לקורסים<br>נוספים</span>
        </div>
    </a>

    <!-- ========================================================================= -->
    <!-- HERO HEADER SECTION: ELEGANT WHITE GLASS CARD CONTAINER                   -->
    <!-- ========================================================================= -->
    <header class="relative w-full flex flex-col items-center justify-center pt-20 sm:pt-16 pb-3 px-4 z-30">
        <div class="relative z-10 text-center px-4 w-full flex flex-col items-center max-w-4xl">
            <!-- Clean White Glassmorphic Card Container -->
            <div class="bg-white/80 backdrop-blur-xl rounded-3xl shadow-xl px-6 md:px-12 py-7 sm:py-8 w-full border border-white/70 transition-all duration-300 hover:shadow-2xl flex flex-col items-center">
                
                <!-- Course Badge Pill -->
                <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-purple-50 border border-purple-200/80 shadow-xs mb-3">
                    <span class="w-2.5 h-2.5 rounded-full bg-purple-600 animate-pulse"></span>
                    <span class="text-xs sm:text-sm font-bold text-purple-950">
                        האוניברסיטה הפתוחה • המחלקה למדעי המחשב • קורס 20906
                    </span>
                </div>

                <!-- Main Headline -->
                <h1 class="text-3xl sm:text-5xl md:text-6xl font-black text-slate-900 tracking-tight leading-none mb-3 sm:mb-4">
                    תכנות מונחה עצמים
                </h1>
                
                <!-- Course & Website General Description (Directly on white card, clean & unboxed) -->
                <div class="max-w-2xl text-slate-600 text-xs sm:text-sm md:text-[14.5px] font-normal leading-relaxed text-center space-y-1.5">
                    <p>
                        פורטל הלמידה המקיף לקורס <strong>תכנות מונחה עצמים (20906)</strong> באוניברסיטה הפתוחה. הקורס מקנה הבנה מעמיקה של עקרונות התכנות מונחה העצמים הטהור (Pure OOP) בסביבת <strong>Smalltalk & Squeak</strong> – מודל ייחודי שבו כל ישות במערכת היא עצם חי וכל חישוב מתבצע באמצעות העברת הודעות.
                    </p>
                    <p class="text-slate-500 text-[11.5px] sm:text-xs md:text-sm">
                        האתר מרכז עבורכם מסלול למידה שלם וחווייתי הכולל מפת דרכים אינטראקטיבית לחקירת 9 פרקי הליבה, סיכומי עומק בהירים, סימולציות גרפיות חיות להמחשת מודלים מופשטים, שאלות תרגול ומאגר בחינות מקיף.
                    </p>
                </div>
            </div>
        </div>
    </header>

    <!-- ========================================================================= -->
    <!-- CENTRAL SQUEAK INTERACTIVE HUB (DIRECTLY ON BACKGROUND CANVAS)            -->
    <!-- ========================================================================= -->
    <main class="relative w-full max-w-[1180px] mx-auto px-2 sm:px-6 py-2 z-20 mb-12 flex-1">
        
        <!-- Squeak Stage Container (Frosted Glass Card with soft ambient separation) -->
        <div id="squeak-hub-card"
            class="relative w-full overflow-visible select-none flex flex-col items-center justify-center p-3 sm:p-5 rounded-[2.5rem] bg-white/75 backdrop-blur-xl border border-white/80 shadow-[0_25px_60px_-15px_rgba(124,58,237,0.08)]">

            <!-- Soft Helper Banner -->
            <div class="mb-3 px-5 py-1.5 rounded-full border border-purple-200/80 bg-white/75 backdrop-blur-md text-xs font-bold text-slate-700 shadow-xs flex items-center gap-2">
                <i data-lucide="mouse-pointer-2" class="w-3.5 h-3.5 text-pink-600"></i>
                <span>רחפו מעל חלקי העכבר – האף יתרחב ויציג את תוכן הפרק</span>
            </div>

            <!-- SVG Squeak Face Drawing Area (ViewBox comfortably fits ears and whiskers!) -->
            <div id="squeak-stage-wrapper" class="relative w-full max-w-[980px] mx-auto overflow-visible flex items-center justify-center">
                
                <svg id="squeak-svg" viewBox="-50 -35 1124 785" class="w-full h-auto overflow-visible" style="max-height: 620px;">
                    <defs>
                        <!-- Smooth Continuous Border Gradient (Unbroken, Pastel Transition) -->
                        <linearGradient id="continuous-border-grad" x1="0%" y1="0%" x2="100%" y2="100%">
                            <stop offset="0%" stop-color="#f472b6" />   <!-- Soft Pastel Rose -->
                            <stop offset="25%" stop-color="#fb923c" />  <!-- Soft Warm Coral / Peach -->
                            <stop offset="50%" stop-color="#c084fc" />  <!-- Soft Lavender -->
                            <stop offset="75%" stop-color="#60a5fa" />  <!-- Soft Periwinkle -->
                            <stop offset="100%" stop-color="#f472b6" /> <!-- Back to Rose -->
                        </linearGradient>

                        <!-- Glowing Laser Light Beam Gradient (Soft Pastel Palette) -->
                        <linearGradient id="light-beam-grad" x1="0%" y1="0%" x2="100%" y2="100%">
                            <stop offset="0%" stop-color="#c4b5fd" />   <!-- Soft Pastel Lavender -->
                            <stop offset="25%" stop-color="#f472b6" />  <!-- Soft Pastel Rose -->
                            <stop offset="50%" stop-color="#fca583" />  <!-- Soft Warm Coral -->
                            <stop offset="75%" stop-color="#a78bfa" />  <!-- Soft Lilac -->
                            <stop offset="100%" stop-color="#c4b5fd" /> <!-- Loop to Soft Lavender -->
                        </linearGradient>

                        <!-- Soft Beam Glow Filter -->
                        <filter id="beam-glow" x="-20%" y="-20%" width="140%" height="140%">
                            <feGaussianBlur stdDeviation="2.8" result="blur" />
                            <feComposite in="SourceGraphic" in2="blur" operator="over" />
                        </filter>

                        <!-- Particle Core Glow Filter -->
                        <filter id="particle-glow" x="-40%" y="-40%" width="180%" height="180%">
                            <feGaussianBlur stdDeviation="2.5" result="blur" />
                            <feComposite in="SourceGraphic" in2="blur" operator="over" />
                        </filter>

                        <!-- Eye Socket Glow Filter -->
                        <filter id="eye-glow" x="-25%" y="-25%" width="150%" height="150%">
                            <feGaussianBlur stdDeviation="4" result="blur" />
                            <feComposite in="SourceGraphic" in2="blur" operator="over" />
                        </filter>

                        <!-- Curved Smile Paths for Eye Arched Text (Left Eye: cx=391, cy=374 | Right Eye: cx=623, cy=384) -->
                        <path id="arc-left-smile" d="M 345,398 A 50,54 0 0,0 437,398" fill="none" />
                        <path id="arc-right-smile" d="M 577,408 A 50,54 0 0,0 669,408" fill="none" />

                        <!-- Creepy Red Eye Glow Filter -->
                        <filter id="creepy-red-glow" x="-50%" y="-50%" width="200%" height="200%">
                            <feGaussianBlur in="SourceGraphic" stdDeviation="5" result="blur" />
                            <feMerge>
                                <feMergeNode in="blur" />
                                <feMergeNode in="SourceGraphic" />
                            </feMerge>
                        </filter>

                        <!-- Fiery Red Iris Gradient -->
                        <radialGradient id="creepy-iris-grad" cx="50%" cy="50%" r="50%">
                            <stop offset="0%" stop-color="#ff1744" />
                            <stop offset="40%" stop-color="#dc2626" />
                            <stop offset="85%" stop-color="#7f1d1d" />
                            <stop offset="100%" stop-color="#450a0a" />
                        </radialGradient>
                    </defs>

                    <!-- ============================================================== -->
                    <!-- LAYER 0: CONTINUOUS GLOWING PERIMETER FRAME (UNBROKEN PASTEL)  -->
                    <!-- (Modeled after the Computational Models standard - No Dashes!)  -->
                    <!-- ============================================================== -->
                    
                    <!-- Ambient Soft White Underlay for Outer Frame -->
                    <path id="bbox-frame-underlay"
                        d="M 15,-15 L 1009,-15 A 40,40 0 0 1 1049,25 L 1049,695 A 40,40 0 0 1 1009,735 L 15,735 A 40,40 0 0 1 -25,695 L -25,25 A 40,40 0 0 1 15,-15 Z"
                        fill="none"
                        stroke="rgba(255, 255, 255, 0.85)"
                        stroke-width="8" />

                    <!-- Continuous Glowing Border Path (Unbroken, Smooth Pastel Gradient) -->
                    <path id="bbox-frame-path"
                        d="M 15,-15 L 1009,-15 A 40,40 0 0 1 1049,25 L 1049,695 A 40,40 0 0 1 1009,735 L 15,735 A 40,40 0 0 1 -25,695 L -25,25 A 40,40 0 0 1 15,-15 Z"
                        fill="none"
                        stroke="url(#continuous-border-grad)"
                        stroke-width="4.5"
                        stroke-linecap="round"
                        filter="url(#beam-glow)" />

                    <!-- Faint Ambient Framing Ring -->
                    <circle cx="512" cy="365" r="348" fill="none" stroke="rgba(255, 255, 255, 0.4)" stroke-width="1.5" />
                    <circle cx="512" cy="365" r="348" fill="none" stroke="url(#light-beam-grad)" stroke-width="2" opacity="0.3" />

                    <!-- Feeder Light Rays Connecting Outer Frame to Whisker & Ear Tips -->
                    <g class="pointer-events-none opacity-40">
                        <path id="feeder-ear-r" d="M 835,-15 L 835,6" stroke="url(#light-beam-grad)" stroke-width="2" />
                        <path id="feeder-ear-l" d="M 157,-15 L 157,6" stroke="url(#light-beam-grad)" stroke-width="2" />
                        <path id="feeder-whisker-rt" d="M 1049,550 L 1005,550" stroke="url(#light-beam-grad)" stroke-width="2" />
                        <path id="feeder-whisker-rm" d="M 1049,645 Q 1012,645 975,645" fill="none" stroke="url(#light-beam-grad)" stroke-width="2" />
                        <path id="feeder-whisker-lt" d="M -25,550 L 20,550" stroke="url(#light-beam-grad)" stroke-width="2" />
                        <path id="feeder-whisker-lm" d="M -25,645 Q 12,645 50,645" fill="none" stroke="url(#light-beam-grad)" stroke-width="2" />
                    </g>


                    <!-- ============================================================== -->
                    <!-- LAYER 1: EARS (4 HALVES) WITH FIXED NON-JUMPING NUMBERS        -->
                    <!-- ============================================================== -->

                    <!-- 1. Right Ear Outer Half -> Intro (מבוא והקדמה) -->
                    <g id="seg-group-intro" class="cursor-pointer" data-id="intro">
                        <!-- Hitbox -->
                        <path d="M 840,385 C 895,250 895,60 835,6" fill="none" stroke="transparent" stroke-width="45" class="squeak-hitbox" />
                        <!-- Soft Ambient Underlayer -->
                        <path d="M 840,385 C 895,250 895,60 835,6" fill="none" stroke="rgba(255, 255, 255, 0.45)" stroke-width="14" stroke-linecap="round" />
                        <!-- Glowing Light Beam Path -->
                        <path id="path-intro" d="M 840,385 C 895,250 895,60 835,6" fill="none" stroke="url(#light-beam-grad)" stroke-width="8" stroke-linecap="round" filter="url(#beam-glow)" class="light-beam-path" />
                        <!-- Flowing light pulse dash -->
                        <path d="M 840,385 C 895,250 895,60 835,6" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="80 160" class="flowing-path-dash pointer-events-none opacity-80" />
                        <!-- Fixed Number Node (Zero Jitter/Jumping) -->
                        <g id="node-intro" class="squeak-node">
                            <circle cx="881" cy="165" r="22" fill="#ffffff" stroke="#f472b6" stroke-width="2.5" class="node-circle" />
                            <text x="881" y="165" text-anchor="middle" dominant-baseline="central" font-size="11" font-weight="900" fill="#be185d">מבוא</text>
                        </g>
                    </g>

                    <!-- 2. Right Ear Inner Half -> Chapter 1 (פרק 1) -->
                    <g id="seg-group-1" class="cursor-pointer" data-id="1">
                        <path d="M 835,6 C 750,40 680,130 655,220" fill="none" stroke="transparent" stroke-width="45" class="squeak-hitbox" />
                        <path d="M 835,6 C 750,40 680,130 655,220" fill="none" stroke="rgba(255, 255, 255, 0.45)" stroke-width="14" stroke-linecap="round" />
                        <path id="path-1" d="M 835,6 C 750,40 680,130 655,220" fill="none" stroke="url(#light-beam-grad)" stroke-width="8" stroke-linecap="round" filter="url(#beam-glow)" class="light-beam-path" />
                        <path d="M 835,6 C 750,40 680,130 655,220" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="60 120" class="flowing-path-dash pointer-events-none opacity-80" />
                        <g id="node-1" class="squeak-node">
                            <circle cx="723" cy="92" r="20" fill="#ffffff" stroke="#fb923c" stroke-width="2.5" class="node-circle" />
                            <text x="723" y="92" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="900" fill="#c2410c">1</text>
                        </g>
                    </g>

                    <!-- 3. Left Ear Inner Half -> Chapter 2 (פרק 2) -->
                    <g id="seg-group-2" class="cursor-pointer" data-id="2">
                        <path d="M 157,6 C 240,40 310,130 351,220" fill="none" stroke="transparent" stroke-width="45" class="squeak-hitbox" />
                        <path d="M 157,6 C 240,40 310,130 351,220" fill="none" stroke="rgba(255, 255, 255, 0.45)" stroke-width="14" stroke-linecap="round" />
                        <path id="path-2" d="M 157,6 C 240,40 310,130 351,220" fill="none" stroke="url(#light-beam-grad)" stroke-width="8" stroke-linecap="round" filter="url(#beam-glow)" class="light-beam-path" />
                        <path d="M 157,6 C 240,40 310,130 351,220" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="60 120" class="flowing-path-dash pointer-events-none opacity-80" />
                        <g id="node-2" class="squeak-node">
                            <circle cx="270" cy="92" r="20" fill="#ffffff" stroke="#fbbf24" stroke-width="2.5" class="node-circle" />
                            <text x="270" y="92" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="900" fill="#b45309">2</text>
                        </g>
                    </g>

                    <!-- 4. Left Ear Outer Half -> Chapter 3 (פרק 3) -->
                    <g id="seg-group-3" class="cursor-pointer" data-id="3">
                        <path d="M 157,6 C 100,60 100,250 165,390" fill="none" stroke="transparent" stroke-width="45" class="squeak-hitbox" />
                        <path d="M 157,6 C 100,60 100,250 165,390" fill="none" stroke="rgba(255, 255, 255, 0.45)" stroke-width="14" stroke-linecap="round" />
                        <path id="path-3" d="M 157,6 C 100,60 100,250 165,390" fill="none" stroke="url(#light-beam-grad)" stroke-width="8" stroke-linecap="round" filter="url(#beam-glow)" class="light-beam-path" />
                        <path d="M 157,6 C 100,60 100,250 165,390" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="80 160" class="flowing-path-dash pointer-events-none opacity-80" />
                        <g id="node-3" class="squeak-node">
                            <circle cx="115" cy="166" r="20" fill="#ffffff" stroke="#c084fc" stroke-width="2.5" class="node-circle" />
                            <text x="115" y="166" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="900" fill="#7e22ce">3</text>
                        </g>
                    </g>


                    <!-- ============================================================== -->
                    <!-- LAYER 2: WHISKERS (6 WHISKERS) WITH FIXED NON-JUMPING NUMBERS  -->
                    <!-- ============================================================== -->

                    <!-- 5. Top Right Whisker -> Chapter 4 (פרק 4) -->
                    <g id="seg-group-4" class="cursor-pointer" data-id="4">
                        <path d="M 618,527 C 750,510 880,520 1005,550" fill="none" stroke="transparent" stroke-width="40" class="squeak-hitbox" />
                        <path d="M 618,527 C 750,510 880,520 1005,550" fill="none" stroke="rgba(255, 255, 255, 0.45)" stroke-width="13" stroke-linecap="round" />
                        <path id="path-4" d="M 618,527 C 750,510 880,520 1005,550" fill="none" stroke="url(#light-beam-grad)" stroke-width="7.5" stroke-linecap="round" filter="url(#beam-glow)" class="light-beam-path" />
                        <path d="M 618,527 C 750,510 880,520 1005,550" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="70 140" class="flowing-path-dash pointer-events-none opacity-80" />
                        <g id="node-4" class="squeak-node">
                            <circle cx="814" cy="521" r="18" fill="#ffffff" stroke="#f472b6" stroke-width="2.5" class="node-circle" />
                            <text x="814" y="521" text-anchor="middle" dominant-baseline="central" font-size="13" font-weight="900" fill="#be185d">4</text>
                        </g>
                    </g>

                    <!-- 6. Mid Right Whisker -> Chapter 5 (פרק 5) -->
                    <g id="seg-group-5" class="cursor-pointer" data-id="5">
                        <path d="M 622,567 C 750,565 870,590 975,645" fill="none" stroke="transparent" stroke-width="40" class="squeak-hitbox" />
                        <path d="M 622,567 C 750,565 870,590 975,645" fill="none" stroke="rgba(255, 255, 255, 0.45)" stroke-width="13" stroke-linecap="round" />
                        <path id="path-5" d="M 622,567 C 750,565 870,590 975,645" fill="none" stroke="url(#light-beam-grad)" stroke-width="7.5" stroke-linecap="round" filter="url(#beam-glow)" class="light-beam-path" />
                        <path d="M 622,567 C 750,565 870,590 975,645" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="70 140" class="flowing-path-dash pointer-events-none opacity-80" />
                        <g id="node-5" class="squeak-node">
                            <circle cx="807" cy="585" r="18" fill="#ffffff" stroke="#fb923c" stroke-width="2.5" class="node-circle" />
                            <text x="807" y="585" text-anchor="middle" dominant-baseline="central" font-size="13" font-weight="900" fill="#c2410c">5</text>
                        </g>
                    </g>

                    <!-- 7. Bot Right Whisker -> Chapter 6 (פרק 6) -->
                    <g id="seg-group-6" class="cursor-pointer" data-id="6">
                        <path d="M 622,622 C 710,618 790,635 860,680" fill="none" stroke="transparent" stroke-width="40" class="squeak-hitbox" />
                        <path d="M 622,622 C 710,618 790,635 860,680" fill="none" stroke="rgba(255, 255, 255, 0.45)" stroke-width="13" stroke-linecap="round" />
                        <path id="path-6" d="M 622,622 C 710,618 790,635 860,680" fill="none" stroke="url(#light-beam-grad)" stroke-width="7.5" stroke-linecap="round" filter="url(#beam-glow)" class="light-beam-path" />
                        <path d="M 622,622 C 710,618 790,635 860,680" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="50 100" class="flowing-path-dash pointer-events-none opacity-80" />
                        <g id="node-6" class="squeak-node">
                            <circle cx="748" cy="633" r="18" fill="#ffffff" stroke="#c084fc" stroke-width="2.5" class="node-circle" />
                            <text x="748" y="633" text-anchor="middle" dominant-baseline="central" font-size="13" font-weight="900" fill="#7e22ce">6</text>
                        </g>
                    </g>

                    <!-- 8. Top Left Whisker -> Chapter 7 (פרק 7) -->
                    <g id="seg-group-7" class="cursor-pointer" data-id="7">
                        <path d="M 405,527 C 275,510 145,520 20,550" fill="none" stroke="transparent" stroke-width="40" class="squeak-hitbox" />
                        <path d="M 405,527 C 275,510 145,520 20,550" fill="none" stroke="rgba(255, 255, 255, 0.45)" stroke-width="13" stroke-linecap="round" />
                        <path id="path-7" d="M 405,527 C 275,510 145,520 20,550" fill="none" stroke="url(#light-beam-grad)" stroke-width="7.5" stroke-linecap="round" filter="url(#beam-glow)" class="light-beam-path" />
                        <path d="M 405,527 C 275,510 145,520 20,550" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="70 140" class="flowing-path-dash pointer-events-none opacity-80" />
                        <g id="node-7" class="squeak-node">
                            <circle cx="211" cy="521" r="18" fill="#ffffff" stroke="#f472b6" stroke-width="2.5" class="node-circle" />
                            <text x="211" y="521" text-anchor="middle" dominant-baseline="central" font-size="13" font-weight="900" fill="#be185d">7</text>
                        </g>
                    </g>

                    <!-- 9. Mid Left Whisker -> Chapter 8 (פרק 8) -->
                    <g id="seg-group-8" class="cursor-pointer" data-id="8">
                        <path d="M 400,567 C 275,565 155,590 50,645" fill="none" stroke="transparent" stroke-width="40" class="squeak-hitbox" />
                        <path d="M 400,567 C 275,565 155,590 50,645" fill="none" stroke="rgba(255, 255, 255, 0.45)" stroke-width="13" stroke-linecap="round" />
                        <path id="path-8" d="M 400,567 C 275,565 155,590 50,645" fill="none" stroke="url(#light-beam-grad)" stroke-width="7.5" stroke-linecap="round" filter="url(#beam-glow)" class="light-beam-path" />
                        <path d="M 400,567 C 275,565 155,590 50,645" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="70 140" class="flowing-path-dash pointer-events-none opacity-80" />
                        <g id="node-8" class="squeak-node">
                            <circle cx="218" cy="585" r="18" fill="#ffffff" stroke="#38bdf8" stroke-width="2.5" class="node-circle" />
                            <text x="218" y="585" text-anchor="middle" dominant-baseline="central" font-size="13" font-weight="900" fill="#0284c7">8</text>
                        </g>
                    </g>

                    <!-- 10. Bot Left Whisker -> Chapter 9 (פרק 9) -->
                    <g id="seg-group-9" class="cursor-pointer" data-id="9">
                        <path d="M 400,622 C 315,618 235,635 165,680" fill="none" stroke="transparent" stroke-width="40" class="squeak-hitbox" />
                        <path d="M 400,622 C 315,618 235,635 165,680" fill="none" stroke="rgba(255, 255, 255, 0.45)" stroke-width="13" stroke-linecap="round" />
                        <path id="path-9" d="M 400,622 C 315,618 235,635 165,680" fill="none" stroke="url(#light-beam-grad)" stroke-width="7.5" stroke-linecap="round" filter="url(#beam-glow)" class="light-beam-path" />
                        <path d="M 400,622 C 315,618 235,635 165,680" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="50 100" class="flowing-path-dash pointer-events-none opacity-80" />
                        <g id="node-9" class="squeak-node">
                            <circle cx="277" cy="633" r="18" fill="#ffffff" stroke="#818cf8" stroke-width="2.5" class="node-circle" />
                            <text x="277" y="633" text-anchor="middle" dominant-baseline="central" font-size="13" font-weight="900" fill="#4338ca">9</text>
                        </g>
                    </g>


                    <!-- ============================================================== -->
                    <!-- LAYER 3: GLOWING LIGHT PARTICLES (FLOWING TO TIPS & CONDUITS)  -->
                    <!-- ============================================================== -->
                    <g id="flowing-particles-layer" class="pointer-events-none">
                        <!-- Frame Perimeter Particles -->
                        <circle r="4" fill="#ffffff" filter="url(#particle-glow)">
                            <animateMotion dur="20s" repeatCount="indefinite">
                                <mpath href="#bbox-frame-path" />
                            </animateMotion>
                            <animate attributeName="r" values="2.5; 5; 2.5" dur="1.8s" repeatCount="indefinite" />
                        </circle>
                        <circle r="7" fill="#f472b6" opacity="0.45" filter="url(#particle-glow)">
                            <animateMotion dur="20s" repeatCount="indefinite">
                                <mpath href="#bbox-frame-path" />
                            </animateMotion>
                        </circle>

                        <circle r="4" fill="#ffffff" filter="url(#particle-glow)">
                            <animateMotion dur="20s" begin="-10s" repeatCount="indefinite">
                                <mpath href="#bbox-frame-path" />
                            </animateMotion>
                            <animate attributeName="r" values="2.5; 5; 2.5" dur="1.8s" repeatCount="indefinite" />
                        </circle>
                        <circle r="7" fill="#fb923c" opacity="0.45" filter="url(#particle-glow)">
                            <animateMotion dur="20s" begin="-10s" repeatCount="indefinite">
                                <mpath href="#bbox-frame-path" />
                            </animateMotion>
                        </circle>

                        <!-- Whisker & Ear Traveling Pulse Particles -->
                        <!-- Whisker 4 Particle (Top Right) -->
                        <circle r="3.5" fill="#ffffff" filter="url(#particle-glow)">
                            <animateMotion dur="4.2s" repeatCount="indefinite">
                                <mpath href="#path-4" />
                            </animateMotion>
                            <animate attributeName="r" values="2; 4.5; 2" dur="1.4s" repeatCount="indefinite" />
                        </circle>
                        <circle r="6.5" fill="#ec4899" opacity="0.5" filter="url(#particle-glow)">
                            <animateMotion dur="4.2s" repeatCount="indefinite">
                                <mpath href="#path-4" />
                            </animateMotion>
                        </circle>

                        <!-- Whisker 5 Particle (Mid Right) -->
                        <circle r="3.5" fill="#ffffff" filter="url(#particle-glow)">
                            <animateMotion dur="3.8s" begin="-1.2s" repeatCount="indefinite">
                                <mpath href="#path-5" />
                            </animateMotion>
                            <animate attributeName="r" values="2; 4.5; 2" dur="1.4s" repeatCount="indefinite" />
                        </circle>
                        <circle r="6.5" fill="#f97316" opacity="0.5" filter="url(#particle-glow)">
                            <animateMotion dur="3.8s" begin="-1.2s" repeatCount="indefinite">
                                <mpath href="#path-5" />
                            </animateMotion>
                        </circle>

                        <!-- Whisker 6 Particle (Bot Right) -->
                        <circle r="3.5" fill="#ffffff" filter="url(#particle-glow)">
                            <animateMotion dur="3.5s" begin="-2.1s" repeatCount="indefinite">
                                <mpath href="#path-6" />
                            </animateMotion>
                            <animate attributeName="r" values="2; 4.5; 2" dur="1.4s" repeatCount="indefinite" />
                        </circle>

                        <!-- Whisker 7 Particle (Top Left) -->
                        <circle r="3.5" fill="#ffffff" filter="url(#particle-glow)">
                            <animateMotion dur="4.2s" begin="-0.7s" repeatCount="indefinite">
                                <mpath href="#path-7" />
                            </animateMotion>
                            <animate attributeName="r" values="2; 4.5; 2" dur="1.4s" repeatCount="indefinite" />
                        </circle>
                        <circle r="6.5" fill="#ec4899" opacity="0.5" filter="url(#particle-glow)">
                            <animateMotion dur="4.2s" begin="-0.7s" repeatCount="indefinite">
                                <mpath href="#path-7" />
                            </animateMotion>
                        </circle>

                        <!-- Whisker 8 Particle (Mid Left) -->
                        <circle r="3.5" fill="#ffffff" filter="url(#particle-glow)">
                            <animateMotion dur="3.8s" begin="-1.8s" repeatCount="indefinite">
                                <mpath href="#path-8" />
                            </animateMotion>
                            <animate attributeName="r" values="2; 4.5; 2" dur="1.4s" repeatCount="indefinite" />
                        </circle>
                        <circle r="6.5" fill="#f97316" opacity="0.5" filter="url(#particle-glow)">
                            <animateMotion dur="3.8s" begin="-1.8s" repeatCount="indefinite">
                                <mpath href="#path-8" />
                            </animateMotion>
                        </circle>

                        <!-- Whisker 9 Particle (Bot Left) -->
                        <circle r="3.5" fill="#ffffff" filter="url(#particle-glow)">
                            <animateMotion dur="3.5s" begin="-2.7s" repeatCount="indefinite">
                                <mpath href="#path-9" />
                            </animateMotion>
                            <animate attributeName="r" values="2; 4.5; 2" dur="1.4s" repeatCount="indefinite" />
                        </circle>

                        <!-- Ear Particles (Intro & 1) -->
                        <circle r="3.5" fill="#ffffff" filter="url(#particle-glow)">
                            <animateMotion dur="5.5s" repeatCount="indefinite">
                                <mpath href="#path-intro" />
                            </animateMotion>
                        </circle>
                        <circle r="3.5" fill="#ffffff" filter="url(#particle-glow)">
                            <animateMotion dur="5.0s" begin="-1.5s" repeatCount="indefinite">
                                <mpath href="#path-1" />
                            </animateMotion>
                        </circle>

                        <!-- Ear Particles (2 & 3) -->
                        <circle r="3.5" fill="#ffffff" filter="url(#particle-glow)">
                            <animateMotion dur="5.0s" begin="-2.5s" repeatCount="indefinite">
                                <mpath href="#path-2" />
                            </animateMotion>
                        </circle>
                        <circle r="3.5" fill="#ffffff" filter="url(#particle-glow)">
                            <animateMotion dur="5.5s" begin="-3.5s" repeatCount="indefinite">
                                <mpath href="#path-3" />
                            </animateMotion>
                        </circle>
                    </g>


                    <!-- ============================================================== -->
                    <!-- LAYER 4: EYES WITH TEXT CURVED ALONG THE LOWER CONTOUR          -->
                    <!-- (Hugs the lower curvature naturally - Pupils completely visible!)-->
                    <!-- ============================================================== -->

                    <!-- Left Eye -> Course Summary (סיכום הקורס) -->
                    <g id="eye-left-group" class="eye-container" data-id="summary">
                        <ellipse cx="391" cy="374" rx="58" ry="72" fill="#120722" stroke="url(#continuous-border-grad)" stroke-width="4.5" filter="url(#eye-glow)" class="eye-socket" />
                        
                        <!-- Normal Shiny Pupil & Reflections (Fades out in Night Mode) -->
                        <g id="pupil-left" class="pupil-group creepy-eye-normal">
                            <ellipse cx="391" cy="374" rx="44" ry="56" fill="#240e3f" />
                            <ellipse cx="391" cy="374" rx="42" ry="54" fill="none" stroke="#a78bfa" stroke-width="1.5" opacity="0.6" />
                            <ellipse cx="399" cy="358" rx="14" ry="20" fill="#ffffff" />
                            <circle cx="382" cy="388" r="4.5" fill="#ffffff" opacity="0.75" />
                        </g>

                        <!-- Creepy Scary Red Eye (Night Mode Only) -->
                        <g class="creepy-eye-night no-invert-dark pointer-events-none">
                            <ellipse cx="391" cy="374" rx="58" ry="72" fill="#0c0414" stroke="#ff1744" stroke-width="3" filter="url(#creepy-red-glow)" />
                            <ellipse cx="391" cy="374" rx="46" ry="58" fill="url(#creepy-iris-grad)" />
                            <ellipse cx="391" cy="374" rx="38" ry="50" fill="none" stroke="#fca5a5" stroke-width="1.5" opacity="0.4" stroke-dasharray="4 2" />
                            <g class="creepy-slit" style="transform-origin: 391px 374px;">
                                <path d="M 391,330 Q 382,374 391,418 Q 400,374 391,330 Z" fill="#000000" stroke="#ff0033" stroke-width="2" filter="url(#creepy-red-glow)" />
                                <path d="M 391,336 Q 385,374 391,412 Q 397,374 391,336 Z" fill="#000000" />
                                <circle cx="387" cy="360" r="3.5" fill="#ffffff" opacity="0.9" />
                                <circle cx="395" cy="385" r="2" fill="#ff4d4d" opacity="0.8" />
                            </g>
                        </g>

                        <!-- Arched Underlay Ribbon hugging the lower curve -->
                        <path d="M 345,398 A 50,54 0 0,0 437,398" fill="none" stroke="rgba(24, 8, 40, 0.88)" stroke-width="22" stroke-linecap="round" />
                        <path d="M 345,398 A 50,54 0 0,0 437,398" fill="none" stroke="#a78bfa" stroke-width="1.5" stroke-linecap="round" opacity="0.75" />

                        <!-- Arched Text along Lower Contour -->
                        <text font-size="11.5" font-weight="900" fill="#fdf2f8" text-anchor="middle" dominant-baseline="central" class="pointer-events-none">
                            <textPath href="#arc-left-smile" startOffset="50%">
                                סיכום הקורס 📖
                            </textPath>
                        </text>
                    </g>

                    <!-- Right Eye -> Exam Preparation (מאגר בחינות) -->
                    <g id="eye-right-group" class="eye-container" data-id="exams">
                        <ellipse cx="623" cy="384" rx="58" ry="72" fill="#120722" stroke="url(#continuous-border-grad)" stroke-width="4.5" filter="url(#eye-glow)" class="eye-socket" />
                        
                        <!-- Normal Shiny Pupil & Reflections (Fades out in Night Mode) -->
                        <g id="pupil-right" class="pupil-group creepy-eye-normal">
                            <ellipse cx="623" cy="384" rx="44" ry="56" fill="#380b26" />
                            <ellipse cx="623" cy="384" rx="42" ry="54" fill="none" stroke="#f472b6" stroke-width="1.5" opacity="0.6" />
                            <ellipse cx="631" cy="368" rx="14" ry="20" fill="#ffffff" />
                            <circle cx="614" cy="398" r="4.5" fill="#ffffff" opacity="0.75" />
                        </g>

                        <!-- Creepy Scary Red Eye (Night Mode Only) -->
                        <g class="creepy-eye-night no-invert-dark pointer-events-none">
                            <ellipse cx="623" cy="384" rx="58" ry="72" fill="#0c0414" stroke="#ff1744" stroke-width="3" filter="url(#creepy-red-glow)" />
                            <ellipse cx="623" cy="384" rx="46" ry="58" fill="url(#creepy-iris-grad)" />
                            <ellipse cx="623" cy="384" rx="38" ry="50" fill="none" stroke="#fca5a5" stroke-width="1.5" opacity="0.4" stroke-dasharray="4 2" />
                            <g class="creepy-slit" style="transform-origin: 623px 384px;">
                                <path d="M 623,340 Q 614,384 623,428 Q 632,384 623,340 Z" fill="#000000" stroke="#ff0033" stroke-width="2" filter="url(#creepy-red-glow)" />
                                <path d="M 623,346 Q 617,384 623,422 Q 629,384 623,346 Z" fill="#000000" />
                                <circle cx="619" cy="370" r="3.5" fill="#ffffff" opacity="0.9" />
                                <circle cx="627" cy="395" r="2" fill="#ff4d4d" opacity="0.8" />
                            </g>
                        </g>

                        <!-- Arched Underlay Ribbon hugging the lower curve -->
                        <path d="M 577,408 A 50,54 0 0,0 669,408" fill="none" stroke="rgba(24, 8, 40, 0.88)" stroke-width="22" stroke-linecap="round" />
                        <path d="M 577,408 A 50,54 0 0,0 669,408" fill="none" stroke="#f472b6" stroke-width="1.5" stroke-linecap="round" opacity="0.75" />

                        <!-- Arched Text along Lower Contour -->
                        <text font-size="11.5" font-weight="900" fill="#fdf2f8" text-anchor="middle" dominant-baseline="central" class="pointer-events-none">
                            <textPath href="#arc-right-smile" startOffset="50%">
                                מאגר בחינות 🎯
                            </textPath>
                        </text>
                    </g>

                    <!-- ============================================================== -->
                    <!-- LAYER 4.5: CREEPY MISCHIEVOUS CHESHIRE SMILE (NIGHT MODE ONLY) -->
                    <!-- (Emerges smoothly under the nose when switching to Dark Mode!) -->
                    <!-- ============================================================== -->
                    <g id="creepy-mouth-group" class="creepy-mouth creepy-glow no-invert-dark pointer-events-none">
                        <!-- Sinister Mouth Opening (Dark Crimson Void) -->
                        <path d="M 425,572 
                                 C 455,655 569,655 599,572 
                                 C 565,618 459,618 425,572 Z" 
                              fill="#180005" 
                              stroke="#ff0033" 
                              stroke-width="3" 
                              stroke-linejoin="round" />

                        <!-- Outer Glowing Grin Perimeter -->
                        <path d="M 415,562 Q 512,670 609,562" 
                              fill="none" 
                              stroke="#ff1744" 
                              stroke-width="3.5" 
                              stroke-linecap="round" 
                              filter="url(#creepy-red-glow)" />

                        <!-- Wicked Dimple Curves at corners -->
                        <path d="M 410,552 Q 417,562 425,572" fill="none" stroke="#ff1744" stroke-width="3.5" stroke-linecap="round" />
                        <path d="M 614,552 Q 607,562 599,572" fill="none" stroke="#ff1744" stroke-width="3.5" stroke-linecap="round" />

                        <!-- Upper Sharp Fangs & Razor Teeth -->
                        <polygon points="445,588 453,608 461,592" fill="#fff1f2" stroke="#dc2626" stroke-width="0.75" />
                        <polygon points="465,594 471,607 478,597" fill="#fff1f2" stroke="#dc2626" stroke-width="0.5" />
                        <polygon points="481,599 487,610 493,601" fill="#fff1f2" stroke="#dc2626" stroke-width="0.5" />
                        <polygon points="498,602 504,612 510,603" fill="#fff1f2" stroke="#dc2626" stroke-width="0.5" />
                        <polygon points="514,603 520,612 526,602" fill="#fff1f2" stroke="#dc2626" stroke-width="0.5" />
                        <polygon points="531,601 537,610 543,599" fill="#fff1f2" stroke="#dc2626" stroke-width="0.5" />
                        <polygon points="546,597 553,607 559,594" fill="#fff1f2" stroke="#dc2626" stroke-width="0.5" />
                        <polygon points="563,592 571,608 579,588" fill="#fff1f2" stroke="#dc2626" stroke-width="0.75" />

                        <!-- Lower Sharp Predatory Teeth -->
                        <polygon points="452,618 459,604 466,619" fill="#fff1f2" stroke="#dc2626" stroke-width="0.7" />
                        <polygon points="488,627 494,615 500,627" fill="#fff1f2" stroke="#dc2626" stroke-width="0.5" />
                        <polygon points="524,627 530,615 536,627" fill="#fff1f2" stroke="#dc2626" stroke-width="0.5" />
                        <polygon points="558,619 565,604 572,618" fill="#fff1f2" stroke="#dc2626" stroke-width="0.7" />
                    </g>

                </svg>

                <!-- ============================================================== -->
                <!-- THE CAT'S NOSE ITSELF: ORGANIC OVAL PILL WITH PARTIAL TRANSPARENCY-->
                <!-- (KEEPS THE NOSE SHAPE & PARTIAL TRANSPARENCY - NEVER A RECTANGLE!)-->
                <!-- ============================================================== -->
                <div id="cat-nose-container"
                    class="absolute left-1/2 top-[75.3%] -translate-x-1/2 -translate-y-1/2 z-30 group cursor-pointer flex items-center justify-center">
                    
                    <!-- The Nose Element (Semi-transparent Glass Pill, expands smoothly) -->
                    <div id="cat-nose-pill"
                        class="relative flex items-center justify-center overflow-hidden transition-all duration-400 ease-out nose-collapsed text-white">
                        
                        <!-- Internal Subtle Neon Shimmer inside the Nose -->
                        <div class="absolute inset-0 accent-spin-bg opacity-20 pointer-events-none"></div>

                        <!-- DEFAULT STATE: The Cat's Cute Nose (Fades out when expanded) -->
                        <div id="nose-default-view"
                            class="absolute inset-0 flex flex-col items-center justify-center transition-opacity duration-300 opacity-100 group-hover:opacity-0 pointer-events-none">
                            <!-- Nose Highlight -->
                            <span class="w-7 h-2 rounded-full bg-pink-400/90 mb-0.5 shadow-sm"></span>
                            <span class="text-[9px] font-black tracking-widest text-purple-200">SQUEAK</span>
                        </div>

                        <!-- EXPANDED STATE: Chapter Details inside the Semi-Transparent Nose (High Readability!) -->
                        <div id="nose-expanded-view"
                            class="absolute inset-0 flex flex-col items-center justify-center px-4 py-3 text-center transition-opacity duration-300 opacity-0 group-hover:opacity-100 pointer-events-auto gap-1">
                            <span id="nose-badge" class="px-3 py-0.5 rounded-full text-xs font-black bg-purple-100 text-purple-900 border border-purple-300 shadow-2xs">
                                פרק 1
                            </span>
                            <h4 id="nose-title" class="text-sm sm:text-[15px] font-black text-slate-900 leading-snug line-clamp-1 max-w-[370px]">
                                יסודות החשיבה מונחית העצמים וההפשטה
                            </h4>
                            <p id="nose-desc" class="text-xs text-slate-600 font-normal leading-normal max-w-[370px] px-1">
                                7 רמות ההפשטה בתוכנה, משל הפרחים של באד, מחזור חיי עצם ו-GC, זהות (==) מול שוויון (= ו-hash), ורמות העתקה.
                            </p>
                            <a id="nose-btn" href="20906_1.html"
                                class="inline-flex items-center gap-1.5 px-4 py-1.5 rounded-full text-xs font-bold text-white bg-gradient-to-r from-purple-600 via-pink-600 to-orange-500 hover:scale-105 active:scale-95 transition-all shadow-md mt-0.5">
                                <span>כניסה לפרק</span>
                                <i data-lucide="arrow-left" class="w-3.5 h-3.5"></i>
                            </a>
                        </div>
                    </div>
                </div>

            </div>

        </div>

    </main>

{footer_html}

    <!-- ========================================================================= -->
    <!-- CORE JAVASCRIPT: DATA & INTERACTIVE LOGIC                                 -->
    <!-- ========================================================================= -->
    <script>
        // 1. CHAPTERS DATA (9 CORE CHAPTERS + INTRO + SUMMARY + EXAMS)
        // Light beam palette: Purple, Pink, Orange
        const CHAPTERS_DATA = [
            {{
                id: "intro",
                numberLabel: "יחידה 0",
                badge: "יחידה 0 • מבוא והקדמה",
                title: "מבוא, הקדמה וארכיטקטורת הקורס",
                desc: "שער הכניסה ל-Pure OOP: הכרת שפת Smalltalk וסביבת Squeak, מפת 9 פרקי הליבה, 3 מצבי הלימוד וסודות ההצלחה בבחינה.",
                link: "0_intro.html",
                color: "#f472b6", // Soft Pastel Rose
                tags: ["Pure OOP", "Squeak", "3 מצבי לימוד", "סודות הבחינה"],
                segmentName: "חצי אוזן ימין חיצונית"
            }},
            {{
                id: "1",
                numberLabel: "פרק 1",
                badge: "פרק 1 • יסודות ה-OOP",
                title: "יסודות החשיבה מונחית העצמים וההפשטה",
                desc: "7 רמות ההפשטה בתוכנה, משל הפרחים של באד, מחזור חיי עצם ו-GC, זהות (==) מול שוויון (= ו-hash), ורמות העתקה.",
                link: "20906_1.html",
                color: "#fb923c", // Soft Pastel Coral
                tags: ["7 רמות הפשטה", "זהות == מול שוויון =", "חוזה hash", "shallow/deepCopy"],
                segmentName: "חצי אוזן ימין פנימית"
            }},
            {{
                id: "2",
                numberLabel: "פרק 2",
                badge: "פרק 2 • סביבת Squeak",
                title: "סביבת העבודה Squeak ופרויקט Quinto",
                desc: "הכרת סביבת הפיתוח החיה: ארכיטקטורת Image ו-Changes, כלי ה-System Browser, Debugger, ופיתוח משחק Quinto.",
                link: "20906_2.html",
                color: "#fbbf24", // Soft Warm Amber
                tags: ["Image & Changes", "System Browser", "Debugger & Inspector", "משחק Quinto"],
                segmentName: "חצי אוזן שמאל פנימית"
            }},
            {{
                id: "3",
                numberLabel: "פרק 3",
                badge: "פרק 3 • תחביר והודעות",
                title: "תחביר שפת Smalltalk וסוגי הודעות",
                desc: "3 סוגי הודעות (אונריות, בינריות ומילות-מפתח), חוקי קדימות משמאל לימין, 6 הפסאודו-משתנים ושרשור קסקייד (;).",
                link: "20906_3.html",
                color: "#c084fc", // Soft Lavender
                tags: ["Unary/Binary/Keyword", "קדימות משמאל לימין", "6 הפסאודו-משתנים", "Cascade ;"],
                segmentName: "חצי אוזן שמאל חיצונית"
            }},
            {{
                id: "4",
                numberLabel: "פרק 4",
                badge: "פרק 4 • בלוקים ו-SUnit",
                title: "מתודות, בלוקים (BlockClosure) ו-SUnit",
                desc: "הגדרת מתודות ואיסור השמה, סגורים לקסיקליים (BlockClosure), יציאה לא-מקומית (^), תנאים ולולאות ובדיקות SUnit.",
                link: "20906_4.html",
                color: "#f472b6", // Soft Pastel Rose
                tags: ["BlockClosure", "יציאה לא-מקומית ^", "ifTrue:ifFalse:", "בדיקות SUnit"],
                segmentName: "שערת שפם עליונה ימנית"
            }},
            {{
                id: "5",
                numberLabel: "פרק 5",
                badge: "פרק 5 • מחלקות והורשה",
                title: "מחלקות, הורשה ומנגנון Method Lookup",
                desc: "משתני מופע ומחלקה, אלגוריתם חיפוש מתודות בעץ הירושה, ההבדל בין self ל-super, ויירוט עם doesNotUnderstand:.",
                link: "20906_5.html",
                color: "#fb923c", // Soft Warm Coral
                tags: ["Method Lookup", "self מול super", "משתני מחלקה ומופע", "doesNotUnderstand:"],
                segmentName: "שערת שפם אמצעית ימנית"
            }},
            {{
                id: "6",
                numberLabel: "פרק 6",
                badge: "פרק 6 • אוספים ומספרים",
                title: "היררכיות הליבה ומערכת האוספים",
                desc: "המחלקה Object, עולם המספרים והשברים, עץ ה-Collections (Set, OrderedCollection, Dictionary) ואיטרטורים עשירים.",
                link: "20906_6.html",
                color: "#c084fc", // Soft Lavender
                tags: ["המחלקה Object", "היררכיית המספרים", "עץ Collections", "איטרטורים פולימורפיים"],
                segmentName: "שערת שפם תחתונה ימנית"
            }},
            {{
                id: "7",
                numberLabel: "פרק 7",
                badge: "פרק 7 • שמונה המלכות",
                title: "תכנון מונחה עצמים – חידת 8 המלכות",
                desc: "פתרון מבוזר ואלגנטי לחידת 8 המלכות ללא לולאות מקוננות, העברת אחריות ואלגוריתם Backtracking בין אובייקטים עצמאיים.",
                link: "20906_7.html",
                color: "#f472b6", // Soft Pastel Rose
                tags: ["Backtracking מבוזר", "חידת 8 המלכות", "QueenTerminator", "הכללה ל-NxN"],
                segmentName: "שערת שפם עליונה שמאלית"
            }},
            {{
                id: "8",
                numberLabel: "פרק 8",
                badge: "פרק 8 • ממשק Morphic",
                title: "ארכיטקטורת ממשק גרפי – Morphic",
                desc: "מודל ה-GUI החי של Squeak: עץ ה-submorphs, ממשק ה-Halo, טיפול באירועי עכבר ומקלדת, ואנימציה חיה עם Stepping.",
                link: "20906_8.html",
                color: "#38bdf8", // Soft Pastel Sky
                tags: ["עץ ה-Morphs", "ממשק Halo", "אירועי עכבר ומקלדת", "אנימציית Stepping"],
                segmentName: "שערת שפם אמצעית שמאלית"
            }},
            {{
                id: "9",
                numberLabel: "פרק 9",
                badge: "פרק 9 • מטה-מחלקות",
                title: "מודל מטה-המחלקות (Metaclass) ורפלקציה",
                desc: "מחלקה כעצם חי בזיכרון, 10 חוקי המודל האקסיומטיים, היררכיית Metaclass המקבילה, מודל 5 הרמות ומסלול Color new.",
                link: "20906_9.html",
                color: "#818cf8", // Soft Pastel Periwinkle
                tags: ["מודל 5 הרמות", "10 חוקי המודל", "היררכיית Metaclass", "מסלול Color new"],
                segmentName: "שערת שפם תחתונה שמאלית"
            }},
            {{
                id: "summary",
                numberLabel: "סיכום",
                badge: "סיכום הקורס המלא",
                title: "מחברת סיכום קורס מקיפה ומלאה",
                desc: "סיכום דיגיטלי הרמטי ושלם של כל 9 פרקי הליבה: עקרונות Pure OOP, תחביר Smalltalk, טבלאות השוואה וחוקי ברזל לבחינה.",
                link: "summary.html",
                color: "#c084fc",
                tags: ["כל 9 הפרקים", "100% כיסוי", "טבלאות השוואה", "חזרה מרוכזת"],
                segmentName: "עין ימין (סיכום הקורס)"
            }},
            {{
                id: "exams",
                numberLabel: "בחינות",
                badge: "מאגר בחינות ותרגול",
                title: "מאגר בחינות גמר ופתרונות מלאים",
                desc: "עשרות מועדי בחינה רשמיים עם פתרונות מלאים ל-100%: ניתוחי מעקב קוד, שאלות מטה-מחלקות, מסננים ומחברת נוסחאות.",
                link: "exams.html",
                color: "#f472b6",
                tags: ["מועדי 2026 ומבחני עבר", "פתרונות מלאים ל-100%", "7 ארכיטיפי שאלות", "מחברת נוסחאות"],
                segmentName: "עין שמאל (מאגר בחינות)"
            }}
        ];

        let activeChapterId = "1";

        // 2. HELPER UTILITIES
        function hexToRgba(hex, alpha) {{
            const r = parseInt(hex.slice(1, 3), 16);
            const g = parseInt(hex.slice(3, 5), 16);
            const b = parseInt(hex.slice(5, 7), 16);
            return `rgba(${{r}}, ${{g}}, ${{b}}, ${{alpha}})`;
        }}

        // 3. SET ACTIVE CHAPTER (EXPANDS THE CAT NOSE ITSELF)
        function setActiveChapter(id, triggerExpand = false) {{
            const chapter = CHAPTERS_DATA.find(c => c.id === id);
            if (!chapter) return;
            activeChapterId = id;

            // Update Cat Nose Content
            const badge = document.getElementById('nose-badge');
            const title = document.getElementById('nose-title');
            const desc = document.getElementById('nose-desc');
            const btn = document.getElementById('nose-btn');
            const pill = document.getElementById('cat-nose-pill');

            if (badge && title && desc && btn) {{
                badge.textContent = chapter.badge;
                badge.style.borderColor = chapter.color;
                badge.style.color = chapter.color;

                title.textContent = chapter.title;
                desc.textContent = chapter.desc;
                btn.href = chapter.link;

                if (triggerExpand && pill) {{
                    pill.style.borderColor = chapter.color;
                    pill.style.boxShadow = `0 22px 50px -10px ${{hexToRgba(chapter.color, 0.35)}}, 0 0 0 1px rgba(255, 255, 255, 0.9)`;
                    pill.classList.remove('nose-collapsed');
                    pill.classList.add('nose-expanded');
                }}
            }}

            // Highlight ONLY the specific SVG light beam path
            CHAPTERS_DATA.forEach(c => {{
                const p = document.getElementById(`path-${{c.id}}`);
                const n = document.getElementById(`node-${{c.id}}`);
                if (p) {{
                    if (c.id === id) {{
                        p.setAttribute('stroke', c.color);
                        p.setAttribute('stroke-width', '11');
                        p.style.filter = `drop-shadow(0 0 10px ${{c.color}})`;
                    }} else {{
                        p.setAttribute('stroke', 'url(#light-beam-grad)');
                        p.setAttribute('stroke-width', '7.5');
                        p.style.filter = 'url(#beam-glow)';
                    }}
                }}
                if (n) {{
                    if (c.id === id) {{
                        n.classList.add('active');
                    }} else {{
                        n.classList.remove('active');
                    }}
                }}
            }});
        }}

        // Collapse the cat nose back to small cute nose
        function collapseNose() {{
            const pill = document.getElementById('cat-nose-pill');
            if (pill) {{
                pill.classList.remove('nose-expanded');
                pill.classList.add('nose-collapsed');
                pill.style.borderColor = 'rgba(244, 114, 182, 0.75)';
                pill.style.boxShadow = '0 10px 25px rgba(0,0,0,0.2)';
            }}
        }}

        // 4. MOUSE TRACKING FOR EYES PUPILS (SMOOTH & ZERO JITTER)
        function initEyeTracking() {{
            const hubCard = document.getElementById('squeak-hub-card');
            const svg = document.getElementById('squeak-svg');
            const pupilL = document.getElementById('pupil-left');
            const pupilR = document.getElementById('pupil-right');
            if (!hubCard || !svg || !pupilL || !pupilR) return;

            hubCard.addEventListener('mousemove', (e) => {{
                const rect = svg.getBoundingClientRect();
                const mouseX = ((e.clientX - rect.left) / rect.width) * 1124 - 50;
                const mouseY = ((e.clientY - rect.top) / rect.height) * 785 - 35;

                // Left eye center: (391, 374)
                const dxL = mouseX - 391;
                const dyL = mouseY - 374;
                const distL = Math.hypot(dxL, dyL);
                const maxRangeL = 16;
                const ratioL = distL > 0 ? Math.min(distL, maxRangeL) / distL : 0;
                pupilL.style.transform = `translate(${{dxL * ratioL}}px, ${{dyL * ratioL}}px)`;

                // Right eye center: (623, 384)
                const dxR = mouseX - 623;
                const dyR = mouseY - 384;
                const distR = Math.hypot(dxR, dyR);
                const maxRangeR = 16;
                const ratioR = distR > 0 ? Math.min(distR, maxRangeR) / distR : 0;
                pupilR.style.transform = `translate(${{dxR * ratioR}}px, ${{dyR * ratioR}}px)`;
            }});

            hubCard.addEventListener('mouseleave', () => {{
                pupilL.style.transform = 'translate(0px, 0px)';
                pupilR.style.transform = 'translate(0px, 0px)';
                collapseNose();
            }});
        }}

        // 5. ATTACH LISTENERS TO SQUEAK SVG SEGMENTS & NODES
        function initSvgInteractivity() {{
            CHAPTERS_DATA.forEach(c => {{
                let elId = `seg-group-${{c.id}}`;
                if (c.id === 'summary') elId = 'eye-left-group';
                if (c.id === 'exams') elId = 'eye-right-group';
                const group = document.getElementById(elId);
                if (group) {{
                    group.style.cursor = 'pointer';
                    group.addEventListener('mouseenter', () => setActiveChapter(c.id, true));
                    group.addEventListener('mouseleave', () => collapseNose());
                    group.addEventListener('click', (e) => {{
                        e.preventDefault();
                        window.location.href = c.link;
                    }});
                    group.addEventListener('touchstart', (e) => {{
                        setActiveChapter(c.id, true);
                    }}, {{ passive: true }});
                }}
            }});

            const noseContainer = document.getElementById('cat-nose-container');
            if (noseContainer) {{
                noseContainer.addEventListener('mouseenter', () => {{
                    setActiveChapter(activeChapterId, true);
                }});
                noseContainer.addEventListener('mouseleave', () => {{
                    collapseNose();
                }});
                noseContainer.addEventListener('click', (e) => {{
                    if (e.target.tagName !== 'A' && !e.target.closest('a')) {{
                        const cur = CHAPTERS_DATA.find(c => c.id === activeChapterId);
                        if (cur) window.location.href = cur.link;
                    }}
                }});
            }}
        }}

        // 6. THEME TOGGLE (NORMAL -> DARK -> READING)
        // Handled centrally by theme-manager.js

        // 7. INITIALIZE ON DOM CONTENT LOADED
        document.addEventListener('DOMContentLoaded', () => {{
            applyTheme();
            initSvgInteractivity();
            initEyeTracking();
            setActiveChapter("1", false);
            collapseNose();
            if (typeof lucide !== 'undefined') lucide.createIcons();
        }});
    </script>

    <script src="ai_widget.js"></script>

    <!-- Cloudflare Web Analytics -->
    <script type='module' src='https://static.cloudflareinsights.com/beacon.min.js'
        data-cf-beacon='{{"token": "c8628b533416460cbb4be9e1b68a786d"}}'></script>
    <!-- End Cloudflare Web Analytics -->
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f'index.html successfully updated! Size: {len(html_content)} bytes')
