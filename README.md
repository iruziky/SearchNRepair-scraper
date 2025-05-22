# 🕸 Plataforma de Web Scraping na OLX

Plataforma full-stack que realiza **web scraping automatizado**, armazena os dados coletados em um banco relacional e os exibe em uma **interface web moderna**. O projeto transforma dados brutos da web em informações organizadas e acessíveis ao público.

---

## 🚀 Tecnologias Utilizadas

### 📤 Scraping
- **Linguagem:** Python
- **Framework:** [Playwright](https://playwright.dev/python/)
- **Testes:** pytest
- **Deploy:** GitHub Actions

### 🧠 Back-end
- **Framework:** [Spring Boot](https://spring.io/projects/spring-boot)
- **Banco de Dados:** PostgreSQL
- **Testes:** JUnit + Mockito
- **Documentação da API:** SpringDoc (OpenAPI)
- **Deploy:** Railway

### 🎨 Front-end
- **Framework:** [React.js](https://reactjs.org/)
- **Estilização:** [Tailwind CSS](https://tailwindcss.com/)
- **Prototipagem:** Figma
- **Testes:**
  - Unitários e de Integração: Jest + React Testing Library
  - E2E: Playwright
- **Deploy:** Netlify

### 🧱 Infraestrutura
- **Containers:** Docker
- **Versionamento:** Git + GitHub

---

## 🛠 Funcionalidades

- 🔎 Coleta automática de dados via scraping (com agendamento)
- 💾 Armazenamento dos dados em banco relacional
- 📡 Exposição dos dados via API REST
- 🌐 Visualização dos dados em um site responsivo
- ✅ Testes automatizados em todas as camadas

---

## 📁 Estrutura do Projeto

```plaintext
scraper-olx/
├── README.md                # Documentação do projeto
├── .gitignore               # Arquivos e pastas ignorados pelo Git
├── requirements.txt         # Dependências Python
├── .env                     # Variáveis de ambiente (como USER_AGENT, URL etc.)
├── src/                     # Código-fonte principal do scraper
│   ├── __init__.py
│   ├── scraper.py           # Script de scraping com Playwright
│   └── config.py            # Configurações de ambiente, URLs, etc.
├── tests/                   # Testes com pytest
│   └── test_scraper.py      # Testes unitários do scraper
