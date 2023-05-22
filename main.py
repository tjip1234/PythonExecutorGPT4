import json
import asyncio
import pyimgbox
import quart
import quart_cors
from quart import request
import os
import re
app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

async def upload_image_and_print_url(image):
    async with pyimgbox.Gallery() as gallery:
        image_path = "temp_image.png"
        image.savefig(image_path)
        submission = gallery.upload(image_path)
        if submission['success']:
            image_url = submission['image_url']
            print("Generated Plot:", image_url)
        else:
            print("Image upload failed. Error:", submission['error'])
        if os.path.exists(image_path):
            os.remove(image_path)

@app.get("/logo.png")
async def plugin_logo():
    filename = 'logo.png'
    return await quart.send_file(filename, mimetype='image/png')

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.headers['Host']
    with open(".well-known/ai-plugin.json") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/json")

@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    with open("openapi.yaml") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/yaml")
async def process_code(code):
    import io
    import sys
    #code = re.sub(r"plt\.show\(\)", lambda _: asyncio.run(upload_image_and_print_url(fig)), code)
    #code = re.sub(r"plt\.savefig\((.*?)\)", lambda _: asyncio.run(upload_image_and_print_url(fig)), code)
    output = io.StringIO()
    sys.stdout = output
    await asyncio.get_running_loop().run_in_executor(None, exec, code)
    sys.stdout = sys.__stdout__
    output_data = {'output': output.getvalue().strip()}
    print(output_data)
    return output_data

@app.route("/execute", methods=["POST"])
async def execute_code():
    request_data = await request.get_json(force=True)
    code = request_data["code"]
    output_data = await process_code(code)
    try:
        return quart.Response(response=json.dumps(output_data), mimetype="application/json")
    except Exception as e:
        return quart.Response(response=str(e), status=500, mimetype="text/plain")


def main():
    app.run(debug=True, host="0.0.0.0", port=5003)

def mains():
    asyncio.run(main())

if __name__ == "__main__":
    mains()
