#  Bandeijão Bot

**Bandeijão Bot** é uma aplicação Python que envia mensagens via WhatsApp com o cardápio do **almoço** e **jantar** dos restaurantes universitários da **UFRJ**: Central, CT e Letras.

As mensagens são enviadas automaticamente, possivelmente com pequena variação de tempo, nos seguintes horários:

-  **06:40*** — Cardápio do **almoço**
-  **14:50** — Cardápio do **jantar**

*Nas segundas o cardápio é enviado as 7:20, devido ao tempo de atualização da [planilha](https://docs.google.com/spreadsheets/d/1YvCqBrNw5l4EFNplmpRBFrFJpjl4EALlVNDk3pwp_dQ/pubhtml) que contém as refeições servidas.

Atualmente, o sistema utiliza a API [WAHA](https://waha.devlike.pro/) para o envio das mensagens.

---

##  Exemplo de mensagem
Hoje é *terça-feira* e para o **almoço** temos:

- **Entrada:** Salada verde  

- **Prato Principal:** Frango assado  

- **Prato Vegano:** Quibe de abóbora  

- **Guarnição:** Arroz integral  

- **Acompanhamentos:** Feijão, farofa  

- **Sobremesa:** Banana  

_O cardápio poderá sofrer alteração sem comunicação prévia._  
_Nossas preparações podem conter glúten._

