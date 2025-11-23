# FarmTech Solutions - Sistema de Gestão Agrícola Integrado (Fase 7)

## 👨‍🎓 Integrantes
* **Pedro Henrique Zani** - RM564956

---

## 📜 Descrição
Este projeto consolida as soluções desenvolvidas nas Fases 1 a 6 do projeto de gestão agrícola, integrando serviços de cálculo, banco de dados, IoT, Machine Learning, Cloud e visão computacional em um único dashboard interativo.

O sistema permite:
- **Planejamento**: Cálculo de área e previsão do tempo.
- **Gestão**: Controle de dados de insumos e colheita.
- **Monitoramento**: Leitura de sensores IoT em tempo real.
- **Inteligência**: Predição de irrigação com Machine Learning.
- **Segurança**: Infraestrutura em Cloud AWS com alertas automáticos.
- **Visão**: Detecção de pragas via análise de imagens.

---

## ☁️ Solução de Mensageria AWS (Entregável)

O sistema utiliza a infraestrutura de nuvem da AWS (Fase 5) para monitoramento ativo. Implementamos um serviço de mensageria utilizando **Amazon SNS (Simple Notification Service)**.

### Funcionamento
1. **Monitoramento**: O sistema monitora constantemente os dados dos sensores (Fase 3) e as análises de visão computacional (Fase 6).
2. **Gatilho**:
   - Se a **umidade do solo** cair abaixo de 45% (Fase 3).
   - Se uma **praga** for detectada na imagem (Fase 6).
3. **Ação**: O script `src/aws_service/messaging.py` é acionado.
4. **Notificação**: Um alerta é enviado via SNS para os tópicos assinados (E-mail/SMS), sugerindo ações corretivas (ex: "Ativar bomba" ou "Aplicar defensivo").

> **Nota**: A solução utiliza a biblioteca `boto3` para comunicação com a API da AWS.

---

## 📁 Estrutura de Pastas

```text
/
├── assets/          # Imagens e recursos estáticos
├── config/          # Arquivos de configuração
├── document/        # Documentação do projeto
├── scripts/         # Scripts auxiliares
├── src/             # Código fonte principal
│   ├── dashboard/   # Aplicação Streamlit (Dashboard)
│   ├── fase1/       # Fase 1: Planejamento
│   ├── fase2/       # Fase 2: Banco de Dados
│   ├── fase3/       # Fase 3: IoT
│   ├── fase4/       # Fase 4: Machine Learning (Código Original)
│   ├── fase5/       # Fase 5: Cloud Computing
│   ├── fase6/       # Fase 6: Visão Computacional
│   └── aws_service/ # Serviço de Mensageria AWS
├── requirements.txt # Dependências do projeto
└── README.md        # Este arquivo
```

---

## 🔧 Instalação e Execução

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/fase7-fiap.git
   cd fase7-fiap
   ```

2. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure as Credenciais AWS (Opcional)**:
   Para o funcionamento dos alertas, configure as variáveis de ambiente:
   ```bash
   export AWS_ACCESS_KEY_ID="sua-chave"
   export AWS_SECRET_ACCESS_KEY="seu-segredo"
   export AWS_REGION="us-east-1"
   ```

4. **Execute o Dashboard**:
   ```bash
   streamlit run src/dashboard/app.py
   ```

---

## ✅ Testes e Verificação

O projeto inclui um script de teste automatizado para verificar a integridade dos módulos e importações.

Para executar os testes:
```bash
python tests/test_smoke.py
```
Se tudo estiver correto, você verá a mensagem: `All modules imported successfully!`


---

## � Histórico de Lançamentos

* **0.7.0** - Fase 7: Consolidação final e integração de todos os serviços.
* **0.6.0** - Fase 6: Visão Computacional com YOLO.
* **0.5.0** - Fase 5: Migração para Cloud AWS.
* **0.4.0** - Fase 4: Dashboard e Machine Learning.
* **0.3.0** - Fase 3: IoT e Automação.
* **0.2.0** - Fase 2: Banco de Dados.
* **0.1.0** - Fase 1: Lógica Inicial.

---

## 📋 Licença
Este projeto está licenciado sob a licença MIT.
