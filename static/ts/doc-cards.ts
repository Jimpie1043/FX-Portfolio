// Collapse and expand the description of the documentation cards
document.addEventListener("DOMContentLoaded", () => {
  const containers = document.querySelectorAll<HTMLElement>("[data-doc-description]");

  containers.forEach((container) => {
    const checkbox = container.querySelector<HTMLInputElement>("input[type=checkbox]");
    const text = container.querySelector<HTMLElement>("[data-doc-description-text]");
    const moreLabel = container.querySelector<HTMLElement>("[data-doc-description-more]");

    if (!checkbox || !text || !moreLabel) {
      return;
    }

    const fullText = text.textContent ?? "";
    const collapsedText = buildCollapsedText(fullText);

    if (collapsedText === fullText) {
      return;
    }

    text.textContent = collapsedText;
    moreLabel.classList.remove("hidden");

    const collapsedHeight = text.scrollHeight;

    checkbox.addEventListener("change", () => {
      text.textContent = checkbox.checked ? fullText : collapsedText;

      if (checkbox.checked) {
        scrollByFast(text.scrollHeight - collapsedHeight, 200);
      }
    });
  });
});

function buildCollapsedText(fullText: string): string {
  const lines = fullText.split("\n");
  const blankIndex = lines.findIndex((line) => line.trim() === "");

  if (blankIndex !== -1) {
    if (blankIndex >= lines.length - 1) {
      return fullText;
    }
    return [...lines.slice(0, blankIndex), "…"].join("\n");
  }

  if (lines.length <= 3) {
    return fullText;
  }

  return [...lines.slice(0, 3), "…"].join("\n");
}

function scrollByFast(deltaY: number, duration: number): void {
  const start = window.scrollY;
  const startTime = performance.now();

  const easeOutQuad = (t: number) => t * (2 - t);

  function step(now: number): void {
    const elapsed = Math.min((now - startTime) / duration, 1);
    window.scrollTo(0, start + deltaY * easeOutQuad(elapsed));

    if (elapsed < 1) {
      requestAnimationFrame(step);
    }
  }

  requestAnimationFrame(step);
}
