import hashlib


def gerar_hash(arquivotxt, hash_algo='md5'):
    hash_obj = hashlib.new(hash_algo)
    with open(arquivotxt, 'rb') as file:
        while chunk := file.read(8192):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()


algoritmos_disponiveis = hashlib.algorithms_available
print(f"Algoritmos de hash disponíveis: {', '.join(algoritmos_disponiveis)}")

arquivotxt = input(r'Digite o caminho do arquivo:')
hash_algo = input(f"Digite o algoritmo de hash desejado (padrão é 'md5'): ") or 'md5'

if hash_algo not in algoritmos_disponiveis:
    print(f"Algoritmo {hash_algo} não é suportado. Usando 'md5' como padrão.")
    hash_algo = 'md5'

hash_result = gerar_hash(arquivotxt, hash_algo)
msg1 = "Esse é o arquivo que você quer criptografar, correto?"
arquivo_msg = f"({arquivotxt})"
hash_msg1 = f"Aqui está o Hash {hash_algo} do arquivo:"
hash_msg2 = f"{hash_result}"

print(f"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{msg1.center(120)}              
{arquivo_msg.center(120)}                                     

{hash_msg1.center(120)}
{hash_msg2.center(120)}                      
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
input('Pressione <enter> para encerrar!')
