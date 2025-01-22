# FileMaster

Sistema de gerenciamento documental desenvolvido, permitindo organização e controle de documentos em salas virtuais com diferentes níveis de permissões.

## 🚀 Funcionalidades

- **Gestão de Salas**
  - Criação de salas virtuais
  - Conexão com salas existentes
  - Organização por setores

- **Controle de Documentos**
  - Upload de múltiplos formatos
  - Categorização de documentos
  - Visualização e download
  - Histórico de uploads

- **Sistema de Permissões**
  - Controle granular de acessos
  - Diferentes níveis de permissões
  - Gestão de usuários por sala

- **Organização por Categorias**
  - Criação de categorias personalizadas
  - Filtros e busca avançada
  - Organização hierárquica

## 🛠️ Tecnologias Utilizadas

- **Backend**
  - Python 3.13
  - Django 5.1.4
  - PostgreSQL

- **Frontend**
  - HTML5
  - CSS3
  - JavaScript
  - Bootstrap 4.5.2
  - Font Awesome 6.0

## 📋 Pré-requisitos

- Python 3.13+
- PostgreSQL
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/filemaster.git
cd filemaster
```

2. Crie um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências
```bash
pip install -r requirements.txt
```

4. Configure o banco de dados no arquivo `settings.py`
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'filemaster',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

5. Execute as migrações
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Crie um superusuário
```bash
python manage.py createsuperuser
```

7. Inicie o servidor
```bash
python manage.py runserver
```

## 📦 Estrutura do Projeto

```
filemaster/
├── accounts/          # App de gestão de usuários
├── app/              # Configurações principais
├── categories/       # App de categorias
├── documents/        # App de documentos
├── media/           # Arquivos de mídia
├── permissions/     # App de permissões
├── positions/       # App de cargos
├── rooms/           # App de salas
├── sectors/         # App de setores
└── templates/       # Templates globais
```

## 👥 Níveis de Acesso

- **Administrador**
  - Acesso total ao sistema
  - Gerenciamento de usuários
  - Configurações globais

- **Proprietário da Sala**
  - Gerenciamento da sala
  - Controle de permissões
  - Gestão de documentos

- **Usuário com Permissões**
  - Acesso baseado em permissões
  - Upload/download de documentos
  - Visualização de conteúdo

## 🔒 Segurança

- Autenticação obrigatória
- Controle de acesso baseado em permissões
- Proteção contra CSRF
- Validação de formulários
- Sanitização de uploads

## 🖥️ Interface

- Design responsivo
- Tema personalizado Pirajuçara
- Ícones intuitivos
- Feedback visual de ações
- Navegação simplificada

## ✒️ Autores

* **Saulo Emmanuel** - *Desenvolvimento* - [saulo](https://github.com/saulosilva2809/)

## 📌 Versão

* 1.0.0
    * Versão inicial

## 📧 Contato

* Email: saulocomercial7@gmail.com
* Telefone: (11) 97293-6309
