import re

def apply_final_modifications(file_path):
    """Applique les modifications finales à une page HTML"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Modifier l'image du composant "à retenir"
    content = re.sub(
        r'src="https://medias\.dstanciel\.com/pages/[^"]*"',
        'src="../../images/png/imageRetenir.png"',
        content
    )
    
    # 2. Remplacer les tailles de titres pour mobile
    content = re.sub(
        r'\.intro-title\s*\{\s*font-size:\s*\d+px;',
        '.intro-title {\n          font-size: 24px;',
        content
    )
    
    # 3. Ajouter les styles manquants pour mobile
    mobile_styles = '''
        .section-number {
          font-size: 28px;
        }

        .section-title {
          font-size: 20px;
        }

        .subsection-heading {
          font-size: 18px;
        }

        /* Titres des composants */
        .title-retenir-conclusion {
          font-size: 16px;
        }

        .text {
          font-size: 14px;
        }

        .sub-text {
          font-size: 12px;
        }
'''
    
    # 4. Ajouter les styles pour tablette
    tablette_styles = '''
      /* ===========================================
           TABLETTE (768px - 1023px) - ADAPTATION MOYENNE
           =========================================== */
      @media (max-width: 1023px) and (min-width: 768px) {
        /* Titres adaptés pour tablette */
        .intro-title {
          font-size: 32px;
        }

        .section-number {
          font-size: 32px;
        }

        .section-title {
          font-size: 22px;
        }

        .subsection-heading {
          font-size: 20px;
        }

        /* Titres des composants pour tablette */
        .title-retenir-conclusion {
          font-size: 18px;
        }

        .text {
          font-size: 16px;
        }

        .sub-text {
          font-size: 14px;
        }

        /* Centrage pour tablette */
        .container-a-retenir,
        .steps,
        .step-content,
        .text,
        .sub-text {
          text-align: center;
          justify-content: center;
          align-items: center;
        }

        .steps {
          flex-direction: column;
          align-items: center;
        }

        .step-content {
          width: 100%;
          max-width: 600px;
          margin: 0 auto;
        }
      }
'''
    
    # 5. Ajouter le centrage et débordement pour mobile
    mobile_centering = '''
        /* Centrage et débordement pour tous les éléments */
        .flex-container,
        .lignes3-container,
        .hierarchie-row,
        .document-container,
        .ase-services-container,
        .box-ligne-entiere-container,
        .imageHautTexteBas-container,
        .accord-cards-container,
        .periode-essai-example-unique,
        .content-section,
        .decentralisation-highlight-section,
        .regime-container,
        .box3lignes-container,
        .structures-grid,
        .structure-box {
          flex-direction: column;
          align-items: center;
          text-align: center;
          padding: 15px;
          justify-content: center;
          width: 100%;
          max-width: 100%;
        }

        /* Réduction de la taille des textes pour éviter le débordement */
        .section-text,
        .text,
        .sub-text,
        .lignes3-yellow-text,
        .hierarchie-content,
        .document-highlight,
        .ase-service-card p,
        .box-ligne-entiere-container p,
        .imageHautTexteBas-text-box p,
        .accord-card p,
        .example-text-unique,
        .content-text p,
        .decentralisation-content p,
        .regime-highlight p,
        .box3lignes-text,
        .structure-content p {
          font-size: 16px;
          line-height: 1.5;
          padding: 20px;
          word-wrap: break-word;
          overflow-wrap: break-word;
        }

        /* Images centrées et redimensionnées */
        .office-image,
        .document-img,
        .imageHautTexteBas-header-image,
        .regime-img,
        .box3lignes-image,
        .content-image {
          max-width: 200px;
          margin: 0 auto;
        }
'''
    
    # Appliquer les modifications
    # Ajouter les styles mobile après la section mobile existante
    if '@media (max-width: 767px)' in content:
        mobile_end = content.find('}', content.find('@media (max-width: 767px)'))
        if mobile_end != -1:
            content = content[:mobile_end] + mobile_centering + content[mobile_end:]
    
    # Ajouter les styles tablette si pas déjà présents
    if '@media (max-width: 1023px) and (min-width: 768px)' not in content:
        mobile_end = content.find('}', content.find('@media (max-width: 767px)'))
        if mobile_end != -1:
            content = content[:mobile_end] + tablette_styles + content[mobile_end:]
    
    # Sauvegarder les modifications
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Modifications finales appliquées à {file_path}")

# Appliquer aux pages 9, 10 et 11
pages = ['page9.html', 'page10.html', 'page11.html']
for page in pages:
    file_path = f'cours/CAP AEPE/{page}'
    try:
        apply_final_modifications(file_path)
    except FileNotFoundError:
        print(f"Fichier {file_path} non trouvé")
