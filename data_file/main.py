from fastapi import File, UploadFile
from fastapi.responses import FileResponse

#upload image
@app.post("/uploadimage")
def upload(file: UploadFile = File(...)):
    try:
        print("mulai upload")
        print(file.filename)
        contents = file.file.read()
        with open("./data_file/"+file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "Error upload file"}
    finally:
        file.file.close()
        return {"message": "Upload berhasil: {file.filename}"}
# ambil image berdasarkan nama file
@app.get("/getimage/{nama_file}")
async def getImage(nama_file:str):
        return FileResponse("./data_file/"+nama_file)