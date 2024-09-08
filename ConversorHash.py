import hashlib


def gerar_hash_md5(arquivotxt, hash_algo='md5'): # Essa função lê arquivo de ate 8192 bytes.
    hash_obj = hashlib.new(hash_algo)
    with open(arquivotxt,'rb') as file:
        while chunk := file.read(8192):
            hash_obj.update(chunk)
        return hash_obj.hexdigest()

arquivotxt = input(r'Digite o caminho do arquivo:')
print(f"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
           Esse é o arquivo que você quer criptografar, correto?              
            ({arquivotxt})                                     
                                                                          
                       Aqui esta o Hash md5 dele:                      
                    {gerar_hash_md5(arquivotxt)}                           
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
input('Pressione <enter> para encerrar!')