# OnlyDucky MVP 🦆

Prototipo funcional de una red de expertos virtuales especializados.

## Ejecutar en VS Code (Windows)

1. Descomprime la carpeta y ábrela en VS Code.
2. Abre **Terminal > New Terminal**.
3. Crea un entorno virtual:
   ```powershell
   py -m venv venv
   ```
4. Actívalo:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
5. Instala dependencias:
   ```powershell
   pip install -r requirements.txt
   ```
6. Ejecuta:
   ```powershell
   python app.py
   ```
7. Abre `http://127.0.0.1:5000`.

## Qué incluye
- Home/feed profesional responsive.
- 4 expertos: DuckyDev, DuckySys, CyberDucky y DataDucky.
- Perfiles individuales.
- Posts, tags, seguidores, empleo y recursos simulados.
- Chat funcional por perfil mediante endpoint Flask.
- Chat local simulado, preparado para sustituir por LLM + RAG.
- Vista Explorar.
- Diseño responsive móvil/escritorio.

## Siguiente fase recomendada
- PostgreSQL + modelos User/DuckyProfile/Post/Follow/Conversation/Message.
- Login/registro.
- API de LLM.
- RAG con pgvector y fuentes autorizadas/propias.
- Panel de administración editorial.
- Profesionales humanos verificados y escalado de consultas.
- Sistema de suscripción y límites de uso.

> Los perfiles IA deben mostrarse siempre como virtuales. Para producción, revisa derechos de marca/diseño y no clones de forma literal interfaces o identidad visual de terceros.
