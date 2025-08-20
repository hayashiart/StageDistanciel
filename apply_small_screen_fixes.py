#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour appliquer automatiquement les media queries pour les très petits écrans
à toutes les pages HTML du projet.
"""

import os
import re
from pathlib import Path

# Media query pour les très petits écrans (375px et moins)
SMALL_SCREEN_MEDIA_QUERY = '''
    /* ===========================================
         TRÈS PETITS ÉCRANS (iPhone 5/SE, iPhone 12 Pro) - 375px et moins
         =========================================== */
    @media (max-width: 375px) {
      /* Layout principal ultra-compact */
      .main-container {
        width: 98%;
        margin: 10px auto;
        padding: 15px;
      }

      .main-content {
        padding: 10px;
      }

      /* Menu burger ultra-compact */
      .menu {
        width: 85%;
        max-width: 280px;
        padding: 50px 10px 15px;
      }

      .menu-toggle {
        width: 28px;
        height: 28px;
        padding: 4px;
        top: 15px;
        left: 15px;
      }

      /* Titres ultra-compacts */
      .intro-title {
        font-size: 20px;
        margin: 15px 0 20px 0;
      }

      .section-header {
        margin: 20px 0 15px;
      }

      .section-number {
        font-size: 24px;
        padding: 15px 20px;
      }

      .section-title {
        font-size: 16px;
        padding: 15px 20px;
      }

      .subsection-heading {
        font-size: 16px;
        padding: 8px 12px;
      }

      /* Centrage ultra-perfect pour tous les composants */
      .regime-container,
      .section1-a-flex-container,
      .powers-list,
      .admin-container,
      .decentralisation-highlight-section,
      .flex-container,
      .admin-cards,
      .decentralisation-content,
      .card,
      .document-container,
      .hierarchie-row,
      .hierarchie-container,
      .imageGaucheTexteDroit-container,
      .imageDroiteTextGauche-container,
      .imageHautTexteBas-container,
      .accord-container,
      .box3lignes-container,
      .box3colonnes-container,
      .box2colonnes-container,
      .galerie-container,
      .timeline-container,
      .tabs-container,
      .tableau-container {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        text-align: center !important;
        width: 100% !important;
        max-width: 100% !important;
        padding: 10px !important;
        margin: 10px 0 !important;
      }

      /* Centrage spécifique pour le composant régime (section 1B) */
      .regime-container {
        padding: 15px !important;
        gap: 15px !important;
      }

      .regime-img {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
        max-width: 150px !important;
        margin: 0 auto !important;
      }

      .regime-img img {
        display: block !important;
        margin: 0 auto !important;
        max-width: 100% !important;
        height: auto !important;
        width: 100% !important;
      }

      .regime-text {
        width: 100% !important;
        text-align: center !important;
        padding: 10px !important;
      }

      /* Cartes de pouvoirs ultra-compactes */
      .powers-list {
        gap: 10px !important;
      }

      .power-card {
        width: 160px !important;
        height: 120px !important;
        margin: 5px !important;
      }

      .card-front,
      .card-back {
        padding: 8px !important;
        font-size: 8px !important;
      }

      .card-title {
        font-size: 12px !important;
      }

      /* Cartes administratives ultra-compactes */
      .admin-cards {
        gap: 10px !important;
      }

      .admin-card {
        min-width: 200px !important;
        padding: 12px !important;
        margin-bottom: 10px !important;
      }

      .admin-card img {
        width: 40px !important;
        height: 40px !important;
      }

      .admin-card-title {
        font-size: 14px !important;
      }

      .admin-card-text {
        font-size: 12px !important;
      }

      /* Composant à retenir ultra-compact */
      .container-a-retenir {
        padding: 15px !important;
        margin: 20px 0 !important;
      }

      .step-content {
        flex-direction: column !important;
        align-items: center !important;
        text-align: center !important;
        gap: 10px !important;
      }

      .step-text {
        text-align: center !important;
        width: 100% !important;
      }

      .number {
        width: 40px !important;
        height: 40px !important;
        font-size: 14px !important;
      }

      /* Tailles de police ultra-compactes */
      .regime-highlight,
      .section1-a-text,
      .admin-intro,
      .decentralisation-highlight,
      .powers-list,
      .admin-card,
      .document-highlight,
      .hierarchie-content,
      .card .text,
      .imageHautTexteBas-text,
      .accord-content,
      .box3lignes-text,
      .box3colonnes-text,
      .box2colonnes-text,
      .galerie-text,
      .timeline-text,
      .tabs-content,
      .tableau-content,
      .regime-highlight p,
      .section1-a-text p,
      .admin-intro p,
      .decentralisation-highlight p,
      .powers-list p,
      .admin-card p,
      .document-highlight p,
      .hierarchie-content p,
      .card .text p,
      .imageHautTexteBas-text p,
      .accord-content p,
      .box3lignes-text p,
      .box3colonnes-text p,
      .box2colonnes-text p,
      .galerie-text p,
      .timeline-text p,
      .tabs-content p,
      .tableau-content p,
      .regime-highlight li,
      .section1-a-text li,
      .admin-intro li,
      .decentralisation-highlight li,
      .powers-list li,
      .admin-card li,
      .document-highlight li,
      .hierarchie-content li,
      .card .text li,
      .imageHautTexteBas-text li,
      .accord-content li,
      .box3lignes-text li,
      .box3colonnes-text li,
      .box2colonnes-text li,
      .galerie-text li,
      .timeline-text li,
      .tabs-content li,
      .tableau-content li {
        font-size: 12px !important;
        line-height: 1.4 !important;
        word-wrap: break-word !important;
        overflow-wrap: break-word !important;
      }

      .regime-highlight h3,
      .regime-highlight h4,
      .section1-a-text h3,
      .section1-a-text h4,
      .powers-list h3,
      .power-card h3,
      .power-card .card-title,
      .commune-title,
      .departement-title,
      .region-title,
      .decentralisation-content h4,
      .admin-card h3,
      .admin-card .card-title,
      .admin-card .card-text h3,
      .admin-card strong,
      .admin-card .paragraphe strong,
      .admin-intro h3,
      .decentralisation-highlight h3,
      .document-highlight h3,
      .hierarchie-content h3,
      .card .text h3,
      .imageHautTexteBas-text h3,
      .accord-content h3,
      .box3lignes-text h3,
      .box3colonnes-text h3,
      .box2colonnes-text h3,
      .galerie-text h3,
      .timeline-text h3,
      .tabs-content h3,
      .tableau-content h3 {
        font-size: 14px !important;
      }

      .text {
        font-size: 14px !important;
      }

      .sub-text {
        font-size: 12px !important;
      }

      .title-retenir-conclusion {
        font-size: 14px !important;
      }

      .container-a-retenir .text {
        font-size: 14px !important;
      }

      .container-a-retenir .sub-text {
        font-size: 12px !important;
      }

      /* Images ultra-compactes */
      .section1-a-image,
      .flex-image,
      .document-img img,
      .card img,
      .imageHautTexteBas-img img,
      .accord-img img,
      .box3lignes-img img,
      .box3colonnes-img img,
      .box2colonnes-img img,
      .galerie-img img,
      .timeline-img img,
      .tabs-img img,
      .tableau-img img {
        max-width: 120px !important;
        margin: 0 auto !important;
        height: auto !important;
      }

      /* Décentralisation ultra-compacte */
      .decentralisation-content {
        grid-template-columns: 1fr !important;
        gap: 10px !important;
      }

      .decentralisation-content > div {
        padding: 10px !important;
      }

      .decentralisation-content h4 {
        font-size: 14px !important;
      }

      .decentralisation-content p {
        font-size: 12px !important;
      }
    }
'''

def apply_small_screen_fixes():
    """Applique les media queries pour les très petits écrans à toutes les pages HTML."""
    
    # Chemin vers le dossier des pages
    pages_dir = Path("cours/CAP AEPE")
    
    # Liste des pages à traiter
    pages = [
        "page3.html", "page4.html", "page5.html", "page6.html", 
        "page7.html", "page8.html", "page9.html", "page10.html", "page11.html"
    ]
    
    for page in pages:
        page_path = pages_dir / page
        if not page_path.exists():
            print(f"⚠️  Page {page} non trouvée, ignorée")
            continue
            
        print(f"🔧 Traitement de {page}...")
        
        try:
            # Lire le contenu du fichier
            with open(page_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Vérifier si la media query existe déjà
            if '@media (max-width: 375px)' in content:
                print(f"   ✅ Media query déjà présente dans {page}")
                continue
            
            # Trouver la fin du dernier style ou la fin du fichier
            # Chercher la dernière balise </style> ou </html>
            if '</style>' in content:
                # Insérer avant la dernière balise </style>
                last_style_pos = content.rfind('</style>')
                new_content = content[:last_style_pos] + SMALL_SCREEN_MEDIA_QUERY + '\n  ' + content[last_style_pos:]
            elif '</html>' in content:
                # Insérer avant la balise </html>
                html_end_pos = content.rfind('</html>')
                new_content = content[:html_end_pos] + '\n  <style>\n' + SMALL_SCREEN_MEDIA_QUERY + '\n  </style>\n' + content[html_end_pos:]
            else:
                print(f"   ❌ Impossible de trouver où insérer la media query dans {page}")
                continue
            
            # Écrire le nouveau contenu
            with open(page_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"   ✅ Media query ajoutée avec succès à {page}")
            
        except Exception as e:
            print(f"   ❌ Erreur lors du traitement de {page}: {e}")
    
    print("\n🎉 Traitement terminé !")

if __name__ == "__main__":
    print("🚀 Application des media queries pour les très petits écrans...")
    apply_small_screen_fixes()
