from flask import Flask, render_template, Response

app = Flask(__name__)




# def gen(video):     
#     yield (b'--frame\r\n'
#             b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')    


@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/view_batch_id/<int:batch_id>')
# def video_stream(batch_id: int):
#     global video
#     return Response(gen(video),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')
    










if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)