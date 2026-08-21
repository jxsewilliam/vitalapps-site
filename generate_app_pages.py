#!/usr/bin/env python3
"""Generate the seven app pages from one shared template (assets/app.css + assets/app.js)."""
import html as H

# ---------- minimal inline SVG icon set ----------
I = {
 'scan':   '<svg viewBox="0 0 24 24" fill="none"><path d="M4 8V6a2 2 0 012-2h2M16 4h2a2 2 0 012 2v2M20 16v2a2 2 0 01-2 2h-2M8 20H6a2 2 0 01-2-2v-2M7 12h10" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
 'bell':   '<svg viewBox="0 0 24 24" fill="none"><path d="M6 9a6 6 0 1112 0c0 5 2 6 2 6H4s2-1 2-6M10 20a2 2 0 004 0" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
 'check':  '<svg viewBox="0 0 24 24" fill="none"><path d="M5 12l5 5L20 7" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
 'spark':  '<svg viewBox="0 0 24 24" fill="none"><path d="M12 3l1.9 5.6L19.5 10l-5.6 1.9L12 17.5l-1.9-5.6L4.5 10l5.6-1.4L12 3z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>',
 'lock':   '<svg viewBox="0 0 24 24" fill="none"><rect x="5" y="11" width="14" height="9" rx="2" stroke="currentColor" stroke-width="2"/><path d="M8 11V8a4 4 0 118 0v3" stroke="currentColor" stroke-width="2"/></svg>',
 'smile':  '<svg viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="2"/><path d="M8 14s1.5 2 4 2 4-2 4-2M9 9h.01M15 9h.01" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
 'camera': '<svg viewBox="0 0 24 24" fill="none"><path d="M4 8h3l2-3h6l2 3h3v11H4V8z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><circle cx="12" cy="13" r="3.2" stroke="currentColor" stroke-width="2"/></svg>',
 'eye':    '<svg viewBox="0 0 24 24" fill="none"><path d="M2 12s3.5-6 10-6 10 6 10 6-3.5 6-10 6-10-6-10-6z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><circle cx="12" cy="12" r="2.6" stroke="currentColor" stroke-width="2"/></svg>',
 'photo':  '<svg viewBox="0 0 24 24" fill="none"><rect x="4" y="5" width="16" height="14" rx="2" stroke="currentColor" stroke-width="2"/><circle cx="9" cy="10" r="1.6" fill="currentColor"/><path d="M5 17l5-4 3 2 4-3 2 2" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>',
 'slider': '<svg viewBox="0 0 24 24" fill="none"><path d="M4 7h10M18 7h2M4 17h2M10 17h10" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><circle cx="16" cy="7" r="2.4" stroke="currentColor" stroke-width="2"/><circle cx="8" cy="17" r="2.4" stroke="currentColor" stroke-width="2"/></svg>',
 'hd':     '<svg viewBox="0 0 24 24" fill="none"><rect x="3" y="6" width="18" height="12" rx="2" stroke="currentColor" stroke-width="2"/><path d="M7 10v4M10 10v4M7 12h3M13.5 10v4h1.8a2 2 0 000-4h-1.8z" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>',
 'infinity':'<svg viewBox="0 0 24 24" fill="none"><path d="M8.5 15.5c-2 0-3.5-1.6-3.5-3.5s1.5-3.5 3.5-3.5c3.5 0 3.5 7 7 7 2 0 3.5-1.6 3.5-3.5S17.5 8.5 15.5 8.5c-1.7 0-2.7 1.6-3.5 3.5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
 'face':   '<svg viewBox="0 0 24 24" fill="none"><path d="M5 8V6a1 1 0 011-1h2M16 5h2a1 1 0 011 1v2M19 16v2a1 1 0 01-1 1h-2M8 19H6a1 1 0 01-1-1v-2" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><circle cx="12" cy="12" r="3.4" stroke="currentColor" stroke-width="2"/></svg>',
 'gauge':  '<svg viewBox="0 0 24 24" fill="none"><path d="M5 19a9 9 0 1114 0" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><path d="M12 13l3.5-3.5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
 'up':     '<svg viewBox="0 0 24 24" fill="none"><path d="M4 17l5-5 3 3 7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M14 8h5v5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
 'flame':  '<svg viewBox="0 0 24 24" fill="none"><path d="M12 3s5 4.5 5 9.5a5 5 0 01-10 0C7 10 9 8 9 8s-.5 2.5 1.5 2.5C12 10.5 12 3 12 3z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>',
 'brain':  '<svg viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="2"/><path d="M12 3v18M12 8c2 0 3-1 3-2.5M12 12c3 0 4.5-1 5.5-2M12 16c2.5 0 4 .5 5 1.5M12 8C10 8 9 7 9 5.5M12 12c-3 0-4.5-1-5.5-2M12 16c-2.5 0-4 .5-5 1.5" stroke="currentColor" stroke-width="1.6"/></svg>',
 'swipe':  '<svg viewBox="0 0 24 24" fill="none"><path d="M4 12h16M4 12l4-4M4 12l4 4M20 12l-4-4M20 12l-4 4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
 'disk':   '<svg viewBox="0 0 24 24" fill="none"><path d="M12 3a9 9 0 109 9" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><path d="M12 7a5 5 0 105 5h-5V7z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>',
 'grid':   '<svg viewBox="0 0 24 24" fill="none"><rect x="4" y="4" width="7" height="7" rx="1.5" stroke="currentColor" stroke-width="2"/><rect x="13" y="4" width="7" height="7" rx="1.5" stroke="currentColor" stroke-width="2"/><rect x="4" y="13" width="7" height="7" rx="1.5" stroke="currentColor" stroke-width="2"/><rect x="13" y="13" width="7" height="7" rx="1.5" stroke="currentColor" stroke-width="2"/></svg>',
 'leaf':   '<svg viewBox="0 0 24 24" fill="none"><path d="M5 19C5 9 12 5 20 5c0 8-4 15-14 15" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><path d="M5 19c3-5 7-8 10-9" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
 'hand':   '<svg viewBox="0 0 24 24" fill="none"><path d="M9 11V5a1.5 1.5 0 013 0v5m0-3a1.5 1.5 0 013 0v4m0-2a1.5 1.5 0 013 0v5a7 7 0 01-7 7c-3 0-4.5-1.5-6-4l-2-4a1.5 1.5 0 012.5-1.5L7 13V6a1.5 1.5 0 012-1.4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>',
 'bulb':   '<svg viewBox="0 0 24 24" fill="none"><path d="M9 18h6M10 21h4M12 3a6 6 0 014 10.5c-.8.7-1 1.5-1 2.5h-6c0-1-.2-1.8-1-2.5A6 6 0 0112 3z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
 'heart':  '<svg viewBox="0 0 24 24" fill="none"><path d="M12 20s-7-4.5-9-9a5 5 0 019-3 5 5 0 019 3c-2 4.5-9 9-9 9z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>',
 'trophy': '<svg viewBox="0 0 24 24" fill="none"><path d="M8 4h8v5a4 4 0 01-8 0V4zM8 5H4c0 3 1.5 5 4 5M16 5h4c0 3-1.5 5-4 5M12 13v4m-4 4h8m-6 0v-4h4v4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
 'stack':  '<svg viewBox="0 0 24 24" fill="none"><rect x="6" y="15" width="12" height="4" rx="1" stroke="currentColor" stroke-width="2"/><rect x="7" y="10" width="10" height="4" rx="1" stroke="currentColor" stroke-width="2"/><rect x="8" y="5" width="8" height="4" rx="1" stroke="currentColor" stroke-width="2"/></svg>',
 'target': '<svg viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="5" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="1.4" fill="currentColor"/></svg>',
 'nosub':  '<svg viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="2"/><path d="M6 6l12 12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
}

APPLE = '<svg viewBox="0 0 24 24" fill="currentColor" style="width:17px;height:17px"><path d="M17.05 12.54c-.03-2.6 2.13-3.85 2.22-3.91-1.21-1.77-3.09-2.01-3.76-2.04-1.6-.16-3.12.94-3.93.94-.8 0-2.06-.92-3.39-.89-1.74.03-3.35 1.01-4.25 2.57-1.81 3.14-.46 7.79 1.3 10.34.86 1.25 1.89 2.65 3.24 2.6 1.3-.05 1.79-.84 3.36-.84 1.57 0 2.01.84 3.39.81 1.4-.02 2.28-1.27 3.13-2.53.99-1.45 1.39-2.85 1.41-2.92-.03-.01-2.71-1.04-2.74-4.13zM14.46 4.9c.71-.86 1.19-2.06 1.06-3.25-1.02.04-2.26.68-2.99 1.54-.66.76-1.23 1.98-1.08 3.15 1.14.09 2.3-.58 3.01-1.44z"/></svg>'

def feat(icon, title, body):
    return {'icon': icon, 'title': title, 'body': body}

APPS = {
 'useby': dict(
   name='UseBy', title='UseBy · Food Expiry Tracker',
   desc="UseBy tracks what's in your kitchen. Scan the barcode, snap the expiry date, and get reminded before food goes off.",
   accent='#2FB47A', accent_ink='#04170D', glow='47,180,122', icon='/assets/useby-icon.webp', icon_bg='#61686F',
   pill='Live on the App Store · iOS',
   h1='Never waste<br/>food <em>again.</em>',
   tagline="UseBy tracks what's in your kitchen so nothing gets forgotten. Point your camera and it handles the rest — no typing required.",
   store='https://apps.apple.com/gb/app/useby-food-expiry-tracker/id6756246350',
   meta=[('Platform','iOS · iPadOS'),('Released','2025'),('Price','£9.99 · pay once')],
   mission="No spreadsheets, no typing, no overcomplicated meal plans — just scan the barcode, snap the expiry date, and UseBy remembers everything for you.",
   mission_accent='scan|snap|remembers',
   feat_eyebrow='Why UseBy', feat_h2='Built around the way you <em>actually</em> use your fridge.',
   feat_lead="A calm app that helps you remember what you have and use it before it goes off.",
   features=[
     feat('scan','Scan, don’t type',"Point your camera at the barcode and it's saved. No friction, no fluff."),
     feat('bell','Smart reminders',"Get notified before things expire — not when it's too late."),
     feat('check','Eat what you have',"See what's in your fridge at a glance and stop buying duplicates."),
     feat('spark','Beautifully simple',"Native iOS, designed to feel like it belongs on your home screen."),
     feat('lock','Stays on your phone',"Your fridge data is stored locally. Nothing about your food leaves your device."),
     feat('smile','No ads. Ever.',"No tracking, no upsells, no nagging. Just a tool that works."),
   ],
   steps_h2="Three taps and you're done.",
   steps=[('Scan the barcode.',"Point your camera at any product and it's saved to your inventory. About three seconds."),
          ('Snap the expiry date.',"Photograph the date on the label and UseBy reads it. It nudges you before food turns — not after it's in the bin."),
          ('Eat it. Don’t bin it.',"Open the app, see what needs eating first, and actually eat it. That's the whole loop.")],
   marquee=['Scan barcodes','Snap expiry dates','Smart reminders','Zero typing','Private by design','No ads ever','Pay once, keep forever'],
   cta_h2='Stop throwing food <em>away.</em>',
   cta_p="UseBy is £9.99, once — no subscriptions, no ads. Built for people who just want their fridge to stop being a graveyard.",
   foot=[('/privacy/useby/','Privacy'),('/support/useby/','Support'),('/studio/','Studio'),('mailto:vitalappsltd@gmail.com','Contact')],
 ),
 'dualshot': dict(
   name='DualShot', title='DualShot · One Tap, Two Videos',
   desc="DualShot records vertical (9:16) and horizontal (16:9) video at the same time, from a single take. Built for creators who post everywhere.",
   accent='#FFCB45', accent_ink='#1E1500', glow='255,203,69', icon='/assets/dualshot-icon.webp', icon_bg='#1C1C1E',
   pill='Live on the App Store · iOS',
   h1='One tap.<br/><em>Two videos.</em>',
   tagline="DualShot records vertical (9:16) and horizontal (16:9) at the exact same time, from a single take. No reshoots, no compromises.",
   store='https://apps.apple.com/gb/app/dualshot-camera-recorder/id6762485242',
   meta=[('Platform','iOS'),('Released','2026'),('Price','£9.99 lifetime')],
   mission="Every creator knows the pain: shoot for TikTok, then re-record for YouTube. DualShot ends it — one take gives you two perfectly framed files.",
   mission_accent='one|two|dualshot',
   feat_eyebrow='Why DualShot', feat_h2='Every format, <em>in one take.</em>',
   feat_lead="Two perfectly framed files, saved straight to your Photo Library.",
   features=[
     feat('camera','Dual recording',"Portrait and landscape captured simultaneously — two separate, synced files."),
     feat('eye','Live dual preview',"See both framings as you shoot — landscape sits picture-in-picture beside your portrait view."),
     feat('photo','Dual photo mode',"Not just video. One shutter tap saves both a 9:16 and a 16:9 photo."),
     feat('slider','Pro controls',"AE/AF lock, tap-to-focus, pinch-to-zoom, 1–3× lenses, exposure slider, grid and timers."),
     feat('hd','4K, your way',"4K or 1080p at 24, 30 or 60 fps. Export as MOV or MP4, saved locally to Photos."),
     feat('infinity','Pay once, keep forever',"£9.99 lifetime. No subscriptions, no nagging. Yours to keep."),
   ],
   steps_h2='Open. Frame. Record.',
   steps=[('Open DualShot.',"Both framings come up instantly — your 9:16 and 16:9 previews, side by side."),
          ('Frame the shot.',"Lock focus, set your zoom, check both previews. Your music keeps playing until you hit record."),
          ('Hit record.',"One take, two perfectly framed files in your Photo Library. Post everywhere.")],
   marquee=['9:16 + 16:9 at once','Two synced files','4K at 60 fps','Dual photo mode','AE/AF lock','MOV or MP4','No subscriptions'],
   cta_h2='Shoot once. Post <em>everywhere.</em>',
   cta_p="One purchase. Lifetime access. No subscriptions, no ads, no nonsense.",
   foot=[('/privacy/dualshot/','Privacy'),('/support/dualshot/','Support'),('/studio/','Studio'),('mailto:vitalappsltd@gmail.com','Contact')],
 ),
 'maxxr': dict(
   name='Maxxr', title='Maxxr · AI Face Analysis & Glow-Up Plan',
   desc="Maxxr gives you an honest AI face analysis from one selfie, then builds a personalised daily glow-up routine around your weakest traits.",
   accent='#C77DFF', accent_ink='#170526', glow='199,125,255', icon='/assets/maxxr-icon.webp', icon_bg='#F4F3F5',
   pill='Live on the App Store · iOS',
   h1='Looksmaxxing,<br/><em>without the noise.</em>',
   tagline="One selfie gets you an honest AI face analysis in under a minute — jawline, symmetry, skin and more. Then Maxxr builds a daily glow-up routine around your weakest traits.",
   store='https://apps.apple.com/gb/app/maxxr-looksmax-glow-up/id6765758864',
   meta=[('Platform','iOS'),('Released','2026'),('Price','Free')],
   mission="Most looksmaxxing advice is loud, vague, or trying to sell you something. Maxxr keeps it private, personal, and actually useful.",
   mission_accent='private|personal|useful',
   feat_eyebrow='Why Maxxr', feat_h2='An honest mirror, <em>in your pocket.</em>',
   feat_lead="A clear read on your features — and the steps that actually move the needle.",
   features=[
     feat('face','Smart facial analysis',"Maps key facial proportions and symmetry from a single photo."),
     feat('gauge','Personal score',"Get a clear, single-number rating you can track over time."),
     feat('check','What’s working',"See your strongest features so you can lean into them."),
     feat('up','Where to improve',"Practical, no-nonsense advice on grooming, posture, and routine."),
     feat('lock','Stays private',"Your photos stay on your phone. We don't store, share, or sell them."),
     feat('spark','Track progress',"Watch your score climb as your routine, sleep, and habits sharpen up."),
   ],
   steps_h2='Three steps. One score.',
   steps=[('Take a quick photo.',"A normal selfie, well lit, looking straight on. No special angles required."),
          ('Get your read.',"Maxxr maps your features in seconds and gives you a personal score plus a breakdown."),
          ('Level up.',"Follow practical tips, retake later, watch your score climb.")],
   marquee=['AI face analysis','Personal score','Jawline & symmetry','Skin breakdown','Daily routine','Photos stay private','Free to try'],
   cta_h2='Become your <em>best version.</em>',
   cta_p="No filters, no fake confidence, no fluff. Just an honest read on you, and the steps that actually move the needle.",
   foot=[('/privacy/maxxr/','Privacy'),('/support/maxxr/','Support'),('/studio/','Studio'),('mailto:vitalappsltd@gmail.com','Contact')],
 ),
 'relapsr': dict(
   name='Relapsr', title='Relapsr · Break the Habit',
   desc="Relapsr — break the habit, track every clean day, and take back control. By VitalApps Ltd.",
   accent='#04B497', accent_ink='#02120E', glow='4,180,151', icon='/relapsr-logo.svg', icon_bg='#151515',
   pill='Live on the App Store · iOS',
   hero_art='/assets/relapsr-phones.webp',
   h1='Break the habit.<br/><em>Take back control.</em>',
   tagline="Track every clean day, understand your triggers, and rebuild better habits — one day at a time.",
   store='https://apps.apple.com/gb/app/relapsr-quit-adult-content/id6779668191',
   meta=[('Platform','iOS'),('Released','2026'),('Price','Free')],
   mission="Relapsr helps you quit the habit you want to leave behind — and your recovery data stays private, on your device.",
   mission_accent='quit|private',
   feat_eyebrow='Why Relapsr', feat_h2='Built for the days it gets <em>hard.</em>',
   feat_lead="A clear streak, honest check-ins, and total privacy.",
   features=[
     feat('flame','Track your streak',"Watch every clean day add up. A clear, motivating count of how far you've come."),
     feat('brain','Know your triggers',"Quick check-ins and quizzes help you understand the patterns behind the urge."),
     feat('lock','Private by design',"Your streaks, journal, and answers stay on your device. We don't sell your data."),
   ],
   steps_h2=None, steps=None,
   marquee=['Streak tracking','Daily check-ins','Know your triggers','Private by design','No data sold','One day at a time'],
   cta_h2='Every clean day <em>counts.</em>',
   cta_p="Free on iOS. Your streaks, journal, and answers stay on your device.",
   note="Relapsr is a self-help and tracking tool, not a substitute for medical or professional treatment. If you're in crisis, please reach out to a healthcare provider or your local emergency services.",
   foot=[('/privacy/relapsr/','Privacy'),('/terms/relapsr/','Terms'),('/support/relapsr/','Support'),('mailto:vitalappsltd@gmail.com','Contact')],
 ),
 'swipeclean': dict(
   name='SwipeClean', title='SwipeClean · Photo Cleaner',
   desc="Swipe left to delete, right to keep. Clean your camera roll in minutes.",
   accent='#FD297B', accent_ink='#20030E', glow='253,41,123', icon='/assets/swipeclean-icon.webp', icon_bg='#FD297B',
   pill='Live on the App Store · iOS',
   h1='Swipe left to delete.<br/><em>Right to keep.</em>',
   tagline="Clean your camera roll in minutes — one photo, one decision at a time.",
   store='https://apps.apple.com/gb/app/swipeclean-photo-cleaner/id6793184550',
   meta=[('Platform','iOS'),('Released','2026'),('Price','Free · Pro')],
   mission="SwipeClean turns cleaning your photo library into something you'll actually finish — and you watch the gigabytes add up as you go.",
   mission_accent='finish|gigabytes',
   feat_eyebrow='Why SwipeClean', feat_h2='Cleaning that actually gets <em>finished.</em>',
   feat_lead="No endless scrolling, no risky deletes, no uploads.",
   features=[
     feat('swipe','Swipe to clean',"One photo at a time, one decision at a time. Left to bin it, right to keep it — no endless scrolling."),
     feat('disk','See the space you free',"Watch the gigabytes add up as you go. Clean by month, album, screenshots, or your whole library."),
     feat('lock','Nothing leaves your phone',"SwipeClean never uploads your photos. Deletions go to Recently Deleted for 30 days, so nothing is lost instantly."),
   ],
   steps_h2=None, steps=None,
   marquee=['Swipe left to delete','Swipe right to keep','Clean by month','Clean by album','Free up gigabytes','Nothing uploaded','30-day safety net'],
   cta_h2='Your camera roll, <em>finally sorted.</em>',
   cta_p="SwipeClean is free to try. SwipeClean Pro unlocks unlimited swiping.",
   note="Deleted items are moved to your Photos app's Recently Deleted album and stay recoverable for 30 days.",
   foot=[('/privacy/swipeclean/','Privacy'),('/support/swipeclean/','Support'),('/studio/','Studio'),('mailto:vitalappsltd@gmail.com','Contact')],
 ),
 'arrowflow': dict(
   name='Arrow Flow', title='Arrow Flow · Escape Puzzle',
   desc="An arrow puzzle game wrapped in colour. Read the flow, find the one path that fits, and untangle every level.",
   accent='#6FA8FF', accent_ink='#04101F', glow='111,168,255', icon='/assets/arrowflow-icon.webp', icon_bg='#0F1117',
   pill='Coming soon · iOS & Android', coming=True,
   h1='Follow the arrows.<br/><em>Escape the maze.</em>',
   tagline="An arrow puzzle game wrapped in colour. Read the flow, find the one path that fits, and untangle every level — one move at a time.",
   store=None,
   meta=[('Platform','iPhone · iPad · Android'),('Price','Free'),('Status','Coming soon')],
   mission="Each level is a tangle of coloured arrows — read the flow, draw the path, untangle the maze. No timer. No noise. No pressure.",
   mission_accent='flow|untangle|pressure',
   feat_eyebrow='What it is', feat_h2='An arrow puzzle that actually <em>feels good</em> to play.',
   feat_lead="Some arrows short, some long, some looping back on themselves. Your job is simple.",
   features=[
     feat('grid','Hundreds of levels',"From easy 4×4 grids to mind-bending tangles. Each one is hand-designed with a single solution and a satisfying “ah” moment."),
     feat('leaf','Calm by design',"No timers, no lives, no pop-ups mid-level. Spend five seconds or five minutes on a puzzle — Arrow Flow doesn't care."),
     feat('check','Easy to learn',"Follow the arrows. Cover every cell. Reach the exit. You'll get it on level 1. Level 100 will still surprise you."),
     feat('hand','One-handed play',"Tap and drag. Designed for the train, the sofa, or the five quiet minutes before your meeting starts."),
     feat('bulb','Hints when you’re stuck',"Tap the bulb for a nudge. Hints are free and unlimited — Arrow Flow is a puzzle, not a paywall."),
     feat('smile','No accounts, no ads',"No sign-up. No email. No banners. Open the app, solve a puzzle, close the app, get on with your day."),
   ],
   steps_h2="Three rules. That's it.",
   steps=[('Follow the arrows.',"Each arrow points where the path must go next. Misread one and the path breaks."),
          ('Cover every cell.',"The path has to pass through every square on the board. No shortcuts, no leftovers."),
          ('Find the exit.',"One way in, one way out. Trace the only path that satisfies both, and the puzzle opens.")],
   marquee=['Hundreds of levels','Hand-designed puzzles','No timers','Free hints','One-handed play','No accounts','No ads'],
   cta_h2='Quiet puzzles. <em>Loud satisfaction.</em>',
   cta_p="Arrow Flow launches soon on the App Store and Google Play. Free to download, no subscriptions, no nonsense.",
   foot=[('/privacy/arrowflow/','Privacy'),('/support/arrowflow/','Support'),('/studio/','Studio'),('mailto:vitalappsltd@gmail.com','Contact')],
 ),
 'rise': dict(
   name='RISE', title='RISE · One-Tap Stacking Game',
   desc="RISE is a one-tap stacking game. Time each block, keep the tower wide, and chase your best score.",
   accent='#F06C84', accent_ink='#1F050B', glow='240,108,132', icon='/assets/rise-icon.webp', icon_bg='#F06C84',
   pill='Coming soon · iOS & Android', coming=True,
   h1='One tap.<br/><em>Stack it high.</em>',
   tagline="Blocks slide across the screen. Tap to drop one. Land it square and the tower climbs — miss and it shaves down until there's nothing left to land on.",
   store=None,
   meta=[('Platform','iPhone · Android'),('Price','Free'),('Status','Coming soon')],
   mission="RISE is simple to start and brutal to master — you'll understand it in three seconds and still be chasing your best score a month later.",
   mission_accent='simple|brutal|best',
   feat_eyebrow='What it is', feat_h2='A tower that only goes up if your <em>timing</em> does.',
   feat_lead="One control, one decision: when to tap.",
   features=[
     feat('hand','One tap, nothing else',"No buttons, no joystick, no menus mid-run. Tap to drop, tap to restart. The whole game fits in one thumb."),
     feat('target','Perfect stacks pay off',"Land a block dead centre and nothing gets sliced away. String perfects together and the tower stays full-width — that's how the big scores happen."),
     feat('heart','Hearts to keep the run alive',"Spend a heart to carry on from where you fell instead of starting over. You begin with three, and you can always watch a short ad for one more shot."),
     feat('trophy','An honest leaderboard',"Your stats track your best score with revives and your best score without one, separately. The no-revive number is the one that actually counts."),
     feat('flame','Streaks and stats',"Games played, blocks stacked, average score, and a day streak that grows every day you come back."),
     feat('nosub','Remove ads for good',"One small purchase clears the ads permanently. No subscription, no timers, no energy meter — RISE never stops you from playing."),
   ],
   steps_h2="Three rules. That's the whole game.",
   steps=[('Tap to drop.',"A block swings back and forth above the tower. Tap and it falls exactly where it was."),
          ('Overhang gets cut.',"Anything hanging over the edge is sliced off and falls away. The next block is only as wide as what's left."),
          ('Miss and it’s over.',"Trim the tower down to nothing and the run ends. Spend a heart to continue, or start again and beat it properly.")],
   marquee=['One-tap gameplay','Perfect stack bonus','No-revive leaderboard','Day streaks','Free to play','No energy meter'],
   cta_h2='How high can <em>you</em> get?',
   cta_p="RISE launches soon on the App Store and Google Play. Free to download, no subscriptions, no nonsense.",
   foot=[('/privacy/rise/','Privacy'),('/terms/rise/','Terms'),('/support/rise/','Support'),('/studio/','Studio'),('mailto:vitalappsltd@gmail.com','Contact')],
 ),
}

BRAND_SVG = '<svg viewBox="0 0 24 24" fill="none"><path d="M4 20 L12 4 L16 12 L12 20 Z" fill="#2FB47A"/><path d="M12 20 L16 12 L20 20 Z" fill="#0F7A4B"/></svg>'
FAVICON = "data:image/svg+xml,%3Csvg viewBox='0 0 24 24' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M4 20 L12 4 L16 12 L12 20 Z' fill='%232FB47A'/%3E%3Cpath d='M12 20 L16 12 L20 20 Z' fill='%230F7A4B'/%3E%3C/svg%3E"

def store_buttons(a, ghost_href='#features'):
    if a.get('coming'):
        return ('<span class="btn btn-accent" aria-disabled="true">%s&nbsp;Coming soon</span>'
                '<a href="#features" class="link-quiet">Learn more <span class="chev">›</span></a>') % APPLE
    return ('<a href="%s" class="btn btn-accent" target="_blank" rel="noopener">%s&nbsp;Download on App Store <span class="chev">›</span></a>'
            '<a href="%s" class="link-quiet">Learn more <span class="chev">›</span></a>') % (a['store'], APPLE, ghost_href)

def hero_art(a):
    if a.get('hero_art'):
        return ('<div class="hero-phones-wrap rv in rv-d3">'
                '<img class="hero-phones" src="%s" alt="%s app screens" /></div>'
                % (a['hero_art'], H.escape(a['name'])))
    return ('<div class="hero-icon-wrap rv in rv-d3">'
            '<div class="hero-icon"><img src="%s" alt="%s app icon" width="512" height="512" /></div></div>'
            % (a['icon'], H.escape(a['name'])))

def cta_button(a):
    if a.get('coming'):
        return '<span class="btn btn-accent" aria-disabled="true">%s&nbsp;Coming soon</span>' % APPLE
    return '<a href="%s" class="btn btn-accent" target="_blank" rel="noopener">%s&nbsp;Download on App Store <span class="chev">›</span></a>' % (a['store'], APPLE)

def render(slug, a):
    feats = '\n'.join(
        '<div class="feat%s rv rv-d%d"><h3>%s</h3><p>%s</p></div>'
        % (' feat-anchor' if i == 0 else '', (i % 3) + 1,
           H.escape(f['title'], quote=False), H.escape(f['body'], quote=False))
        for i, f in enumerate(a['features']))

    steps_html = ''
    if a.get('steps'):
        rows = '\n'.join(
            '<div class="step rv rv-d%d"><p class="step-num">0%d</p><h3>%s</h3><p>%s</p></div>'
            % (i + 1, i + 1, H.escape(t, quote=False), H.escape(b, quote=False))
            for i, (t, b) in enumerate(a['steps']))
        steps_html = ('<section class="steps-band"><div class="section">'
                      '<p class="eyebrow rv">How it works</p><h2 class="rv rv-d1">%s</h2>'
                      '<div class="steps-grid">%s</div></div></section>') % (H.escape(a['steps_h2'], quote=False), rows)

    pills = ''.join('<span class="mq-pill"><span class="dot"></span>%s</span>' % H.escape(w, quote=False) for w in a['marquee'])
    marquee = '<div class="marquee" aria-hidden="true"><div class="marquee-track">%s</div></div>' % (pills + pills)

    meta = ''.join('<div>%s<strong>%s</strong></div>' % (H.escape(k), H.escape(v)) for k, v in a['meta'])
    foot = ''.join('<a href="%s">%s</a>' % (h_, t) for h_, t in a['foot'])
    note = ('<p class="note">%s</p>' % H.escape(a['note'], quote=False)) if a.get('note') else ''
    og_image = ('https://vitalapps.co.uk' + a['icon']) if a['icon'].startswith('/assets/') else ''
    og_image_tag = ('<meta property="og:image" content="%s" />' % og_image) if og_image else ''

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{a['title']}</title>
<meta name="description" content="{H.escape(a['desc'])}" />
<meta name="theme-color" content="#0B0B0D" />
<link rel="icon" href="{FAVICON}" />
<meta property="og:type" content="website" />
<meta property="og:title" content="{H.escape(a['title'])}" />
<meta property="og:description" content="{H.escape(a['desc'])}" />
<meta property="og:url" content="https://vitalapps.co.uk/{slug}/" />
{og_image_tag}
<meta name="twitter:card" content="summary" />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Instrument+Serif:ital@1&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/app.css">
<style>:root {{ --accent: {a['accent']}; --accent-ink: {a['accent_ink']}; --glow: {a['glow']}; --icon-bg: {a['icon_bg']}; }}</style>
</head>
<body>

<nav class="nav">
  <a href="/" class="brand">{BRAND_SVG} Vital Apps</a>
  <div class="nav-right">
    <a href="/" class="nav-link hide-m">Apps</a>
    <a href="/studio/" class="nav-link hide-m">Studio</a>
    <a href="/" class="nav-link">← All apps</a>
    {'<span class="nav-cta" aria-disabled="true">Coming soon</span>' if a.get('coming') else '<a href="%s" class="nav-cta" target="_blank" rel="noopener">Download</a>' % a['store']}
  </div>
</nav>

<header class="hero">
  <div class="hero-glow"></div>
  <p class="pill rv in"><span class="dot"></span>{H.escape(a['pill'], quote=False)}</p>
  <h1 class="rv in rv-d1">{a['h1']}</h1>
  <p class="hero-tagline rv in rv-d2">{H.escape(a['tagline'], quote=False)}</p>
  <div class="hero-cta rv in rv-d3">{store_buttons(a)}</div>
  {hero_art(a)}
  <div class="hero-meta rv in rv-d4">{meta}</div>
</header>

<section class="mission">
  <div class="mission-sticky">
    <p data-accent="{a['mission_accent']}">{H.escape(a['mission'], quote=False)}</p>
  </div>
</section>

<section class="section" id="features">
  <p class="eyebrow rv">{H.escape(a['feat_eyebrow'], quote=False)}</p>
  <h2 class="rv rv-d1">{a['feat_h2']}</h2>
  <p class="section-lead rv rv-d2">{H.escape(a['feat_lead'], quote=False)}</p>
  <div class="features">{feats}</div>
</section>

{steps_html}

{marquee}

<section class="cta-final">
  <div class="cta-glow"></div>
  <h2 class="rv">{a['cta_h2']}</h2>
  <p class="rv rv-d1">{H.escape(a['cta_p'], quote=False)}</p>
  <div class="hero-cta rv rv-d2">{cta_button(a)}</div>
</section>

{note}

<footer>
  <span>© 2026 VitalApps Ltd</span>
  <div class="foot-links">{foot}</div>
</footer>

<script src="/assets/app.js"></script>
</body>
</html>
'''

import os
for slug, a in APPS.items():
    os.makedirs(slug, exist_ok=True)
    out = render(slug, a)
    open(f'{slug}/index.html', 'w').write(out)
    print(f'{slug}/index.html  {len(out)//1024} KB')
