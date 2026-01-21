import streamlit as st
import numpy as np
import pandas as pd
import os
import glob
import tensorflow.compat.v1 as tf  # Pour compatibilité avec Mask R-CNN
from PIL import Image
from mrcnn.model import MaskRCNN
from mrcnn.config import Config
import time
from io import BytesIO
from skimage.measure import label, regionprops
import base64
import xlsxwriter
from PIL import ImageDraw, ImageFont
st.set_page_config(page_title="Détection d’Organoïdes", layout="wide")
import zipfile







page = st.sidebar.selectbox("Navigation", ["Home", "Segmentation des organoïdes"])


 
#PAGE 1 HOME


if page == "Home":


    # Fonction pour afficher une image centrée avec moins d'espace
    def center_image(image_path, width=None):
        encoded = base64.b64encode(open(image_path, "rb").read()).decode()
        width_attr = f"width='{width}'" if width else "style='width:60%;'"
        
        st.markdown(f"""
            <div style='display: flex; justify-content: center; align-items: center; padding: 0px;'>
                <img src='data:image/png;base64,{encoded}' {width_attr}>
            </div>
        """, unsafe_allow_html=True)

    # Réduction de l’espace en haut de la page
    st.markdown("""
        <style>
        .block-container {
            padding-top: 1rem !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- HEADER ---
    center_image("images/Logo_Projet5D3TECT.png", width=450)

    # --- SECTION 1 ---
    st.markdown("""
    <div style='
        background-color:#e0f0ff;
        padding:60px;
        border-top:1px solid black;
        border-left:1px solid black;
        border-right:1px solid black;
        border-bottom:none;
        border-top-left-radius:15px;
        border-top-right-radius:15px;
    '>
        <div style='display:flex;align-items:center;'>
            <div style='flex:1;padding-right:30px;'>
                <h2 style='font-family:Times New Roman;font-weight:bold;'>Notre solution</h2>
                <h4>La puissance de l’IA au service de vos organoïdes cérébraux</h4>
                <p style='text-align:justify;'>
                Avec <strong>D3TECT</strong>, nous avons créé une webapp intelligente qui révolutionne le suivi de croissance des organoïdes cérébraux. 
                Grâce à notre technologie de détourage automatique, vous pouvez traiter un grand nombre de fichiers en un temps record, sans sacrifier la précision.<br><br>
                Notre solution identifie et isole les contours des organoïdes de façon fiable, permettant une analyse visuelle et quantitative fluide au fil du temps. 
                Plus besoin de passer des heures sur chaque image : <strong>D3TECT</strong> le fait pour vous, de manière rapide, cohérente et reproductible.<br><br>
                Accélérez vos recherches, libérez du temps, et concentrez-vous sur l’innovation !
                </p>
            </div>
            <div style='flex:1;'>
                <img src='data:image/png;base64,{}' width='100%'/>
            </div>
        </div>
    </div>
""".format(base64.b64encode(open("images/brain-organoid-crosssection.webp", "rb").read()).decode()), unsafe_allow_html=True)


    # --- SECTION 2 ---
    st.markdown("""
    <div style='
        background-color:#f1f8fe;
        padding:60px;
        border-left:1px solid black;
        border-right:1px solid black;
        border-top:none;
        border-bottom:none;
    '>
        <div style='display:flex;align-items:center;'>
            <div style='flex:1;'>
                <img src='data:image/png;base64,{}' width='100%'/>
            </div>
            <div style='flex:1;padding-left:30px;'>
                <h2 style='font-family:Times New Roman;font-weight:bold;'>D3TECT en profondeur</h2>
                <h4>Du pixel à la donnée : l’analyse intelligente</h4>
                <p style='text-align:justify;'>
                <strong>D3TECT</strong> s’appuie sur le meilleur de l’intelligence artificielle pour révéler ce que l’œil humain mettrait des heures à analyser.<br><br>
                Au cœur de notre solution : <strong>Mask R-CNN</strong>, un puissant modèle de deep learning capable de détecter et détourer automatiquement chaque organoïde dans vos images.<br><br>
                Entraîné avec soin à partir de données annotées issues de notre partenariat avec <strong>CellTechs</strong> et complétées par des ressources open source, notre IA est devenue experte pour reconnaître précisément les contours des organoïdes cérébraux.<br><br>
                Avec <strong>D3TECT</strong>, vous bénéficiez d’une technologie rapide, précise et accessible à tous, même sans compétences techniques. 
                L’analyse d’image devient simple, fiable, et surtout… incroyablement efficace.
                </p>
            </div>
        </div>
    </div>
""".format(base64.b64encode(open("images/Section_2.png", "rb").read()).decode()), unsafe_allow_html=True)


# --- SECTION 3 ---
    # Liste des membres
    membres = [
        {"nom": "Marion DERET", "role": "Ingénieure DeepLearning", "photo": "images/marion.jpg"},
        {"nom": "Kenza GUERBAA", "role": "Responsable Marketing", "photo": "images/kenza.jpg"},
        {"nom": "Necla GUVEN", "role": "Business Analyst", "photo": "images/necla.jpg"},
        {"nom": "Thibaud ROYON", "role": "Data Analyst", "photo": "images/thibaud.jpg"},
        {"nom": "Shéhanie UDUGAMPOLAGE", "role": "Développeur FullStack Web", "photo": "images/shehanie.jpg"},
        {"nom": "Dimitri ZETEA", "role": "Data Scientist", "photo": "images/dimitri.jpg"},
    ]

    # Ouvre le conteneur principal de la section 3
    st.markdown("""
    <div style='
        background-color:#e0f0ff;
        padding:60px;
        text-align:center;
        border-left:1px solid black;
        border-right:1px solid black;
        border-bottom:1px solid black;
        border-top:none;
        border-bottom-left-radius:15px;
        border-bottom-right-radius:15px;
    '>
        <h2 style='font-family:Times New Roman; font-weight:bold;'>L'équipe D3TECT</h2>
        <h4>Un groupe d'étudiants scientifiques unis par l'ambition de repousser les limites de l'IA pour la biologie</h4>
        <div style='margin-top:40px;'>
            <p>
            Nous sommes des étudiants ingénieurs en alternance à Sup'Biotech, l’école d’ingénieurs en biotechnologies située à Paris.<br><br>
            Dans le cadre de notre projet 5D, nous avons développé une solution unique pour répondre à une problématique concrète, en alliant nos compétences scientifiques, techniques et notre expérience en entreprise.
            </p>
        </div>        
    </div>
    """, unsafe_allow_html=True)


    # Affichage des membres 3 par 3 avec encadré noir fin
    for i in range(0, len(membres), 3):
        cols = st.columns([1, 1, 1], gap="medium")
        for j in range(3):
            if i + j < len(membres):
                m = membres[i + j]
                encoded = base64.b64encode(open(m['photo'], 'rb').read()).decode()
                with cols[j]:
                    st.markdown(f"""
                        <div style='
                            text-align:center;
                            background-color:#e0f0ff;
                            padding:10px 10px 15px 10px;
                            border-radius:15px;
                            margin-top:20px;
                            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
                            border: 1px solid black;
                        '>
                            <div style='
                                border:1px solid black;
                                border-radius:50%;
                                width:120px;
                                height:120px;
                                overflow:hidden;
                                margin:auto;
                            '>
                                <img src='data:image/png;base64,{encoded}' width='120' height='120' style='object-fit:cover;'/>
                            </div>
                            <h4 style='margin:10px 0 0px 0; font-weight:bold;'>{m['nom']}</h4>
                            <p style='margin:0; padding-top:2px;'>{m['role']}</p>
                        </div>
                    """, unsafe_allow_html=True)



   

    # --- FOOTER ---
    st.markdown("""
    <hr style='margin-top:60px;'>
    <div style='text-align:center;font-size:14px;'>
        <a href="#">A propos</a> | <a href="#">Nous contacter</a> | <a href="#">Mentions légales</a>
    </div>
    """, unsafe_allow_html=True)


elif page == "Segmentation des organoïdes":

    # Réduction de l’espace en haut de la page
    st.markdown("""
        <style>
        .block-container {
            padding-top: 0rem !important;
        }
        </style>
    """, unsafe_allow_html=True)

 # Fonction pour afficher une image centrée
    def center_image(image_path, width=None):
        encoded = base64.b64encode(open(image_path, "rb").read()).decode()
        width_attr = f"width='{width}'" if width else "style='width:60%;'"
        
        st.markdown(f"""
            <div style='display: flex; justify-content: center; align-items: center; padding: 20px 0;'>
                <img src='data:image/png;base64,{encoded}' {width_attr}>
            </div>
        """, unsafe_allow_html=True)
# --- HEADER ---
    center_image("images/Logo_Projet5D3TECT.png", width=350)  # <- Mets ici le bon nom de fichier image du logo



    st.markdown("<h1 style='text-align: center;'>Segmentation des organoïdes</h1>", unsafe_allow_html=True)

    tf.disable_v2_behavior()

    class InferenceConfig(Config):
        NAME = "organoids"
        GPU_COUNT = 1
        IMAGES_PER_GPU = 1
        NUM_CLASSES = 1 + 1

    @st.cache_resource
    def load_model(model_path):
        graph = tf.Graph()
        with graph.as_default():
            session = tf.Session(graph=graph)
            with session.as_default():
                model = MaskRCNN(mode="inference", config=InferenceConfig(), model_dir=os.path.dirname(model_path))
                model.load_weights(model_path, by_name=True)
                return model, session, graph

    def convert_image_to_bytes(img_array):
        img_pil = Image.fromarray(img_array.astype(np.uint8))
        buffer = BytesIO()
        img_pil.save(buffer, format="PNG")
        buffer.seek(0)
        return buffer

    def calculate_area_perimeter_diameter(mask):
        labeled = label(mask)
        props = regionprops(labeled)
        if not props:
            return 0, 0, 0, 0
        region = props[0]
        area = region.area
        perimeter = region.perimeter
        diameter = region.equivalent_diameter
        circularity = (4 * np.pi * area) / (perimeter ** 2) if perimeter > 0 else 0
        return area, perimeter, diameter, circularity



    model_path = "models/mask_rcnn_organoid_segmentation_0010.h5"
    model, session, graph = load_model(model_path)

    uploaded_file = st.file_uploader(
        "📤 Téléversez une ou plusieurs images",
        type=["jpg", "jpeg", "png", "tif", "tiff"],
        accept_multiple_files=True
    )

    if uploaded_file:
        all_mesures = []
        masked_images = {}

        st.subheader("Prédiction en cours...")
        progress_bar = st.progress(0)
        time_text = st.empty()

        total_images = len(uploaded_file)

        for idx, file in enumerate(uploaded_file, start=1):
            image = Image.open(file).convert("RGB")
            img_array = np.array(image)

            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image(img_array, caption=f"Image originale : {file.name}", width=400)

            time_text.text(f"Traitement de l'image {idx}/{total_images} : {file.name}")
            progress_bar.progress(idx / total_images)

            with graph.as_default():
                with session.as_default():
                    results = model.detect([img_array], verbose=0)

            r = results[0]

            mask = np.zeros_like(img_array[:, :, 0], dtype=np.uint8)
            overlay = img_array.astype(np.uint8).copy()
            masked_image = overlay.copy()

            if r.get("masks") is None or r["masks"].size == 0:
                st.warning(f"Aucune détection pour : {file.name}")
                masked_images[file.name] = Image.fromarray(masked_image)
                continue

            for i_det in range(r["masks"].shape[-1]):
                m = r["masks"][:, :, i_det]
                score = r["scores"][i_det]
                y1, x1, y2, x2 = r["rois"][i_det]

                red = np.array([255, 0, 0], dtype=np.uint8)
                alpha = 0.4
                masked_image[m] = ((1 - alpha) * masked_image[m] + alpha * red).astype(np.uint8)

                mask = np.maximum(mask, (m.astype(np.uint8) * 255))

                area, perimeter, diameter, circularity = calculate_area_perimeter_diameter(m)

                all_mesures.append({
                    "Image": file.name,
                    "Organoïde": f"# {i_det + 1}",
                    "Seuil de confiance": f"{score:.3f}",
                    "Surface (px²)": area,
                    "Périmètre (px)": f"{perimeter:.2f}",
                    "Diamètre (px)": f"{diameter:.2f}",
                    "Circularité": f"{circularity:.3f}"
                })

            pil_overlay = Image.fromarray(masked_image)
            draw = ImageDraw.Draw(pil_overlay)
            try:
                font = ImageFont.truetype("DejaVuSans-Bold.ttf", size=32)
            except:
                font = ImageFont.load_default()

            for i_det in range(r["masks"].shape[-1]):
                score = r["scores"][i_det]
                y1, x1, y2, x2 = r["rois"][i_det]
                draw.rectangle([(x1, y1), (x2, y2)], outline=(255, 255, 0), width=3)
                draw.text((x1, max(0, y1 - 30)), f"organoid {score:.3f}", fill=(255, 255, 255), font=font)

            masked_image = np.array(pil_overlay)

            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image(mask, caption=f"Masque détecté : {file.name}", width=400)

            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image(masked_image, caption=f"Masque superposé : {file.name}", width=400)

            masked_images[file.name] = Image.fromarray(masked_image)

        time_text.text("✅ Détection terminée")

        df = pd.DataFrame(all_mesures)

        st.markdown("<br><hr><br>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align:center;'> Convertisseur pixels → cm</h3>", unsafe_allow_html=True)

        c1, c2, c3 = st.columns([1, 2, 1])
        with c2:
            dpi = st.number_input(
                "Résolution de votre image (pixels par pouce - dpi)",
                min_value=1,
                value=300,
                help="Indiquez la résolution utilisée lors de la capture de l'image (cf propriétés de l'image)"
            )
            pixel_to_cm = 2.54 / dpi
            st.markdown(
                f"<p style='text-align:center;'>🔁 1 pixel = <b>{pixel_to_cm:.5f} cm</b></p>",
                unsafe_allow_html=True
            )

        df_cm = df.copy()
        if not df_cm.empty:
            df_cm["Surface (cm²)"] = df["Surface (px²)"] * (pixel_to_cm ** 2)
            df_cm["Périmètre (cm)"] = df["Périmètre (px)"].astype(float) * pixel_to_cm
            df_cm["Diamètre (cm)"] = df["Diamètre (px)"].astype(float) * pixel_to_cm
            df_cm["Circularité (%)"] = df["Circularité"].astype(float) * 100
            df_cm = df_cm[[
                "Image", "Organoïde", "Seuil de confiance",
                "Surface (cm²)", "Périmètre (cm)", "Diamètre (cm)", "Circularité (%)"
            ]]

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
                <div style='border:1px solid black; border-radius:12px; padding:20px; background-color:#d4f4e7;'>
                    <h4 style='text-align:center;'> Mesures en pixels (toutes les images)</h4>
            """, unsafe_allow_html=True)
            st.dataframe(df, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("""
                <div style='border:1px solid black; border-radius:12px; padding:20px; background-color:#d4f4e7;'>
                    <h4 style='text-align:center;'> Mesures converties (en cm) - toutes les images</h4>
            """, unsafe_allow_html=True)
            st.dataframe(df_cm, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zf:
            for name, pil_img in masked_images.items():
                img_bytes = BytesIO()
                pil_img.save(img_bytes, format="PNG")
                img_bytes.seek(0)
                base = name.rsplit(".", 1)[0]
                zf.writestr(f"{base}_organoide_masque.png", img_bytes.getvalue())
        zip_buffer.seek(0)

        with col1:
            st.download_button(
                label="📥 Télécharger les images avec masque (ZIP)",
                data=zip_buffer,
                file_name="images_organoides_masques.zip",
                mime="application/zip"
            )
            st.download_button(
                label="📊 Télécharger les mesures (CSV)",
                data=df.to_csv(index=False).encode("utf-8"),
                file_name="mesures_organoides_px.csv",
                mime="text/csv"
            )
            excel_px = BytesIO()
            with pd.ExcelWriter(excel_px, engine="xlsxwriter") as writer:
                df.to_excel(writer, sheet_name="Mesures_px", index=False)
            excel_px.seek(0)
            st.download_button(
                label="📊 Télécharger les mesures (Excel)",
                data=excel_px,
                file_name="mesures_organoides_px.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        with col2:
            st.download_button(
                label="📊 Télécharger les mesures converties (CSV)",
                data=df_cm.to_csv(index=False).encode("utf-8"),
                file_name="mesures_organoides_cm.csv",
                mime="text/csv"
            )
            excel_cm = BytesIO()
            with pd.ExcelWriter(excel_cm, engine="xlsxwriter") as writer:
                df_cm.to_excel(writer, sheet_name="Mesures_cm", index=False)
            excel_cm.seek(0)
            st.download_button(
                label="📊 Télécharger les mesures converties (Excel)",
                data=excel_cm,
                file_name="mesures_organoides_cm.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
