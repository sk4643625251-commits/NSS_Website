/**
 * NSS Team Page – Anti-Gravity Scroll + Mouse-Tilt Effect
 * Applies a subtle 3D floating / parallax-tilt effect to .profile-card elements.
 * The shadow softens and expands as cards "rise" during scroll.
 */

(function () {
  'use strict';

  /* ─── helpers ─────────────────────────────────────────────────── */
  const clamp = (v, lo, hi) => Math.min(Math.max(v, lo), hi);

  /* ─── scroll-lift (anti-gravity) ──────────────────────────────── */
  function applyScrollLift() {
    const cards = document.querySelectorAll('.profile-card');
    const winH  = window.innerHeight;

    cards.forEach(card => {
      const rect   = card.getBoundingClientRect();
      // 0 when card centre is at bottom of viewport, 1 when at top
      const centre = rect.top + rect.height / 2;
      const ratio  = clamp(1 - centre / winH, 0, 1);

      // translateZ lifts the card; subtle rotateX tilts it forward
      const lift   = ratio * 22;          // max 22 px lift
      const tiltX  = ratio * -5;          // max −5° forward tilt
      const blurR  = 18 + ratio * 22;    // shadow blur 18→40
      const spread = ratio * 8;           // shadow spread 0→8
      const opSha  = 0.28 + ratio * 0.22; // shadow opacity

      card.style.transform = `perspective(900px) translateZ(${lift}px) rotateX(${tiltX}deg)`;
      card.style.boxShadow =
        `0 ${8 + lift}px ${blurR}px ${spread}px rgba(0,0,0,${opSha}),` +
        `0 0 ${20 + ratio * 20}px rgba(99,102,241,${0.08 + ratio * 0.12})`;
    });
  }

  /* ─── mouse-tilt 3-D effect ───────────────────────────────────── */
  function initMouseTilt() {
    document.querySelectorAll('.profile-card').forEach(card => {
      card.addEventListener('mousemove', e => {
        const r    = card.getBoundingClientRect();
        const x    = e.clientX - r.left - r.width  / 2;
        const y    = e.clientY - r.top  - r.height / 2;
        const rotY =  clamp((x / (r.width  / 2)) * 10, -10, 10);
        const rotX = -clamp((y / (r.height / 2)) * 10, -10, 10);
        card.style.transform =
          `perspective(900px) rotateX(${rotX}deg) rotateY(${rotY}deg) translateZ(18px)`;
        card.style.boxShadow =
          `${-rotY * 2}px ${rotX * 2}px 40px 10px rgba(0,0,0,0.45),` +
          `0 0 30px rgba(168,85,247,0.2)`;
      });

      card.addEventListener('mouseleave', () => {
        card.style.transition = 'transform 0.6s cubic-bezier(0.23,1,0.32,1), box-shadow 0.6s ease';
        card.style.transform  = '';
        card.style.boxShadow  = '';
        // re-apply scroll lift after mouse leaves
        applyScrollLift();
        // Remove the transition override after it finishes so
        // scroll-lift updates are immediate again
        setTimeout(() => { card.style.transition = ''; }, 620);
      });

      card.addEventListener('mouseenter', () => {
        card.style.transition = 'transform 0.15s ease, box-shadow 0.15s ease';
      });
    });
  }

  /* ─── intersection-based entrance animation ───────────────────── */
  function initEntranceObserver() {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('card-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });

    document.querySelectorAll('.profile-card').forEach(c => observer.observe(c));
  }

  /* ─── boot ────────────────────────────────────────────────────── */
  document.addEventListener('DOMContentLoaded', () => {
    initMouseTilt();
    initEntranceObserver();
    applyScrollLift();
    window.addEventListener('scroll', applyScrollLift, { passive: true });
    window.addEventListener('resize', applyScrollLift, { passive: true });
  });
})();
