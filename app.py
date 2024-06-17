import os
from flask import Flask, render_template, request, make_response, redirect
from flask import send_from_directory

app = Flask(__name__)

# Define the sound_permission_check function
def sound_permission_check():
    # Check if the 'sound_permission' cookie is set to 'true'
    if request.cookies.get('sound_permission') == 'true':
        return True
    else:
        return False

# Set the main static folder
app.static_folder = 'static'

# Add Jambo folder as a separate static folder
app.config['JAMBO_FOLDER'] = 'Jambo'

@app.route('/')
def index():
    return render_template('index.html', sound_permission_check=sound_permission_check)

@app.route('/set_sound_permission')
def set_sound_permission():
    # Set the 'sound_permission' cookie to 'true' within the application context
    with app.app_context():
        response = make_response(redirect('/'))
        response.set_cookie('sound_permission', 'true')
        response.set_cookie("auto_play", 'true')
        return response

@app.route('/view_archive')
def view_archive():
    # Get the path to the directory containing the images
    image_dir = os.path.join(app.root_path, 'Jambo')

    # Get a list of all image files in the directory
    images = [f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    
    return render_template('archive.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)
