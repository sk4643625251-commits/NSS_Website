/* ============================================================
   js/contact.js — Contact Form → WhatsApp
   NSS NIT Kurukshetra
   ============================================================ */

const CONTACT_WA = '917068357521'; // NSS Coordinator

document.addEventListener('DOMContentLoaded', function () {

  /* Scroll reveal */
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) entry.target.classList.add('active');
    });
  }, { threshold: 0.1 });
  document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

  /* Contact form submit → WhatsApp */
  const form = document.getElementById('contactForm');
  if (!form) return;

  form.addEventListener('submit', function (e) {
    e.preventDefault();

    const name    = document.getElementById('contactName').value.trim();
    const email   = document.getElementById('contactEmail').value.trim();
    const subject = document.getElementById('contactSubject').value.trim();
    const message = document.getElementById('contactMessage').value.trim();

    if (!name || !email || !subject || !message) {
      showToast('⚠️ Please fill in all fields.', 'error');
      return;
    }

    /* Animate button */
    const btn = form.querySelector('button[type="submit"]');
    if (btn) {
      btn.disabled = true;
      btn.innerHTML = '<i class="fab fa-whatsapp me-2"></i>Opening WhatsApp…';
    }

    /* Build pre-filled WhatsApp message */
    const msg = encodeURIComponent(
      `📩 *New Contact Message — NSS Website*\n\n` +
      `👤 *Name:* ${name}\n` +
      `📧 *Email:* ${email}\n` +
      `📌 *Subject:* ${subject}\n\n` +
      `💬 *Message:*\n${message}\n\n` +
      `— NSS NIT Kurukshetra Website`
    );

    window.open(`https://wa.me/${CONTACT_WA}?text=${msg}`, '_blank');

    showToast('✅ Message sent via WhatsApp!', 'success');

    setTimeout(() => {
      form.reset();
      if (btn) {
        btn.disabled = false;
        btn.innerHTML = 'Send Message <i class="fas fa-paper-plane ms-2"></i>';
      }
    }, 2000);
  });

  /* Toast helper */
  function showToast(msg, type) {
    document.querySelectorAll('.ct-toast').forEach(t => t.remove());
    const toast = document.createElement('div');
    toast.className = 'ct-toast ct-toast-' + type;
    toast.textContent = msg;
    document.body.appendChild(toast);
    requestAnimationFrame(() => requestAnimationFrame(() => toast.classList.add('show')));
    setTimeout(() => {
      toast.classList.remove('show');
      setTimeout(() => toast.remove(), 400);
    }, 4000);
  }

});
