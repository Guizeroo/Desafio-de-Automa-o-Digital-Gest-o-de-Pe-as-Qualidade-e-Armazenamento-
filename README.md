# Sistema de Gestão de Peças

> Projeto desenvolvido para a disciplina de **Algoritmos e Lógica de Programação**  

## Sobre o Projeto

Este sistema foi criado como parte de um desafio acadêmico para simular o controle de qualidade e armazenamento de peças em uma linha de produção industrial. O objetivo é automatizar o processo de inspeção, que atualmente é feito manualmente em muitas empresas, reduzindo erros humanos e aumentando a eficiência operacional.

O programa implementa uma solução em Python capaz de:
- Cadastrar peças com suas características (ID, peso, cor e comprimento)
- Validar automaticamente se cada peça atende aos critérios de qualidade
- Organizar peças aprovadas em caixas com capacidade definida
- Gerar relatórios consolidados de produção e qualidade

## Funcionalidades

### 1. Cadastro de Peças
O sistema permite o cadastro individual de peças com validação de entrada para garantir dados consistentes. Cada peça é avaliada segundo três critérios:

**Critérios de Aprovação:**
- **Peso:** Entre 95g e 105g
- **Cor:** Azul ou Verde
- **Comprimento:** Entre 10cm e 20cm

Peças que não atendem a qualquer um desses critérios são automaticamente reprovadas, e o sistema registra os motivos específicos da reprovação.

### 2. Listagem de Peças
Exibe duas listas separadas:
- **Peças Aprovadas:** Mostra todas as peças que passaram nos testes de qualidade
- **Peças Reprovadas:** Lista as peças que falharam, incluindo os motivos específicos da reprovação

### 3. Remoção de Peças
Permite remover peças cadastradas do sistema através do ID, útil para correção de erros de digitação ou exclusão de registros duplicados.

### 4. Sistema de Caixas
As peças aprovadas são automaticamente organizadas em caixas com capacidade máxima de 10 unidades. Quando uma caixa atinge sua capacidade, o sistema:
- Fecha a caixa automaticamente
- Registra a caixa fechada com todas as peças contidas
- Inicia uma nova caixa vazia
- Incrementa o número da caixa

É possível visualizar tanto as caixas já fechadas quanto o status da caixa atual (quantas peças possui e quantas faltam para completar).

### 5. Relatório Final
Gera um relatório consolidado contendo:
- Total de peças processadas
- Quantidade de peças aprovadas e reprovadas
- Taxa de aprovação percentual
- Número de caixas utilizadas
- Estatísticas dos motivos de reprovação (quantas peças foram reprovadas por peso, cor ou comprimento)

## Pré-requisitos
- Python 3.x instalado no computador
- Terminal ou Prompt de Comando

## Exemplos de Uso

### Exemplo 1: Cadastrando uma peça aprovada

```
=== CADASTRAR NOVA PEÇA ===
Digite o ID da peça: P001
Digite o peso da peça (em gramas): 100
Digite a cor da peça (azul ou verde): azul
Digite o comprimento da peça (em cm): 15

Peça P001 APROVADA e adicionada à caixa 1!
```

### Exemplo 2: Cadastrando uma peça reprovada

```
=== CADASTRAR NOVA PEÇA ===
Digite o ID da peça: P002
Digite o peso da peça (em gramas): 120
Digite a cor da peça (azul ou verde): verde
Digite o comprimento da peça (em cm): 8

Peça P002 REPROVADA!
Motivos da reprovação:
 - Peso fora do padrão (120.0g - deve estar entre 95g e 105g)
 - Comprimento fora do padrão (8.0cm - deve estar entre 10cm e 20cm)
```

### Exemplo 3: Fechamento automático de caixa

```
Peça P010 APROVADA e adicionada à caixa 1!

CAIXA 1 CHEIA! Fechando caixa...
Nova caixa 2 iniciada.
```

### Exemplo 4: Relatório Final

```
==================================================
 RELATÓRIO FINAL DO SISTEMA
==================================================

RESUMO GERAL:
 - Total de peças processadas: 15
 - Total de peças aprovadas: 12
 - Total de peças reprovadas: 3
 - Taxa de aprovação: 80.0%

ARMAZENAMENTO:
 - Caixas fechadas: 1
 - Peças na caixa atual: 2

MOTIVOS DE REPROVAÇÃO:
 - Peso fora do padrão: 2 peça(s)
 - Comprimento fora do padrão: 1 peça(s)

==================================================
```

## Estrutura do Código

O programa está organizado em funções modulares para facilitar manutenção e compreensão:

- `cadastrar_peca()` - Gerencia o cadastro e validação de novas peças
- `adicionar_na_caixa()` - Controla o sistema de empacotamento
- `listar_pecas()` - Exibe listas de peças aprovadas e reprovadas
- `remover_peca()` - Remove peças do sistema pelo ID
- `listar_caixas()` - Mostra status das caixas fechadas e da caixa atual
- `gerar_relatorio()` - Produz relatório consolidado com estatísticas
- `menu_principal()` - Controla o fluxo do programa e interface com usuário

### Estruturas de Dados Utilizadas

- **Listas:** Para armazenar coleções de peças e caixas
- **Dicionários:** Para representar cada peça com seus atributos
- **Variáveis Globais:** Para manter o estado do sistema durante a execução

## Validações Implementadas

O sistema possui validações robustas para garantir a integridade dos dados:

1. **Validação de Tipo:** Verifica se peso e comprimento são números válidos
2. **Validação de Valor:** Garante que peso e comprimento sejam maiores que zero
3. **Validação de Cor:** Aceita apenas "azul" ou "verde" 
4. **Tratamento de Erros:** Usa try-except para capturar entradas inválidas sem quebrar o programa

## Autor

Desenvolvido como projeto acadêmico por Guilherme de Oliveira Rêgo 
Disciplina: Algoritmos e Lógica de Programação  
Instituição: UNIFECAF 
Este projeto foi desenvolvido para fins educacionais.
