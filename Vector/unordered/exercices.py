# Inserir um novo jogador no vetor
# Inserindo ao final do vetor
# Em cada celula vaga do vetor
# Podemos definir um tamanho fixo para quantos elementos podem ser armazenados.
# O algoritmo ja sabe qual e ultima posição do vetor pois ele ja sabe quem e o ultimo item e seu tamanho
# Big - O e O (1)
#
#
# Pesquisa Linear no vetor
# Percorrer cada posição do vetor
# Verificar item por item
# Melhor caso e se encontrar na primeira verificação ai e O(`1`)
# Pior caso e se o item procurado estiver na ultima posição ou caso ele não encontre vai ter que ser na ultima posição
# Em media metade dos itens devem ser examinados
# Big - O - O (n)
#
#
# Excluir
# Precisamos excluir ele do vetor apagar
# Isso que dizer que substituimos aquele valor por seu proximo valor
# Logo em seguida tambem significa que
# Vamos ter que fazer isso com todos apos essa posição que foi excluida
# Remanejar as posições apos aquele vetor
# Big O(n) + O(n)
# Depende - se de quantos tem e de quantos precisam mudar de lugar
# Para pesquisar e para remanejar
#
#
#
# Você deve decidir se item com as chaves duplicadas serão ou nao permitidas
# Por exemplo se a chave for ou não um registro
# Um unico registro no caso
# So aceita duplicadas dependendo se a chave for unica
# Pesquisa mesmo se encontrar o valor o algoritmo vai ter que continuar pesquisando ate a ultima celula
# Se nao permitir vai ter que ficar andando todo vetor pois ele pode encontrar outros
# Caso nao permita na primeira vez que econtrar nao precisa ficar andando novamente toda vez
# Inserção caso nao permita que seja duplicados você vai precisar fazer a verificação em toda nova inserção
# Exlcusão se matem da mesma forma.
# Agora se você permitir duplicados voce pode verificar (n) celulas e mais de (n/2)
# Para cada celula que for encontrada
