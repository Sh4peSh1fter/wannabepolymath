document.addEventListener("DOMContentLoaded", function() {
  // Find all the top-level navigation items that can be expanded
  const topLevelToggles = document.querySelectorAll(".md-nav--primary > .md-nav__list > .md-nav__item--nested > .md-toggle");
  
  // Programmatically check the box to expand the section
  topLevelToggles.forEach(toggle => {
    toggle.checked = true;
  });
});
