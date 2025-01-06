# Sistema Bancário em Python

Este projeto implementa um sistema bancário simples utilizando Python, com funcionalidades essenciais como cadastro de clientes, débito, depósito, transferência entre contas, visualização de extratos, exclusão de clientes e junção de contas. O sistema armazena dados em arquivos de texto (`.txt`) para persistência de informações e utiliza dicionários para manipulação dos dados de clientes.

## Funcionalidades

### 1. **Novo Cliente**
   - Permite o cadastro de um novo cliente com as seguintes informações:
     - Nome
     - CPF
     - Tipo de Conta (Comum ou Plus)
     - Saldo Inicial
     - Senha
   - Caso o CPF já esteja cadastrado, o cliente não será adicionado.

### 2. **Apagar Cliente**
   - Permite a exclusão de um cliente já cadastrado. O sistema remove o cliente tanto da lista de clientes quanto da lista de extratos.

### 3. **Listar Clientes**
   - Exibe a lista completa de clientes cadastrados no sistema.

### 4. **Débito**
   - Realiza um débito na conta do cliente.
   - Dependendo do tipo de conta (Comum ou Plus), o débito pode ter uma tarifa (5% para contas comuns e 3% para contas Plus).
   - Verifica se o saldo do cliente é suficiente para o débito.
   - Caso o saldo após a operação seja inferior ao limite permitido (R$-1000 para contas Comum e R$-5000 para contas Plus), a operação é cancelada.

### 5. **Depósito**
   - Realiza um depósito na conta do cliente.
   - O valor depositado é adicionado ao saldo da conta e a transação é registrada no extrato do cliente.

### 6. **Extrato**
   - Exibe o extrato completo de um cliente, incluindo todas as transações realizadas (débitos e depósitos) e os respectivos saldos após cada operação.
   - As transações são registradas com data, valor e tarifa aplicada.

### 7. **Transferência entre Contas**
   - Permite a transferência de um valor entre duas contas de clientes.
   - Verifica se o cliente remetente tem saldo suficiente para realizar a operação.
   - O valor transferido é subtraído do saldo do remetente e adicionado ao saldo do destinatário, e ambas as contas têm suas transações registradas no extrato.

### 8. **Junção de Contas**
   - Permite a junção de duas contas em uma única conta (escolhendo qual conta será a principal).
   - A conta principal recebe o saldo da conta secundária e a conta secundária é excluída do sistema.
   - A senha da conta principal é alterada para uma nova senha fornecida.

### 9. **Relistar as Opções**
   - Exibe novamente o menu de opções para o usuário.

### 10. **Sair**
   - Encerra o programa.

## Estrutura de Dados

O sistema utiliza os seguintes arquivos de dados:

- **`lista.txt`**: Armazena os dados dos clientes. Cada linha contém as seguintes informações:
  - Nome
  - CPF
  - Tipo de Conta (Comum ou Plus)
  - Saldo
  - Senha
  - Exemplo de linha:
    ```
    João da Silva,12345678901,comum,1000.00,senha123
    ```

- **`extrato.txt`**: Armazena os extratos dos clientes. Cada linha contém as seguintes informações:
  - Nome
  - CPF
  - Tipo de Conta
  - Extrato (registro de transações, com data e valores)
  - Exemplo de linha:
    ```
    João da Silva,12345678901,comum,2025-01-06 10:00:00 - 200.00 Tarifa: 0.05 Saldo: 800.00!
    ```

## Como Usar

### 1. **Inicie o programa**
   Ao rodar o programa, o menu de opções será exibido no terminal.

### 2. **Escolha a opção desejada**
   Digite o número da opção correspondente à operação que você deseja realizar.

### 3. **Siga as instruções**
   Dependendo da opção escolhida, o programa solicitará que você insira informações como CPF, senha, valores e outros dados.

## Exemplo de Uso

### **Cadastrar Novo Cliente**
   - Selecione a opção 1 para cadastrar um novo cliente.
   - O programa solicitará o nome, CPF, tipo de conta, saldo inicial e senha.
   - Após fornecer as informações, o cliente será adicionado ao sistema.

### **Realizar Débito**
   - Selecione a opção 4 para realizar um débito.
   - O programa solicitará o CPF, a senha e o valor a ser debitado.
   - Caso o saldo do cliente seja insuficiente, a operação será cancelada.

### **Consultar Extrato**
   - Selecione a opção 6 para consultar o extrato de um cliente.
   - O programa exibirá todas as transações realizadas, com a data, valores debitados/depositados e saldo final.

### **Transferir entre Contas**
   - Selecione a opção 7 para realizar uma transferência entre contas.
   - O programa solicitará o CPF e senha do remetente, o CPF do destinatário e o valor da transferência.

### **Junção de Contas**
   - Selecione a opção 8 para juntar duas contas.
   - O programa solicitará os dados das duas contas (CPF e senha) e qual delas será a conta principal.

## Requisitos

- Python 3.x
- Arquivos `lista.txt` e `extrato.txt` devem existir no diretório onde o programa é executado.

## Como Executar o Programa

1. **Baixe ou clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/sistema-bancario-python.git
