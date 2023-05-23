import requests
def ReqBody(input_user):
    url= "https://httpbin.org/post"
    nama="Hary Nugroho"
    email="harynugroho93@gmail.com"
    alamat="terminal ledeng"
    Input_MyData={
                "nama":"Hary Nugroho",
                "email":"harynugroho93@gmail",
                "alamat":"terminal ledeng"
                }
    response=requests.post(url, json=Input_MyData).json()
    # kalau ngambil lewat data isinya string jadi harus slicing
    data=response['data'][1:23]
    #lebih mudah ambil data lewat json
    get_data=response['json']
    #
    result=get_data[input_user]

    print(response)
    print (data)
    print(get_data)
    # (f) digunakan untuk memasukkan suatu variable ke dalam string 
    print(f"Hasil : {result}")
ReqBody("nama")