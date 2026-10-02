from flask import Flask, render_template, jsonify, request, abort

app = Flask(__name__)

DUCKS = {
    "duckydev": {
        "name": "DuckyDev", "handle": "@duckydev", "role": "Full Stack Developer",
        "emoji": "💻", "avatar": "duckydev.png", "cover": "Code • APIs • Web", "followers": "12.4K",
        "bio": "Convierto café en APIs. Python, Django, JavaScript, React y arquitectura web explicados sin humo.",
        "tags": ["Python", "Django", "React", "APIs"], "accent": "dev",
        "welcome": "¡Cuac! Soy DuckyDev. Pregúntame sobre Python, Django, APIs, JavaScript o React.", "quote":"Código claro, proyectos reales y cero humo.", "focus":[("Construye","APIs y web"),("Aprende","con proyectos"),("Mejora","tu código")], "cover_icon":"</>"
    },
    "duckysys": {
        "name": "DuckySys", "handle": "@duckysys", "role": "Systems & DevOps",
        "emoji": "⚙️", "avatar": "duckysys.png", "cover": "Linux • Docker • Cloud", "followers": "8.9K",
        "bio": "Servidores tranquilos, despliegues repetibles. Linux, Docker, redes, CI/CD y cloud.",
        "tags": ["Linux", "Docker", "AWS", "CI/CD"], "accent": "sys",
        "welcome": "Soy DuckySys. Puedo ayudarte con Linux, Docker, redes, despliegues y cloud.", "quote":"Automatiza lo repetible; entiende lo importante.", "focus":[("Opera","Linux y redes"),("Despliega","Docker y CI/CD"),("Escala","cloud")], "cover_icon":"⚙"
    },
    "cyberducky": {
        "name": "CyberDucky", "handle": "@cyberducky", "role": "Cybersecurity Mentor",
        "emoji": "🛡️", "avatar": "cyberducky.png", "cover": "Security • OWASP • Defense", "followers": "10.1K",
        "bio": "Aprende seguridad defensiva, desarrollo seguro y OWASP con ejemplos responsables.",
        "tags": ["OWASP", "AppSec", "Networks", "Security"], "accent": "cyber",
        "welcome": "Soy CyberDucky. Pregúntame sobre seguridad defensiva, OWASP o desarrollo seguro.", "quote":"Piensa como atacante; construye como defensor.", "focus":[("Detecta","riesgos"),("Protege","aplicaciones"),("Aprende","OWASP")], "cover_icon":"🛡"
    },
    "dataducky": {
        "name": "DataDucky", "handle": "@dataducky", "role": "Data & AI Scientist",
        "emoji": "📊", "avatar": "dataducky.png", "cover": "Data • ML • AI", "followers": "11.7K",
        "bio": "Datos que cuentan historias. Python, SQL, machine learning e IA explicados paso a paso.",
        "tags": ["Python", "SQL", "ML", "AI"], "accent": "data",
        "welcome": "Soy DataDucky. Podemos hablar de Python, SQL, machine learning, datos e IA.", "quote":"De datos dispersos a decisiones que tienen sentido.", "focus":[("Explora","datos"),("Modela","ML e IA"),("Explica","resultados")], "cover_icon":"▥"
    },
}

POSTS = [
    {"duck":"duckydev", "type":"tutorial", "title":"Django REST Framework: serializers sin misterio", "text":"Un serializer transforma objetos complejos en datos que una API puede enviar y valida lo que recibe. Te lo explico con un ejemplo de 5 minutos.", "meta":"8 min · Tutorial", "likes":842, "comments":63},
    {"duck":"duckysys", "type":"guide", "title":"Docker Compose para tu primer proyecto real", "text":"App + PostgreSQL + variables de entorno. Esta es la estructura mínima que usaría para un proyecto de clase que luego quieras desplegar.", "meta":"12 min · Guía", "likes":691, "comments":41},
    {"duck":"dataducky", "type":"news", "title":"No memorices ML: aprende a formular el problema", "text":"Antes de elegir un modelo, define variable objetivo, métrica, baseline y cómo evitarás leakage. El algoritmo viene después.", "meta":"5 min · Data Note", "likes":1103, "comments":88},
    {"duck":"cyberducky", "type":"security", "title":"5 errores de seguridad que aparecen en proyectos junior", "text":"Secretos en Git, validación insuficiente, permisos demasiado amplios, dependencias olvidadas y mensajes de error que revelan demasiado.", "meta":"7 min · Security", "likes":974, "comments":72},
    {"duck":"duckydev", "type":"job", "title":"Radar de empleo: Junior Backend / Python", "text":"Cómo leer una oferta sin descartarte por no cumplir el 100% y qué proyectos enseñar para demostrar APIs, SQL, Git y Docker.", "meta":"Empleo · Career", "likes":524, "comments":37},
]

RESPONSES = {
    "duckydev": "Te lo explicaría como developer: empieza por separar el problema en entrada, lógica y salida. Si me das el código o el error concreto, puedo guiarte paso a paso.",
    "duckysys": "Desde sistemas miraría primero entorno, logs, puertos, variables y dependencias. Cuéntame qué estás ejecutando y qué mensaje aparece.",
    "cyberducky": "Lo analizaría desde una perspectiva defensiva: superficie de ataque, validación, permisos y exposición de datos. Puedo ayudarte a revisar el diseño de forma segura.",
    "dataducky": "Primero definiría qué quieres predecir o medir, qué datos tienes y cómo evaluarás el resultado. Con eso podemos elegir un enfoque razonable.",
}

@app.route('/')
def home():
    return render_template('index.html', ducks=DUCKS, posts=POSTS)

@app.route('/duck/<slug>')
def profile(slug):
    duck = DUCKS.get(slug)
    if not duck: abort(404)
    posts = [p for p in POSTS if p['duck'] == slug]
    return render_template('profile.html', duck=duck, slug=slug, posts=posts, ducks=DUCKS)

@app.post('/api/chat/<slug>')
def chat(slug):
    if slug not in DUCKS: abort(404)
    message = (request.json or {}).get('message', '').strip()
    if not message:
        return jsonify({"error":"Escribe una pregunta"}), 400
    return jsonify({"reply": RESPONSES[slug] + "\n\n🧠 Demo local: conecta aquí tu proveedor LLM + RAG para respuestas reales."})

@app.route('/explore')
def explore():
    return render_template('explore.html', ducks=DUCKS)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
