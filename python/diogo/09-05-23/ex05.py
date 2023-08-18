initialValue = 50
value = initialValue

# like this post = value * 2
# follow facebook = value * 3
# in whatsapp = value * 4
# follow twitter = value * 2
# retweet = value * 3

likeFacebook = input("Curtiu a página do Facebook? (s/n) ")
followFacebook = input("Seguiu a página do Facebook? (s/n) ")
inWhatsapp = input("Entrou no grupo do Whatsapp? (s/n) ")
followTwitter = input("Seguiu a página do Twitter? (s/n) ")
retweet = input("Retweetou a página do Twitter? (s/n) ")

if likeFacebook == "s" or likeFacebook == "S":
    value = value * 2

if followFacebook == "s" or followFacebook == "S":
    value = value * 3

if inWhatsapp == "s" or inWhatsapp == "S":
    value = value * 4

if followTwitter == "s" or followTwitter == "S":
    value = value * 2

if retweet == "s" or retweet == "S":
    value = value * 3
    
print('Valor a ser pago: R$ ' + str(value) + ', caso cumprisse todas as tarefas receberia ' + str(initialValue * 144))