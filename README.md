# 💧 Controle de Níveis de Água

Projeto desenvolvido para a **Agenda 11 da disciplina Desenvolvimento de Sistemas I**.

O objetivo da atividade é simular, no terminal, um sistema simples de monitoramento de um reservatório de água, exibindo mensagens coloridas de alerta conforme o nível do reservatório.

---

## 📌 Sobre o projeto

Este programa foi criado em **Python** e utiliza a biblioteca **colorama** para exibir mensagens coloridas no terminal.

A ideia é representar uma situação real de monitoramento, em que cada nível do reservatório exige uma atenção diferente. Assim, o sistema mostra uma mensagem específica para cada nível, utilizando cores para facilitar a identificação visual da situação.

---

## 🚦 Níveis monitorados

| Nível | Situação do reservatório | Cor exibida |
|---|---|---|
| Nível 1 | Muito baixo (crítico) | Vermelho |
| Nível 2 | Baixo | Amarelo |
| Nível 3 | Médio | Verde |
| Nível 4 | Alto | Ciano |
| Nível 5 | Muito alto (alerta) | Azul |

---

## 🧠 Conceitos utilizados

Neste projeto foram aplicados conceitos básicos de programação em Python, como:

- Uso de listas;
- Criação de funções;
- Estruturas condicionais;
- Importação de bibliotecas;
- Exibição de mensagens no terminal;
- Organização e legibilidade do código.

---

## 📚 Biblioteca utilizada

O projeto utiliza a biblioteca:

```bash
colorama
```

A biblioteca `colorama` permite aplicar cores aos textos exibidos no terminal, tornando a saída do programa mais visual e fácil de compreender.

---

## ⚙️ Como instalar a biblioteca

Antes de executar o programa, é necessário instalar a biblioteca `colorama`.

No terminal, digite:

```bash
pip install colorama
```

---

## ▶️ Como executar o programa

Após instalar a biblioteca, execute o arquivo Python com o seguinte comando:

```bash
python jefferson_astuti_magalhaes_de_barros_ag11_ds_i.py
```

---

## 🖥️ Funcionamento

Ao executar o programa, o sistema percorre uma lista com os cinco níveis do reservatório.

Para cada nível, uma função chamada `definir_cor` verifica a situação correspondente e retorna a cor adequada.

Em seguida, o programa exibe no terminal a mensagem de alerta com a cor definida, simulando um sistema simples de acompanhamento do nível de água.

---

## 📁 Arquivos do projeto

```text
controle-niveis-agua/
│
├── jefferson_astuti_magalhaes_de_barros_ag11_ds_i.py
└── README.md
```

---

## ✅ Resultado esperado

O programa deve exibir no terminal as cinco situações do reservatório, cada uma com sua respectiva cor:

```text
Sistema de Monitoramento do Reservatório de Água
-------------------------------------------------------
Nível 1 - Muito baixo (crítico)
Nível 2 - Baixo
Nível 3 - Médio
Nível 4 - Alto
Nível 5 - Muito alto (alerta)
-------------------------------------------------------
Monitoramento finalizado.
```

As mensagens aparecerão coloridas no terminal, conforme o nível de risco.

---

## 👨‍💻 Autor

**Jefferson Astuti Magalhães de Barros**

---

## 📝 Atividade

**Agenda 11 - Desenvolvimento de Sistemas I**  
**Tema:** Controle de Níveis de Água
