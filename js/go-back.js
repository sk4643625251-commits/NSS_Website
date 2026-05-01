// Go Back Navigation Script
function goBack() {
  if (window.history.length > 1 && document.referrer !== "") {
    window.history.back();
  } else {
    // Fallback if opened in a new tab or no history
    window.location.href = 'index.html'; 
  }
}
