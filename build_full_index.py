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
            0% {{ background-position: -200% 0; }}
            100% {{ background-position: 200% 0; }}
        }}

        .silver-waves-bg {{
            background: linear-gradient(90deg, transparent 0%, rgba(255, 255, 255, 0.65) 50%, transparent 100%);
            background-size: 200% 100%;
            animation: silver-waves 3s linear infinite;
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
            width: 88px !important;
            height: 56px !important;
            border-radius: 28px !important;
            background: rgba(24, 8, 40, 0.7) !important;
            backdrop-filter: blur(12px) !important;
            -webkit-backdrop-filter: blur(12px) !important;
            border: 2px solid rgba(244, 114, 182, 0.75) !important;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.25) !important;
        }}

        /* Expanded State: Smooth organic oval pill with partial transparency */
        #cat-nose-container:hover #cat-nose-pill,
        #cat-nose-pill.nose-expanded {{
            width: 350px !important;
            min-height: 160px !important;
            height: auto !important;
            border-radius: 36px !important;
            background: rgba(20, 8, 35, 0.88) !important;
            backdrop-filter: blur(18px) !important;
            -webkit-backdrop-filter: blur(18px) !important;
            box-shadow: 0 20px 45px -5px rgba(236, 72, 153, 0.45) !important;
            padding: 0.75rem 1rem !important;
        }}

        @media (max-width: 640px) {{
            #cat-nose-container:hover #cat-nose-pill,
            #cat-nose-pill.nose-expanded {{
                width: 300px !important;
                min-height: 145px !important;
                border-radius: 30px !important;
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
    <!-- TOP-LEFT FIXED BUTTON: OTHER COURSES (SILVERY WHITE INTERIOR, ACCENT FRAME)-->
    <!-- ========================================================================= -->
    <a href="https://all-the-courses.pages.dev/"
        class="fixed top-4 left-4 sm:top-6 sm:left-6 z-50 group block bg-transparent rounded-full p-[3px] transition-all duration-500 hover:shadow-2xl hover:shadow-pink-500/30 hover:-translate-y-1 hover:scale-105 w-24 h-24 sm:w-28 sm:h-28 overflow-hidden"
        title="מעבר לפורטל כל הקורסים">
        
        <!-- Rotating Conic Border: Bordeaux, Purple, Pink, Orange -->
        <div class="accent-spin-bg"></div>

        <!-- Inner Silvery-White Glass Container (לבן כסוף, NOT colored inside!) -->
        <div class="bg-white/85 backdrop-blur-xl rounded-full w-full h-full relative z-10 flex flex-col items-center justify-center border border-white/80 group-hover:bg-white/95 transition-all duration-500 shadow-md text-center p-1 sm:p-2 overflow-hidden">
            <!-- Silver Waves Shimmer -->
            <div class="absolute inset-0 silver-waves-bg pointer-events-none z-0"></div>

            <!-- Silvery-white Icon Bubble -->
            <div class="w-8 h-8 sm:w-9 sm:h-9 mb-0.5 rounded-full bg-slate-100/90 border border-slate-200/50 flex items-center justify-center text-slate-700 group-hover:text-purple-900 group-hover:scale-110 transition-all duration-500 shadow-xs relative z-20">
                <i data-lucide="library" class="w-4 h-4 sm:w-5 sm:h-5"></i>
            </div>
            
            <!-- Text -->
            <span class="text-xs sm:text-sm font-black text-slate-800 group-hover:text-purple-950 transition-colors leading-tight relative z-20">
                לקורסים<br>נוספים
            </span>
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
                <h1 class="text-3xl sm:text-5xl md:text-6xl font-black text-slate-900 tracking-tight leading-none mb-3">
                    תכנות מונחה עצמים
                </h1>
                
                <!-- Subtitle -->
                <p class="text-sm sm:text-lg md:text-xl font-medium text-slate-700 max-w-2xl leading-relaxed mb-4">
                    פורטל הלמידה הראשי • סביבת <span class="font-extrabold text-purple-900">Smalltalk & Squeak</span>, מפת דרכים אינטראקטיבית, סיכומי עומק ומאגר בחינות
                </p>

                <!-- Quick Concept Tags -->
                <div class="flex flex-wrap items-center justify-center gap-2">
                    <span class="px-3 py-1 rounded-full text-xs font-bold bg-purple-50 text-purple-900 border border-purple-200">Pure OOP</span>
                    <span class="px-3 py-1 rounded-full text-xs font-bold bg-pink-50 text-pink-900 border border-pink-200">Everything is an Object</span>
                    <span class="px-3 py-1 rounded-full text-xs font-bold bg-orange-50 text-orange-900 border border-orange-200">Method Lookup</span>
                    <span class="px-3 py-1 rounded-full text-xs font-bold bg-fuchsia-50 text-fuchsia-900 border border-fuchsia-200">Morphic GUI</span>
                    <span class="px-3 py-1 rounded-full text-xs font-bold bg-rose-50 text-rose-950 border border-rose-200">Metaclass Loop</span>
                </div>

                <!-- Quick Direct Navigation Links Bar -->
                <div class="mt-5 pt-4 border-t border-purple-100/90 w-full flex flex-wrap items-center justify-center gap-2 sm:gap-3">
                    <a href="0_intro.html" class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs font-bold bg-white/90 hover:bg-purple-100/80 text-purple-900 border border-purple-200 shadow-xs hover:shadow-sm hover:scale-105 active:scale-95 transition-all">
                        <span>📖</span>
                        <span>יחידה 0: מבוא והקדמה</span>
                    </a>
                    <a href="summary.html" class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs font-bold bg-white/90 hover:bg-indigo-100/80 text-indigo-900 border border-indigo-200 shadow-xs hover:shadow-sm hover:scale-105 active:scale-95 transition-all">
                        <span>📑</span>
                        <span>מחברת סיכום הקורס</span>
                    </a>
                    <a href="exams.html" class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs font-bold bg-white/90 hover:bg-pink-100/80 text-pink-900 border border-pink-200 shadow-xs hover:shadow-sm hover:scale-105 active:scale-95 transition-all">
                        <span>⚔️</span>
                        <span>מאגר בחינות ופתרונות</span>
                    </a>
                    <a href="https://all-the-courses.pages.dev/" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs font-bold bg-gradient-to-r from-purple-50 to-pink-50 hover:from-purple-100 hover:to-pink-100 text-purple-950 border border-purple-200/80 shadow-xs hover:scale-105 active:scale-95 transition-all">
                        <span>🌐</span>
                        <span>כל הקורסים</span>
                    </a>
                    <a href="https://wa.me/972586736525" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs font-bold bg-green-50 hover:bg-green-100 text-green-900 border border-green-200 shadow-xs hover:scale-105 active:scale-95 transition-all">
                        <i class="fa-brands fa-whatsapp text-green-600 text-sm"></i>
                        <span>וואטסאפ</span>
                    </a>
                </div>
            </div>
        </div>
    </header>

    <!-- ========================================================================= -->
    <!-- CENTRAL SQUEAK INTERACTIVE HUB (DIRECTLY ON BACKGROUND CANVAS)            -->
    <!-- ========================================================================= -->
    <main class="relative w-full max-w-[1180px] mx-auto px-2 sm:px-6 py-2 z-20 mb-12 flex-1">
        
        <!-- Squeak Stage Container (Transparent, directly over the base64 background!) -->
        <div id="squeak-hub-card"
            class="relative w-full overflow-visible select-none flex flex-col items-center justify-center p-1 sm:p-2">

            <!-- Soft Helper Banner -->
            <div class="mb-3 px-5 py-1.5 rounded-full border border-purple-200/80 bg-white/75 backdrop-blur-md text-xs font-bold text-slate-700 shadow-xs flex items-center gap-2">
                <i data-lucide="mouse-pointer-2" class="w-3.5 h-3.5 text-pink-600"></i>
                <span>רחפו מעל חלקי העכבר – האף יתרחב ויציג את תוכן הפרק</span>
            </div>

            <!-- SVG Squeak Face Drawing Area (ViewBox comfortably fits ears and whiskers!) -->
            <div id="squeak-stage-wrapper" class="relative w-full max-w-[980px] mx-auto overflow-visible flex items-center justify-center">
                
                <svg id="squeak-svg" viewBox="-50 -35 1124 785" class="w-full h-auto overflow-visible" style="max-height: 620px;">
                    <defs>
                        <!-- Glowing Laser Light Beam Gradient (Purple, Pink, Orange) -->
                        <linearGradient id="light-beam-grad" x1="0%" y1="0%" x2="100%" y2="100%">
                            <stop offset="0%" stop-color="#7c3aed" />   <!-- Vibrant Purple -->
                            <stop offset="25%" stop-color="#ec4899" />  <!-- Neon Pink -->
                            <stop offset="50%" stop-color="#f97316" />  <!-- Bright Orange -->
                            <stop offset="75%" stop-color="#db2777" />  <!-- Deep Pink -->
                            <stop offset="100%" stop-color="#7c3aed" /> <!-- Loop to Purple -->
                        </linearGradient>

                        <!-- Soft Beam Glow Filter -->
                        <filter id="beam-glow" x="-20%" y="-20%" width="140%" height="140%">
                            <feGaussianBlur stdDeviation="3.5" result="blur" />
                            <feComposite in="SourceGraphic" in2="blur" operator="over" />
                        </filter>

                        <!-- Particle Core Glow Filter -->
                        <filter id="particle-glow" x="-40%" y="-40%" width="180%" height="180%">
                            <feGaussianBlur stdDeviation="3" result="blur" />
                            <feComposite in="SourceGraphic" in2="blur" operator="over" />
                        </filter>

                        <!-- Eye Socket Glow Filter -->
                        <filter id="eye-glow" x="-25%" y="-25%" width="150%" height="150%">
                            <feGaussianBlur stdDeviation="5" result="blur" />
                            <feComposite in="SourceGraphic" in2="blur" operator="over" />
                        </filter>
                    </defs>

                    <!-- ============================================================== -->
                    <!-- LAYER 0: EXPANDED BOUNDING FRAME & CONTINUOUS LIGHT BEAM PIPE   -->
                    <!-- (Ears & Whiskers are 100% comfortably contained inside!)        -->
                    <!-- ============================================================== -->
                    
                    <!-- Expanded Bounding Rect Path with ambient glow and light beam -->
                    <path id="bbox-frame-path"
                        d="M 15,-15 L 1009,-15 A 40,40 0 0 1 1049,25 L 1049,695 A 40,40 0 0 1 1009,735 L 15,735 A 40,40 0 0 1 -25,695 L -25,25 A 40,40 0 0 1 15,-15 Z"
                        fill="rgba(255, 255, 255, 0.04)"
                        stroke="rgba(255, 255, 255, 0.25)"
                        stroke-width="12" />

                    <path
                        d="M 15,-15 L 1009,-15 A 40,40 0 0 1 1049,25 L 1049,695 A 40,40 0 0 1 1009,735 L 15,735 A 40,40 0 0 1 -25,695 L -25,25 A 40,40 0 0 1 15,-15 Z"
                        fill="none"
                        stroke="url(#light-beam-grad)"
                        stroke-width="3"
                        stroke-dasharray="140 35 70 35"
                        stroke-linecap="round"
                        class="flowing-frame"
                        filter="url(#beam-glow)" />

                    <!-- Circular Framing Pipe Conduit enclosing the Squeak Face -->
                    <circle cx="512" cy="365" r="348" fill="none" stroke="rgba(255, 255, 255, 0.22)" stroke-width="20" />
                    <circle cx="512" cy="365" r="338" fill="none" stroke="rgba(255, 255, 255, 0.45)" stroke-width="1.5" />
                    <circle cx="512" cy="365" r="358" fill="none" stroke="rgba(255, 255, 255, 0.45)" stroke-width="1.5" />
                    <circle id="circular-pipe-path" cx="512" cy="365" r="348" fill="none" stroke="url(#light-beam-grad)" stroke-width="6" stroke-dasharray="150 50 70 50" stroke-linecap="round" class="flowing-pipe" />

                    <!-- Feeder Light Rays Connecting Outer Frame to Whisker & Ear Tips -->
                    <g class="pointer-events-none opacity-60">
                        <path id="feeder-ear-r" d="M 835,-15 L 835,6" stroke="url(#light-beam-grad)" stroke-width="2.5" stroke-dasharray="6 4" class="flowing-feeder" />
                        <path id="feeder-ear-l" d="M 157,-15 L 157,6" stroke="url(#light-beam-grad)" stroke-width="2.5" stroke-dasharray="6 4" class="flowing-feeder" />
                        <path id="feeder-whisker-rt" d="M 1049,550 L 1005,550" stroke="url(#light-beam-grad)" stroke-width="2.5" stroke-dasharray="6 4" class="flowing-feeder" />
                        <path id="feeder-whisker-rm" d="M 1049,645 Q 1012,645 975,645" fill="none" stroke="url(#light-beam-grad)" stroke-width="2.5" stroke-dasharray="6 4" class="flowing-feeder" />
                        <path id="feeder-whisker-lt" d="M -25,550 L 20,550" stroke="url(#light-beam-grad)" stroke-width="2.5" stroke-dasharray="6 4" class="flowing-feeder" />
                        <path id="feeder-whisker-lm" d="M -25,645 Q 12,645 50,645" fill="none" stroke="url(#light-beam-grad)" stroke-width="2.5" stroke-dasharray="6 4" class="flowing-feeder" />
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
                            <circle cx="881" cy="165" r="22" fill="#180828" stroke="#ec4899" stroke-width="2.5" class="node-circle" />
                            <text x="881" y="165" text-anchor="middle" dominant-baseline="central" font-size="11" font-weight="900" fill="#ffffff">מבוא</text>
                        </g>
                    </g>

                    <!-- 2. Right Ear Inner Half -> Chapter 1 (פרק 1) -->
                    <g id="seg-group-1" class="cursor-pointer" data-id="1">
                        <path d="M 835,6 C 750,40 680,130 655,220" fill="none" stroke="transparent" stroke-width="45" class="squeak-hitbox" />
                        <path d="M 835,6 C 750,40 680,130 655,220" fill="none" stroke="rgba(255, 255, 255, 0.45)" stroke-width="14" stroke-linecap="round" />
                        <path id="path-1" d="M 835,6 C 750,40 680,130 655,220" fill="none" stroke="url(#light-beam-grad)" stroke-width="8" stroke-linecap="round" filter="url(#beam-glow)" class="light-beam-path" />
                        <path d="M 835,6 C 750,40 680,130 655,220" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="60 120" class="flowing-path-dash pointer-events-none opacity-80" />
                        <g id="node-1" class="squeak-node">
                            <circle cx="723" cy="92" r="20" fill="#180828" stroke="#f97316" stroke-width="2.5" class="node-circle" />
                            <text x="723" y="92" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="900" fill="#ffffff">1</text>
                        </g>
                    </g>

                    <!-- 3. Left Ear Inner Half -> Chapter 2 (פרק 2) -->
                    <g id="seg-group-2" class="cursor-pointer" data-id="2">
                        <path d="M 157,6 C 240,40 310,130 351,220" fill="none" stroke="transparent" stroke-width="45" class="squeak-hitbox" />
                        <path d="M 157,6 C 240,40 310,130 351,220" fill="none" stroke="rgba(255, 255, 255, 0.45)" stroke-width="14" stroke-linecap="round" />
                        <path id="path-2" d="M 157,6 C 240,40 310,130 351,220" fill="none" stroke="url(#light-beam-grad)" stroke-width="8" stroke-linecap="round" filter="url(#beam-glow)" class="light-beam-path" />
                        <path d="M 157,6 C 240,40 310,130 351,220" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="60 120" class="flowing-path-dash pointer-events-none opacity-80" />
                        <g id="node-2" class="squeak-node">
                            <circle cx="270" cy="92" r="20" fill="#180828" stroke="#f97316" stroke-width="2.5" class="node-circle" />
                            <text x="270" y="92" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="900" fill="#ffffff">2</text>
                        </g>
                    </g>

                    <!-- 4. Left Ear Outer Half -> Chapter 3 (פרק 3) -->
                    <g id="seg-group-3" class="cursor-pointer" data-id="3">
                        <path d="M 157,6 C 100,60 100,250 165,390" fill="none" stroke="transparent" stroke-width="45" class="squeak-hitbox" />
                        <path d="M 157,6 C 100,60 100,250 165,390" fill="none" stroke="rgba(255, 255, 255, 0.45)" stroke-width="14" stroke-linecap="round" />
                        <path id="path-3" d="M 157,6 C 100,60 100,250 165,390" fill="none" stroke="url(#light-beam-grad)" stroke-width="8" stroke-linecap="round" filter="url(#beam-glow)" class="light-beam-path" />
                        <path d="M 157,6 C 100,60 100,250 165,390" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="80 160" class="flowing-path-dash pointer-events-none opacity-80" />
                        <g id="node-3" class="squeak-node">
                            <circle cx="115" cy="166" r="20" fill="#180828" stroke="#a855f7" stroke-width="2.5" class="node-circle" />
                            <text x="115" y="166" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="900" fill="#ffffff">3</text>
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
                            <circle cx="814" cy="521" r="18" fill="#180828" stroke="#ec4899" stroke-width="2.5" class="node-circle" />
                            <text x="814" y="521" text-anchor="middle" dominant-baseline="central" font-size="13" font-weight="900" fill="#ffffff">4</text>
                        </g>
                    </g>

                    <!-- 6. Mid Right Whisker -> Chapter 5 (פרק 5) -->
                    <g id="seg-group-5" class="cursor-pointer" data-id="5">
                        <path d="M 622,567 C 750,565 870,590 975,645" fill="none" stroke="transparent" stroke-width="40" class="squeak-hitbox" />
                        <path d="M 622,567 C 750,565 870,590 975,645" fill="none" stroke="rgba(255, 255, 255, 0.45)" stroke-width="13" stroke-linecap="round" />
                        <path id="path-5" d="M 622,567 C 750,565 870,590 975,645" fill="none" stroke="url(#light-beam-grad)" stroke-width="7.5" stroke-linecap="round" filter="url(#beam-glow)" class="light-beam-path" />
                        <path d="M 622,567 C 750,565 870,590 975,645" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="70 140" class="flowing-path-dash pointer-events-none opacity-80" />
                        <g id="node-5" class="squeak-node">
                            <circle cx="807" cy="585" r="18" fill="#180828" stroke="#f97316" stroke-width="2.5" class="node-circle" />
                            <text x="807" y="585" text-anchor="middle" dominant-baseline="central" font-size="13" font-weight="900" fill="#ffffff">5</text>
                        </g>
                    </g>

                    <!-- 7. Bot Right Whisker -> Chapter 6 (פרק 6) -->
                    <g id="seg-group-6" class="cursor-pointer" data-id="6">
                        <path d="M 622,622 C 710,618 790,635 860,680" fill="none" stroke="transparent" stroke-width="40" class="squeak-hitbox" />
                        <path d="M 622,622 C 710,618 790,635 860,680" fill="none" stroke="rgba(255, 255, 255, 0.45)" stroke-width="13" stroke-linecap="round" />
                        <path id="path-6" d="M 622,622 C 710,618 790,635 860,680" fill="none" stroke="url(#light-beam-grad)" stroke-width="7.5" stroke-linecap="round" filter="url(#beam-glow)" class="light-beam-path" />
                        <path d="M 622,622 C 710,618 790,635 860,680" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="50 100" class="flowing-path-dash pointer-events-none opacity-80" />
                        <g id="node-6" class="squeak-node">
                            <circle cx="748" cy="633" r="18" fill="#180828" stroke="#7c3aed" stroke-width="2.5" class="node-circle" />
                            <text x="748" y="633" text-anchor="middle" dominant-baseline="central" font-size="13" font-weight="900" fill="#ffffff">6</text>
                        </g>
                    </g>

                    <!-- 8. Top Left Whisker -> Chapter 7 (פרק 7) -->
                    <g id="seg-group-7" class="cursor-pointer" data-id="7">
                        <path d="M 405,527 C 275,510 145,520 20,550" fill="none" stroke="transparent" stroke-width="40" class="squeak-hitbox" />
                        <path d="M 405,527 C 275,510 145,520 20,550" fill="none" stroke="rgba(255, 255, 255, 0.45)" stroke-width="13" stroke-linecap="round" />
                        <path id="path-7" d="M 405,527 C 275,510 145,520 20,550" fill="none" stroke="url(#light-beam-grad)" stroke-width="7.5" stroke-linecap="round" filter="url(#beam-glow)" class="light-beam-path" />
                        <path d="M 405,527 C 275,510 145,520 20,550" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="70 140" class="flowing-path-dash pointer-events-none opacity-80" />
                        <g id="node-7" class="squeak-node">
                            <circle cx="211" cy="521" r="18" fill="#180828" stroke="#ec4899" stroke-width="2.5" class="node-circle" />
                            <text x="211" y="521" text-anchor="middle" dominant-baseline="central" font-size="13" font-weight="900" fill="#ffffff">7</text>
                        </g>
                    </g>

                    <!-- 9. Mid Left Whisker -> Chapter 8 (פרק 8) -->
                    <g id="seg-group-8" class="cursor-pointer" data-id="8">
                        <path d="M 400,567 C 275,565 155,590 50,645" fill="none" stroke="transparent" stroke-width="40" class="squeak-hitbox" />
                        <path d="M 400,567 C 275,565 155,590 50,645" fill="none" stroke="rgba(255, 255, 255, 0.45)" stroke-width="13" stroke-linecap="round" />
                        <path id="path-8" d="M 400,567 C 275,565 155,590 50,645" fill="none" stroke="url(#light-beam-grad)" stroke-width="7.5" stroke-linecap="round" filter="url(#beam-glow)" class="light-beam-path" />
                        <path d="M 400,567 C 275,565 155,590 50,645" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="70 140" class="flowing-path-dash pointer-events-none opacity-80" />
                        <g id="node-8" class="squeak-node">
                            <circle cx="218" cy="585" r="18" fill="#180828" stroke="#f97316" stroke-width="2.5" class="node-circle" />
                            <text x="218" y="585" text-anchor="middle" dominant-baseline="central" font-size="13" font-weight="900" fill="#ffffff">8</text>
                        </g>
                    </g>

                    <!-- 10. Bot Left Whisker -> Chapter 9 (פרק 9) -->
                    <g id="seg-group-9" class="cursor-pointer" data-id="9">
                        <path d="M 400,622 C 315,618 235,635 165,680" fill="none" stroke="transparent" stroke-width="40" class="squeak-hitbox" />
                        <path d="M 400,622 C 315,618 235,635 165,680" fill="none" stroke="rgba(255, 255, 255, 0.45)" stroke-width="13" stroke-linecap="round" />
                        <path id="path-9" d="M 400,622 C 315,618 235,635 165,680" fill="none" stroke="url(#light-beam-grad)" stroke-width="7.5" stroke-linecap="round" filter="url(#beam-glow)" class="light-beam-path" />
                        <path d="M 400,622 C 315,618 235,635 165,680" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="50 100" class="flowing-path-dash pointer-events-none opacity-80" />
                        <g id="node-9" class="squeak-node">
                            <circle cx="277" cy="633" r="18" fill="#180828" stroke="#7c3aed" stroke-width="2.5" class="node-circle" />
                            <text x="277" y="633" text-anchor="middle" dominant-baseline="central" font-size="13" font-weight="900" fill="#ffffff">9</text>
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
                    <!-- LAYER 4: EYES WITH TEXT DIRECTLY WRITTEN ON THEM               -->
                    <!-- ============================================================== -->

                    <!-- Left Eye -> Course Summary (סיכום הקורס) -->
                    <g id="eye-left-group" class="eye-container" data-id="summary">
                        <ellipse cx="391" cy="374" rx="58" ry="72" fill="#120722" stroke="url(#light-beam-grad)" stroke-width="5" filter="url(#eye-glow)" class="eye-socket" />
                        
                        <!-- Roving Pupil Behind Text -->
                        <g id="pupil-left" class="pupil-group">
                            <ellipse cx="391" cy="374" rx="42" ry="54" fill="#240e3f" />
                            <ellipse cx="391" cy="374" rx="40" ry="52" fill="none" stroke="#a855f7" stroke-width="2" opacity="0.8" />
                            <ellipse cx="399" cy="360" rx="14" ry="20" fill="#ffffff" />
                            <circle cx="382" cy="390" r="4.5" fill="#ffffff" opacity="0.75" />
                        </g>

                        <!-- Text Directly on Eye Surface -->
                        <g class="pointer-events-none">
                            <rect x="331" y="360" width="120" height="28" rx="14" fill="rgba(18, 7, 34, 0.85)" stroke="#a855f7" stroke-width="1.5" />
                            <text x="391" y="374" text-anchor="middle" dominant-baseline="central" font-size="12" font-weight="900" fill="#fdf2f8">סיכום הקורס 📖</text>
                        </g>
                    </g>

                    <!-- Right Eye -> Exam Preparation (מאגר בחינות) -->
                    <g id="eye-right-group" class="eye-container" data-id="exams">
                        <ellipse cx="623" cy="384" rx="58" ry="72" fill="#120722" stroke="url(#light-beam-grad)" stroke-width="5" filter="url(#eye-glow)" class="eye-socket" />
                        
                        <!-- Roving Pupil Behind Text -->
                        <g id="pupil-right" class="pupil-group">
                            <ellipse cx="623" cy="384" rx="42" ry="54" fill="#380b26" />
                            <ellipse cx="623" cy="384" rx="40" ry="52" fill="none" stroke="#db2777" stroke-width="2" opacity="0.8" />
                            <ellipse cx="631" cy="370" rx="14" ry="20" fill="#ffffff" />
                            <circle cx="614" cy="400" r="4.5" fill="#ffffff" opacity="0.75" />
                        </g>

                        <!-- Text Directly on Eye Surface -->
                        <g class="pointer-events-none">
                            <rect x="563" y="370" width="120" height="28" rx="14" fill="rgba(18, 7, 34, 0.85)" stroke="#db2777" stroke-width="1.5" />
                            <text x="623" y="384" text-anchor="middle" dominant-baseline="central" font-size="12" font-weight="900" fill="#fdf2f8">מאגר בחינות 🎯</text>
                        </g>
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

                        <!-- EXPANDED STATE: Chapter Details inside the Semi-Transparent Nose -->
                        <div id="nose-expanded-view"
                            class="absolute inset-0 flex flex-col items-center justify-center p-3 text-center transition-opacity duration-300 opacity-0 group-hover:opacity-100 pointer-events-auto">
                            <span id="nose-badge" class="px-2.5 py-0.5 rounded-full text-[10px] font-black bg-white/10 text-pink-300 border border-pink-400/40 mb-1">
                                פרק 1
                            </span>
                            <h4 id="nose-title" class="text-xs sm:text-sm font-black text-white leading-tight mb-1 line-clamp-1 drop-shadow-sm">
                                יסודות החשיבה מונחית העצמים
                            </h4>
                            <p id="nose-desc" class="text-[10px] sm:text-[11px] text-purple-200 leading-snug line-clamp-3 mb-2 drop-shadow-xs">
                                7 שלבי התפתחות ההפשטה בתוכנה, משל המלצר והשף, ועקרונות Pure OOP.
                            </p>
                            <a id="nose-btn" href="20906_1.html"
                                class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-[10px] font-bold text-white bg-gradient-to-r from-purple-600 via-pink-600 to-orange-500 hover:scale-105 active:scale-95 transition-all shadow-md">
                                <span>כניסה לפרק</span>
                                <i data-lucide="arrow-left" class="w-3 h-3"></i>
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
                desc: "שער הכניסה ל-Pure OOP: הכרת שפת Smalltalk וסביבת Squeak, מפת 9 פרקי הליבה, מדריך 3 מצבי הלימוד באתר, וסודות ההצלחה בבחינת הגמר.",
                link: "0_intro.html",
                color: "#ec4899", // Pink
                tags: ["Pure OOP", "Squeak", "3 מצבי לימוד", "סודות הבחינה"],
                segmentName: "חצי אוזן ימין חיצונית"
            }},
            {{
                id: "1",
                numberLabel: "פרק 1",
                badge: "פרק 1 • יסודות ה-OOP",
                title: "יסודות החשיבה מונחית העצמים, התפתחות ההפשטה והמושג 'עצם'",
                desc: "7 רמות ההפשטה בתוכנה, משבר התוכנה, משל הפרחים של באד, ADT מול מחלקה, מחזור חיי עצם ו-GC, זהות (==) מול שוויון (= ו-hash), ו-3 רמות העתקה.",
                link: "20906_1.html",
                color: "#f97316", // Warm Orange
                tags: ["7 רמות הפשטה", "זהות == מול שוויון =", "חוזה hash", "shallow/deepCopy"],
                segmentName: "חצי אוזן ימין פנימית"
            }},
            {{
                id: "2",
                numberLabel: "פרק 2",
                badge: "פרק 2 • סביבת Squeak",
                title: "סביבת העבודה Squeak, כלי הפיתוח ופרויקט Quinto",
                desc: "הכרת סביבת הפיתוח החיה: ארכיטקטורת Image ו-Changes, ממשק 3 כפתורי העכבר, ה-System Browser, ה-Inspector וה-Debugger, תכנון RDD ופיתוח משחק Quinto.",
                link: "20906_2.html",
                color: "#fb923c", // Light Orange
                tags: ["Image & Changes", "System Browser", "Debugger & Inspector", "משחק Quinto"],
                segmentName: "חצי אוזן שמאל פנימית"
            }},
            {{
                id: "3",
                numberLabel: "פרק 3",
                badge: "פרק 3 • תחביר והודעות",
                title: "תחביר שפת Smalltalk, סוגי הודעות וסדרי קדימויות",
                desc: "3 סוגי הודעות (אונריות, בינריות ומילות-מפתח), חוק קדימות משמאל לימין ללא עדיפות לכפל, 6 הפסאודו-משתנים, מערכים סטטיים מול דינמיים ושרשור קסקייד (;).",
                link: "20906_3.html",
                color: "#a855f7", // Purple
                tags: ["Unary/Binary/Keyword", "קדימות משמאל לימין", "6 הפסאודו-משתנים", "Cascade ;"],
                segmentName: "חצי אוזן שמאל חיצונית"
            }},
            {{
                id: "4",
                numberLabel: "פרק 4",
                badge: "פרק 4 • בלוקים ו-SUnit",
                title: "מתודות, בלוקים (BlockClosure), מבני בקרה פולימורפיים ו-SUnit",
                desc: "הגדרת מתודות ואיסור השמה לפרמטר, סגורים לקסיקליים (BlockClosure), יציאה לא-מקומית (^), תנאים ולולאות כהודעות פולימורפיות, וכתיבת בדיקות יחידה ב-SUnit.",
                link: "20906_4.html",
                color: "#db2777", // Pink Rose
                tags: ["BlockClosure", "יציאה לא-מקומית ^", "ifTrue:ifFalse:", "בדיקות SUnit"],
                segmentName: "שערת שפם עליונה ימנית"
            }},
            {{
                id: "5",
                numberLabel: "פרק 5",
                badge: "פרק 5 • מחלקות והורשה",
                title: "המושג 'מחלקה', הורשה, Traits ומנגנון ה-Method Lookup",
                desc: "3 תפקידי המחלקה, משתני מופע מול מחלקה, אלגוריתם חיפוש מתודות בעץ הירושה, ההבדל היסודי בין self ל-super, שימוש ב-Traits, ויירוט הודעות עם doesNotUnderstand:.",
                link: "20906_5.html",
                color: "#f97316", // Orange
                tags: ["Method Lookup", "self מול super", "משתני מחלקה ומופע", "doesNotUnderstand:"],
                segmentName: "שערת שפם אמצעית ימנית"
            }},
            {{
                id: "6",
                numberLabel: "פרק 6",
                badge: "פרק 6 • אוספים ומספרים",
                title: "היררכיות הליבה, מספרים ומערכת האוספים (Collections)",
                desc: "המחלקה Object, עולם המספרים והשברים (Fraction), עץ האוספים (Array, OrderedCollection, Set, Dictionary), הבדל בין Set ל-IdentitySet, ואיטרטורים עשירים (do, collect, inject).",
                link: "20906_6.html",
                color: "#7c3aed", // Royal Purple
                tags: ["המחלקה Object", "היררכיית המספרים", "עץ Collections", "איטרטורים פולימורפיים"],
                segmentName: "שערת שפם תחתונה ימנית"
            }},
            {{
                id: "7",
                numberLabel: "פרק 7",
                badge: "פרק 7 • שמונה המלכות",
                title: "תכנון מונחה עצמים מבוזר – חידת שמונה המלכות",
                desc: "פתרון מבוזר ואלגנטי לחידת 8 המלכות ללא לולאות מקוננות, העברת אחריות ואלגוריתם Backtracking בין אובייקטים עצמאיים (QueenTerminator), הכללה ל-NxN וניתוח 8 הסימטריות.",
                link: "20906_7.html",
                color: "#ec4899", // Pink
                tags: ["Backtracking מבוזר", "חידת 8 המלכות", "QueenTerminator", "הכללה ל-NxN"],
                segmentName: "שערת שפם עליונה שמאלית"
            }},
            {{
                id: "8",
                numberLabel: "פרק 8",
                badge: "פרק 8 • ממשק Morphic",
                title: "ארכיטקטורת ממשק גרפי מונחה עצמים – Morphic",
                desc: "מודל ה-GUI החי והישיר של Squeak: עץ ההכלה (submorphs ו-owner), ממשק ה-Halo, מערכת הצירים, ציור על Canvas, טיפול באירועי עכבר ומקלדת, ואנימציה חיה עם Stepping.",
                link: "20906_8.html",
                color: "#f97316", // Orange
                tags: ["עץ ה-Morphs", "ממשק Halo", "אירועי עכבר ומקלדת", "אנימציית Stepping"],
                segmentName: "שערת שפם אמצעית שמאלית"
            }},
            {{
                id: "9",
                numberLabel: "פרק 9",
                badge: "פרק 9 • מטה-מחלקות",
                title: "מודל מטה-המחלקות (Metaclass) ורפלקציה ב-Smalltalk",
                desc: "גולת הכותרת של הקורס: מחלקה כעצם חי בזיכרון, 10 חוקי המודל האקסיומטיים, היררכיית המטה-מחלקות המקבילה, מודל 5 הרמות, מעקב שיגור Color new, ורפלקציה בזמן ריצה.",
                link: "20906_9.html",
                color: "#8b5cf6", // Purple
                tags: ["מודל 5 הרמות", "10 חוקי המודל", "היררכיית Metaclass", "מסלול Color new"],
                segmentName: "שערת שפם תחתונה שמאלית"
            }},
            {{
                id: "summary",
                numberLabel: "סיכום",
                badge: "סיכום הקורס המלא",
                title: "מחברת סיכום קורס מקיפה ומלאה (100% כיסוי)",
                desc: "סיכום דיגיטלי הרמטי ושלם של כל 9 פרקי הליבה: עקרונות Pure OOP, תחביר שפת Smalltalk, כלי סביבת Squeak, טבלאות השוואה, חוקי ברזל ומודל 5 הרמות – מושלם לחזרה לקראת הבחינה.",
                link: "summary.html",
                color: "#a855f7",
                tags: ["כל 9 הפרקים", "100% כיסוי", "טבלאות השוואה", "חזרה מרוכזת"],
                segmentName: "עין ימין (סיכום הקורס)"
            }},
            {{
                id: "exams",
                numberLabel: "בחינות",
                badge: "מאגר בחינות ותרגול",
                title: "מאגר בחינות גמר אינטראקטיבי ופתרונות מלאים",
                desc: "עשרות מועדי בחינה רשמיים עם פתרונות מומחה מפורטים ל-100%: ניתוחי מעקב קוד, שאלות מטה-מחלקות ורפלקציה, מסננים לפי 7 ארכיטיפים, מחברת נוסחאות ותרשימים מלאה.",
                link: "exams.html",
                color: "#ec4899",
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
                    pill.style.boxShadow = `0 18px 40px -5px ${{hexToRgba(chapter.color, 0.45)}}`;
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
                pill.style.boxShadow = '0 10px 25px rgba(0,0,0,0.25)';
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
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f'index.html successfully updated! Size: {len(html_content)} bytes')
