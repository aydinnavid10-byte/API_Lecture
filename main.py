from fastapi import FastAPI, HTTPException
import pandas as pd

#create object
app = FastAPI()

#endpoint -> get data halaman utama
@app.get("/")
def handleGetData():
    # ..... ada proses yang berjalan

    return {
        "massage": "never give up, dont surrender and trust to Allah"
    }

#endpoint baru -> getdata from csv
@app.get("/data")
def handleCSV():
    # 1. Baca data daru csv
    df = pd.read_csv("mock-employees.csv")
    
    # 2. ubah dataframe menjadi json
    df = df.to_dict(orient= 'records') 

    # 3. Return json
    return {
        "data": df
    }

#endpoint -> get data by id (filter)
@app.get("/data/{id}")
def handleFilter(id: int):
        # 1. Baca data csv
        df = pd.read_csv("mock-employees.csv")

        # 2. Filter data
        df = df[ df["id"]== id]

        # 2.1 error handling -> ketika hasil filter kosong 
        # tampilkan pesan error
        if df.empty == True:
             raise HTTPException(status_code=404, detail="data tidak ditemukan!")
        
        # dalam API menggunakan Raise untuk menampilkan pesan error

        # 3. Ubah dataframe -> json
        df = df.to_dict(orient="records")
    
        # 4. return jason
        return {"data": df}