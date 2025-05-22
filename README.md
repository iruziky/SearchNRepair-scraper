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
├── README.md                # Project documentation
├── .gitignore               # Files and folders ignored by Git
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (e.g., USER_AGENT, URL)
├── src/                     # Main source code
│   ├── main.py              # Entry point
│   ├── config.py            # Centralized configuration
│   ├── scrapers/            # One scraper per site
│   ├── parsers/             # Functions to extract and clean data from HTML
│   ├── storage/             # Persistence layer: save to CSV, JSON, DB, etc.
│   ├── utils/               # Helper functions: user-agent, delays, proxies
│   ├── models/              # Data structure representation (POPOs or dataclasses)
├── tests/                   # Tests using pytest
│   └── test_scraper.py      # Unit tests for the scraper
