import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

with st.sidebar:
    opciones = option_menu(
        "FioStudio",
        ["Inicio", "Experiencia", "Gráficos"],
        icons=["house-heart", "journal-code", "bar-chart-line"],
        menu_icon="stars",
        default_index=0
    )

if opciones == "Inicio":
    st.markdown("<h1 style='text-align:center; color:#C97B84; font-size:60px;'>FioStudio</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align:center; color:#7A6467;'>Publicidad • Creatividad • Branding</h4>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1.2])

    with col1:
        st.image("perfil.png", caption="Fiorella", width=360)

    with col2:
        st.markdown("""
        <div style='background-color:#FFF8F6; padding:25px; border-radius:18px;
        border:1px solid #E8C7CC; color:#403838; font-size:18px; line-height:1.6;
        text-align:justify;'>

        Hola, soy Fiorella. Soy de Lima, Perú, y estudio Publicidad en la PUCP.<br><br>

        Lo que más me gusta de mi carrera es reconocer la identidad de una marca:
        entender qué comunica, cómo se diferencia y de qué manera puede conectar
        con las personas.<br><br>

        En el futuro me gustaría trabajar en una empresa de publicidad y también
        fortalecer mi propia marca, FioStudio, un estudio de uñas y maquillaje.<br><br>

        En mi tiempo libre me gusta cantar y pintar, porque son actividades que me
        permiten expresarme de manera creativa.

        </div>
        """, unsafe_allow_html=True)

elif opciones == "Experiencia":
    st.markdown("<h1 style='text-align:center; color:#C97B84;'>Mi experiencia aprendiendo Python 💻</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div style='background-color:#FFF8F6; padding:25px; border-radius:18px;
    border:1px solid #E8C7CC; color:#403838; font-size:18px; line-height:1.6;
    text-align:justify;'>

    Al inicio me sentí perdida aprendiendo Python. Los códigos y los comentarios
    juntos me mareaban bastante, y una de las partes más difíciles fue memorizar
    la estructura de los comandos.<br><br>

    Sin embargo, poco a poco entendí que programar no se trata solo de memorizar,
    sino de practicar, equivocarse, corregir y volver a intentar. Durante este proceso
    aprendí a crear mi propio blog usando Streamlit.<br><br>

    Este aprendizaje se relaciona con mi carrera porque la programación puede ayudarme
    a comunicar ideas de manera digital. En el futuro me gustaría crear una plataforma
    para mi negocio, FioStudio, y usarla como una herramienta de publicidad para mostrar
    mis servicios de uñas y maquillaje.

    </div>
    """, unsafe_allow_html=True)

    st.subheader("🎥 Video 1 - Práctica 1")
    st.link_button(
        "Ver Video 1",
        "https://drive.google.com/file/d/1Z5aKKugC8L50TMEY0LHF22ZNNuZJXZa7/view?usp=drive_link"
    )
    st.caption("En este video presento una de las prácticas desarrolladas durante el curso de programación.")

    st.subheader("🎥 Video 2 - Práctica 2")
    st.link_button(
        "Ver Video 2",
        "https://drive.google.com/file/d/1IHWLU8fvY7cO7ju8_ot9j3geth_jmcD9/view?usp=drivesdk"
    )
    st.caption("En este video presento otra práctica realizada durante el curso aplicando los conocimientos adquiridos.")

elif opciones == "Gráficos":
    st.markdown("<h1 style='text-align:center; color:#C97B84;'>Gráficos y visualizaciones 📊</h1>", unsafe_allow_html=True)

    graficos = ["Nube de palabras", "Histograma", "Gráfico de barras", "Gráfico de pastel", "Mapa interactivo"]
    grafico_seleccionado = st.selectbox("Selecciona un gráfico", graficos)

    if grafico_seleccionado == "Nube de palabras":
        st.subheader("☁️ Gráfico 1: Nube de palabras")
        st.write("La nube de palabras permite identificar los conceptos más importantes asociados a FioStudio, como belleza, creatividad, uñas, maquillaje, branding e identidad.")
        st.image("grafico1.png", width=800)

    elif grafico_seleccionado == "Histograma":
        st.subheader("📊 Gráfico 2: Histograma")
        st.write("El histograma muestra una distribución referencial de edades de clientas potenciales. Esto ayuda a orientar el tono de comunicación de FioStudio.")
        st.image("grafico2.png", width=800)

    elif grafico_seleccionado == "Gráfico de barras":
        st.subheader("📈 Gráfico 3: Servicios más solicitados")
        st.write("El gráfico de barras compara distintos servicios ofrecidos por FioStudio y permite identificar cuáles generan mayor interés.")
        st.image("grafico3.png", width=800)

    elif grafico_seleccionado == "Gráfico de pastel":
        st.subheader("🥧 Gráfico 4: Canales de contacto")
        st.write("El gráfico de pastel muestra los canales por los que las clientas podrían llegar a FioStudio, como Instagram, TikTok, WhatsApp y recomendaciones.")
        st.image("grafico4.png", width=800)

    elif grafico_seleccionado == "Mapa interactivo":
        st.subheader("🗺️ Mapa interactivo")
        st.write("El mapa interactivo muestra una ubicación referencial de FioStudio en Lima, Perú.")

        with open("mapa.html", "r", encoding="utf-8") as f:
            html_content = f.read()

        components.html(html_content, height=600)