// JavaScript to toggle the visibility of small screen navigation
document.addEventListener("DOMContentLoaded", function () {
  const navbarCta = document.getElementById("navbar-cta");
  const toggleButton = document.querySelector(
    '[data-collapse-toggle="navbar-cta"]'
  );

  toggleButton.addEventListener("click", function () {
    const expanded = navbarCta.getAttribute("aria-expanded") === "true";
    navbarCta.style.display = expanded ? "none" : "block";
    navbarCta.setAttribute("aria-expanded", !expanded);
  });
});

function hireMeBtnClickHandler() {
  // Scroll to the contact section
  var contactSection = document.getElementById("contactMe"); // Replace 'contact' with the actual ID of your contact section
  contactSection.scrollIntoView({ behavior: "smooth" });

  // Pre-fill the textarea with a default message
  var messageTextarea = document.getElementById("message");
  messageTextarea.value =
    "I'm interested in hiring you. Let's discuss further!";
}

// Attach the event listener to both buttons
document
  .getElementById("hireMeBtn1")
  .addEventListener("click", hireMeBtnClickHandler);
document
  .getElementById("hireMeBtn2")
  .addEventListener("click", hireMeBtnClickHandler);
