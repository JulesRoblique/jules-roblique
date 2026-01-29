console.log("hello");

const starContainer = document.querySelector('.stars');

// crée 200 étoiles pour augmenter leur quantité
for (let i = 0; i < 200; i++) {
    const star = document.createElement('div');
    star.classList.add('star');
    star.style.width = '${Math.random() * 4 + 1}px'; // Taille accrue des étoiles
    star.style.height = star.style.width;
    star.style.top = '${Math.random() *100}vh';
    star.style.left = '${Math.random() *100}vw';
    star.style.animationDuration = '${Math.random() * 2 + 3}s'; // Durée d'animation plus lente
    star.style.animationDelay = '${Math.random() * 3}s'; // Délai variable
    // Ajoute l'étoile à l'écran
    starContainer.appendChild(star);
}