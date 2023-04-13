# Request in python
import requests

username = input('Digite seu usuário do GitHub: ')

response = requests.get('https://api.github.com/users/' +
                        username + '/repos', timeout=50)
print(response.status_code)

print('\n ----------- Repositórios ----------- \n')
for repo in response.json():
    print('\n')
    print('Nome: ', repo['name'])
    print('Descrição: ', repo['description'])
    print('Linguagem: ', repo['language'])
    print('URL: ', repo['html_url'])
    print('Criado em: ', repo['created_at'])
    print('Última atualização: ', repo['updated_at'])
    print('Tamanho: ', repo['size'])
    print('Forks: ', repo['forks'])
    print('Stars: ', repo['stargazers_count'])
    print('Watchers: ', repo['watchers'])
    print('\n')


# To use python with a REST API, you need to use frameworks like Flask, Django, Bottle, etc.

# here has a error because  0.0001 + 0.0001 + 0.0001 = 0.00030000000000000003
# this ocurred because the float number is not precise in python
TEST = 0.0003 == 0.0001 + 0.0001 + 0.0001
print(TEST) # False

# to solve this problem, we can use the Decimal class from the decimal module
from decimal import Decimal

TEST = Decimal('0.0003') == Decimal('0.0001') + Decimal('0.0001') + Decimal('0.0001')
print(TEST) # True