// Script pour améliorer le responsive de tous les composants
// Ce script peut être utilisé pour ajouter des media queries manquantes

const responsiveTemplate = `
  /* Mobile (≤768px) */
  @media (max-width: 768px) {
    .container {
      width: 95%;
      padding: 15px;
    }
    
    .col-1, .col-2, .col-3, .col-4, .col-5, .col-6,
    .col-7, .col-8, .col-9, .col-10, .col-11, .col-12 {
      width: 100%;
    }
    
    .is-flex {
      flex-direction: column;
    }
    
    .text {
      font-size: 14px;
    }
    
    .title {
      font-size: 18px;
    }
  }

  /* Tablet (768px-1024px) */
  @media (min-width: 769px) and (max-width: 1024px) {
    .container {
      width: 90%;
    }
  }

  /* Laptop (1024px-1440px) */
  @media (min-width: 1025px) and (max-width: 1440px) {
    .container {
      width: 85%;
    }
  }

  /* Desktop (>1440px) */
  @media (min-width: 1441px) {
    .container {
      width: 80%;
      max-width: 1200px;
    }
  }
`;

console.log("Template de responsive créé pour améliorer tous les composants");
console.log("Points clés du responsive amélioré :");
console.log("- Mobile (≤768px) : Layout vertical, tailles réduites");
console.log("- Tablet (768px-1024px) : Adaptation intermédiaire");
console.log("- Laptop (1024px-1440px) : Optimisation pour écrans moyens");
console.log("- Desktop (>1440px) : Utilisation optimale de l'espace");
