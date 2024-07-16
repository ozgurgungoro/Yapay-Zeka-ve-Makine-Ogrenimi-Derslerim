message = 'Hello There. My name is Özgür Güngör'



# message = message.upper()     #tüm mesajı büyük harf yapar
# message = message.lower()     #tüm mesajı küçük harf yapar
# message = message.title()     #her kelimenin ilk harfini büyük yapar
# message = message.capitalize()  #sadece ilk harf büyük olur
# message = message.strip()      #mesajın başındaki ve sondaki boşlukları sil

# message = message.split()      #mesajı ayrı ayrı dizilere/parçalara ayırdı 

# message = message.split('.')    # burada noktadan itibaran iki parçaya/guruba ayırmasını söyledik


# print(message)
# print(message[0])       # dizilerden parça çağırma 

# message = message.split()

# message= '---'.join(message)  # join ile parça parça olan verileri birleştirir '' içerisine aralarına hangi karakteri koyacaksanız onu ekler boşluk ta olur  


#index = message.find('Özgür')    # find bu işlem ile hangi rakamdan itibaren var olduğunu söylüyor   # eğer -1 döndürürse aranan kelimenin olmadığını bildirir

#print(index)




# isFound = message.startswith('H')
# print(isFound)  # başlangıçta H var mı diye sorar



# isFound = message.endswith('r')   #sonunda r harfi varmı diye sorduk ve true yanıtını aldık

# print(isFound)



# message = message.replace('Özgür','Değişim')  # cümle içerisindeki Özgür ü bu şekilde bulur ve değiştirir


# message = message.replace(' ','*')        # örneğin bu şekilde boşluk harflerini bulur ve onun yerine * ekler



# message = message.replace('ç','c').replace('ö','o').replace(' ','-')

message = message.center(100)


print(message)