"use strict";
// Collapse and expand the description of the documentation cards
document.addEventListener("DOMContentLoaded", () => {
    const containers = document.querySelectorAll("[data-doc-description]");
    containers.forEach((container) => {
        const checkbox = container.querySelector("input[type=checkbox]");
        const text = container.querySelector("[data-doc-description-text]");
        const moreLabel = container.querySelector("[data-doc-description-more]");
        if (!checkbox || !text || !moreLabel) {
            return;
        }
        const collapsedHeight = text.clientHeight;
        const isOverflowing = text.scrollHeight > collapsedHeight + 1;
        if (isOverflowing) {
            moreLabel.classList.remove("hidden");
        }
        checkbox.addEventListener("change", () => {
            if (checkbox.checked) {
                scrollByFast(text.scrollHeight - collapsedHeight);
            }
        });
    });
});
function scrollByFast(deltaY, duration = 200) {
    const start = window.scrollY;
    const startTime = performance.now();
    const easeOutQuad = (t) => t * (2 - t);
    function step(now) {
        const elapsed = Math.min((now - startTime) / duration, 1);
        window.scrollTo(0, start + deltaY * easeOutQuad(elapsed));
        if (elapsed < 1) {
            requestAnimationFrame(step);
        }
    }
    requestAnimationFrame(step);
}
