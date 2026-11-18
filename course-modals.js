/**
 * course-modals.js - מודאלים אינטראקטיביים לקורס תכנות מונחה עצמים (20906)
 * 1. מדריך ומפת האתר (כניסה ראשונה / יום 1)
 * 2. תזכורת הפצה ושיתוף מאגר הקורסים (אחרי 24 שעות ומחזורי כל 5 ימים)
 * מבוסס על localStorage מלא, ללא מעקב חיצוני, ועיצוב Glassmorphism תואם פלטת Squeak Purple & Fuchsia.
 */

(function () {
    const COURSE_ID = 'oop';
    const COURSE_NAME = 'תכנות מונחה עצמים (20906)';
    const PORTAL_URL = 'https://all-the-courses.pages.dev/';

    const KEY_FIRST_VISIT = `${COURSE_ID}_modal_first_seen_ts`;
    const KEY_DAY1_SHOWN = `${COURSE_ID}_welcome_modal_shown`;
    const KEY_LAST_SHARE_POPUP = `${COURSE_ID}_last_share_popup_ts`;

    const ONE_DAY_MS = 24 * 60 * 60 * 1000;
    const FIVE_DAYS_MS = 5 * 24 * 60 * 60 * 1000;

    // Injected styles
    function injectStyles() {
        if (document.getElementById(`${COURSE_ID}-modals-style`)) return;
        const style = document.createElement('style');
        style.id = `${COURSE_ID}-modals-style`;
        style.textContent = `
            .oop-modal-overlay {
                position: fixed;
                inset: 0;
                z-index: 99999;
                background: rgba(7, 22, 44, 0.7);
                backdrop-filter: blur(4px);
                -webkit-backdrop-filter: blur(4px);
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 1rem;
                opacity: 0;
                pointer-events: none;
                transition: opacity 0.3s ease;
            }
            .oop-modal-overlay.active {
                opacity: 1;
                pointer-events: auto;
            }
            .oop-modal-card {
                background: #ffffff !important;
                color: #0f172a !important;
                border: 1.5px solid #e9d5ff;
                border-radius: 1.5rem;
                box-shadow: 0 25px 50px -12px rgba(147, 51, 234, 0.22), 0 0 0 1px #e9d5ff;
                max-width: 44rem;
                width: 100%;
                max-height: 90vh;
                display: flex;
                flex-direction: column;
                transform: scale(0.96);
                transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
                direction: rtl;
                text-align: right;
                overflow: hidden;
                font-family: system-ui, -apple-system, 'Segoe UI', Roboto, 'Heebo', sans-serif;
                -webkit-font-smoothing: antialiased;
            }
            .oop-modal-overlay.active .oop-modal-card {
                transform: scale(1);
            }
            .oop-modal-header {
                padding: 1.25rem 1.5rem;
                border-bottom: 1px solid #e9d5ff;
                display: flex;
                align-items: center;
                justify-content: space-between;
                background: linear-gradient(180deg, #faf5ff 0%, #ffffff 100%);
            }
            .oop-modal-body {
                padding: 1.25rem 1.5rem;
                overflow-y: auto;
                flex: 1;
            }
            .oop-accordion-item {
                border: 1.5px solid #e2e8f0;
                border-radius: 0.85rem;
                margin-bottom: 0.65rem;
                overflow: hidden;
                background: #ffffff;
                transition: border-color 0.2s ease, box-shadow 0.2s ease, background-color 0.2s ease;
            }
            .oop-accordion-item:hover {
                border-color: #e9d5ff;
                background: #faf5ff;
                box-shadow: 0 4px 14px rgba(147, 51, 234, 0.22);
            }
            .oop-accordion-item.open {
                border-color: #9333ea;
                box-shadow: 0 4px 18px rgba(147, 51, 234, 0.22);
            }
            .oop-accordion-header {
                width: 100%;
                padding: 0.85rem 1.15rem;
                background: #ffffff;
                border: none;
                display: flex;
                justify-content: space-between;
                align-items: center;
                cursor: pointer;
                font-weight: 700;
                font-size: 0.92rem;
                color: #0f172a;
                transition: background 0.15s ease;
            }
            .oop-accordion-header:hover {
                background: #faf5ff;
            }
            .oop-accordion-content {
                display: none;
                padding: 0.85rem 1.15rem 1rem 1.15rem;
                background: #f8fafc;
                border-top: 1px dashed #e9d5ff;
                font-size: 0.875rem;
                line-height: 1.6;
                color: #334155;
            }
            .oop-accordion-content.open {
                display: block;
                animation: oopFadeDown 0.2s ease forwards;
            }
            @keyframes oopFadeDown {
                from { opacity: 0; transform: translateY(-4px); }
                to { opacity: 1; transform: translateY(0); }
            }
            .oop-copy-toast {
                position: fixed;
                bottom: 2rem;
                left: 50%;
                transform: translateX(-50%) translateY(20px);
                background: #0f172a;
                color: #ffffff;
                padding: 0.75rem 1.5rem;
                border-radius: 9999px;
                font-weight: 600;
                font-size: 0.9rem;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.25);
                border: 1px solid #9333ea;
                opacity: 0;
                pointer-events: none;
                transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
                z-index: 100000;
            }
            .oop-copy-toast.show {
                opacity: 1;
                transform: translateX(-50%) translateY(0);
            }
        `;
        document.head.appendChild(style);
    }

    // Modal 1: Day 1 Guide & Course Map
    function buildWelcomeModal() {
        if (document.getElementById('oop-welcome-modal')) return;

        const overlay = document.createElement('div');
        overlay.id = 'oop-welcome-modal';
        overlay.className = 'oop-modal-overlay no-invert active';

        overlay.innerHTML = `
            <div class="oop-modal-card">
                <div class="oop-modal-header">
                    <div style="display: flex; align-items: center; gap: 0.75rem;">
                        <span style="font-size: 1.6rem;">🐭</span>
                        <div>
                            <h3 style="margin: 0; font-size: 1.15rem; font-weight: 800; color: #7e22ce;">
                                מדריך שימוש באתר • תכנות מונחה עצמים (Smalltalk & Squeak) (20906)
                            </h3>
                            <p style="margin: 0; font-size: 0.8rem; color: #475569; font-weight: 500;">
                                המדריך המעשי לעולם ה-Pure OOP, סביבת Squeak ומפת הקורס
                            </p>
                        </div>
                    </div>
                    <button onclick="window.closeCourseWelcomeModal()" aria-label="סגירה"
                        style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 9999px; width: 2.2rem; height: 2.2rem; display: flex; align-items: center; justify-content: center; cursor: pointer; color: #9333ea; font-size: 1.1rem; font-weight: bold; transition: all 0.2s ease;">
                        ✕
                    </button>
                </div>

                <div class="oop-modal-body">
                    <div style="background: #faf5ff; border: 1.5px solid #e9d5ff; border-radius: 1rem; padding: 1rem 1.25rem; margin-bottom: 1.25rem;">
                        <p style="margin: 0; font-size: 0.9rem; line-height: 1.55; color: #1e293b; font-weight: 600;">
                            🧭 <strong>איך לעבוד עם האתר, מצבי הלימוד וכלי התרגול:</strong> כל הסעיפים מטה מוצגים כתיבות מכתב סגורות ומסודרות. לחצו על כל סעיף כדי לפתוח אותו ולקבל פירוט מלא על אופן הפעולה, הכלים והיתרונות המובנים בו:
                        </p>
                    </div>

                    <div style="margin-bottom: 1rem;">
                        <h4 style="margin: 0 0 0.65rem 0; font-size: 0.95rem; font-weight: 800; color: #0f172a;">
                            🧭 מבנה האתר וארגז הכלים לקורס:
                        </h4>

                        <!-- פריט 1: פרקי הלימוד (סגור בהתחלה) -->
                        <div class="oop-accordion-item" id="oop-accordion-item-1">
                            <button class="oop-accordion-header" onclick="window.__oopToggleAcc(1)">
                                <span>📚 1. פרקי הלימוד ואופן הלמידה המודולרי</span>
                                <span id="oop-acc-arrow-1" style="font-size: 0.85rem; color: #9333ea; transition: transform 0.2s;">▼</span>
                            </button>
                            <div class="oop-accordion-content" id="oop-acc-content-1">
                                <div style="font-size: 0.86rem; color: #334155; line-height: 1.6; margin-bottom: 0.75rem;">
                                    9 פרקי לימוד מקיפים (מודל האובייקטים הטהור, תחביר Smalltalk וסביבת Squeak, שיגור הודעות, מחלקות וירושה, ההבדל בין self ל-super, בלוקים ופונקציות מסדר גבוה, אוספים Collections, ורפלקציה).
                                    
                                <div style="background: #faf5ff; border: 1.5px solid #e9d5ff; border-radius: 12px; padding: 12px 14px; margin: 10px 0;">
                                    <strong style="color: #7e22ce; font-size: 14px; display: block; margin-bottom: 6px;">📑 מבנה הלימוד המודולרי:</strong>
                                    <p style="margin: 0 0 8px 0; font-size: 13px; line-height: 1.55; color: #334155;">
                                        הפרקים בנויים בלמידה מודולרית הדרגתית: מעבר מתפיסה עיונית, דרך פירוק מנגנונים ותרשימי זרימה, ועד תרגול מעשי של שאלות מבחן מוטמעות בכל נושא.
                                    </p>
                                </div>
                                </div>
                                <div style="display: flex; justify-content: flex-end;">
                                    <a href="20906_1.html" style="display: inline-flex; align-items: center; gap: 0.35rem; font-size: 0.8rem; font-weight: 700; color: #ffffff; background: #9333ea; padding: 0.35rem 0.85rem; border-radius: 0.5rem; text-decoration: none;">
                                        <span>כניסה לפרק 1: מודל האובייקטים והודעות</span>
                                        <span>←</span>
                                    </a>
                                </div>
                            </div>
                        </div>

                        <!-- פריט 2: הסימולציות והעזרים (סגור בהתחלה) -->
                        <div class="oop-accordion-item" id="oop-accordion-item-2">
                            <button class="oop-accordion-header" onclick="window.__oopToggleAcc(2)">
                                <span>🌊 2. הסימולציות והעזרים הגרפיים — מה לומדים מהם ואיך לתפעל</span>
                                <span id="oop-acc-arrow-2" style="font-size: 0.85rem; color: #9333ea; transition: transform 0.2s;">▼</span>
                            </button>
                            <div class="oop-accordion-content" id="oop-acc-content-2">
                                <div style="font-size: 0.86rem; color: #334155; line-height: 1.6; margin-bottom: 0.75rem;">
                                    העזרים הוויזואליים שזורים ישירות בתוך פרקי הלימוד:
                                    <ul style="margin: 6px 0; padding-right: 18px; line-height: 1.6; font-size: 12.5px;">
                                        <li><strong>🎯 מה הערך הפדגוגי שלהם:</strong> הסימולציות נועדו להמחיש את המנגנונים הדינמיים (התנהגות אלגוריתמים, תנועת נתונים ופרוטוקולים) שקשה לתפוס מטקסט סטטי בלבד.</li>
                                        <li><strong>💡 איך ללמוד מהם נכון:</strong> אל תסתפקו בהתבוננות פסיבית! שנו פרמטרים, הזינו קלטים שונים, הריצו תהליכים צעד-אחר-צעד, ובדקו מקרי קצה כדי לראות את התגובה בזמן אמת.</li>
                                        <li><strong>🔍 בקורס זה:</strong> סימולטור ויזואלי של מנגנון שיגור ההודעות (Message Dispatch) במעלה עץ ההורשה: המחשה חיה של ההבדל הקריטי בין self (חיפוש ממחלקת המקבל) ל-super (חיפוש ממחלקת האב).</li>
                                    </ul>
                                </div>
                                <div style="display: flex; justify-content: flex-end;">
                                    <a href="20906_1.html" style="display: inline-flex; align-items: center; gap: 0.35rem; font-size: 0.8rem; font-weight: 700; color: #ffffff; background: #9333ea; padding: 0.35rem 0.85rem; border-radius: 0.5rem; text-decoration: none;">
                                        <span>למעבדות בפרק הראשון</span>
                                        <span>←</span>
                                    </a>
                                </div>
                            </div>
                        </div>

                        <!-- פריט 3: שאלות ופתרונות (סגור בהתחלה) -->
                        <div class="oop-accordion-item" id="oop-accordion-item-3">
                            <button class="oop-accordion-header" onclick="window.__oopToggleAcc(3)">
                                <span>🎯 3. תרגול שאלות, מצבי הפתרון וניתוח מסיחים</span>
                                <span id="oop-acc-arrow-3" style="font-size: 0.85rem; color: #9333ea; transition: transform 0.2s;">▼</span>
                            </button>
                            <div class="oop-accordion-content" id="oop-acc-content-3">
                                <div style="font-size: 0.86rem; color: #334155; line-height: 1.6; margin-bottom: 0.75rem;">
                                    תרגול אקטיבי המכין ישירות לבחינה:
                                    <ul style="margin: 6px 0; padding-right: 18px; line-height: 1.6; font-size: 12.5px;">
                                        <li><strong>❓ שאלות הכוונה (Active Recall):</strong> לצד תת-סעיפים מוטמע כפתור ❓. נסו לענות בעצמכם לפני פתיחת הפתרון כדי לוודא שאתם מסוגלים לשחזר את החומר לבד.</li>
                                        <li><strong>🎚️ שלבי חשיפת הפתרון:</strong> רמז (כיוון ראשוני מבלי לחשוף את התשובה), שלד פתרון (שלבי מפתח), ופתרון מלא ומנומק שלב-אחר-שלב.</li>
                                        <li><strong>🧠 ניתוח מסיחים מעמיק:</strong> בשאלות רב-ברירה, המערכת מפרקת עבורכם למה כל מסיח מטעה, איזו הנחה שגויה הובילה אליו, ואיך להיזהר ממלכודות הבחינה.</li>
                                    </ul>
                                </div>
                                <div style="display: flex; justify-content: flex-end;">
                                    <a href="20906_1.html" style="display: inline-flex; align-items: center; gap: 0.35rem; font-size: 0.8rem; font-weight: 700; color: #ffffff; background: #9333ea; padding: 0.35rem 0.85rem; border-radius: 0.5rem; text-decoration: none;">
                                        <span>לתרגול בפרקים</span>
                                        <span>←</span>
                                    </a>
                                </div>
                            </div>
                        </div>

                        <!-- פריט 4: מאגר הבחינות והדרייב (סגור בהתחלה) -->
                        <div class="oop-accordion-item" id="oop-accordion-item-4">
                            <button class="oop-accordion-header" onclick="window.__oopToggleAcc(4)">
                                <span>📑 4. מאגר הבחינות, קובצי המקור ב-Google Drive ומחברות (91–100)</span>
                                <span id="oop-acc-arrow-4" style="font-size: 0.85rem; color: #9333ea; transition: transform 0.2s;">▼</span>
                            </button>
                            <div class="oop-accordion-content" id="oop-acc-content-4">
                                <div style="font-size: 0.86rem; color: #334155; line-height: 1.6; margin-bottom: 0.75rem;">
                                    הכנה מעשית ממוקדת לבחינת הגמר:
                                    <ul style="margin: 6px 0; padding-right: 18px; line-height: 1.6; font-size: 12.5px;">
                                        <li><strong>📁 מה כולל מאגר ה-Google Drive:</strong> סריקות מקור של טפסי בחינה, פתרונות רשמיים, ומחברות בחינה אמיתיות של סטודנטים שקיבלו 91–100 להשוואת רמת הניסוח והנימוק.</li>
                                        <li><strong>🎯 מצב מיקוד לבחינה:</strong> תרגול שאלות ומבחנים בסביבה נקייה מהסחות דעת עם שעון עצר לסימולציית תנאי אמת.</li>
                                    </ul>
                                </div>
                                <div style="display: flex; justify-content: flex-end;">
                                    <a href="exams.html" style="display: inline-flex; align-items: center; gap: 0.35rem; font-size: 0.8rem; font-weight: 700; color: #ffffff; background: #9333ea; padding: 0.35rem 0.85rem; border-radius: 0.5rem; text-decoration: none;">
                                        <span>מאגר הבחינות וארכיון הדרייב</span>
                                        <span>←</span>
                                    </a>
                                </div>
                            </div>
                        </div>

                        <!-- פריט 5: סיכום ועזרים (סגור בהתחלה) -->
                        <div class="oop-accordion-item" id="oop-accordion-item-5">
                            <button class="oop-accordion-header" onclick="window.__oopToggleAcc(5)">
                                <span>📝 5. חומרי הסיכום והעזרים המשלימים</span>
                                <span id="oop-acc-arrow-5" style="font-size: 0.85rem; color: #9333ea; transition: transform 0.2s;">▼</span>
                            </button>
                            <div class="oop-accordion-content" id="oop-acc-content-5">
                                <div style="font-size: 0.86rem; color: #334155; line-height: 1.6; margin-bottom: 0.75rem;">
                                    כלי עיון וחזרה מרוכזת לשלבי הסיום של הלמידה:
                                    <ul style="margin: 6px 0; padding-right: 18px; line-height: 1.6; font-size: 12.5px;">
                                        <li><strong>📝 סיכום הקורס המקיף:</strong> זמין בדף <a href="summary.html" style="color: #9333ea; font-weight: bold; text-decoration: underline;">סיכום הקורס המקיף (מחברת דיגיטלית עם מרקרים)</a> — מחברת סיכום דיגיטלית עם הדגשות צבעוניות וטבלאות השוואה, המיועדת למעבר מרוכז ב-48–72 השעות שלפני הבחינה.</li>
                                        
                                    </ul>
                                </div>
                                <div style="display: flex; justify-content: flex-end;">
                                    <a href="summary.html" style="display: inline-flex; align-items: center; gap: 0.35rem; font-size: 0.8rem; font-weight: 700; color: #ffffff; background: #9333ea; padding: 0.35rem 0.85rem; border-radius: 0.5rem; text-decoration: none;">
                                        <span>לסיכום הקורס</span>
                                        <span>←</span>
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Footer notice & buttons -->
                    <div style="background: #f1f5f9; border-radius: 0.75rem; padding: 0.85rem 1rem; display: flex; align-items: center; justify-content: space-between; gap: 0.75rem; flex-wrap: wrap;">
                        <span style="font-size: 0.8rem; color: #475569; font-weight: 600;">
                            💬 מכירים חברים שלומדים את הקורס? נשמח שתשתפו אותם בקישור הישיר לאתר.
                        </span>
                        <div style="display: flex; gap: 0.5rem;">
                            <button onclick="window.copyCourseLinkOnly(this)"
                                style="background: #ffffff; border: 1px solid #cbd5e1; color: #334155; padding: 0.4rem 0.85rem; border-radius: 0.5rem; font-size: 0.8rem; font-weight: 700; cursor: pointer;">
                                📋 העתקת קישור לאתר
                            </button>
                            <button onclick="window.closeCourseWelcomeModal()"
                                style="background: #9333ea; border: none; color: #ffffff; padding: 0.4rem 1rem; border-radius: 0.5rem; font-size: 0.8rem; font-weight: 700; cursor: pointer;">
                                🚀 הבנתי, בואו נתחיל
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        `;

        document.body.appendChild(overlay);

        window.copyCourseLinkOnly = function(btn) {
            const url = 'https://object-oriented-programming.pages.dev/';
            if (navigator.clipboard && navigator.clipboard.writeText) {
                navigator.clipboard.writeText(url).then(() => {
                    showCopyToast('הקישור הועתק בהצלחה: ' + url);
                    if (btn) {
                        const orig = btn.innerHTML;
                        btn.innerHTML = '✓ הועתק!';
                        setTimeout(() => { btn.innerHTML = orig; }, 2000);
                    }
                }).catch(() => {
                    showCopyToast('הקישור: ' + url);
                });
            } else {
                showCopyToast('הקישור: ' + url);
            }
        };

        overlay.addEventListener('click', (e) => {
            if (e.target === overlay) window.closeCourseWelcomeModal();
        });

        const handleEsc = (e) => {
            if (e.key === 'Escape') {
                window.closeCourseWelcomeModal();
                document.removeEventListener('keydown', handleEsc);
            }
        };
        document.addEventListener('keydown', handleEsc);
    }

    // Modal 2: 5-Day Share & Course Directory
    function buildShareModal() {
        if (document.getElementById('oop-share-modal')) return;

        const overlay = document.createElement('div');
        overlay.id = 'oop-share-modal';
        overlay.className = 'oop-modal-overlay no-invert';

        overlay.innerHTML = `
            <div class="oop-modal-card" style="max-width: 38rem;">
                <div class="oop-modal-header" style="background: linear-gradient(135deg, rgba(253, 242, 248, 0.95), rgba(250, 232, 255, 0.95));">
                    <div style="display: flex; align-items: center; gap: 0.75rem;">
                        <span style="font-size: 1.6rem;">💙</span>
                        <div>
                            <h3 style="margin: 0; font-size: 1.15rem; font-weight: 800; color: #581c87;">
                                נהנים מהאתר? שתפו עם חברים לקורס!
                            </h3>
                            <p style="margin: 0; font-size: 0.8rem; color: #9333ea; font-weight: 500;">
                                שיתוף קורס תכנות מונחה עצמים ומאגר הקורסים החינמי
                            </p>
                        </div>
                    </div>
                    <button onclick="window.closeCourseShareModal()" aria-label="סגירה"
                        style="background: #ffffff; border: 1px solid #f0abfc; border-radius: 9999px; width: 2.2rem; height: 2.2rem; display: flex; align-items: center; justify-content: center; cursor: pointer; color: #581c87; font-size: 1.1rem; font-weight: bold; transition: all 0.2s ease;">
                        ✕
                    </button>
                </div>

                <div class="oop-modal-body">
                    <div style="background: #fdf4ff; border: 1px solid #f0abfc; border-radius: 1rem; padding: 1.15rem; margin-bottom: 1.25rem;">
                        <p style="margin: 0; font-size: 0.925rem; line-height: 1.6; color: #581c87; font-weight: 600;">
                            אם האתר מסייע לכם בלמידה לקראת המבחן — נשמח שתשתפו את הקישור הישיר עם חברים לקורס ובקבוצות הלימוד.
                        </p>
                    </div>

                    <div style="background: #ffffff; border: 1px solid #f5d0fe; border-radius: 1rem; padding: 1rem; margin-bottom: 1.25rem;">
                        <label style="display: block; font-size: 0.8rem; font-weight: 700; color: #701a75; margin-bottom: 0.5rem;">
                            📋 קישור ישיר לאתר (נטו קישור):
                        </label>
                        <div style="display: flex; gap: 0.5rem; align-items: center;">
                            <input id="oop-share-link-input" type="text" readonly
                                value="https://object-oriented-programming.pages.dev/"
                                style="flex: 1; padding: 0.6rem 0.85rem; border: 1px solid #e879f9; border-radius: 0.65rem; font-size: 0.825rem; background: #fdf4ff; color: #3b0764; direction: ltr; text-align: left; font-family: monospace; font-weight: 600; outline: none;">
                            <button onclick="window.__oopCopyShareLink()"
                                style="padding: 0.6rem 1.1rem; background: #9333ea; hover:background: #7e22ce; color: #ffffff; border: none; border-radius: 0.65rem; font-weight: 700; font-size: 0.85rem; cursor: pointer; white-space: nowrap; display: flex; align-items: center; gap: 0.35rem; transition: background 0.15s ease;">
                                <span>📋</span>
                                <span>העתק קישור</span>
                            </button>
                        </div>
                    </div>

                    <div style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); border: 1px solid #bbf7d0; border-radius: 1rem; padding: 1rem 1.15rem; display: flex; align-items: center; justify-content: space-between; gap: 1rem; flex-wrap: wrap;">
                        <div>
                            <h4 style="margin: 0; font-size: 0.925rem; font-weight: 800; color: #166534;">
                                🌐 מחפשים קורסים נוספים במדעי המחשב ומתמטיקה?
                            </h4>
                            <p style="margin: 0.25rem 0 0 0; font-size: 0.8rem; color: #15803d;">
                                אינפי 1 ו-2, לינארית 1 ו-2, מערכות הפעלה, שפות תכנות, מודלים חישוביים, בינה מלאכותית, רשתות תקשורת, סייבר ועוד!
                            </p>
                        </div>
                        <a href="${PORTAL_URL}" target="_blank" rel="noopener noreferrer"
                            style="padding: 0.6rem 1.25rem; background: #16a34a; color: #ffffff; text-decoration: none; border-radius: 0.65rem; font-weight: 700; font-size: 0.85rem; display: inline-flex; align-items: center; gap: 0.4rem; box-shadow: 0 4px 10px rgba(22, 163, 74, 0.25); white-space: nowrap;">
                            <span>למאגר הקורסים הראשי</span>
                            <span>←</span>
                        </a>
                    </div>
                </div>

                <div class="oop-modal-footer">
                    <button onclick="window.closeCourseShareModal()"
                        style="padding: 0.65rem 1.25rem; background: #fdf4ff; color: #581c87; border: 1px solid #f0abfc; border-radius: 0.75rem; font-weight: 600; font-size: 0.875rem; cursor: pointer; transition: background 0.15s ease;">
                        סגירה
                    </button>
                </div>
            </div>
        `;

        document.body.appendChild(overlay);

        overlay.addEventListener('click', (e) => {
            if (e.target === overlay) window.closeCourseShareModal();
        });
    }

    // Toast helper
    function showCopyToast(msg) {
        let toast = document.getElementById('oop-copy-toast');
        if (!toast) {
            toast = document.createElement('div');
            toast.id = 'oop-copy-toast';
            toast.className = 'oop-copy-toast';
            document.body.appendChild(toast);
        }
        toast.innerHTML = `<span>✅</span><span>${msg}</span>`;
        toast.classList.add('show');
        setTimeout(() => toast.classList.remove('show'), 3200);
    }

    // Global action handlers
    window.__oopToggleAcc = function (num) {
        const content = document.getElementById(`oop-acc-content-${num}`);
        const arrow = document.getElementById(`oop-acc-arrow-${num}`);
        if (!content) return;
        const isOpen = content.classList.contains('open');
        if (isOpen) {
            content.classList.remove('open');
            if (arrow) arrow.style.transform = 'rotate(0deg)';
        } else {
            content.classList.add('open');
            if (arrow) arrow.style.transform = 'rotate(180deg)';
        }
    };

    window.__oopCopyShareLink = function () {
        const input = document.getElementById('oop-share-link-input');
        if (input) {
            input.select();
            input.setSelectionRange(0, 99999);
            try {
                navigator.clipboard.writeText(input.value).then(() => {
                    showCopyToast('הקישור הועתק בהצלחה: ' + input.value);
                }).catch(() => {
                    document.execCommand('copy');
                    showCopyToast('הקישור הועתק בהצלחה: ' + input.value);
                });
            } catch (err) {
                document.execCommand('copy');
                showCopyToast('הקישור הועתק בהצלחה: ' + input.value);
            }
        }
    };

    window.showCourseWelcomeModal = function () {
        injectStyles();
        buildWelcomeModal();
        const modal = document.getElementById('oop-welcome-modal');
        if (modal) modal.classList.add('active');
    };

    window.closeCourseWelcomeModal = function () {
        const modal = document.getElementById('oop-welcome-modal');
        if (modal) modal.classList.remove('active');
        localStorage.setItem(KEY_DAY1_SHOWN, 'true');
    };

    window.showCourseShareModal = function () {
        injectStyles();
        buildShareModal();
        const modal = document.getElementById('oop-share-modal');
        if (modal) modal.classList.add('active');
    };

    window.closeCourseShareModal = function () {
        const modal = document.getElementById('oop-share-modal');
        if (modal) modal.classList.remove('active');
        localStorage.setItem(KEY_LAST_SHARE_POPUP, Date.now().toString());
    };

    // Logic Evaluation on Load
    function checkModalTriggers() {
        injectStyles();
        buildWelcomeModal();
        buildShareModal();

        const now = Date.now();
        let firstVisit = localStorage.getItem(KEY_FIRST_VISIT);
        if (!firstVisit) {
            localStorage.setItem(KEY_FIRST_VISIT, now.toString());
            firstVisit = now.toString();
        }
        const firstVisitTs = parseInt(firstVisit, 10) || now;
        const timeSinceFirstVisit = now - firstVisitTs;

        const day1Shown = localStorage.getItem(KEY_DAY1_SHOWN) === 'true';
        const lastShareTs = parseInt(localStorage.getItem(KEY_LAST_SHARE_POPUP) || '0', 10);

        // First Visit Check: If welcome hasn't been shown yet
        if (!day1Shown) {
            setTimeout(() => {
                window.showCourseWelcomeModal();
            }, 800);
            return;
        }

        // 5-Day Share Popup Check:
        // Must be at least 24 hours since initial visit AND at least 5 days since last share popup
        if (timeSinceFirstVisit >= ONE_DAY_MS) {
            const timeSinceLastShare = now - lastShareTs;
            if (timeSinceLastShare >= FIVE_DAYS_MS) {
                setTimeout(() => {
                    window.showCourseShareModal();
                }, 1200);
            }
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', checkModalTriggers);
    } else {
        checkModalTriggers();
    }
})();
