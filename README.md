# 📍 Consulta de CEP (Python + ViaCEP)

Um script Python simples e eficiente para validar e buscar informações de endereços brasileiros utilizando a API pública do **ViaCEP**.

---

## 🚀 Funcionalidades

* **Tratamento de Input:** Remove automaticamente caracteres não numéricos (como hifens e pontos).
* **Validação de Formato:** Verifica se o CEP possui exatamente 8 dígitos antes de fazer a requisição.
* **Integração em Tempo Real:** Consome dados atualizados diretamente da API ViaCEP.
* **Gestão de Erros:** Identifica CEPs inexistentes e trata falhas de conexão com o servidor.

## 🛠️ Tecnologias e Dependências

* **Linguagem:** Python 3.x
* **Biblioteca:** `requests` (para comunicação HTTP)

## 📦 Instalação e Uso

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
   cd nome-do-repositorio
2. **Instale a biblioteca requests:**


```Bash
pip install requests
```
3. **Execute o script:**

```Bash
python nome_do_seu_arquivo.py
```

📋 Exemplo de Retorno
Ao inserir um CEP válido (ex: 01001000), o script retornará um dicionário como este:
<pre>
JSON
{
  "cep": "01001-000",
  "logradouro": "Praça da Sé",
  "complemento": "lado ímpar",
  "bairro": "Sé",
  "localidade": "São Paulo",
  "uf": "SP",
  "ibge": "3550308",
  "gia": "1004",
  "ddd": "11",
  "siafi": "7107"
}
<pre> 

📂 Estrutura do Código
O código utiliza uma função principal validar_cep(cep) que:

Limpa a string.

Valida o tamanho.

Faz a requisição GET.

Retorna os dados ou uma mensagem de erro amigável.

Desenvolvido para fins de estudo e automação. 💻
