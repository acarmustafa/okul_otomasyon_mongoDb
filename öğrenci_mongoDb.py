from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
client = MongoClient("mongodb://localhost:27017/")
db=client.okul_veritabani
öğrenci_koleksiyonu = db["öğrenci"]
sınıf_koleksiyonu = db['sınıf']
hobi_koleksiyonu=db['hobi']
for öğrenci in db.öğrenci.find():
    doğum_tarihi_str = öğrenci['doğum_tarihi']
    
    if isinstance(doğum_tarihi_str, str):  
        doğum_tarihi = datetime.strptime(doğum_tarihi_str, '%Y-%m-%d')
        db.öğrenci.update_one(
            {'_id': öğrenci['_id']},
            {'$set': {'doğum_tarihi': doğum_tarihi}}
        )

    
def sınıf_ekle(isim,kat):
    sınıf= {
    'isim':isim,
    'kat':kat
    }
    result=db.sınıf.insert_one(sınıf)
    print(f'{isim} isimli sınıf başarıyla kaydedildi.Sınıf ID: {result.inserted_id}')
    return result.inserted_id

def hobi_ekle(isim):
    hobi= {
    'isim':isim
        
    }  
    db.hobi.insert_one(hobi) 
    print(f'{isim} isimli hobi başarıyla eklendi.') 
def branş_ekle(isim):
    branş={
        'isim':isim
    } 
    result=db.branş.insert_one(branş)
    print(f'{isim} isimli ders başarıyla eklendi.Branş ID:{result.inserted_id}') 
    return result.inserted_id
    
    
    
def öğrenci_ekle(isim,soyisim,doğum_tarihi,cinsiyet,telefon,sınıf_id):
    öğrenci={
        'isim':isim,
        'soyisim':soyisim,
        'doğum_tarihi':doğum_tarihi,
        'cinsiyet':cinsiyet,
        'telefon':telefon,
        'sınıf_id':sınıf_id
        
        }
    db.öğrenci.insert_one(öğrenci)
    print(f'{isim} isimli öğrenci başarıyla eklendi.')
def öğretmen_ekle(isim,soyisim,branş_id,doğum_tarihi,cinsiyet,telefon):
    öğretmen={
        'isim':isim,
        'soyisim':soyisim,
        'branş_id':branş_id,
        'doğum_tarihi':doğum_tarihi,
        'cinsiyet':cinsiyet,
        'telefon':telefon
    }  
    db.öğretmen.insert_one(öğretmen) 
    print(f'{isim} isimli öğretmen başarıyla eklendi.')
def öğrenci_getir():
    öğrenciler=db.öğrenci.find()
    for öğrenci in öğrenciler:
        print(f'isim:{öğrenci['isim']},soyisim:{öğrenci['soyisim']},doğum_tarihi:{öğrenci['doğum_tarihi']},cinsiyet:{öğrenci['cinsiyet']},telefon:{öğrenci['telefon']},sınıf_id:{öğrenci['sınıf_id']}')
def sınıf_getir():
    sınıflar=db.sınıf.find()
    for sınıf in sınıflar:
        print(f'isim:{sınıf['isim']},kat:{sınıf['kat']}')
def hobi_getir():
    hobiler=db.hobi.find()
    for hobi in hobiler:
        print(f'isim:{hobi['isim']}')
def branş_getir():
    branşlar=db.branş.find()
    for branş in branşlar:
        print(f'isim:{branş['isim']}') 
def öğretmen_getir():
    öğretmenler=db.öğretmen.find()
    for öğretmen in öğretmenler:
        print(f'isim:{öğretmen['isim']},soyisim:{öğretmen['soyisim']},branş_id:{öğretmen['branş_id']},doğum_tarihi:{öğretmen['doğum_tarihi']},cinsiyet:{öğretmen['cinsiyet']},telefon:{öğretmen['telefon']}')
def sınıf_güncelle(eski_isim,yeni_isim=None,kat=None):
    sınıf=db.sınıf.find_one({'isim':eski_isim})
    if not sınıf:
        print(f'{eski_isim} isimli sınıf bulunamadı.')
        return
    güncelleme={}
    if yeni_isim:
        güncelleme['isim']=yeni_isim
    if kat:
        güncelleme['kat']=kat 
    if güncelleme:
        db.sınıf.update_one({'_id':sınıf['_id']},{'$set':güncelleme})
        print(f'{eski_isim} isimli sınıf güncellendi.')
    else:
        print('Güncellenecek veri bulunamadı.')  
def hobi_güncelle(eski_isim,yeni_isim=None):
    hobi=db.hobi.find_one({'isim':eski_isim}) 
    if not hobi:
        print(f'{eski_isim} isimli hobi bulunamadı.')
        return
    güncelleme={}
    if yeni_isim:
        güncelleme['isim']=yeni_isim
    if güncelleme:
        db.hobi.update_one({'_id':hobi['_id']},{'$set':güncelleme})
        print(f'{eski_isim} isimli hobi güncellendi')
    else:
         print('Güncellenecek veri bulunamadı.') 
def öğrenci_güncelle(eski_isim,yeni_isim=None,soyisim=None,doğum_tarihi=None,cinsiyet=None,telefon=None,sınıf_id=None):
    öğrenci=db.öğrenci.find_one({'isim':eski_isim}) 
    if not öğrenci:
        print(f'{eski_isim} isimli öğrenci bulunamadı')
        return
    güncelleme={}
    if yeni_isim:
        güncelleme['isim']=yeni_isim
    if soyisim:
        güncelleme['soyisim']=soyisim
    if doğum_tarihi:
        güncelleme['doğum tarihi']=doğum_tarihi
    if cinsiyet:
        güncelleme['cinsiyet']=cinsiyet
    if telefon:
        güncelleme['telefon']=telefon
    if sınıf_id:
        güncelleme['sınıf_id']=sınıf_id
    if güncelleme:
        db.öğrenci.update_one({'_id':öğrenci['_id']},{'$set':güncelleme}) 
        print(f'{eski_isim} isimli öğrenci güncellendi')
def öğretmen_güncelle(eski_isim,yeni_isim=None,soyisim=None,branş_id=None,doğum_tarihi=None,cinsiyet=None,telefon=None):
    öğretmen=db.öğretmen.find_one({'isim':eski_isim}) 
    if not öğretmen:
        print(f'{eski_isim} isimli öğretmen bulunamadı')
        return
    güncelleme={}
    if yeni_isim:
        güncelleme['isim']=yeni_isim
    if soyisim:
        güncelleme['soyisim']=soyisim
    if branş_id:
        güncelleme['branş_id']=branş_id
    if doğum_tarihi:
        güncelleme['doğum_tarihi']=doğum_tarihi
    if cinsiyet:
        güncelleme['cinsiyet']=cinsiyet
    if telefon:
        güncelleme['telefon']=telefon
    if güncelleme:
        db.öğretmen.update_one({'_id':öğretmen['_id']},{'$set':güncelleme})
        print(f'{eski_isim} isimli öğretmen güncellendi')
def branş_güncelle(eski_isim,yeni_isim=None):
    branş=db.branş.find_one({'isim':eski_isim})
    if not branş:
        print(f'{eski_isim} isimli branş bulunamadı')
        return 
    güncelleme={}
    if yeni_isim:
        güncelleme['isim']=yeni_isim
    if güncelleme:
        db.branş.update_one({'_id':branş['_id']},{'$set':güncelleme}) 
        print(f'{eski_isim} isimli branş güncellendi')

def branş_sil(isim):
    branş=db.branş.find_one({'isim': isim}) 
    if not branş:
        print(f'{isim} isimli branş bulunamadı.')
        return
    db.branş.delete_one({'_id':branş['_id']})
    print(f'{isim} isimli branş başarıyla silindi')
def hobi_sil(isim):
    hobi=db.hobi.find_one({'isim':isim})
    if not hobi:
        print(f'{isim} isimli hobi bulunamadı.')
        return
    db.hobi.delete_one({'_id':hobi['_id']})
    print(f'{isim} isimli hobi başarıyla silindi') 
def öğrenci_sil(isim):
    öğrenci=db.öğrenci.find_one({'isim':isim})
    if not öğrenci:
        print(f'{isim} isimli öğrenci bulunamadı.')
        return
    db.öğrenci.delete_one({'_id':öğrenci['_id']})
    print(f'{isim} isimli öğrenci başarıyla silindi') 
def öğretmen_sil(isim):
    öğretmen=db.öğretmen.find_one({'isim':isim})
    if not öğretmen:
        print(f'{isim} isimli öğretmen bulunamadı.')
        return
    db.öğretmen.delete_one({'_id':öğretmen['_id']})
    print(f'{isim} isimli öğretmen başarıyla silindi') 
def sınıf_sil(isim):
    sınıf=db.sınıf.find_one({'isim':isim}) 
    if not sınıf:
        print(f'{isim} isimli sınıf bulunamadı.')
        return
    db.sınıf.delete_one({'_id':sınıf['_id']})
    print(f'{isim} isimli sınıf başarıyla silindi') 
def menu():
    print('Hoşgeldiniz, seçiminizi yapınız:')
    print('1- Yeni kayıt ekle')
    print('2- Kayıt Güncelleme')
    print('3- Kayıt Silme')
    print('4- Kayıt Listeleme')
    print('5 -Sınıf bilgisi ve doğum tarihi alınarak belirtilen tarihten  önce ve sonra doğanlar')
    print('6 -Ismi girilen öğrencinin hangi katta olduğu ')
    print('7 - Öğrenciye yeni hobi ekle: ')  
    print('0-  Çıkış') 
def insert_case():
    print('Öğrenci için: ')
    print('Eklemek istemiyorsanız q tuşuna basın.')
    isim = input("ISIM: ")
    if isim=='q':
        pass
    else:
        soyisim = input("SOYISIM: ")
        doğum_tarihi = input("DOGUM TARIHI (YYYY-AA-GG): ")
        cinsiyet = input("CINSIYET: ")
        telefon = input("TELEFON: ")
        sınıf_id = input("Sınıf ID: ")
        try:
            sınıf_id = ObjectId(sınıf_id)  
        except:
            print("Geçersiz Sınıf ID!")
            return
        öğrenci_ekle(isim, soyisim, doğum_tarihi, cinsiyet, telefon, sınıf_id)
    print('Branş için: ')
    print('Eklemek istemiyorsanız q tuşuna basın.')
    isim=input('Branş ismini girin: ')
    if isim=='q':
        pass    
    else:
        
        branş_ekle(isim)
    print('Öğretmen için: ')
    print('Eklemek istemiyorsanız q tuşuna basın.')
    isim=input('ISIM: ')
    if isim=='q':
        pass
    else:
        soyisim=input('SOYISIM: ')
        branş_id=input('BRANS_ID: ')
        try:
            branş_id = ObjectId(branş_id)  
        except:
            print("Geçersiz Branş ID!")
            return
        doğum_tarihi = input("DOGUM_TARIHI (YYYY-AA-GG): ")
        cinsiyet=input('CINSIYET: ')
        telefon = input("TELEFON: ")
        öğretmen_ekle(isim,soyisim,branş_id,doğum_tarihi,cinsiyet,telefon)
    print('Hobi için: ') 
    print('Eklemek istemiyorsanız q tuşuna basın.')
    isim=input('ISIM: ')
    if isim=='q':
        pass   
    else:
         hobi_ekle(isim)
    print('Sınıf için') 
    print('Eklemek istemiyorsanız q tuşuna basın.')
    isim=input('ISIM: ')
    if isim=='q':
        pass
    else:
        kat=input('KAT: ') 
        sınıf_ekle(isim,kat) 
def update_case():
    print('Öğrenci için')
    print('Güncellemek istemiyorsanız q tuşuna basın.')
    eski_isim=input('ESKI_ISIM: ')  
    if eski_isim=='q':
        pass
    else:
        isim=input('ISIM: ')
        soyisim=input('SOYISIM: ') 
        doğum_tarihi=input('DOĞUM TARIHI: ')
        cinsiyet= input('CINSIYET: ')
        telefon=input('TELEFON: ')
        sınıf_id=input('SINIF_ID: ')
        sınıf_id = ObjectId(sınıf_id) if sınıf_id != 'q' else None
        öğrenci_güncelle(eski_isim,isim,soyisim,doğum_tarihi,cinsiyet,telefon,sınıf_id)
    print('Sınıf için')
    print('Güncellemek istemiyorsanız q tuşuna basın.')
    eski_isim=input('ESKI_ISIM: ') 
    if eski_isim=='q':
        pass
    else:
        isim=input('ISIM: ')
        kat=input('KAT: ')  
        sınıf_güncelle(eski_isim,isim,kat)
    print('Branş için')
    print('Güncellemek istemiyorsanız q tuşuna basın.')
    eski_isim=input('ESKI_ISIM: ')  
    if eski_isim=='q':
        pass
    else:
        isim=input('ISIM: ') 
        branş_güncelle(eski_isim,isim)
    print('Hobi için')
    print('Güncellemek istemiyorsanız q tuşuna basın.')
    eski_isim=input('ESKI_ISIM: ')
    if eski_isim=='q':
        pass
    else: 
        isim=input('ISIM: ')  
        hobi_güncelle(eski_isim,isim) 
    print('Öğretmen için')
    print('Güncellemek istemiyorsanız q tuşuna basın.')
    eski_isim=input('ESKI_ISIM: ')
    if eski_isim=='q':
        pass
    else:
        isim=input('ISIM: ') 
        soyisim=input('SOYISIM: ')
        branş_id=input('BRANS_ID: ') 
        doğum_tarihi=input('DOGUM_TARIHI: ')
        cinsiyet=input('CINSIYET: ')
        telefon=input('TELEFON: ')
        branş_id = ObjectId(branş_id) if branş_id != 'q' else None
        öğretmen_güncelle(eski_isim,isim,soyisim,branş_id,doğum_tarihi,cinsiyet,telefon) 
def delete_case(): 
    print('Öğrenci için: ')
    print('Silmek istemiyorsanız q tuşuna basın.')
    isim = input("ISIM: ") 
    if isim=='q':
        pass 
    else:
        öğrenci_sil(isim)
    print('Sınıf için: ')
    print('Silmek istemiyorsanız q tuşuna basın.')
    isim = input("ISIM: ") 
    if isim=='q':
        pass
    else:
        sınıf_sil(isim)
    print('Branş için: ')
    print('Silmek istemiyorsanız q tuşuna basın.')
    isim = input("ISIM: ") 
    if isim=='q':
        pass 
    else:
        branş_sil(isim)
    print('Hobi için: ')
    print('Silmek istemiyorsanız q tuşuna basın.')
    isim = input("ISIM: ") 
    if isim=='q':
        pass
    else:
        hobi_sil(isim)  
    print('Öğretmen için: ')
    print('Silmek istemiyorsanız q tuşuna basın.')
    isim = input("ISIM: ") 
    if isim=='q':
        pass
    else:
        öğretmen_sil(isim) 
def list_case():
    def listele(koleksiyon_adı):
        koleksiyon=db[koleksiyon_adı]
        kayıtlar = koleksiyon.find()
        if koleksiyon.count_documents({}) == 0:
            print(f'{koleksiyon_adı} bulunamadı.')
            return
        for kayıt in kayıtlar:
            print(f"{koleksiyon_adı.capitalize()} ID: {str(kayıt['_id'])}")
            del kayıt['_id']
            print(kayıt)
            print('-' * 30)
    
    listele('öğrenci')
    listele('sınıf')
    listele('branş')
    listele('hobi')
    listele('öğretmen')

      
            
def filter_by_class_and_birth():
    sınıf_id = input("Sınıf ID'sini girin: ")
    doğum_tarihi_str = input("Doğum tarihini girin (YYYY-AA-GG): ")

    try:
        sınıf_id = ObjectId(sınıf_id)
    except Exception as e:
        print("Geçersiz Sınıf ID'si girdiniz.")
        exit()

    
    doğum_tarihi = datetime.strptime(doğum_tarihi_str, '%Y-%m-%d')

    sonuçlar_öncesi = list(db.öğrenci.find({
        "sınıf_id": sınıf_id,
        "doğum_tarihi": {"$lt": doğum_tarihi}
    }))

    sonuçlar_sonrası = list(db.öğrenci.find({
        "sınıf_id": sınıf_id,
        "doğum_tarihi": {"$gte": doğum_tarihi}
    }))

    if not sonuçlar_öncesi and not sonuçlar_sonrası:
        print("Belirtilen sınıf ve doğum tarihi kriterlerine uyan öğrenci bulunamadı.")
    else:
        print("Belirtilen sınıfta belirtilen tarihten önce doğan öğrenciler:")
        for öğrenci in sonuçlar_öncesi:
            print(öğrenci)
        print("Belirtilen sınıfta belirtilen tarihten sonra doğan öğrenciler:")
        for öğrenci in sonuçlar_sonrası:
            print(öğrenci)
def find_floor():
    isim = input("Öğrencinin ismini girin: ")
    öğrenci=öğrenci_koleksiyonu.find_one({'isim':isim})
    if öğrenci is None:
        print('Belirtilen isimde öğrenci bulunamadı.')
        return
    sınıf_id=öğrenci.get('sınıf_id')
    if sınıf_id is None:
        print('öğrencinin sınıf bilgisi bulunamadı.') 
        return 
    sınıf= sınıf_koleksiyonu.find_one({'_id':sınıf_id}) 
    if sınıf is None:
        print('öğrencinin sınıf bilgisi bulunamadı.')
        return
    kat=sınıf.get('kat')
    print(f"{isim} isimli öğrenci {kat} katta yer alıyor.")
def add_hobbies_to_student(): 
    öğrenci_id=input('öğrenci id girin: ')
    hobi=input('Ekelemek istediğin hobiyi gir: ')
    try:
        öğrenci_id=ObjectId(öğrenci_id)
    except Exception as e:
        print("Geçersiz Öğrenci ID'si girdiniz.")
        return
    öğrenci=öğrenci_koleksiyonu.find_one({'_id':öğrenci_id})  
    if öğrenci is None:
        print("Belirtilen id'ye sahip öğrenci bulunamadı.") 
        return
    mevcut_hobiler=öğrenci.get('hobiler',[])    
    if hobi not in mevcut_hobiler:
        mevcut_hobiler.append(hobi)
    else:
        print("Bu hobi zaten mevcut.")
        return

    
    result = öğrenci_koleksiyonu.update_one(
        {'_id': öğrenci_id},
        {'$set': {'hobiler': mevcut_hobiler}}
    )

    if result.modified_count > 0:
        print(f"{öğrenci_id} ID'li öğrenciye '{hobi}' hobisi başarıyla eklendi.")
    else:
        print("Hobi ekleme işlemi başarısız oldu.")    
    
    
    
    
    
    
    



switch={
    '1':insert_case,
    '2':update_case,
    '3':delete_case,
    '4':list_case,
    '5':filter_by_class_and_birth,
    '6':find_floor,
    '7':add_hobbies_to_student
    
}
    
while True:
    
    menu()
    seçim = input("Lütfen seçiminizi yapın: ")
    
    
    action = switch.get(seçim)
    if action:
        if seçim == '0':  
            if not action():
                break
        else:
            action()
    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.")
       



       
          
          
    
                       
        
            
      
                                                                  
                              
          
                                            
        
       