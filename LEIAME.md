# Projeto 1 de Sistemas distribuídos

Modelo _publish-subscribe_
---

## Instruções

### Host e porta
- Ajuste devidamente o endereço e a porta em `constCS.py`
- Certifique-se de que servidor e cliente estarão usando as mesmas portas.

#### **IMPORTANTE:** Arquivos dentro da pasta "linda" não funcionarão diretamente.

### No lado do servidor
Execute o programa `server.py` na raíz deste repositório.

```bash
python server.py
```

### No lado do cliente 
Execute qualquer exemplo (`alice-src`, `bob-src`, `chuck-src`) na raíz deste repositório.
- Você pode criar um novo contendo as instruções que desejar
- Se criar, certifique-se de importar o pacote `linda` e utilize as instruções no formato apropriado

### Um exemplo para testar tudo
O programa `example_all_op.py` foi criado para demonstrar todas as operações, contendo as operações de `out`, `rd`, e `in`.
```bash
python example_all_op.py
```
