/* ============================================================
   js/blood.js  —  Blood Donation Page Scripts
   NSS NIT Kurukshetra
   ============================================================

   ⚙️  CONFIG — Update these two values:
   ──────────────────────────────────────
   WA_COORDINATOR : WhatsApp number of NSS blood coordinator
                    (country code + number, no +, no spaces)
                    Example: '919876543210'

   WA_GROUP_LINK  : WhatsApp group invite link for NSS Blood Donors
                    Get it from WhatsApp group → Invite link
                    Example: 'https://chat.whatsapp.com/AbCdEfGhIjKlM'
   ──────────────────────────────────────────────────────────── */

  const WA_COORDINATOR = '917068357521';                                          // NSS Coordinator
  const WA_GROUP_LINK  = 'https://chat.whatsapp.com/CQ4IyMHJ9uQ4o0rILwczbK';    // NSS Blood Donor Group

/* ============================================================ */

document.addEventListener('DOMContentLoaded', function () {

  /* ── 1. SMOOTH SCROLL for all internal hash links ──────── */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (!target) return;
      e.preventDefault();
      const navH = document.querySelector('.navbar')?.offsetHeight || 80;
      const top = target.getBoundingClientRect().top + window.scrollY - navH - 20;
      window.scrollTo({ top, behavior: 'smooth' });
    });
  });

  /* ── 2. COUNTER ANIMATION ───────────────────────────────── */
  function animateCounter(el, target, suffix) {
    let count = 0;
    const step = Math.ceil(target / 60);
    const timer = setInterval(() => {
      count = Math.min(count + step, target);
      el.textContent = count + suffix;
      if (count >= target) clearInterval(timer);
    }, 25);
  }

  const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const vals = document.querySelectorAll('.stat-value');
        if (vals[0]) animateCounter(vals[0], 500,  '+');
        if (vals[1]) animateCounter(vals[1],   8,  '');
        if (vals[2]) animateCounter(vals[2], 1500, '+');
        statsObserver.disconnect();
      }
    });
  }, { threshold: 0.5 });

  const statsEl = document.querySelector('.stats-glass-row');
  if (statsEl) statsObserver.observe(statsEl);

  /* ── 3. SCROLL REVEAL ───────────────────────────────────── */
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('bd-revealed');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });

  document.querySelectorAll('.bd-reveal').forEach(el => revealObserver.observe(el));

  /* ── 4. FLOATING "NEED BLOOD?" BUTTON ───────────────────── */
  const floatBtn = document.getElementById('bloodFloatBtn');
  if (floatBtn) {
    window.addEventListener('scroll', () => {
      const heroH = document.querySelector('.blood-hero')?.offsetHeight || 500;
      floatBtn.classList.toggle('visible', window.scrollY > heroH * 0.6);
    }, { passive: true });

    floatBtn.addEventListener('click', () => {
      const formsSection = document.getElementById('forms-section');
      if (formsSection) {
        const navH = document.querySelector('.navbar')?.offsetHeight || 80;
        window.scrollTo({
          top: formsSection.getBoundingClientRect().top + window.scrollY - navH - 20,
          behavior: 'smooth'
        });
      }
    });
  }

  /* ── 5. DONATE FORM ─────────────────────────────────────────
     Submit → send donor info to coordinator only.
     Joining the group is separate (Join Group button).
  ────────────────────────────────────────────────────────────── */
  const donateForm = document.getElementById('bloodDonateForm');
  if (donateForm) {
    donateForm.addEventListener('submit', function (e) {
      e.preventDefault();

      const name  = document.getElementById('donName').value.trim();
      const phone = document.getElementById('donPhone').value.trim();
      const blood = document.getElementById('donBlood').value;
      const loc   = document.getElementById('donLocation').value.trim();

      if (!name || !phone || !blood || blood === 'Select Group' || !loc) {
        showFormError('⚠️ Please fill in all required fields.');
        return;
      }

      /* Animate button */
      const submitBtn = donateForm.querySelector('button[type="submit"]');
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<span><i class="fab fa-whatsapp me-2"></i>Sending…</span>';
      }

      /* Send donor details to coordinator */
      const donorMsg = encodeURIComponent(
        `✅ *New Blood Donor Registration* ✅\n\n` +
        `👤 *Name:* ${name}\n` +
        `📞 *Phone:* ${phone}\n` +
        `🩸 *Blood Group:* ${blood}\n` +
        `📍 *Location:* ${loc}\n\n` +
        `— NSS NIT Kurukshetra Website`
      );
      window.open(`https://wa.me/${WA_COORDINATOR}?text=${donorMsg}`, '_blank');

      showSuccessToast('✅ Your details have been sent to the coordinator!');

      setTimeout(() => {
        donateForm.reset();
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerHTML = '<span><i class="fab fa-whatsapp me-2"></i>Register via WhatsApp</span>';
        }
      }, 2000);
    });
  }

  /* ── 6. BLOOD REQUEST MODAL ──────────────────────────────────
     Submit → send urgent request info to coordinator only.
     Joining the group is separate (Join Group button).
  ────────────────────────────────────────────────────────────── */
  const requestForm = document.getElementById('bloodRequestForm');
  if (requestForm) {
    requestForm.addEventListener('submit', function (e) {
      e.preventDefault();

      const name     = document.getElementById('reqName').value.trim();
      const blood    = document.getElementById('reqBlood').value;
      const location = document.getElementById('reqLocation').value.trim();
      const contact  = document.getElementById('reqContact').value.trim();

      if (!name || !blood || blood === 'Select Group' || !location || !contact) {
        showFormError('⚠️ Please fill in all required fields.');
        return;
      }

      /* Send urgent request details to coordinator */
      const reqMsg = encodeURIComponent(
        `🚨 *URGENT Blood Request* 🚨\n\n` +
        `👤 *Patient Name:* ${name}\n` +
        `🩸 *Blood Group Needed:* ${blood}\n` +
        `📍 *Hospital / Location:* ${location}\n` +
        `📞 *Contact:* ${contact}\n\n` +
        `— NSS NIT Kurukshetra Website`
      );
      window.open(`https://wa.me/${WA_COORDINATOR}?text=${reqMsg}`, '_blank');

      /* Close modal */
      const modalEl = document.getElementById('bloodRequestModal');
      if (modalEl) {
        const bsModal = bootstrap.Modal.getInstance(modalEl) || new bootstrap.Modal(modalEl);
        bsModal.hide();
      }

      showSuccessToast('🚨 Urgent request sent to coordinator!');
      requestForm.reset();
    });
  }

  /* ── 7. WHATSAPP GROUP JOIN BUTTONS ─────────────────────── */
  /* Patch any placeholder href on the group join buttons */
  document.querySelectorAll('[data-wa-group]').forEach(el => {
    el.setAttribute('href', WA_GROUP_LINK);
  });

  /* ── 8. NAVBAR active state on scroll ─────────────────── */
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
  window.addEventListener('scroll', () => {
    let current = '';
    sections.forEach(sec => {
      if (window.scrollY >= sec.offsetTop - 120) current = sec.id;
    });
    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === `#${current}`) link.classList.add('active');
    });
  }, { passive: true });

  /* ── HELPERS ─────────────────────────────────────────────── */
  function showFormError(msg) {
    showToast(msg, 'bd-toast-error');
  }

  function showSuccessToast(msg) {
    showToast(msg, 'bd-toast-success');
  }

  function showToast(msg, cls) {
    /* Remove existing */
    document.querySelectorAll('.bd-toast-error, .bd-toast-success').forEach(t => t.remove());

    const toast = document.createElement('div');
    toast.className = cls;
    toast.textContent = msg;
    document.body.appendChild(toast);

    /* Trigger reflow then show */
    requestAnimationFrame(() => {
      requestAnimationFrame(() => toast.classList.add('show'));
    });

    setTimeout(() => {
      toast.classList.remove('show');
      setTimeout(() => toast.remove(), 400);
    }, 4000);
  }

});
