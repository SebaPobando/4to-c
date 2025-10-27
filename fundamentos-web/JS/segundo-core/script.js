document.querySelectorAll('.like-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        const p = btn.parentElement.querySelector('.like-parrafo');
        const n = parseInt(p.textContent) || 0;
        p.textContent = `${n + 1} like(s)`;
    });
});
