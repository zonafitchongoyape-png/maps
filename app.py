from flask import Flask, render_template, request, jsonify
import pandas as pd
import folium
from folium import plugins

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        file = request.files['file']
        df = pd.read_excel(file)
        
        locations = []
        for idx, row in df.iterrows():
            try:
                desc = str(row[df.columns[0]])
                coords = str(row[df.columns[1]]).replace(' ', '').split(',')
                lat = float(coords[0])
                lng = float(coords[1])
                locations.append({'descripcion': desc, 'lat': lat, 'lng': lng})
            except:
                continue
        
        if not locations:
            return jsonify({'error': 'No se encontraron ubicaciones válidas'}), 400
        
        center_lat = sum(l['lat'] for l in locations) / len(locations)
        center_lng = sum(l['lng'] for l in locations) / len(locations)
        
        # Crear mapa con ambas opciones
        m = folium.Map(
            location=[center_lat, center_lng], 
            zoom_start=15,
            tiles=None,  # No usar tiles por defecto
            width='100%',
            height='100%'
        )
        
        # OPCIÓN 1: Vista Satélite (Google Earth Style) - PREDETERMINADA
        folium.TileLayer(
            tiles='https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
            attr='Google',
            name='🛰️ Vista Satélite (Google Earth)',
            overlay=False,
            control=True
        ).add_to(m)
        
        # OPCIÓN 2: Mapa de Calles (OpenStreetMap)
        folium.TileLayer(
            'OpenStreetMap',
            name='🗺️ Mapa de Calles',
            overlay=False,
            control=True
        ).add_to(m)
        
        # Control de capas (selector)
        folium.LayerControl(position='topright', collapsed=False).add_to(m)
        
        # Plugin de pantalla completa
        plugins.Fullscreen(
            position='topleft',
            title='Pantalla completa',
            title_cancel='Salir',
            force_separate_button=True
        ).add_to(m)
        
        # Agregar marcadores rojos
        for loc in locations:
            popup_html = f"""
            <div style='font-family: Arial; padding: 14px; min-width: 260px;'>
                <h3 style='margin: 0 0 12px 0; color: #1976D2; font-size: 17px; 
                           border-bottom: 2px solid #1976D2; padding-bottom: 8px;'>
                    📍 {loc['descripcion']}
                </h3>
                <div style='background: #f5f5f5; padding: 10px; border-radius: 6px; margin: 10px 0;'>
                    <p style='margin: 6px 0; font-size: 13px;'><b>📐 Latitud:</b> {loc['lat']:.6f}</p>
                    <p style='margin: 6px 0; font-size: 13px;'><b>📐 Longitud:</b> {loc['lng']:.6f}</p>
                </div>
                <a href='https://www.google.com/maps?q={loc['lat']},{loc['lng']}' 
                   target='_blank' 
                   style='display: block; text-align: center; margin: 8px 0; padding: 10px; 
                          background: #4CAF50; color: white; text-decoration: none; 
                          border-radius: 6px; font-size: 14px; font-weight: bold;'>
                    🌐 Abrir en Google Maps
                </a>
                <a href='https://earth.google.com/web/search/{loc['lat']},{loc['lng']}' 
                   target='_blank' 
                   style='display: block; text-align: center; margin: 8px 0; padding: 10px; 
                          background: #2196F3; color: white; text-decoration: none; 
                          border-radius: 6px; font-size: 14px; font-weight: bold;'>
                    🌍 Ver en Google Earth
                </a>
            </div>
            """
            
            folium.Marker(
                [loc['lat'], loc['lng']],
                popup=folium.Popup(popup_html, max_width=320),
                tooltip=f"<b>{loc['descripcion']}</b>",
                icon=folium.Icon(color='red', icon='home', prefix='fa')
            ).add_to(m)
        
        map_html = m._repr_html_()
        return jsonify({'success': True, 'map_html': map_html, 'count': len(locations)})
        
    except Exception as e:
        return jsonify({'error': f'Error: {str(e)}'}), 400

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 SERVIDOR INICIADO - VISOR DE UBICACIONES")
    print("=" * 60)
    print("📍 Abre tu navegador en: http://localhost:5000")
    print("⌨️  Presiona Ctrl+C para detener el servidor")
    print("=" * 60)
    app.run(debug=True, port=5000, host='0.0.0.0')