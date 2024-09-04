import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# decorador
@app.get('/')
def get_list():
    return[1, 2, 3]

@app.get('/contact')
def get_list():
    return {'name': 'Platzi'}

@app.get('/home', response_class=HTMLResponse)
def get_list():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Juegos Paralímpicos 2024</title>
        <!-- Favicon -->
        <link rel="icon" href="https://upload.wikimedia.org/wikipedia/commons/9/94/Paralympic_Agitos_logo.svg" type="image/svg+xml">
    </head>
    <body>
        <h1 style="text-align: center; color: #2e8b57; font-family: Arial, sans-serif; margin-top: 20px;">
            Juegos Paralímpicos 2024
        </h1>

        <!-- Descripción introductoria -->
        <p style="text-align: center; font-size: 18px; color: #555; font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
            Únete a la celebración del deporte, la inclusión y la excelencia. Los Juegos Paralímpicos 2024 reúnen a atletas de todo el mundo para demostrar que no hay límites para el espíritu humano.
        </p>

        <!-- Sección de imagen destacada -->
        <div style="text-align: center; margin: 30px 0;">
            <img src="https://i.pinimg.com/1200x/06/7a/af/067aaf6172e95b06aa0a5e870bc814e1.jpg" alt="Juegos Paralímpicos" style="width: 80%; max-width: 600px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);">
        </div>

        <!-- Sección de eventos destacados -->
        <h2 style="text-align: center; color: #2e8b57; font-family: Arial, sans-serif; margin-top: 40px;">
            Eventos Destacados
        </h2>
        <ul style="list-style: none; padding: 0; max-width: 600px; margin: 20px auto; font-family: Arial, sans-serif; font-size: 18px; color: #333;">
            <li style="margin: 10px 0; text-align: center;">Atletismo</li>
            <li style="margin: 10px 0; text-align: center;">Natación</li>
            <li style="margin: 10px 0; text-align: center;">Baloncesto en silla de ruedas</li>
            <li style="margin: 10px 0; text-align: center;">Esgrima</li>
            <li style="margin: 10px 0; text-align: center;">Levantamiento de pesas</li>
        </ul>

        <!-- Sección de llamada a la acción -->
        <div style="text-align: center; margin: 40px 0;">
            <a href="register.html" style="background-color: #2e8b57; color: white; padding: 15px 30px; text-decoration: none; border-radius: 5px; font-family: Arial, sans-serif; font-size: 18px;">
                Regístrate Ahora
            </a>
        </div>

        <!-- Sección de patrocinadores -->
        <h2 style="text-align: center; color: #2e8b57; font-family: Arial, sans-serif; margin-top: 40px;">
            Patrocinadores Oficiales
        </h2>
        <div style="display: flex; justify-content: center; align-items: center; gap: 20px; margin: 30px 0;">
            <img src="https://i.pinimg.com/736x/73/24/da/7324daee0903190950b8aa7ad2edbf2d.jpg" alt="Patrocinador 1" style="width: 100px;">
            <img src="https://i.pinimg.com/originals/d0/e3/5b/d0e35bb963d24f5339725f61cca9cda1.jpg" alt="Patrocinador 2" style="width: 100px;">
            <img src="https://i.pinimg.com/736x/ac/e7/bf/ace7bfe29e0f3550ee305b52d490576f.jpg" alt="Patrocinador 3" style="width: 100px;">
        </div>

        <!-- Información de contacto -->
        <p style="text-align: center; font-size: 16px; color: #777; font-family: Arial, sans-serif;">
            Para más información, contáctanos en <a href="mailto:info@paralympics2024.com" style="color: #2e8b57; text-decoration: none;">info@paralympics2024.com</a>
        </p>
    </body>
    </html>
    """


def run():
    store.get_categories()
    
if __name__ == '__main__':
    run()