# Visor de Ubicaciones

Proyecto Flask que permite subir un Excel con dos columnas (`DESCRIPCION`, `COORDENADAS`) y mostrar las ubicaciones en un mapa (Leaflet/Folium).

Archivos importantes
- `app.py` — aplicación Flask
- `templates/index.html` — interfaz web
- `requirements.txt` — dependencias
- `Procfile` — comando para ejecutar en Render/Heroku

Instalación local (Windows - cmd.exe)

1. Crear y activar un virtualenv (recomendado):

```cmd
python -m venv venv
venv\Scripts\activate
```

2. Instalar dependencias:

```cmd
pip install -r requirements.txt
```

3. Ejecutar localmente:

```cmd
python app.py
```

Abrir `http://localhost:5000` en el navegador.

Subir a GitHub (comandos):

```cmd
cd c:\xampp\htdocs\maps
git init
git add .
git commit -m "Initial commit - Visor de Ubicaciones"
# Crear repo en GitHub (usa la web o la CLI 'gh')
# Con la CLI (opcional):
# gh repo create <usuario>/<repo> --public --source=. --remote=origin
git remote add origin https://github.com/<TU_USUARIO>/<TU_REPO>.git
git branch -M main
git push -u origin main
```

Desplegar en Render

1. Crear una cuenta en https://render.com e iniciar sesión.
2. Crear un nuevo *Web Service* y conectar tu cuenta de GitHub.
3. Seleccionar el repo que subiste.
4. En *Build Command* deja vacío o `pip install -r requirements.txt` (Render detecta Python).
5. En *Start Command* usa:

```
gunicorn app:app
```

6. Desplegar; Render hará build y arrancará el servicio.

Notas
- Si prefieres mantener `index.html` fuera de `templates/`, ajusta `app.py` a `send_from_directory`.
- Asegúrate de que tu Excel tenga exactamente las columnas `DESCRIPCION` y `COORDENADAS`.
- Si ves errores de HTML en la respuesta ("Unexpected token '<'"), revisa la consola del servidor para ver el stack trace.

Si quieres, puedo:
- Generar un repo remoto con la API de GitHub (necesitaré un token tuyo si quieres que yo lo haga), o
- Generar los comandos `gh` y/o GUI paso a paso para que lo ejecutes.
